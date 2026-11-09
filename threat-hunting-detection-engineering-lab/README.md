# Threat Hunting & Detection Engineering Lab

An advanced blue-team portfolio project for learning how to turn security telemetry into tested detections, investigate suspicious activity, and improve detection quality.

This project complements the Wazuh SOC Home Lab. The Wazuh project focuses on building and operating a SIEM environment; this project focuses on the analyst and detection-engineering work performed with the telemetry.

## Learning outcomes

- Explain telemetry, indicators, behavioral analytics, detection logic, and alert fidelity.
- Build a repeatable detection lifecycle: hypothesis, data source, logic, test, triage, tuning, documentation.
- Work with Windows Security logs, Sysmon events, and Linux authentication telemetry.
- Understand Sigma rules and the process of adapting generic rules to a SIEM.
- Conduct structured threat hunts and document evidence-based conclusions.
- Measure false positives, false negatives, coverage gaps, and detection limitations.
- Map confirmed behaviors to MITRE ATT&CK without forcing mappings.

## Lab approach

Use your existing Wazuh server and Windows/Linux endpoints. Do not reinstall anything just for this project. First inventory what is already installed, then enable or verify the telemetry needed for each exercise. Keep all simulations limited to systems you own or are authorized to test.

## Project status

**Current stage:** Documentation and exercise plans prepared; practical validation remains to be completed.

Hands-on validation, screenshots, alert IDs, event samples, and measured outcomes are intentionally left for the learner to add after running each exercise. No detection is claimed as validated until evidence is recorded.

## Learning path

1. Foundations: telemetry, events, logs, detections, alerts, and hypotheses.
2. Data engineering: Windows Security auditing, Sysmon, Linux auth logs, timestamps, normalization.
3. Detection engineering: Sigma structure, logic, thresholds, exclusions, severity, ATT&CK mapping.
4. Threat hunting: hypothesis-led hunts, scoping, pivoting, timelines, and reporting.
5. Validation: safe simulations, expected telemetry, observed results, tuning, regression tests.
6. Capstone: deliver a detection pack and a professional hunt report.

## Repository map

- docs/: theory, architecture, workflow, and practical guides.
- detections/: detection catalogue and rule-writing standards.
- sigma/: starter Sigma rules for defensive review and adaptation.
- hunts/: hypothesis-led hunt playbooks.
- validation/: test plans and evidence records.
- investigations/: investigation template and case reports.
- evidence/screenshots/: screenshot placeholders; add your own sanitized screenshots.
- scripts/: small local utilities for learning and validation.

## Start here

Read docs/learning-roadmap.md, then docs/existing-lab-audit.md. Complete one exercise at a time. Record the date, lab configuration, exact steps, expected result, observed result, and evidence.

## Safety and evidence rules

- Use synthetic data or your own isolated lab.
- Do not run tests against public systems or other people’s devices.
- Never upload passwords, tokens, private IP details you consider sensitive, personal data, or unredacted logs.
- A rule matching an event does not automatically prove malicious activity.
- Clearly label planned, attempted, passed, failed, and not-tested work.

## Skills demonstrated

SOC analysis • Threat hunting • Windows event analysis • Sysmon • Linux logs • SIEM workflows • Sigma • Detection validation • MITRE ATT&CK • Incident documentation • False-positive tuning

Created as a defensive cybersecurity learning project.
