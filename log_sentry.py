#!/usr/bin/env python3
"""LogSentry: local analysis of SSH-style authentication log lines.

Reads a user-supplied local file only. It does not connect to hosts or block IPs.
"""

from __future__ import annotations

import argparse
import re
import sys
from collections import Counter
from dataclasses import dataclass
from pathlib import Path


IP_PATTERN = r"(?:\d{1,3}\.){3}\d{1,3}"
FAILED_RE = re.compile(
    rf"Failed password for (?:invalid user )?(?P<user>\S+) from (?P<ip>{IP_PATTERN})\b",
    re.IGNORECASE,
)
SUCCESS_RE = re.compile(
    rf"Accepted (?:password|publickey) for (?P<user>\S+) from (?P<ip>{IP_PATTERN})\b",
    re.IGNORECASE,
)


@dataclass(frozen=True)
class LogReport:
    total_lines: int
    failed: int
    successful: int
    unrecognized: int
    failed_by_ip: Counter[str]
    failed_by_user: Counter[str]
    successful_by_ip: Counter[str]


def analyze_lines(lines: list[str]) -> LogReport:
    """Parse SSH-style authentication messages from supplied text lines."""
    failed_by_ip: Counter[str] = Counter()
    failed_by_user: Counter[str] = Counter()
    successful_by_ip: Counter[str] = Counter()
    failed = 0
    successful = 0
    unrecognized = 0

    for line in lines:
        failed_match = FAILED_RE.search(line)
        if failed_match:
            failed += 1
            failed_by_ip[failed_match.group("ip")] += 1
            failed_by_user[failed_match.group("user")] += 1
            continue

        success_match = SUCCESS_RE.search(line)
        if success_match:
            successful += 1
            successful_by_ip[success_match.group("ip")] += 1
            continue

        if line.strip():
            unrecognized += 1

    return LogReport(
        total_lines=len(lines),
        failed=failed,
        successful=successful,
        unrecognized=unrecognized,
        failed_by_ip=failed_by_ip,
        failed_by_user=failed_by_user,
        successful_by_ip=successful_by_ip,
    )


def render_report(report: LogReport, threshold: int = 5) -> str:
    """Return a human-readable summary; findings are leads, not verdicts."""
    if threshold < 1:
        raise ValueError("threshold must be at least 1")

    lines = [
        "LogSentry - Authentication Log Summary",
        f"Events analyzed: {report.total_lines}",
        f"Failed logins: {report.failed}",
        f"Successful logins: {report.successful}",
        f"Other/unrecognized lines: {report.unrecognized}",
        "",
        f"Sources with repeated failed logins (threshold: {threshold}):",
    ]

    repeated = [
        (ip, count) for ip, count in report.failed_by_ip.most_common()
        if count >= threshold
    ]
    if repeated:
        lines.extend(f"  {ip}: {count} failures" for ip, count in repeated)
    else:
        lines.append("  None")

    lines.extend(["", "Most targeted usernames:"])
    if report.failed_by_user:
        lines.extend(
            f"  {user}: {count} failed attempts"
            for user, count in report.failed_by_user.most_common(5)
        )
    else:
        lines.append("  None")

    lines.extend(["", "Successful logins by source:"])
    if report.successful_by_ip:
        lines.extend(
            f"  {ip}: {count} successful event(s)"
            for ip, count in report.successful_by_ip.most_common(5)
        )
    else:
        lines.append("  None")

    lines.append("")
    lines.append("Reminder: investigate in context; repeated failures alone do not prove an attack.")
    return "\n".join(lines)


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description="Summarize SSH-style authentication logs from a local text file."
    )
    parser.add_argument("--file", required=True, help="Path to a local log file")
    parser.add_argument(
        "--threshold", type=int, default=5,
        help="Failed logins from one IP that trigger a repeated-failure alert (default: 5)",
    )
    args = parser.parse_args(argv)

    if args.threshold < 1:
        parser.error("--threshold must be at least 1")

    try:
        lines = Path(args.file).read_text(encoding="utf-8", errors="replace").splitlines()
    except OSError as exc:
        print(f"Could not read log file: {exc}", file=sys.stderr)
        return 2

    report = analyze_lines(lines)
    print(render_report(report, args.threshold))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
