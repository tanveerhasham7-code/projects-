"""SMTP notification. Never logs credentials or full raw alert bodies."""
import smtplib
from email.message import EmailMessage

def send_alert(event: dict, decision: dict, ai_result: dict | None, settings) -> str:
    if not settings.SMTP_ENABLED:
        return "disabled"
    required = (settings.SMTP_HOST, settings.SMTP_USERNAME, settings.SMTP_PASSWORD,
                settings.SMTP_FROM, settings.SOC_ANALYST_EMAIL)
    if not all(required):
        return "misconfigured"
    msg = EmailMessage()
    msg["Subject"] = f"[AI-SOC Sentinel] {decision['severity'].upper()} risk {decision['risk_score']}/100"
    msg["From"] = settings.SMTP_FROM
    msg["To"] = settings.SOC_ANALYST_EMAIL
    lines = [
        "AI-SOC Sentinel generated an analyst notification.",
        "",
        f"Severity: {decision['severity']}",
        f"Risk score: {decision['risk_score']}/100",
        f"Rule: {event.get('rule_id')} — {event.get('rule_description')}",
        f"Agent: {event.get('agent_name')} ({event.get('agent_id')})",
        f"Timestamp: {event.get('timestamp')}",
        f"Source IP: {event.get('source_ip') or 'not supplied'}",
        f"Username: {event.get('username') or 'not supplied'}",
        "",
        "Deterministic rationale:",
        *[f"- {item}" for item in decision.get("rationale", [])],
        "",
        "AI summary (advisory only):",
        (ai_result or {}).get("summary", "AI triage disabled or unavailable."),
        "",
        "Required action: human analyst review. No containment action was executed.",
        "Treat this message as an alert lead, not confirmation of compromise.",
    ]
    msg.set_content("\n".join(lines))
    try:
        with smtplib.SMTP(settings.SMTP_HOST, settings.SMTP_PORT, timeout=15) as server:
            if settings.SMTP_STARTTLS:
                server.starttls()
            server.login(settings.SMTP_USERNAME, settings.SMTP_PASSWORD)
            server.send_message(msg)
        return "sent"
    except (OSError, smtplib.SMTPException):
        return "failed"
