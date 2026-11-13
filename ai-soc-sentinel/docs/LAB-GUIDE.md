# Guided practical lab

Complete the stages in order. Do not connect Wazuh or enable AI until local deterministic triage works.

## Stage 1 — Prepare
Record OS/Python version, create a virtual environment, install requirements, copy `.env.example` to `.env`, set a long webhook token, and leave AI/SMTP disabled.

## Stage 2 — Unit tests
```bash
python -m unittest discover -s tests -v
```
Read each test. Verify that AI cannot downgrade deterministic critical severity and low-risk events do not email by default.

## Stage 3 — Start and health-check
```bash
uvicorn app.main:app --host 127.0.0.1 --port 8080
```
Open `http://127.0.0.1:8080/health`.

## Stage 4 — Submit synthetic high-risk event
```bash
curl -X POST http://127.0.0.1:8080/webhook/wazuh \
  -H "Content-Type: application/json" \
  -H "X-Webhook-Token: replace-with-your-token" \
  --data-binary @sample_data/high-risk-alert.json
```
Inspect severity, score, rationale, response action, and notification status. With SMTP disabled, a case is still recorded. Repeat the same event to test duplicate suppression.

## Stage 5 — Benign event
Create a JSON event with low Wazuh rule level and a routine service-start message. Confirm it does not request analyst email.

## Stage 6 — Email test
Use a dedicated test mailbox and app password. Configure SMTP environment variables; never use your normal mailbox password. Keep the recipient under your control. Submit a fresh synthetic event and inspect the email for secrets.

## Stage 7 — Optional AI
Review provider retention, region, cost, and data handling. Configure API key/model, set `AI_ENABLED=true`, and submit benign, suspicious, ambiguous, and prompt-injection-like synthetic strings. Confirm model failure falls back to deterministic triage and no containment occurs.

## Stage 8 — Wazuh lab connection
Follow `WAZUH-INTEGRATION.md`. Record exact Wazuh version, manager/agent topology, filters, and sanitized evidence. Use only owned systems.

## Stage 9 — Evaluate
Build at least 20 labeled synthetic events. Record expected class, deterministic result, AI assessment, email result, and analyst conclusion. Calculate precision/recall only with defined labels and denominators. Document false positives and misses.

## Evidence
Capture actual test output, health response, redacted webhook response, controlled email screenshot, sanitized Wazuh alert, completed case report, and evaluation notes. Never mark a planned step complete.
