# Cloud Security Monitoring & Incident Response Lab

A practical blue-team project for learning how to collect, understand, triage, and investigate AWS CloudTrail security events using Python and structured incident-response workflows.

> **Project status:** Documentation, a local Python triage tool, synthetic sample events, and automated tests are included. The sample data is fictional. No AWS account, live cloud telemetry, GuardDuty finding, or production detection is claimed. Complete the optional AWS exercises in an account you own and record real evidence before marking them complete.

## Objectives

By completing this project, you will learn to:

- Understand AWS shared responsibility, IAM, CloudTrail, regions, and security groups.
- Read CloudTrail JSON event records and identify security-relevant activity.
- Triage suspicious identity, authentication, and network-exposure events.
- Use Python to automate first-level event enrichment and prioritization.
- Build an investigation timeline and document containment, eradication, and recovery.
- Map observed behaviors to MITRE ATT&CK where appropriate.
- Distinguish an alert from a confirmed incident and explain false positives.

## Project architecture

```text
AWS account (optional, owned lab only)
        |
        v
AWS CloudTrail management events
        |
        v
JSON event export / synthetic JSONL sample
        |
        v
Python CloudTrail Triage
        |
        +--> Findings (JSON)
        +--> Analyst review and timeline
        +--> Incident report
```

The local workflow works without AWS credentials or cloud charges. AWS exercises are optional and must be performed only in an account you control.

## Repository layout

- `scripts/cloudtrail_triage.py` — standard-library Python event triage tool.
- `sample_data/cloudtrail-events.jsonl` — fictional test events.
- `tests/test_cloudtrail_triage.py` — automated unit tests.
- `docs/LAB-GUIDE.md` — guided learning and optional AWS exercises.
- `docs/DETECTION-USE-CASES.md` — detection logic, investigation pivots, and limitations.
- `templates/incident-report.md` — reusable analyst report.

## Quick start (local, no AWS required)

Requirements: Python 3.9+.

```bash
python scripts/cloudtrail_triage.py sample_data/cloudtrail-events.jsonl
python scripts/cloudtrail_triage.py sample_data/cloudtrail-events.jsonl --json-out findings.json
python -m unittest discover -s tests -v
```

The tool reads one JSON CloudTrail event per line and reports rule matches. It is a learning aid, not a replacement for AWS-native controls, SIEM correlation, or analyst judgment.

## Detection scenarios included

1. Repeated failed AWS console sign-in events.
2. Root account activity.
3. IAM policy or role permission changes.
4. IAM access-key creation.
5. Security-group ingress opened to the world (IPv4 `0.0.0.0/0`).
6. Console sign-in without MFA when the event record contains the relevant field.

Each finding includes a rule ID, severity, event time, actor, event name, source IP, and a short explanation. A rule match is a lead for investigation—not proof of compromise.

## Learning path

1. Read the AWS and CloudTrail foundations in the lab guide.
2. Run the local tool against the synthetic sample.
3. Read each finding and trace it back to the original event.
4. Run the unit tests and understand what each test validates.
5. Complete the investigation exercises and write a report.
6. If you have an AWS account, perform the optional controlled exercises.
7. Export sanitized evidence and update the project status honestly.

## Evidence checklist

- [ ] Python version and operating system recorded.
- [ ] Sample analysis command and output captured.
- [ ] Unit tests executed successfully; output recorded.
- [ ] One investigation report completed using actual findings.
- [ ] Optional AWS CloudTrail event captured from an owned lab account.
- [ ] Screenshots sanitized (account IDs, emails, IPs, keys, and other secrets removed).
- [ ] Detection limitations and false positives documented.

Do not check an item until you have performed it. Never upload access keys, credentials, raw sensitive logs, or unredacted account identifiers.

## Safety and cost

- Use only an AWS account and resources you own or are explicitly authorized to assess.
- Do not create public exposure in a real environment. If testing a security-group rule, use a disposable lab resource and remove the rule immediately.
- Prefer synthetic events for local practice.
- AWS services and data retention can incur charges. Review current AWS pricing and delete lab resources after use.
- Never commit credentials, secret keys, session tokens, or production CloudTrail records.

## Success criteria

A successful learning outcome is a reproducible local analysis, passing tests, a clearly reasoned investigation report, and—if optional cloud exercises are completed—sanitized evidence showing exactly what was tested. No practical completion is implied by the presence of this repository.

---
Built as a defensive cloud-security learning project.