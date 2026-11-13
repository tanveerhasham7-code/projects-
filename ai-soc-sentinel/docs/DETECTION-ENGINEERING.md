# Detection engineering use cases

These are investigation leads, not proof of malicious activity.

| Use case | Telemetry clue | Analyst validation |
|---|---|---|
| Password guessing | Repeated authentication failures from one source | Time window, targeted accounts, source context, successful logins |
| Valid account misuse | Login after failures or unusual context | User baseline, MFA, device, source network, session activity |
| Suspicious PowerShell | Encoded command or download/execute-like string | Process tree, parent, script-block logs, signer, change ticket |
| Privilege change | Group membership, sudo, role or policy modification | Actor authorization, ticket, target identity, follow-on actions |
| Endpoint alert | Wazuh syscheck/rootcheck/malware group | Original event, file hash/path, process lineage, endpoint state |

## Advanced correlation extension
A sequence analytic can correlate several failures for the same account/source, a later successful login, and a new process or privilege change soon after. The starter code does **not** implement stateful multi-event correlation windows. Add a time-window store, grouping keys, late-event handling, duplicate handling, and clock-skew tests as an advanced extension. Do not claim correlation from one isolated event.

## Tuning workflow
State the hypothesis, identify telemetry and required fields, create benign/suspicious tests, record false/true positives and misses, tune with documented reasons, map to ATT&CK only when supported, and review after environment changes.
