# 03 — Windows Forensics

Windows systems produce many useful artefacts. Their meaning depends on Windows version, configuration, retention, user activity, and collection method.

## 1. Event logs

Windows Event Viewer and EVTX files can contain:
- Security events: authentication, account changes, privileges, and audit activity.
- System events: service, driver, and operating-system events.
- Application events: application-specific errors and activity.
- PowerShell operational logs: script-engine and operational events when logging is enabled.
- Sysmon events: detailed process, network, file, registry, and other telemetry when Sysmon is installed and configured.

Useful investigation questions:
- Which account logged on, from where, and when?
- Was a new account created or a group membership changed?
- Which process started, with what parent process and command line?
- Did a service or scheduled task appear unexpectedly?
- Are there related DNS, network, or file events?

Do not rely on a single event ID without validating its provider, version, and context.

## 2. Registry

The Windows Registry stores system and user configuration. Hives of forensic interest can include SYSTEM, SOFTWARE, SAM, SECURITY, and user NTUSER.DAT/USRCLASS.DAT. Some artefacts may help explain installed software, services, user activity, or persistence.

Registry interpretation requires care: values can be absent, overwritten, disabled, or affected by OS version and configuration.

## 3. Services and scheduled tasks

Review service configuration, executable paths, account context, creation or modification times, and related event logs. For scheduled tasks, examine task definitions, triggers, actions, author, and execution history where available. An unfamiliar name alone is not proof of maliciousness.

## 4. Prefetch, Amcache, and execution artefacts

These artefacts may provide clues about program execution or application inventory. They have different semantics and limitations. Do not claim a precise execution time from an artefact unless the artefact supports that interpretation.

## 5. Browser and user activity

Browser history, downloads, cache, and profile data can be relevant but are sensitive. Collect only with explicit authorization and minimize personal data. Browser artefacts may be deleted, synchronized, or shared across profiles.

## 6. PowerShell investigation

When available, correlate PowerShell operational logs, script block logging, process creation telemetry, parent process, user logon, and network activity. Logging coverage depends on policy and configuration; absence of an event does not prove that an action did not occur.

## Practical exercises

1. In your own Windows VM, open Event Viewer and inspect recent System and Security events.
2. Export a small, non-sensitive event-log sample from the lab VM.
3. Identify the timestamp, provider, event ID, account, and message for three events.
4. If Sysmon is installed in your lab, inspect process-creation events and parent-child relationships.
5. Document what the records show and what they do not prove.

Do not inspect another person's Windows profile or browser data without authorization.
