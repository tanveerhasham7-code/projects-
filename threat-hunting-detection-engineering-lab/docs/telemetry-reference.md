# Telemetry Reference

## Windows Security log
Useful event IDs for defensive learning include:
- 4624: successful logon
- 4625: failed logon
- 4688: process creation, when the relevant audit policy is enabled
- 4720: user account created
- 4728 / 4732: member added to a security-enabled group
- 4740: account locked out

The meaning and available fields depend on event version, audit policy, and collection configuration. Verify the actual event XML and SIEM-parsed fields.

## Sysmon
Sysmon provides detailed endpoint telemetry when installed and configured. Common event IDs:
- 1: process creation
- 3: network connection, if configured
- 7: image loaded, if configured
- 11: file created
- 13: registry value set
- 22: DNS query

Sysmon is not a complete security solution. Configuration determines what is recorded; excessive logging can create noise and storage pressure.

## Linux authentication
Depending on distribution, authentication events may be recorded in /var/log/auth.log, /var/log/secure, or the system journal. Verify the actual source. Common SSH messages include failed authentication, accepted authentication, and invalid-user attempts.

## Data quality checklist
- Host identity is consistent.
- Timestamps and time zones are understood.
- Required event channels are enabled.
- Agents are connected.
- Parsing preserves important fields.
- Event volume and retention are sufficient.
- Missing telemetry is documented rather than silently assumed.
