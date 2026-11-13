# DFIR — Digital Forensics & Incident Response Lab

A structured, portfolio-grade Digital Forensics and Incident Response (DFIR) learning environment. This project teaches how to preserve digital evidence, establish integrity, examine host and network artefacts, construct timelines, investigate incidents, and communicate defensible findings.

> **Project status:** The learning material, local Python utilities, synthetic case data, and automated tests are provided. Synthetic data is not evidence from a real incident. No real disk image, memory image, endpoint compromise, forensic acquisition, or completed investigation is claimed. Complete the practical labs and add sanitized evidence before marking them as done.

## Why this project matters

Security analysts must do more than notice an alert. They need to answer: What happened? When? On which system? Which evidence supports the conclusion? What could have changed the evidence? What is still unknown? DFIR provides a repeatable method for answering those questions while protecting evidence integrity.

## Learning outcomes

By completing the project, you will learn to:

- Explain the incident-response lifecycle and the role of forensic readiness.
- Distinguish acquisition, preservation, examination, analysis, and reporting.
- Calculate and verify SHA-256 hashes and maintain a chain-of-custody record.
- Understand Windows event logs, registry, services, scheduled tasks, browser artefacts, and PowerShell logs.
- Understand Linux authentication, process, persistence, package, and system journal artefacts.
- Explain disk imaging, file systems, deleted-file recovery, memory forensics, and network evidence.
- Build a normalized event timeline and correlate events across sources.
- Form evidence-based hypotheses, record limitations, and avoid overclaiming.
- Write a professional incident investigation report.

## Lab architecture

```text
Authorized lab endpoint / synthetic case files
                 |
                 v
       Evidence preservation
       - case identifier
       - source and collector
       - timestamps and timezone
       - SHA-256 manifest
       - chain of custody
                 |
                 v
       Forensic examination
       - Windows / Linux artefacts
       - disk / memory / network
       - event logs and metadata
                 |
                 v
       Timeline + correlation
                 |
                 v
       Findings, confidence, limitations
                 |
                 v
       Incident report and lessons learned
```

## Repository structure

- `docs/01-dfir-foundations.md` — DFIR concepts, roles, and workflow.
- `docs/02-evidence-preservation.md` — evidence handling, integrity, and chain of custody.
- `docs/03-windows-forensics.md` — Windows artefacts and investigation pivots.
- `docs/04-linux-forensics.md` — Linux artefacts and investigation pivots.
- `docs/05-disk-and-filesystem-forensics.md` — disk imaging and file-system concepts.
- `docs/06-memory-forensics.md` — volatile evidence and memory analysis.
- `docs/07-network-forensics.md` — PCAP analysis and network evidence.
- `docs/08-timeline-analysis.md` — timeline normalization and correlation.
- `docs/09-investigation-methodology.md` — hypothesis-led analysis and reporting.
- `docs/10-tools-and-workflows.md` — tool selection and safe workflows.
- `docs/PRACTICAL-LABS.md` — guided beginner-to-advanced exercises.
- `scripts/evidence_manifest.py` — read-only SHA-256 evidence inventory utility.
- `scripts/timeline_builder.py` — CSV event timeline normalizer and sorter.
- `sample_data/` — clearly fictional training data.
- `tests/` — automated tests for the local utilities.
- `templates/` — case notes, chain of custody, and final report templates.

## Quick start — local practice

Requirements: Python 3.9+; no third-party Python packages are required.

From the project directory:

```bash
python scripts/evidence_manifest.py sample_data --output manifest.json
python scripts/timeline_builder.py sample_data/sample-events.csv --output timeline.csv
python -m unittest discover -s tests -v
```

The evidence utility reads files and writes a separate manifest. It does not alter evidence files. The timeline utility sorts supplied CSV events; it does not determine whether an event is malicious.

## Professional workflow

1. **Authorize:** confirm written authority, scope, purpose, and applicable policy.
2. **Prepare:** create a case ID, record system time/timezone, and prepare a clean evidence destination.
3. **Preserve:** minimize interaction with the source; use approved acquisition procedures.
4. **Verify:** calculate cryptographic hashes and document transfers.
5. **Examine:** use appropriate tools on verified working copies where possible.
6. **Analyze:** correlate artefacts, test hypotheses, and document alternative explanations.
7. **Report:** distinguish facts, interpretations, confidence, and limitations.
8. **Close:** securely retain or dispose of evidence according to policy.

## Evidence and completion checklist

- [ ] Record OS, Python version, case ID, and lab scope.
- [ ] Run the evidence manifest against the synthetic sample directory.
- [ ] Independently verify at least one SHA-256 value.
- [ ] Run the timeline builder and explain the event ordering.
- [ ] Execute the automated tests and save the output.
- [ ] Complete one Windows artefact practical in an owned VM.
- [ ] Complete one Linux artefact practical in an owned VM.
- [ ] Analyze a public training PCAP or a capture you created yourself.
- [ ] Complete a case report with evidence references and limitations.
- [ ] Add sanitized screenshots and actual outputs to your portfolio.

Do not tick an item until you have completed it. A provided script or sample file is not proof that you performed the practical.

## Safety, ethics, and evidence handling

- Investigate only devices, accounts, images, and network traffic you own or are explicitly authorized to examine.
- Do not access another person's files, accounts, messages, or devices without authorization.
- Do not upload personal, employer, customer, or production evidence to a public repository.
- Never publish passwords, tokens, private keys, personal data, or unredacted identifiers.
- Preserve originals. Work from verified copies when possible.
- Do not run cleanup, malware, or destructive recovery actions on original evidence.
- Follow local law, organizational policy, and the evidence-handling requirements of your jurisdiction.

## What makes a strong DFIR portfolio submission?

A strong submission includes a clearly scoped case, reproducible steps, original evidence references, SHA-256 verification, a defensible timeline, screenshots of the actual tool output, findings linked to evidence, alternative explanations, limitations, and a concise executive summary.

**Important:** This is an educational lab, not legal advice or a substitute for certified forensic procedures.