# 10 — DFIR Tools and Professional Workflows

Tools are selected based on the question, source, authorization, evidence format, and organizational standards. Tool output must be interpreted and validated.

## Core tool categories

| Area | Example tools | Learning purpose |
|---|---|---|
| Evidence hashing | sha256sum, Get-FileHash, project manifest script | Integrity verification |
| Disk examination | Autopsy, The Sleuth Kit, FTK Imager | File systems and disk images |
| Memory analysis | Volatility 3 | RAM artefacts |
| Network analysis | Wireshark, Zeek | Packet and network metadata |
| Endpoint telemetry | Sysmon, Windows Event Viewer | Process and host events |
| Linux logs | journalctl, auditd tools | Authentication and system events |
| Artifact collection | KAPE, Velociraptor | Structured endpoint collection |
| Timeline analysis | Plaso/log2timeline, Timesketch | Cross-source event timelines |
| Case documentation | Case notes and report templates | Traceability and communication |

This is an educational list, not an endorsement. Check official documentation, supported versions, licensing, and organizational approval.

## Workflow A — Endpoint alert

1. Record alert ID, host, identity, timestamp, and source.
2. Preserve relevant telemetry according to policy.
3. Establish process ancestry and command-line context.
4. Correlate authentication, file, registry, service, and network events.
5. Compare against expected administration and software deployment.
6. Record evidence references and uncertainty.
7. Recommend containment through the incident owner.

## Workflow B — Suspected data theft

1. Confirm scope and authority.
2. Preserve identity, endpoint, DNS, proxy, firewall, and cloud audit logs.
3. Identify unusual access and transfer patterns.
4. Compare volume, destination, timing, and user role to baseline.
5. Determine whether evidence supports access, staging, transfer, or confirmed exfiltration.
6. Document what cannot be established from available telemetry.

## Workflow C — Suspected malware

1. Avoid executing the suspected file.
2. Preserve its path, metadata, hash, and source context.
3. Use approved isolated analysis environments.
4. Correlate endpoint process, persistence, and network telemetry.
5. Consult trusted intelligence sources and record lookup time.
6. Never treat a single antivirus verdict or hash match as the entire investigation.

## Tool validation checklist

- Tool name and exact version.
- Source and destination evidence identifiers.
- Exact command or GUI procedure.
- Relevant configuration and plugins.
- Hash before and after analysis where appropriate.
- Known limitations and parsing errors.
- Reproducible notes and output references.
