# 06 — Memory Forensics

## 1. Why RAM matters

RAM may contain evidence of current system state, including processes, loaded modules, command lines, network connections, handles, and other data. Some information disappears when a system is powered off. Memory acquisition can also alter system state and may be affected by virtualization, encryption, and acquisition tooling.

## 2. Acquisition planning

Before acquiring memory:
- Confirm authorization and incident-response policy.
- Determine whether collection is safe and necessary.
- Record device, OS build, time, timezone, logged-in user, and collector.
- Record acquisition tool name, version, options, and output.
- Hash the resulting image and preserve it securely.
- Document errors and any interaction with the source system.

Use only a disposable VM or approved training environment for learning.

## 3. Volatility concepts

Volatility 3 is a framework used to analyze supported memory images. Plugin availability and symbol requirements depend on OS and framework version. Common investigation areas include:
- Process listing and process-tree relationships.
- Command-line information.
- Network connections and sockets.
- Loaded modules and drivers.
- Handles and suspicious process relationships.
- OS-specific structures and artefacts.

A plugin result is an observation to validate, not an automatic malware verdict.

## 4. Analysis workflow

1. Verify the image hash.
2. Identify the OS and image compatibility.
3. Record framework version and exact plugin commands.
4. Examine process and network views.
5. Correlate with endpoint logs, disk artefacts, and known-good baselines.
6. Preserve output and explain limitations.

## 5. Practical exercise

Use a publicly provided memory-forensics training image or a memory image generated from your own isolated VM under an approved lab procedure. Follow the image provider's license and instructions. Do not download random memory dumps containing unknown personal data.

For each command, record the exact command, tool version, image hash, output, and interpretation. If you do not have a suitable image, complete the conceptual worksheet rather than claiming a live analysis.
