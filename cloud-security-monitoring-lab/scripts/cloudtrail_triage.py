#!/usr/bin/env python3
"""Triage newline-delimited AWS CloudTrail JSON events using local rules.

This tool is intentionally read-only and uses only the Python standard library.
It does not connect to AWS, modify cloud resources, or prove malicious activity.
"""
from __future__ import annotations

import argparse
import json
import sys
from collections import Counter
from pathlib import Path
from typing import Any


def get_actor(event: dict[str, Any]) -> str:
    identity = event.get("userIdentity") or {}
    return str(
        identity.get("arn")
        or identity.get("principalId")
        or identity.get("userName")
        or identity.get("type")
        or "unknown"
    )


def get_source_ip(event: dict[str, Any]) -> str:
    return str(event.get("sourceIPAddress") or "unknown")


def event_findings(event: dict[str, Any]) -> list[dict[str, str]]:
    """Return deterministic rule matches for one CloudTrail event."""
    name = str(event.get("eventName") or "")
    source = get_source_ip(event)
    actor = get_actor(event)
    timestamp = str(event.get("eventTime") or "unknown")
    identity = event.get("userIdentity") or {}
    params = event.get("requestParameters") or {}
    findings: list[dict[str, str]] = []

    def add(rule_id: str, severity: str, title: str, reason: str) -> None:
        findings.append({
            "rule_id": rule_id,
            "severity": severity,
            "title": title,
            "event_time": timestamp,
            "event_name": name or "unknown",
            "actor": actor,
            "source_ip": source,
            "reason": reason,
        })

    if name == "ConsoleLogin":
        response = event.get("responseElements") or {}
        if response.get("ConsoleLogin") == "Failure" or event.get("errorCode"):
            add(
                "CLOUD-AUTH-001", "medium", "Failed console sign-in",
                "The console sign-in event records a failure; correlate actor, IP, and time window."
            )
        if identity.get("type") == "Root":
            add(
                "CLOUD-IAM-001", "high", "Root account console activity",
                "The event is associated with the AWS root identity; verify whether this activity was expected."
            )
        additional = event.get("additionalEventData") or {}
        if additional.get("MFAUsed") == "No":
            add(
                "CLOUD-AUTH-002", "high", "Console sign-in without MFA",
                "The event indicates MFAUsed=No; verify account policy and identity context."
            )

    if name in {"PutUserPolicy", "PutRolePolicy", "AttachUserPolicy",
                "AttachRolePolicy", "PutGroupPolicy", "AttachGroupPolicy",
                "CreatePolicyVersion", "SetDefaultPolicyVersion"}:
        add(
            "CLOUD-IAM-002", "high", "IAM permissions changed",
            "An IAM policy or policy attachment changed; inspect the principal, policy, and change approval."
        )

    if name == "CreateAccessKey":
        add(
            "CLOUD-IAM-003", "high", "IAM access key created",
            "A new access key was created; confirm the owner, business need, and secure storage."
        )

    if name == "AuthorizeSecurityGroupIngress":
        permissions = params.get("ipPermissions") or {}
        ranges = permissions.get("ipRanges") or []
        public_cidrs = [
            str(item.get("cidrIp"))
            for item in ranges
            if item.get("cidrIp") == "0.0.0.0/0"
        ]
        if public_cidrs:
            add(
                "CLOUD-NET-001", "high", "Security group ingress open to IPv4 internet",
                "An ingress permission includes 0.0.0.0/0; verify protocol, port range, resource, and intended exposure."
            )

    return findings


def analyze_events(events: list[dict[str, Any]]) -> dict[str, Any]:
    findings: list[dict[str, str]] = []
    for event in events:
        findings.extend(event_findings(event))
    counts = Counter(item["severity"] for item in findings)
    return {
        "events_analyzed": len(events),
        "findings_count": len(findings),
        "severity_counts": dict(sorted(counts.items())),
        "findings": findings,
    }


def load_jsonl(path: Path) -> tuple[list[dict[str, Any]], list[str]]:
    events: list[dict[str, Any]] = []
    errors: list[str] = []
    with path.open("r", encoding="utf-8") as handle:
        for line_number, line in enumerate(handle, start=1):
            if not line.strip():
                continue
            try:
                item = json.loads(line)
            except json.JSONDecodeError as exc:
                errors.append(f"line {line_number}: invalid JSON ({exc.msg})")
                continue
            if not isinstance(item, dict):
                errors.append(f"line {line_number}: event must be a JSON object")
                continue
            events.append(item)
    return events, errors


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Analyze newline-delimited CloudTrail JSON events with local triage rules."
    )
    parser.add_argument("input", type=Path, help="Path to a JSONL event file")
    parser.add_argument("--json-out", type=Path, help="Optional path to save findings as JSON")
    args = parser.parse_args()

    if not args.input.is_file():
        print(f"Error: input file not found: {args.input}", file=sys.stderr)
        return 2

    try:
        events, errors = load_jsonl(args.input)
    except OSError as exc:
        print(f"Error reading input: {exc}", file=sys.stderr)
        return 2

    report = analyze_events(events)
    print(f"Events analyzed: {report['events_analyzed']}")
    print(f"Findings: {report['findings_count']}")
    for severity, count in report["severity_counts"].items():
        print(f"  {severity}: {count}")

    if report["findings"]:
        print("\nFindings:")
        for finding in report["findings"]:
            print(
                f"- [{finding['severity'].upper()}] {finding['rule_id']} "
                f"{finding['title']} | {finding['event_time']} | "
                f"{finding['actor']} | {finding['source_ip']}\n  {finding['reason']}"
            )
    else:
        print("\nNo configured rule matched the supplied events.")

    if errors:
        print("\nInput warnings:", file=sys.stderr)
        for error in errors:
            print(f"- {error}", file=sys.stderr)

    if args.json_out:
        try:
            args.json_out.write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")
            print(f"\nJSON report written to: {args.json_out}")
        except OSError as exc:
            print(f"Error writing JSON report: {exc}", file=sys.stderr)
            return 2

    return 1 if errors else 0


if __name__ == "__main__":
    raise SystemExit(main())
