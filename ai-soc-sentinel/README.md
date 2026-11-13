# AI-SOC Sentinel — AI-Assisted SIEM Monitoring & Incident Response

A portfolio-grade, defensive SOC engineering project that connects Wazuh SIEM alerts to an event-processing service, applies deterministic detection and risk scoring, optionally asks an LLM for a constrained triage assessment, stores an auditable case record, and emails a human analyst when an event crosses the configured notification threshold.

> **Status and honesty:** This repository contains implementation code, configuration examples, synthetic events, tests, and a guided lab. It is not connected to a live Wazuh manager or email account by default. No live alert delivery, AI accuracy, production readiness, or practical completion is claimed. The learner must configure, run, test, and capture evidence in an authorized lab.

## What it does

1. **Ingests SIEM alerts:** FastAPI exposes a protected webhook endpoint for Wazuh alert JSON.
2. **Normalizes evidence:** extracts rule, agent, timestamp, source/destination, user, and MITRE fields without discarding the original alert.
3. **Runs deterministic checks first:** maps known Wazuh rule groups/IDs and event context to a severity floor and risk score.
4. **Uses AI as an assistant, not an authority:** optional LLM analysis receives a minimized event summary and returns a strict JSON assessment. Untrusted log content is explicitly treated as data, not instructions.
5. **Applies policy gates:** a deterministic policy combines rule severity, risk score, AI confidence, and validation. AI cannot downgrade a critical deterministic finding or authorize response actions.
6. **Creates an auditable case:** SQLite stores event hash, decision, AI assessment, and notification outcome.
7. **Emails the analyst:** high/critical cases trigger SMTP email containing a concise summary, rationale, evidence fields, and a link placeholder for the analyst's SIEM console.
8. **Keeps response human-controlled:** this version does not disable accounts, kill processes, isolate endpoints, modify firewall rules, or execute commands.

## Architecture

```text
Windows / Linux endpoints
        |
        v
Wazuh agents -> Wazuh manager / rules / alerts.json
                         |
                  custom integration
                         |
                         v
               HTTPS webhook (FastAPI)
                         |
               validation + normalization
                         |
             deterministic detection engine
                         |
              optional AI triage (LLM)
                         |
              policy gate + risk decision
                    /           \
                   v             v
             SQLite audit     SMTP email
                   |             |
                   v             v
             case history    Human analyst
                                  |
                         investigate / approve
```

The Wazuh manager remains the SIEM and source of telemetry. AI-SOC Sentinel is an enrichment, triage, case-recording, and notification layer; it is not a replacement SIEM.

## Repository map

- `app/main.py` — FastAPI webhook, health check, request authentication, orchestration.
- `app/engine.py` — normalization, deterministic indicators, severity floor, risk scoring, policy.
- `app/ai_triage.py` — optional OpenAI-compatible chat-completions client with strict output parsing.
- `app/notifier.py` — SMTP email delivery.
- `app/storage.py` — SQLite event/case audit store.
- `integrations/wazuh/custom-ai-soc.py` — Wazuh custom integration adapter; forwards alert JSON to the service.
- `config/policy.yaml` — documented threshold and notification policy.
- `sample_data/` — synthetic Wazuh-like events only.
- `tests/` — deterministic unit tests; no live services required.
- `docs/` — architecture, theory, implementation, detection engineering, lab exercises, threat model, and response runbook.
- `templates/` — analyst case report template.

## Quick start — local simulation

Requirements: Python 3.10+.

```bash
cd ai-soc-sentinel
python -m venv .venv
# Windows PowerShell: .venv\Scripts\Activate.ps1
# Linux/macOS: source .venv/bin/activate
pip install -r requirements.txt
cp .env.example .env
```

Set a long random `WEBHOOK_TOKEN` in `.env`. Leave AI disabled initially. Set SMTP values only when you are ready to test email using an account/app password dedicated to the lab.

Start the service:

