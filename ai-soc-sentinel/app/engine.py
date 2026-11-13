"""Deterministic event normalization, detection hints, risk scoring and policy gates."""
from __future__ import annotations
import hashlib
import json
from datetime import datetime, timezone
from typing import Any

SEVERITY_POINTS = {"low": 10, "medium": 30, "high": 55, "critical": 75}

def _first(mapping: dict, *keys, default=None):
    for key in keys:
        value = mapping.get(key)
        if value not in (None, ""):
            return value
    return default

def normalize_alert(alert: dict[str, Any]) -> dict[str, Any]:
    rule = alert.get("rule") or {}
    agent = alert.get("agent") or {}
    data = alert.get("data") or {}
    mitre = rule.get("mitre") or {}
    groups = rule.get("groups") or []
    if isinstance(groups, str):
        groups = [groups]
    if isinstance(mitre, dict):
        techniques = mitre.get("id") or []
        if isinstance(techniques, str):
            techniques = [techniques]
    else:
        techniques = []
    normalized = {
        "timestamp": _first(alert, "timestamp", "@timestamp", default=datetime.now(timezone.utc).isoformat()),
        "alert_id": str(_first(alert, "id", "alert_id", default="")),
        "rule_id": str(_first(rule, "id", default="")),
        "rule_level": int(rule.get("level") or 0),
        "rule_description": str(_first(rule, "description", default="")),
        "rule_groups": [str(x) for x in groups],
        "agent_id": str(_first(agent, "id", default="")),
        "agent_name": str(_first(agent, "name", default="")),
        "manager_name": str(_first(alert, "manager", "manager_name", default="")),
        "source_ip": str(_first(data, "srcip", "source_ip", default="")),
        "destination_ip": str(_first(data, "dstip", "destination_ip", default="")),
        "username": str(_first(data, "srcuser", "dstuser", "user", "username", default="")),
        "process": str(_first(data, "process", "process_name", "win", default="")),
        "mitre_techniques": [str(x) for x in techniques],
        "location": str(_first(data, "location", default="")),
        "full_log": str(_first(alert, "full_log", default=""))[:4000],
    }
    return normalized

def event_fingerprint(normalized: dict[str, Any]) -> str:
    stable = {k: normalized.get(k) for k in (
        "timestamp", "alert_id", "rule_id", "agent_id", "source_ip",
        "username", "rule_description", "full_log"
    )}
    raw = json.dumps(stable, sort_keys=True, separators=(",", ":")).encode()
    return hashlib.sha256(raw).hexdigest()

def deterministic_triage(event: dict[str, Any]) -> dict[str, Any]:
    level = int(event.get("rule_level") or 0)
    groups = " ".join(event.get("rule_groups") or []).lower()
    text = " ".join([
        str(event.get("rule_description", "")),
        str(event.get("full_log", "")),
        str(event.get("process", "")),
        groups,
    ]).lower()
    if level >= 12:
        severity, reasons = "critical", ["Wazuh rule level is 12 or higher"]
    elif level >= 10:
        severity, reasons = "high", ["Wazuh rule level is 10 or higher"]
    elif level >= 7:
        severity, reasons = "medium", ["Wazuh rule level is 7 or higher"]
    else:
        severity, reasons = "low", ["No high-severity deterministic rule threshold matched"]

    indicators = []
    if any(term in text for term in ("authentication_failed", "failed password", "invalid user", "brute force")):
        indicators.append("authentication_failure")
        reasons.append("Authentication-failure indicator found")
    if "powershell" in text and any(term in text for term in ("encodedcommand", "-enc ", "downloadstring", "invoke-expression")):
        indicators.append("suspicious_powershell")
        reasons.append("PowerShell command-line indicator needs analyst review")
    if "privilege" in text or "sudo" in text or "group_membership" in text:
        indicators.append("privilege_change")
        reasons.append("Privilege-change indicator found")
    if "malware" in groups or "rootcheck" in groups or "syscheck" in groups:
        indicators.append("endpoint_security_alert")
        reasons.append("Endpoint security telemetry group matched")

    score = max(SEVERITY_POINTS[severity], min(100, level * 6))
    score += min(15, len(indicators) * 5)
    score = min(score, 100)
    return {"severity": severity, "risk_score": score, "indicators": indicators, "reasons": reasons}

def apply_policy(deterministic: dict, ai_result: dict | None, threshold: int = 70) -> dict:
    """AI can raise attention but cannot downgrade deterministic severity or trigger containment."""
    base_score = int(deterministic["risk_score"])
    score = base_score
    rationale = list(deterministic["reasons"])
    if ai_result:
        confidence = float(ai_result.get("confidence", 0))
        ai_severity = str(ai_result.get("severity", "low")).lower()
        if confidence >= 0.70:
            score = max(score, {"low": 10, "medium": 35, "high": 70, "critical": 90}.get(ai_severity, 0))
            rationale.append("AI triage considered with confidence >= 0.70; deterministic score was not reduced")
        else:
            rationale.append("AI confidence below 0.70; AI severity not used to raise risk")
    notify = score >= threshold or deterministic["severity"] == "critical"
    return {
        "severity": deterministic["severity"] if deterministic["severity"] == "critical" else (
            "critical" if score >= 90 else "high" if score >= 70 else "medium" if score >= 35 else "low"
        ),
        "risk_score": score,
        "notify_analyst": notify,
        "response_action": "human_review_required",
        "rationale": rationale,
    }
