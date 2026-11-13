# Threat model and safeguards

## Assets
Webhook token, AI provider key, SMTP credential, event metadata, analyst mailbox, SQLite history, and decision-pipeline integrity.

## Trust boundaries
Wazuh manager to webhook; webhook to model provider; service to SMTP; service filesystem/database; analyst email client.

## Threats and controls
- Unauthorized webhook: shared token, constant-time comparison, network restriction, TLS outside localhost, rotation.
- Prompt injection in logs: untrusted-data prompt, no tools or execution privileges, strict JSON parsing, deterministic policy gate.
- Hallucination/downgrade: AI advisory only; schema/confidence validation; deterministic critical floor.
- Credential leakage: environment variables locally, .gitignore, dedicated credentials, production secret manager.
- Email data leakage: authenticated SMTP, minimized content, controlled recipient, no secrets.
- Replay/duplicate storm: fingerprint and unique key; production needs rate limiting and replay protection.
- Database tampering/loss: restrictive permissions and backups; production needs centralized immutable audit.
- Denial of service: production needs request limits, rate limiting, reverse proxy, queue, and bounded timeouts.

## Residual risks
This educational service lacks RBAC, rate limiting, TLS termination, signed timestamped requests, and a durable queue. Model-provider data handling is external. Do not deploy this starter publicly.
