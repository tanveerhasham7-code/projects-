# 04 — Linux Forensics

Linux artefacts vary across distributions, init systems, logging configuration, and installed services.

## 1. Authentication and system logs

Common locations and sources include:
- Debian/Ubuntu: commonly `/var/log/auth.log` and `/var/log/syslog`.
- RHEL-family systems: commonly `/var/log/secure` and `/var/log/messages`.
- systemd journal: `journalctl` output, subject to journal configuration and retention.
- SSH daemon logs: often included in authentication logs or the journal.

Useful questions:
- Were there successful or failed SSH logins?
- Which account used sudo?
- Were users, groups, or SSH authorized keys changed?
- Did a service start, stop, or fail?
- Did a new package or scheduled job appear?

File paths and event detail are distribution-specific. Verify on the lab machine.

## 2. Processes and network state

Live commands such as `ps`, `ss`, and `lsof` can show current state, but running them changes system state and may not reflect historical activity. Record commands and collection time. Use approved acquisition procedures for incident evidence.

## 3. Persistence and execution clues

Potential sources include:
- systemd service and timer units.
- cron configuration and user crontabs.
- shell history (incomplete and user-controlled).
- SSH authorized_keys and configuration.
- package manager logs.
- executable metadata and file timestamps.
- auditd records, if configured.

A file in a persistence location is a lead, not automatic proof of compromise. Validate owner, content, package provenance, timestamps, and related logs.

## 4. File metadata and timestamps

Linux filesystems commonly expose access, modification, status-change, and creation/birth time where supported. Timestamp semantics vary. Copying, extraction, backup, filesystem behavior, and clock differences can affect interpretation.

## Practical exercises

1. On your own Linux VM, inspect authentication logs or the system journal.
2. Identify one successful and one failed authentication event if present.
3. Review the current service list and explain one service's purpose.
4. Inspect cron and systemd timer configuration without changing it.
5. Record command, timestamp, output summary, and limitations.

Example read-only commands:

```bash
who
last
sudo journalctl -u ssh --since "today"
systemctl list-units --type=service --state=running
systemctl list-timers
```

Some commands may require elevated privileges or differ by distribution. Do not alter a live or production host for this exercise.
