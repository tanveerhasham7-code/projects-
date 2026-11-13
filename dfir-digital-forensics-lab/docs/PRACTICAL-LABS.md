# DFIR Practical Labs — Beginner to Advanced

Complete the labs in order. Use only your own isolated VMs, synthetic data, or training material whose license permits analysis. Do not use employer, customer, or third-party evidence.

## Level 1 — Foundations

### Lab 1: Case setup and scope
- Create a unique case ID.
- Write the investigation question and scope.
- Record authorization, systems, time window, and exclusions.
- Create folders for originals, working copies, output, and reports.
- Deliverable: sanitized case setup note.

### Lab 2: Evidence hashing
- Run the evidence manifest script against `sample_data/`.
- Compare one file hash using an independent operating-system command.
- Change a disposable copy and observe that its hash changes.
- Deliverable: manifest and short explanation.
- Do not modify the supplied original sample.

### Lab 3: Chain of custody
- Complete the chain-of-custody template for a fictional evidence transfer.
- Identify missing fields and explain why each matters.
- Deliverable: completed training record clearly labeled fictional.

## Level 2 — Host forensics

### Lab 4: Windows event-log review
- Use your Windows VM.
- Inspect Security, System, and PowerShell logs where available.
- Identify three events and record provider, event ID, timestamp, account, and meaning.
- Deliverable: evidence table with screenshots from your VM.

### Lab 5: Sysmon process investigation
- If Sysmon is installed, review process creation telemetry.
- Trace one process to its parent and identify user, command line, and time.
- Correlate with a related network or file event if present.
- Deliverable: process tree and evidence-backed notes.
- Do not run malware or untrusted payloads.

### Lab 6: Linux authentication review
- Use your own Linux VM.
- Review SSH/authentication logs and system journal.
- Identify successful/failed logins if present and inspect relevant service events.
- Deliverable: short timeline with timezone and source paths.

## Level 3 — Disk, memory, and network

### Lab 7: Disk-image examination
- Use a training image or a disk image created from a disposable VM you own.
- Verify image hash, inspect partitions, and review selected file metadata with an approved tool.
- Deliverable: acquisition notes, hash, screenshots, and limitations.

### Lab 8: Memory-forensics introduction
- Use an authorized training memory image.
- Record image hash, framework version, and OS identification.
- Examine process and network views with documented commands.
- Deliverable: output excerpts and interpretation.
- If no suitable image is available, submit a tool-workflow worksheet instead.

### Lab 9: PCAP investigation
- Use your own lab capture or a permitted training PCAP.
- Hash the capture, inspect protocol distribution, DNS, and one TCP conversation.
- Deliverable: packet references, findings, and capture limitations.

## Level 4 — Correlation and case investigation

### Lab 10: Timeline reconstruction
- Use the supplied CSV or map events from your own lab into its schema.
- Run the timeline builder.
- Identify a sequence, timezone uncertainty, and at least one alternative explanation.
- Deliverable: normalized timeline and written analysis.

### Lab 11: Multi-source investigation
- Combine at least two authorized sources (for example, Windows event logs and DNS/proxy logs).
- Build one hypothesis and one alternative hypothesis.
- Link every key statement to an evidence ID.
- Deliverable: investigation worksheet.

### Lab 12: Capstone DFIR case
Produce a complete case report with:
- Scope and authorization.
- Evidence register and hashes.
- Chain-of-custody record.
- Timeline.
- At least three findings with evidence references.
- Facts versus interpretations.
- Confidence and limitations.
- Containment/recovery recommendations.
- Lessons learned.

## Practical evidence rules

- A screenshot must come from the actual tool and environment used.
- Keep originals private and preserve their hashes.
- Sanitize hostnames, usernames, IPs, email addresses, account IDs, and personal data before publishing.
- Do not fabricate tool output or mark a lab complete based on reading instructions.
- State clearly whether data is synthetic, training-provided, or collected in your own lab.
