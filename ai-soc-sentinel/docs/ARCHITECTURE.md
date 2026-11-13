# Architecture and data flow

## Components and trust boundaries
1. **Endpoints and Wazuh agents:** generate endpoint telemetry.
2. **Wazuh manager:** decodes events, applies rules, and writes alerts. It remains the SIEM source.
3. **Custom integration adapter:** reads a Wazuh alert from stdin and forwards it to Sentinel.
4. **Webhook API:** validates a shared secret, parses JSON, normalizes fields, and fingerprints events.
5. **Deterministic engine:** assigns baseline severity and risk from Wazuh rule level and observable indicators.
6. **AI triage client:** optionally summarizes a minimized event and suggests read-only checks.
7. **Policy gate:** combines deterministic and AI output; AI cannot downgrade a deterministic critical finding or issue response actions.
8. **SQLite audit store:** records each unique case and notification state.
9. **SMTP notifier:** sends a high-risk summary to the analyst.

## Event lifecycle

```text
Receive -> Authenticate -> Parse -> Normalize -> Fingerprint
  -> Deterministic triage -> Optional AI enrichment -> Policy decision
  -> Persist audit -> Email if threshold met -> Human investigation
```

## Reliability notes
This educational service uses a synchronous webhook and local SQLite. Production needs a durable queue, bounded retries, dead-letter handling, transactional outbox, migrations, horizontal scaling, and delivery monitoring. Verify actual Wazuh integration delivery behavior for the installed version.

## Network placement
Place Sentinel on a protected management segment reachable only from the Wazuh manager. Use a reverse proxy with TLS for cross-host traffic. Restrict inbound access, rotate the token, and never expose the development server publicly.
