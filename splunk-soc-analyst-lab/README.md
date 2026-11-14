# Splunk SOC Analyst Lab — SIEM, SPL, Detection Engineering and Incident Response

## 1. Project overview
A defensive SOC project for learning Splunk through a small isolated lab. You will plan a deployment, onboard Windows or synthetic events, validate data, search with SPL, investigate authentication and endpoint activity, design detections, build dashboard concepts, hunt for suspicious behavior, and write an incident report.

**Status:** This is a project blueprint. Splunk installation, forwarder configuration, live data ingestion, SPL execution, alerts, dashboards, and investigations are not claimed as completed. Add genuine, sanitized evidence after performing each phase.

## 2. Learning outcomes
- Explain Splunk architecture and data flow.
- Plan a safe local or approved training deployment.
- Onboard Windows or synthetic security events.
- Validate index, host, source, sourcetype, fields, and timestamps.
- Write SPL searches and summarize events.
- Investigate authentication, process, and network activity.
- Document detection logic, thresholds, and false positives.
- Design alerts and dashboards.
- Conduct a hypothesis-led hunt and triage a case.
- Produce an evidence-based incident report.

## 3. Proposed architecture
    [Windows endpoint / synthetic source]
                    |
           [Universal Forwarder]
                    |
           [Splunk receiving input]
                    |
                 [Indexer]
                    |
               [Search Head]
                    |
             [SOC analyst / SPL]

A single-instance deployment may combine several roles for learning. A separate forwarder is optional initially. Check current Splunk product, training, trial, and license availability before selecting an environment.

## 4. Safety, cost and privacy
- Use systems and accounts you own or are authorized to administer.
- Keep management interfaces private; do not expose Splunk Web or receiving ports publicly.
- Use strong unique credentials and least privilege.
- Check current product, trial, license, and ingestion terms before deployment.
- Monitor infrastructure or cloud costs and stop unused resources.
- Use synthetic events where real data is unnecessary.
- Sanitize hostnames, usernames, IP addresses, command lines, and screenshots.
- Never commit passwords, tokens, private keys, license files, or customer data.

## 5. Prerequisites
Basic Windows and networking knowledge, a supported Splunk learning environment, and a permitted Windows host/VM or sample dataset. A Universal Forwarder is optional. Check system requirements for the exact version. Start with one Splunk instance and one source; avoid overloading your computer with multiple large VMs.

## 6. Implementation phases

### Phase 1 — Plan
Select local, cloud, or sample-data learning. Record product edition/version, OS, resources, topology, trust boundary, data sources, licensing, and cost checks.
**Evidence:** architecture diagram and environment worksheet.

### Phase 2 — Deploy
Download only from official sources, follow version-specific instructions, create a strong admin credential, restrict management access, and validate service status.
**Evidence:** sanitized version and service-status screenshot. Never include credentials.

### Phase 3 — Onboard data
Start with Windows Security events or synthetic data. If using a forwarder, configure only the required source and destination. Validate index, sourcetype, host, source, timestamps, and recent event arrival.
**Evidence:** sanitized event sample and ingestion validation notes.

### Phase 4 — SPL fundamentals
Practice index/time filters, keywords, field filters, Boolean logic, stats, table, sort, dedup, top, eval, and where.
**Evidence:** query notebook with objective, SPL, time range, result summary, and limitations.

### Phase 5 — Authentication monitoring
Relevant Windows event families may include 4624, 4625, 4648, 4672, 4768, 4769, 4771, and 4776. Verify event meaning and availability for your source.

Detection hypotheses:
1. Repeated failures from one source.
2. One source targeting many accounts.
3. Successful logon after a burst of failures.
4. Privileged logon from an unusual host or time.
5. Explicit credential use requiring review.

A high count does not prove malicious behavior. Consider user errors, VPNs, shared NAT, service accounts, and scheduled jobs.

### Phase 6 — Endpoint and network investigations
Use process, Sysmon, Defender, firewall, DNS, or network telemetry when available. Review process ancestry, command line, destination, user, host, and time.

Detection hypotheses:
1. Unusual process execution from a user-writable path.
2. Suspicious parent-child process relationship.
3. Unexpected outbound connection.
4. Endpoint protection alert followed by related process activity.

These are investigation hypotheses, not validated detections until tested.

### Phase 7 — Alerts and dashboards
Design panels for authentication failures, endpoint alerts, ingestion health, and open cases. For every alert document query, schedule, threshold, severity, confidence, required fields, suppression, false positives, and response guidance. Feature availability depends on product edition.

### Phase 8 — Threat hunting
Write a testable hypothesis, identify data sources, validate time coverage, run bounded searches, pivot across entities, build a timeline, record evidence and gaps, and recommend detection improvements.

### Phase 9 — SOC case and report
Triage a fictional or authorized case. Preserve exact SPL, time range, timezone, event references, and sanitized screenshots. Separate facts from assumptions. Follow approved response procedures.

## 7. SPL query starter pack
Examples only. Replace index and fields with those present in your environment.

