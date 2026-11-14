# Cybersecurity Projects

A portfolio of defensive security, SOC operations, threat hunting, detection engineering, and purple-team labs.

## 1. LogSentry — Security Log Analyzer
A Python tool that analyzes local synthetic authentication logs and highlights repeated failed logins for further review.

[Open LogSentry](./)

## 2. Wazuh SOC Home Lab — Windows + Linux
A structured SIEM/SOC lab covering Wazuh architecture, endpoint telemetry, detection use cases, investigation workflow, incident reporting, and evidence collection.

**Status:** The author reports the lab is installed and has been used for practice. Exact versions, topology, agent health, telemetry, and tested detections are being documented and verified.

[Open Wazuh SOC Home Lab](wazuh-soc-home-lab/README.md)

## 3. Threat Hunting & Detection Engineering Lab
An advanced blue-team project covering telemetry engineering, Sigma rule candidates, hypothesis-led hunts, detection validation, false-positive tuning, MITRE ATT&CK mapping, and investigation reports.

**Status:** Documentation and exercise plans are prepared. Practical tests and screenshots will be added after practice; rules are not presented as validated detections.

[Open Threat Hunting & Detection Engineering Lab](threat-hunting-detection-engineering-lab/README.md)

## 4. Purple Team Three-Machine Lab — Windows + Ubuntu + Kali
An end-to-end, isolated purple-team environment with a Windows monitored endpoint, Ubuntu monitored server, and Kali authorized testing workstation. It combines safe reconnaissance, endpoint telemetry, Wazuh monitoring, detection engineering, threat hunting, incident investigation, and capstone reporting.

**Status:** Theory, architecture, safe exercise plans, and documentation are prepared. No scans, alerts, or successful detections are claimed until the author performs and documents the exercises. Screenshots are reserved for real practical evidence.

[Open Three-Machine Purple Team Lab](purple-team-three-machine-lab/README.md)

## 5. Cloud Security Monitoring & Incident Response Lab — AWS CloudTrail + Python
A cloud blue-team project for analyzing CloudTrail events, triaging IAM and authentication activity, reviewing public network exposure, and documenting cloud incident investigations. Includes a local Python triage tool, fictional JSONL events, automated tests, detection use cases, a guided lab, and an incident-report template.

**Status:** Local tooling, synthetic sample data, documentation, and tests are added. No live AWS telemetry, GuardDuty finding, or production detection is claimed. Optional AWS exercises require an account owned by the author and careful cost review.

[Open Cloud Security Monitoring Lab](cloud-security-monitoring-lab/README.md)

## 6. DFIR — Digital Forensics & Incident Response Lab
A comprehensive forensic investigation project covering evidence preservation, SHA-256 integrity verification, chain of custody, Windows and Linux artefacts, disk and memory forensics, network evidence, timeline reconstruction, hypothesis-led investigation, and professional reporting. Includes two Python utilities, synthetic training data, automated tests, 12 guided practical labs, and reusable case templates.

**Status:** Learning material, local utilities, synthetic examples, and templates are added. No real forensic acquisition, live incident investigation, or practical completion is claimed until exercises are performed and evidence is documented.

[Open DFIR Digital Forensics Lab](dfir-digital-forensics-lab/README.md)

## 7. AI-SOC Sentinel — AI-Assisted SIEM Monitoring & Incident Response
An advanced SOC automation project integrating Wazuh alert ingestion, deterministic event triage and risk scoring, optional LLM-based alert summarization, policy-gated decisions, SQLite case auditing, and SMTP email notifications for human analysts. Includes a Wazuh integration adapter, synthetic alerts, unit tests, theory, architecture, threat model, detection-engineering guidance, lab exercises, and incident-response templates.

**Status:** Implementation and learning materials are committed. The project is not yet connected to a live Wazuh manager, AI provider, or SMTP mailbox. No live alert delivery, model accuracy, or completed practical is claimed. AI is advisory; disruptive containment remains under human approval.

[Open AI-SOC Sentinel](ai-soc-sentinel/README.md)

## 8. Active Directory SOC Monitoring Lab
An isolated Windows domain blue-team project covering AD DS architecture, identity and authentication telemetry, Windows Security event analysis, privileged group monitoring, detection engineering, SOC investigation and evidence-based reporting.

**Status:** Project blueprint, proposed architecture, detection hypotheses and practical backlog are published. Domain deployment, event collection, SIEM integration and detections remain unverified until the author performs the labs and uploads sanitized evidence.

[Open Active Directory SOC Monitoring Lab](active-directory-soc-monitoring-lab/README.md)

## Portfolio principles
- Document only work that was actually performed.
- Separate planned work from tested results.
- Use isolated systems that you own or are authorized to test.
- Sanitize screenshots and logs before publishing.
- Explain limitations and false positives, not only successful outcomes.

Created as a cybersecurity learning portfolio.
