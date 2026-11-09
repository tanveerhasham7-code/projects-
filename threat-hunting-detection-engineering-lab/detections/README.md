# Detection Catalogue

Use one specification per detection. Suggested initial detections:

| ID | Detection | Data source | Status |
|---|---|---|---|
| DET-001 | Repeated failed Windows logons | Security 4625 | Planned |
| DET-002 | PowerShell with encoded command indicator | Sysmon 1 / process telemetry | Planned |
| DET-003 | New local account creation | Security 4720 | Planned |
| DET-004 | Addition to privileged local group | Security 4732 / 4728 | Planned |
| DET-005 | Repeated SSH authentication failures | Linux authentication logs | Planned |
| DET-006 | Suspicious parent-child process relationship | Sysmon 1 | Planned |

Status vocabulary: Planned, Implemented, Tested-Pass, Tested-Fail, Tuned, Retired. Use Tested-Pass only after attaching reproducible evidence.

Each detection should have a specification, rule or query, test cases, expected benign activity, observed results, limitations, and a change history.
