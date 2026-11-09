# 02 — Hardware and VM Planning

## 1. Plan before creating VMs

Check the host's available RAM, CPU cores, disk space, and virtualization support. Do not allocate all host resources to virtual machines.

A practical starting point for a 16 GB host is to run two or three VMs at a time, depending on the existing Wazuh management footprint. Resource needs vary by OS version, desktop environment, indexing load, and concurrent activity.

## 2. Suggested starting allocation

| VM | RAM starting point | vCPU starting point | Disk starting point |
|---|---:|---:|---:|
| Kali Linux | 2–4 GB | 2 | 30–40 GB |
| Ubuntu Server | 2 GB | 2 | 25–30 GB |
| Windows 10/11 | 4–6 GB | 2 | 60–80 GB |
| Wazuh manager | Existing allocation; often resource-heavy | Based on deployment | Based on retained data |

These are planning estimates, not guaranteed minimums. If Wazuh is already running on another VM, account for its RAM and disk usage. If resources are tight, shut down unused VMs and perform exercises sequentially.

## 3. Before installing anything

Record:
- Hypervisor and version.
- Host OS.
- CPU model and core count.
- Available RAM and free disk.
- Existing VM names and operating-system versions.
- Existing Wazuh manager location and version.
- Current network adapter mode for each VM.

## 4. Snapshots

Create a clean snapshot after each VM is updated and configured. Name snapshots clearly, for example:
- clean-kali
- clean-windows-agent
- clean-ubuntu-agent
- baseline-before-exercise

A snapshot is a recovery aid, not a replacement for backups.
