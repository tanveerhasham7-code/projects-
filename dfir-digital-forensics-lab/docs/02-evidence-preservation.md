# 02 — Evidence Preservation, Integrity, and Chain of Custody

## 1. Why preservation comes first

Analysis can change metadata, access times, logs, or other system state. The exact effects depend on the operating system, filesystem, tool, and acquisition method. Before touching a source, confirm authority, scope, volatility, and the approved response procedure.

## 2. Order of volatility

The order of volatility is a planning concept: collect evidence that is likely to disappear sooner before less volatile evidence, when authorized and operationally safe. A simplified example is:
1. CPU/register and live process state.
2. RAM contents and active network connections.
3. Temporary and short-lived system data.
4. Local disk data.
5. Centralized logs, backups, and archival records.

This is not a universal acquisition checklist. Business continuity, safety, legal direction, and incident-response policy may change priorities.

## 3. Evidence handling record

For each item, record:
- Case ID and unique evidence ID.
- Description, source device, and source owner/custodian.
- Collector and authority/approval reference.
- Date/time collected, timezone, and clock source if known.
- Collection method, tool name, version, and relevant settings.
- Original location and destination.
- SHA-256 hash at acquisition and after transfer where appropriate.
- Every transfer, access, storage location, and person responsible.
- Any error, interruption, or deviation.

## 4. Hashes and integrity

A cryptographic hash maps data to a fixed-length digest. SHA-256 is widely used for integrity checking. If two independently calculated hashes of the same byte sequence match, this supports the conclusion that the bytes match. A hash does not prove who created the file, when it was created, or whether the original source was trustworthy.

Example:

```bash
sha256sum evidence-copy.E01
```

Windows PowerShell:

```powershell
Get-FileHash .\evidence-copy.E01 -Algorithm SHA256
```

Compare the output with the recorded acquisition hash. Explain any mismatch; do not silently replace the value.

## 5. Original versus working copy

- Store original evidence in controlled, access-restricted storage.
- Verify the acquisition and transfer hashes.
- Create a working copy using the approved process.
- Perform examination on the working copy where feasible.
- Record tool versions, commands, output paths, and timestamps.
- Keep evidence and generated analysis output separate.

## 6. Chain of custody

Chain of custody is the chronological record of possession and handling. Every handoff should identify who transferred the item, who received it, when, why, and in what condition. A missing entry should be documented honestly; do not reconstruct or invent a handoff.

Use `templates/chain-of-custody.csv` for the exercise.

## 7. Common mistakes

- Examining the only copy of evidence.
- Failing to record timezone or clock drift.
- Hashing a file after it has already been modified and calling that the acquisition hash.
- Copying sensitive evidence to personal cloud storage.
- Omitting tool versions and exact commands.
- Treating a matching hash as proof of maliciousness or authenticity.
- Publishing raw logs or evidence in a public repository.

## Practical task

Create a case folder with a case ID. Run `scripts/evidence_manifest.py` against the supplied synthetic data. Compare one output hash with an independent SHA-256 command. Record the results in a chain-of-custody form. The supplied synthetic sample is for learning and is not real incident evidence.
