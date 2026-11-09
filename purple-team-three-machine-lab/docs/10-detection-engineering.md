# 10 — Detection Engineering for the Three-Machine Lab

## Detection lifecycle
1. Define a behavior in plain language.
2. Identify the source host and telemetry.
3. Confirm required fields are collected.
4. Write detection logic and expected benign causes.
5. Run a safe test.
6. Compare expected and observed events.
7. Tune carefully.
8. Document limitations and version changes.

## Starter detection ideas

| ID | Behavior | Data source | Caution |
|---|---|---|---|
| PT-001 | Repeated SSH failures | Ubuntu auth log | User mistakes and stale clients |
| PT-002 | New local Windows account | Security 4720 | Approved provisioning |
| PT-003 | Windows failed logon | Security 4625 | Single failure is weak evidence |
| PT-004 | PowerShell process start | Sysmon 1 | PowerShell is used legitimately |
| PT-005 | Unusual web paths | Web access log | Crawlers and broken links |
| PT-006 | Unexpected exposed service | Nmap inventory | Exposure is not necessarily vulnerability |

## Rule implementation
Use the detection catalogue and rule template. Wazuh rules use Wazuh-specific XML syntax and field mappings. Sigma is a generic detection format and does not automatically become a Wazuh rule. Confirm the actual event schema and test the rule in your own environment before enabling it.

## Tuning
Document why an exclusion is needed. Avoid broad exclusions such as ignoring all PowerShell or all failed logons. Keep original evidence and compare alert counts before and after a change.

## Validation status
All detections begin as Planned. Update to Implemented only after creating the rule. Update to Tested-Pass only after the expected telemetry and alert are observed and documented.