**Recent events**
    index=security earliest=-24h
    | head 50

**Failed logons by user and source**
    index=windows EventCode=4625
    | stats count by user src host
    | sort - count

**Successful and failed logons**
    index=windows (EventCode=4624 OR EventCode=4625)
    | stats count by EventCode user host

**Top event-producing hosts**
    index=security
    | stats count by host
    | sort - count
    | head 10

**Process activity**
    index=endpoint
    | table _time host user parent_process process_name command_line
    | sort - _time

**Network activity**
    index=network
    | stats count by src dest dest_port action
    | sort - count

A zero-result search may indicate a wrong index, time range, field, sourcetype, parsing issue, or missing ingestion. It does not prove the activity did not occur.

## 8. Detection specification template
- Detection name and objective.
- Threat behavior / hypothesis.
- Data sources and required fields.
- Exact SPL and tested version.
- Schedule and time window.
- Threshold rationale and baseline.
- Severity, confidence, and impacted entities.
- False positives and exclusions.
- Investigation and escalation steps.
- Test data, observed results, tuning, owner, and review date.

## 9. Practical exercise backlog
1. Draw Splunk architecture.
2. Complete environment and safety worksheet.
3. Access or install a permitted Splunk environment.
4. Record product/version and service status.
5. Onboard Windows Security or synthetic events.
6. Validate index, host, source, sourcetype, and timestamps.
7. Run basic searches and time filters.
8. Practice stats, table, sort, top, and dedup.
9. Analyze failed logons by user and source.
10. Investigate success-after-failures.
11. Review process creation and parent-child relationships.
12. Analyze a network dataset.
13. Write two detection specifications with false-positive notes.
14. Design an authentication and endpoint dashboard.
15. Conduct a hypothesis-led threat hunt.
16. Complete a case triage worksheet and incident report.

## 10. SOC investigation playbook
1. **Validate:** confirm alert, source, query, time range, and fields.
2. **Identify:** determine impacted account, host, source, destination, and process.
3. **Scope:** search related activity across relevant sources.
4. **Timeline:** order evidence and record timezone.
5. **Assess:** compare with baseline and business context.
6. **Classify:** benign, suspicious/needs evidence, or likely incident according to policy.
7. **Escalate:** follow organizational procedures.
8. **Document:** preserve searches, evidence, decisions, and limitations.
9. **Improve:** tune detection and record lessons.

## 11. Case report template
- Case ID:
- Date/time opened and timezone:
- Analyst:
- Detection / alert:
- Severity and confidence:
- Summary:
- Affected accounts and assets:
- Timeline:
- Exact SPL and time range:
- Evidence references:
- Analysis:
- Scope and impact:
- False-positive checks:
- Actions taken by authorized responders:
- Recommendations:
- Closure reason:
- Lessons learned:

## 12. Suggested evidence structure
    splunk-soc-analyst-lab/
    ├── README.md
    ├── evidence/
    │   ├── 01-architecture/
    │   ├── 02-environment/
    │   ├── 03-data-onboarding/
    │   ├── 04-spl-searches/
    │   ├── 05-detections/
    │   ├── 06-dashboards/
    │   ├── 07-threat-hunting/
    │   └── 08-investigation-reports/
    ├── queries/
    │   ├── authentication/
    │   ├── endpoint/
    │   └── network/
    ├── detections/
    └── reports/

Only add genuine evidence. Do not create placeholder screenshots that look like completed work.

## 13. Success criteria
Call the project practically completed only when you can demonstrate a documented working environment, successful data ingestion, SPL queries run against actual lab or clearly labeled synthetic events, at least two tested and tuned detections, a dashboard/report, a completed hunt and case report, and sanitized evidence with honest limitations.

## 14. Official references
- [Splunk Documentation](https://docs.splunk.com/)
- [Splunk Enterprise installation](https://docs.splunk.com/Documentation/Splunk/latest/Installation/InstallonWindows)
- [Universal Forwarder](https://docs.splunk.com/Documentation/Forwarder/latest/Forwarder/Abouttheuniversalforwarder)
- [SPL Search Reference](https://docs.splunk.com/Documentation/Splunk/latest/SearchReference/)
- [Splunk CIM](https://docs.splunk.com/Documentation/CIM/latest/User/Overview)
- [Splunk Security Content](https://research.splunk.com/)
- [Splunk Education](https://www.splunk.com/en_us/training.html)
- [MITRE ATT&CK](https://attack.mitre.org/)
- [Microsoft logon auditing](https://learn.microsoft.com/en-us/windows/security/threat-protection/auditing/basic-audit-logon-events)

## 15. Project status
**Published:** blueprint, architecture, phased plan, SPL examples, detection hypotheses, 16 exercises, playbook, templates, safety guidance, and references.

**Not yet verified:** deployment, forwarder setup, live data ingestion, SPL execution, alert creation, dashboards, threat hunting, or completed investigation. Update only when supported by your own sanitized evidence.
