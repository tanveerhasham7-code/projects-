# Existing Lab Audit — Start Without Reinstalling

The learner has reported that a Wazuh lab with Windows and Linux components is already installed and has been used for practice. The exact topology and versions still need to be recorded from the actual environment.

## Step 1 — Record the topology
Fill in the table from your own machines and dashboards.

| Component | Actual value |
|---|---|
| Wazuh server / all-in-one host | To record |
| Wazuh version | To record |
| Dashboard accessible | Yes / No / Not checked |
| Windows endpoint name and version | To record |
| Windows Wazuh agent status | To verify |
| Linux distribution and version | To record |
| Linux Wazuh agent status | To verify |
| Sysmon installed on Windows | Yes / No / To verify |
| Sysmon configuration source/version | To record |
| Lab network mode | NAT / Host-only / Bridged / Other |
| Time zone and time sync | To record |

## Step 2 — Verify agent health
Open the Wazuh dashboard and inspect agent status. Record the displayed status and last keep-alive time for each endpoint. Do not infer agent health from the fact that the agent software is installed.

## Step 3 — Verify telemetry
On Windows, check whether Security and Sysmon event channels exist and contain recent events. On Linux, identify the authentication log location used by the distribution. Then verify whether corresponding events are visible in Wazuh.

## Step 4 — Save sanitized evidence
Take screenshots of the dashboard agent list, endpoint event channel, and a matching SIEM event. Hide personal usernames, public addresses, tokens, and other private details.

## Completion criteria
- [ ] Topology recorded
- [ ] Versions recorded
- [ ] Windows agent status verified
- [ ] Linux agent status verified
- [ ] Windows Security telemetry verified
- [ ] Sysmon telemetry verified or documented as unavailable
- [ ] Linux authentication telemetry verified
- [ ] At least one endpoint event located in Wazuh

**Important:** This is an audit checklist, not a claim that these checks have already passed.
