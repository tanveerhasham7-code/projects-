from __future__ import annotations
import hmac
from fastapi import FastAPI, Header, HTTPException, Request
from app import config
from app.ai_triage import ai_triage
from app.engine import normalize_alert, event_fingerprint, deterministic_triage, apply_policy
from app.notifier import send_alert
from app.storage import save_case

app = FastAPI(title="AI-SOC Sentinel", version="1.0.0",
              description="AI-assisted SIEM triage and human-approved incident workflow")

@app.get("/health")
def health():
    return {"status": "ok", "ai_enabled": config.AI_ENABLED, "smtp_enabled": config.SMTP_ENABLED}

@app.post("/webhook/wazuh")
async def wazuh_webhook(request: Request, x_webhook_token: str | None = Header(default=None)):
    if not config.WEBHOOK_TOKEN or not x_webhook_token or not hmac.compare_digest(
        config.WEBHOOK_TOKEN, x_webhook_token
    ):
        raise HTTPException(status_code=401, detail="Unauthorized")
    try:
        alert = await request.json()
    except Exception:
        raise HTTPException(status_code=400, detail="Request body must be valid JSON")
    if not isinstance(alert, dict):
        raise HTTPException(status_code=400, detail="Alert must be a JSON object")

    event = normalize_alert(alert)
    fingerprint = event_fingerprint(event)
    deterministic = deterministic_triage(event)
    ai_result = None
    if config.AI_ENABLED:
        ai_result = ai_triage(event, config.AI_API_KEY, config.AI_MODEL,
                              config.AI_BASE_URL, config.AI_TIMEOUT_SECONDS)
    decision = apply_policy(deterministic, ai_result, config.RISK_EMAIL_THRESHOLD)

    # Store before sending to ensure every accepted alert has an audit record.
    # Duplicate fingerprints are ignored to avoid repeated email storms.
    notification_status = "not_required"
    if decision["notify_analyst"]:
        notification_status = "pending"
    inserted = save_case(config.DATABASE_PATH, fingerprint, event, decision, notification_status, ai_result)
    if not inserted:
        return {"status": "duplicate_ignored", "fingerprint": fingerprint}
    if decision["notify_analyst"]:
        notification_status = send_alert(event, decision, ai_result, config)
        # Persist delivery result in a separate update.
        from app.storage import update_notification
        update_notification(config.DATABASE_PATH, fingerprint, notification_status)
    return {
        "status": "processed",
        "fingerprint": fingerprint,
        "decision": decision,
        "ai_assessment": ai_result,
        "notification": notification_status,
        "response_action": "human_review_required",
    }
