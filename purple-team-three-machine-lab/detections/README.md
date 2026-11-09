# Detection Catalogue

| ID | Behavior | Telemetry | Status |
|---|---|---|---|
| PT-001 | Repeated SSH authentication failures | Ubuntu authentication logs | Planned |
| PT-002 | Windows failed logon | Security 4625 | Planned |
| PT-003 | New Windows account | Security 4720 | Planned |
| PT-004 | PowerShell process with unusual arguments | Sysmon 1 | Planned |
| PT-005 | Unusual web path patterns | Web access log | Planned |
| PT-006 | Unexpected exposed service | Authorized Kali inventory + asset baseline | Planned |

A port being open is an exposure observation, not proof of vulnerability. A failed login or PowerShell process is not automatically malicious. Define context, benign causes, and validation before enabling a rule.