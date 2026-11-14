# Windows Advanced Security Monitoring Lab

**Track:** Blue Team / Junior SOC Analyst / Windows Detection Engineering  
**Level:** Beginner to Advanced  
**Status:** Detailed blueprint published. Deployment, event generation, Sysmon installation, forwarding, detections and investigation results are not yet verified.

## 1. Project overview
Build a controlled Windows endpoint monitoring environment and learn to collect, interpret and investigate security telemetry. This project complements the [Windows Advanced Security Monitoring Learning Journey](https://github.com/tanveerhasham7-code/learning-journey/tree/main/windows-advanced-security-monitoring).

Progress from native event logs to advanced audit policy, Sysmon, PowerShell logging, endpoint protection telemetry, centralized collection and detection engineering. Start with one Windows test VM and add optional components later.

**Portfolio integrity:** This repository currently contains the blueprint, designs, commands, exercise plans and templates. It does not claim Sysmon is installed, events have been generated, a SIEM is connected or detections have been validated. Add screenshots and outputs only after performing the task.

## 2. Learning outcomes
1. Explain Windows providers, channels, event records and telemetry flow.
2. Review effective audit policy and validate event generation.
3. Install and validate Sysmon safely in a test VM.
4. Interpret process, network, DNS, registry and file telemetry.
5. Review PowerShell logging and privacy implications.
6. Inspect Defender, Firewall, services and scheduled-task telemetry.
7. Design centralized collection and validate forwarding.
8. Write testable detection hypotheses and tune false positives.
9. Investigate endpoint alerts using timelines and evidence.
10. Produce professional case reports with limitations and recommendations.

## 3. Proposed architecture

### Minimum lab
- One Windows 10/11 VM or spare device owned by the learner.
- Local Event Viewer and PowerShell.
- Sysmon from official Microsoft Sysinternals source (optional initially).
- A notes/evidence folder with sanitized outputs.

### Extended lab
- Windows Server or second endpoint for central policy/collection (optional).
- Windows Event Collector (WEC) with Windows Event Forwarding (WEF), or a SIEM agent.
- Wazuh manager or another SIEM (optional).
- Analyst workstation for queries, timelines and reporting.

~~~text
+--------------------------+
| Windows test endpoint    |
| Security / System logs   |
| PowerShell / Defender    |
| Sysmon (optional)        |
+------------+-------------+
             |
       WEF or SIEM agent
             |
             v
+--------------------------+
| WEC / SIEM collector     |
| Parsing and retention    |
+------------+-------------+
             |
             v
+--------------------------+
| SOC analyst              |
| Search -> triage         |
| timeline -> case report  |
+--------------------------+
~~~

This is a proposed logical architecture, not a running environment.

## 4. Safety and preparation
- Use only systems you own or are explicitly authorized to administer.
- Prefer a disposable VM with a snapshot before configuration changes.
- Keep test systems isolated or appropriately firewalled.
- Do not disable Defender, Firewall or audit controls to manufacture alerts.
- Do not execute malware, destructive commands or unauthorized simulations.
- Use fictional test accounts and non-sensitive data.
- Do not publish credentials, tokens, private keys, raw personal data or unredacted logs.
- Review privacy and retention before enabling broad PowerShell transcription.
- Download Sysmon only from Microsoft's official Sysinternals page.

## 5. Staged build plan

### Phase 0 — Baseline and scope
Record Windows edition/version, hostname alias, VM resources, timezone, network mode and authorization scope. Take a clean snapshot if using a VM.
**Validation:** Owner, scope and rollback method documented.

### Phase 1 — Native event-log exploration
Explore Application, System, Security and relevant Operational channels. Use Event Viewer and read-only Get-WinEvent commands. Record provider, ID, computer, timestamp and fields.
**Validation:** At least one benign event retrieved and explained.

### Phase 2 — Advanced audit policy
Review effective settings with:

~~~cmd
auditpol /get /category:*
~~~

Select one safe use case, enable the minimum required setting in the lab, perform a controlled action and verify the event on the correct computer.
**Validation:** Save policy output and event record, explaining why it was generated.

### Phase 3 — Sysmon
Review official documentation and configuration. Install in a test VM only after reviewing binary source and configuration. Verify service and Microsoft-Windows-Sysmon/Operational channel.

~~~powershell
.\Sysmon64.exe -?
.\Sysmon64.exe -accepteula -i .\sysmon-lab-config.xml
Get-Service Sysmon*
Get-WinEvent -LogName 'Microsoft-Windows-Sysmon/Operational' -MaxEvents 20
~~~

Use a reviewed local configuration file. **Validation:** Record version, service state, configuration provenance and an actual event.

### Phase 4 — PowerShell logging
Identify installed PowerShell versions and channels. Review Script Block Logging, module logging and transcription. Enable only required lab settings, protect transcript output and run a harmless test.
**Validation:** Confirm actual events and document privacy limitations.

### Phase 5 — Endpoint activity review
Review process creation, network, DNS, registry, file, Defender, Firewall, service and scheduled-task information. Start with read-only inventory.
**Validation:** Complete two event analyses with actor/process/host context and benign explanations.

### Phase 6 — Centralized collection (optional)
Choose WEF/WEC or a SIEM agent. Define channels, filters, access controls, transport security, retention and health checks. Generate a harmless event and verify at source, collector and SIEM.
**Validation:** Preserve source and destination evidence; document gaps or delays.

### Phase 7 — Detection and investigation
Write detection specifications, test with safe activity or synthetic records, tune false positives and prepare a case report.
**Validation:** At least two detections have documented test results and one investigation timeline is complete.

## 6. Windows telemetry reference

| Source | Example telemetry | SOC use |
|---|---|---|
| Security | 4624, 4625, 4688, 4720, 4732, 1102 | Logons, process creation, account changes, audit integrity |
| Sysmon | 1, 3, 7, 8, 10, 11, 12–14, 22 | Process, network, image, process access, file, registry and DNS |
| PowerShell | 4103, 4104 and engine events where applicable | Module and script-block analysis |
| Defender | Defender Operational events | Detection, remediation and protection health |
| Firewall | Configured profile/rule and traffic logs | Network policy and traffic review |
| Task Scheduler | Operational task events | Scheduled execution and persistence |
| System | Service and driver events | Service lifecycle and system changes |

Availability depends on Windows version, provider, audit policy, Sysmon configuration and collection method. Verify IDs and fields on the actual system.

## 7. Detection use-case backlog

These are hypotheses, not deployed or validated rules.

### WIN-DET-01 — Unusual process execution
- **Sources:** Security 4688 and/or Sysmon 1.
- **Hypothesis:** A process from an unusual path or unexpected parent requires review.
- **Review:** Image, command line, user, parent, host role and hash/signature.
- **False positives:** Software deployment, updaters and administration tools.

### WIN-DET-02 — Suspicious PowerShell context
- **Sources:** PowerShell Operational, process telemetry and optional EDR.
- **Hypothesis:** PowerShell activity outside a user's normal role may be suspicious.
- **Review:** Script-block records if available, parent, user, host, network and files.
- **False positives:** IT automation and support scripts.

### WIN-DET-03 — Process-to-network correlation
- **Sources:** Sysmon 1 and 3, DNS Event 22 if configured.
- **Hypothesis:** An unexpected process followed by an unusual connection deserves review.
- **Review:** Process, destination, protocol, host role and application purpose.
- **False positives:** Browsers, updaters, sync clients and enterprise agents.

### WIN-DET-04 — Sensitive registry modification
- **Sources:** Sysmon 12–14 and relevant native events.
- **Hypothesis:** Unexpected change to a sensitive configuration or autorun location may indicate tampering.
- **Review:** Path, value, actor/process, timestamp, host and approved change.
- **False positives:** Installers, updates and policy refresh.

### WIN-DET-05 — New or modified service
- **Sources:** System/service events, Security and Sysmon.
- **Hypothesis:** Service change outside approved maintenance may require review.
- **Review:** Service, binary path, start account, creator and authorization.
- **False positives:** Software installation and IT management.

### WIN-DET-06 — Scheduled task change
- **Sources:** Task Scheduler Operational, process and Security telemetry.
- **Hypothesis:** A task with unusual executable or principal may require investigation.
- **Review:** Task path, author, trigger, action, principal and related events.
- **False positives:** Software updates and approved maintenance.

### WIN-DET-07 — Security control health change
- **Sources:** Defender, Firewall, audit policy and system telemetry.
- **Hypothesis:** Unexpected reduction in endpoint protection or logging creates a visibility gap.
- **Review:** Actor, policy, management system and maintenance window.
- **False positives:** Approved maintenance and centrally managed policy.

### WIN-DET-08 — Audit log cleared
- **Sources:** Security Event 1102 and collector health.
- **Hypothesis:** A cleared Security log may indicate evidence removal or approved maintenance.
- **Review:** Actor, host, time, surrounding events and centralized copies.
- **False positives:** Authorized troubleshooting, which must be documented.

## 8. Practical exercise backlog

All tasks begin as Planned. Change status only after performing the exercise and reviewing evidence.

| ID | Exercise | Expected evidence | Status |
|---|---|---|---|
| LAB-01 | Document host baseline and scope | Sanitized OS/VM inventory | Planned |
| LAB-02 | Explore Event Viewer channels | Channel/provider notes | Planned |
| LAB-03 | Retrieve events with Get-WinEvent | Commands and output | Planned |
| LAB-04 | Review effective audit policy | auditpol output | Planned |
| LAB-05 | Generate benign process event | 4688 or equivalent | Planned |
| LAB-06 | Review official Sysmon configuration | Configuration notes | Planned |
| LAB-07 | Install and validate Sysmon in test VM | Version, service and channel | Planned |
| LAB-08 | Analyze Sysmon process event | Event 1 field analysis | Planned |
| LAB-09 | Review network or DNS telemetry | Event 3/22 if configured | Planned |
| LAB-10 | Review PowerShell logging | Channel and event evidence | Planned |
| LAB-11 | Inspect Defender and Firewall | Sanitized status output | Planned |
| LAB-12 | Inventory services and tasks | Read-only output | Planned |
| LAB-13 | Write and test two detection hypotheses | Logic, results and tuning | Planned |
| LAB-14 | Validate WEF/SIEM forwarding (optional) | Source-to-collector evidence | Planned |
| LAB-15 | Investigate synthetic endpoint scenario | Timeline and case report | Planned |

## 9. Detection specification template

~~~yaml
detection_id: WIN-DET-EXAMPLE
name: Example endpoint behavior
status: experimental
hypothesis: Describe behavior that should be investigated.
data_sources:
  - Sysmon Event ID 1
required_fields:
  - Computer
  - Image
  - CommandLine
  - ParentImage
  - User
logic_summary: Describe filter or correlation in plain language.
false_positives:
  - Approved administrative activity
limitations:
  - Requires relevant telemetry and configuration
response:
  - Validate host, user, process lineage and business context
~~~

## 10. Investigation playbook
1. Validate alert logic and raw source event.
2. Confirm host, user, timestamp, provider and channel.
3. Identify process, parent and command line.
4. Search related PowerShell, registry, file, network and Defender telemetry.
5. Build a timeline with explicit timezone.
6. Compare activity with host role, baseline and approved changes.
7. Scope related endpoints and identities.
8. Preserve relevant exports and query details.
9. Escalate or recommend containment only under approved procedures.
10. Document findings, confidence, gaps and next steps.

## 11. Evidence and report templates

### Lab evidence record

~~~markdown
# LAB-XX — Exercise title
Date/time and timezone:
Host alias and Windows version:
Objective:
Authorized scope:
Commands/settings:
Expected result:
Actual result:
Event provider/channel/ID:
Evidence filenames:
Interpretation:
Limitations and troubleshooting:
Status: Planned / In Progress / Verified
~~~

### Case report
- Case ID and alert:
- Severity and rationale:
- Summary:
- Affected host and user:
- Timeline (timezone stated):
- Evidence and query references:
- Findings:
- Assessment: Benign / Suspicious / Confirmed incident / Inconclusive
- Scope and impact:
- Actions and approvals:
- Recommendations:
- Detection gaps and lessons learned:

## 12. Suggested repository structure

~~~text
windows-advanced-security-monitoring-lab/
├── README.md
├── docs/
│   ├── ARCHITECTURE.md
│   ├── AUDIT-POLICY.md
│   ├── SYSMON-CONFIGURATION.md
│   ├── POWERSHELL-LOGGING.md
│   ├── EVENT-REFERENCE.md
│   └── INVESTIGATION-RUNBOOK.md
├── detections/
│   ├── README.md
│   └── specifications/
├── queries/
│   ├── powershell/
│   └── siem/
├── sample-data/
│   └── README.md
├── evidence/
│   └── README.md
├── reports/
│   └── CASE-REPORT-TEMPLATE.md
└── lab-notes/
    └── TEMPLATE.md
~~~

Create additional files when there is useful content or real evidence. Never commit secrets or unredacted logs.

## 13. Success criteria
- Host and authorized lab scope documented.
- At least one native event generated and explained.
- Effective audit settings reviewed and validated.
- Sysmon installed and validated if in scope.
- PowerShell logging tested if included.
- At least two detection hypotheses have test results and tuning notes.
- One investigation timeline and case report complete.
- Evidence sanitized and reproducible.

## 14. References
- [Microsoft Learn — Windows Security Auditing](https://learn.microsoft.com/en-us/windows/security/threat-protection/auditing/)
- [Microsoft Learn — Advanced Security Audit Policy](https://learn.microsoft.com/en-us/windows/security/threat-protection/auditing/advanced-security-audit-policy-settings)
- [Microsoft Sysinternals — Sysmon](https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon)
- [Microsoft Learn — PowerShell Logging](https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.core/about/about_logging)
- [Microsoft Learn — Windows Event Forwarding](https://learn.microsoft.com/en-us/windows/security/operating-system-security/device-management/use-windows-event-forwarding-to-assist-in-intrusion-detection)
- [Wazuh Documentation](https://documentation.wazuh.com/current/)
- [SigmaHQ](https://sigmahq.io/)

## Current status
**Published:** Project blueprint, architecture, build phases, telemetry reference, eight detection hypotheses, 15 exercises, investigation playbook and evidence templates.  
**Pending validation:** VM setup, audit policy, Sysmon, PowerShell logging, forwarding, SIEM integration, detections, screenshots and case reports.