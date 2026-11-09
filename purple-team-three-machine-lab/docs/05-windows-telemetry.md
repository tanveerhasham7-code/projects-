# 05 — Windows Telemetry: Security Log and Sysmon

## Windows Security log
The Security channel records selected authentication and account-management events when the relevant audit policies are enabled.

Useful event IDs:
- 4624 — successful logon.
- 4625 — failed logon.
- 4688 — process creation, if process-creation auditing is enabled.
- 4720 — user account created.
- 4732 — member added to a security-enabled local group.
- 4740 — user account locked out.

The exact fields depend on event version and audit configuration. Inspect the event details/XML rather than relying only on an event ID.

## Sysmon
Sysmon is a Windows system service and driver that can record detailed system activity. It is not installed by default on every Windows machine and its configuration determines which events are generated.

Useful event IDs:
- 1 — process creation.
- 3 — network connection, if enabled.
- 11 — file creation.
- 13 — registry value set.
- 22 — DNS query.

## Practical verification
1. Open Event Viewer.
2. Navigate to the Security channel.
3. Open a recent event and inspect General and Details.
4. If Sysmon exists, inspect its Operational channel.
5. Locate a benign process-creation event such as opening Notepad or PowerShell.
6. Find the corresponding event in Wazuh, if collection is configured.
7. Record the fields that are present and missing.

## Important
Do not install random Sysmon configurations from untrusted sources. Use a reputable, documented configuration and understand its logging volume. Do not claim a Sysmon event is visible in Wazuh until you have confirmed it.
