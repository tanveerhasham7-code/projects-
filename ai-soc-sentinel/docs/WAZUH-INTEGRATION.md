# Wazuh integration guide

This is a lab integration outline. Exact paths, permissions, and syntax vary by Wazuh version and installation method. Verify against documentation for the installed version before editing manager configuration.

## Prerequisites
- Working Wazuh manager in an isolated lab.
- Sentinel API reachable from the manager.
- Shared webhook token configured on both sides.
- Python 3 on the manager.
- Backup of manager configuration.

## Adapter installation
Copy `integrations/wazuh/custom-ai-soc.py` to the manager custom integrations directory (commonly `/var/ossec/integrations/`) and set executable permissions. Verify the Python interpreter path.

## Secret configuration
The adapter reads `AI_SOC_WEBHOOK_URL` and `AI_SOC_WEBHOOK_TOKEN` from its environment. Do not hard-code the token in a world-readable script. Use a secure supported configuration mechanism and restrict ownership/permissions.

## Configure selected alerts
Use the Wazuh custom integration configuration documented for your exact version. Begin with a narrow alert-level threshold and selected groups. Back up `ossec.conf`, validate configuration, and restart only in the lab maintenance window. The integration command name and arguments must match the installed Wazuh version.

## End-to-end validation
1. Confirm Sentinel health from the manager host.
2. Send a synthetic event directly to the webhook.
3. Trigger a safe authentication event on a lab endpoint.
4. Confirm Wazuh generates an alert.
5. Confirm the integration forwards it.
6. Confirm Sentinel stores one unique case.
7. Confirm only qualifying events send email.
8. Compare Sentinel fields to the original alert and document mapping gaps.

## Troubleshooting
- HTTP 401: token mismatch or missing token.
- Connection refused: service bind address, route, or firewall.
- Timeout: manager cannot reach Sentinel.
- No alert: Wazuh rule did not match or integration filter excluded it.
- Duplicate ignored: event fingerprint already exists.
- No email: threshold not reached, SMTP disabled/misconfigured, or SMTP delivery failed.

Never publish tokens, SMTP passwords, API keys, or raw production alerts.
