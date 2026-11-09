# 03 — Build and Baseline

This guide assumes the learner may already have some VMs. Audit first; do not reinstall a working system without a reason.

## Phase A — Inventory

For each VM, record OS version, hostname, IP address, network mode, RAM, CPU, and snapshot name. Keep sensitive details private.

## Phase B — Verify network isolation

On each VM, inspect its network configuration. Confirm all lab machines are on the same intended host-only/internal network. Confirm Kali is not bridged to a production network.

From Kali, test reachability only to the two declared lab target addresses. If an address is unexpected, stop and fix the virtual network before scanning.

## Phase C — Windows baseline

1. Sign in to the Windows lab VM.
2. Record Windows edition and build.
3. Open Event Viewer.
4. Inspect Windows Logs > Security.
5. Confirm recent normal logon events exist.
6. If Sysmon is installed, inspect Applications and Services Logs > Microsoft > Windows > Sysmon > Operational.
7. Record whether process-creation events are visible.
8. Confirm the Wazuh agent service state and dashboard status.

Do not change audit policies until you have recorded the starting state.

## Phase D — Ubuntu baseline

1. Record Ubuntu release and hostname.
2. Identify the authentication logging mechanism used by the installed release.
3. Inspect recent authentication messages using the system's available log source.
4. Record whether SSH is installed and enabled.
5. Confirm the Wazuh agent service and dashboard status.
6. Record whether a web service is installed; do not assume one exists.

## Phase E — Kali baseline

1. Record Kali release and hostname.
2. Confirm its virtual network adapter is isolated.
3. Record the lab-only target addresses.
4. Confirm basic tools are available.
5. Do not run broad network discovery.

## Phase F — Baseline report

Complete ../templates/asset-inventory-template.md and ../templates/baseline-template.md. Baseline means ordinary system activity before a simulation. It is essential for distinguishing normal behavior from unusual behavior.