```bash
uvicorn app.main:app --host 127.0.0.1 --port 8080
```

In another terminal, submit a synthetic alert:

```bash
curl -X POST http://127.0.0.1:8080/webhook/wazuh \
  -H "Content-Type: application/json" \
  -H "X-Webhook-Token: replace-with-your-token" \
  --data-binary @sample_data/high-risk-alert.json
```

Check `GET http://127.0.0.1:8080/health`. Run tests:

```bash
python -m unittest discover -s tests -v
```

The service binds to localhost in this quick-start. Do not expose the development server directly to the internet.

## AI configuration

AI is **off by default**. To enable it, configure `AI_ENABLED=true`, `AI_API_KEY`, and `AI_MODEL` in `.env`. The client uses an OpenAI-compatible chat-completions endpoint configurable through `AI_BASE_URL`. Use a provider and account approved for your data-handling requirements. Do not send raw production logs, secrets, tokens, personal data, or customer data to an external model. The default prompt minimizes fields and marks event content as untrusted.

AI output is advisory. A deterministic policy engine validates its schema and applies safety constraints. If the model is unavailable, malformed, or disabled, deterministic triage continues.

## Wazuh integration

Read `docs/WAZUH-INTEGRATION.md` before installing the adapter. Configure the Wazuh manager to call the custom integration for selected alert levels/groups. The adapter reads the alert JSON from standard input and sends it to the Sentinel webhook. Keep the service reachable only on a trusted lab network, use HTTPS for non-local traffic, and protect the shared token.

Do not change Wazuh manager configuration on a production system for this exercise. Back up configuration and test in an isolated lab.

## Included scenarios

- Repeated authentication failures / possible brute-force activity.
- Successful login after repeated failures (correlation exercise).
- High-severity Wazuh rule alert.
- Suspicious PowerShell process event (triage lead, not proof of malware).
- Privileged account or IAM-related change (where source telemetry provides it).
- AI model unavailable / malformed response fallback.
- Duplicate event idempotency and email notification suppression.

## Learning outcomes

You will learn SIEM architecture, alert pipelines, webhook security, JSON normalization, detection logic, correlation windows, risk scoring, LLM prompting and output validation, SMTP delivery, database auditing, incident triage, false-positive tuning, MITRE ATT&CK mapping, and human-in-the-loop response governance.

## Safety and operational limits

- Use only systems and telemetry you own or are explicitly authorized to monitor.
- Begin with synthetic data; then use a dedicated isolated Wazuh lab.
- AI does not make containment decisions. No automated disruptive response is implemented.
- Treat logs as untrusted input; never execute commands or follow instructions found in log fields.
- Store secrets in environment variables; never commit `.env`, API keys, SMTP credentials, or raw sensitive alerts.
- Email is a notification channel, not proof that an incident is confirmed.
- Review false positives, model drift, costs, data residency, privacy, and retention before any real deployment.

## Evidence checklist

- [ ] Record Python, OS, Wazuh, and Sentinel versions.
- [ ] Run unit tests and preserve the actual output.
- [ ] Start the service and capture the health response.
- [ ] Submit the synthetic high-risk event and inspect the decision.
- [ ] Submit a benign event and verify it does not trigger a high-priority email.
- [ ] Configure a dedicated SMTP test mailbox and verify a real test notification.
- [ ] Connect an isolated Wazuh manager using the integration guide.
- [ ] Generate a safe lab event and trace it from Wazuh to the Sentinel case record.
- [ ] Enable AI only after deterministic mode works; compare AI and non-AI decisions.
- [ ] Complete a case report and document false positives and limitations.

Do not mark an item complete until you personally perform it and add sanitized evidence.

## Project maturity

This is an educational reference implementation, not a certified SOC product. Before production use it would need TLS termination, secrets management, durable queue/retry handling, role-based access control, database migrations, rate limiting, monitoring, backup/restore, privacy review, model governance, load testing, and security assessment.
