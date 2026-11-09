# Detection Use-Case Backlog

All cases begin as **Planned / Not yet validated**. Record actual results only after running the lab.

| ID | Use case | Telemetry | Investigation focus | ATT&CK reference |
|---|---|---|---|---|
| DET-01 | Repeated Windows failed logons | Windows Security 4625 | Account, source/workstation context, time window, pattern | T1110 — Brute Force |
| DET-02 | Successful logon after repeated failures | 4625 + 4624 | Same account/source correlation, logon type, timing | T1110 — Brute Force |
| DET-03 | New local account created | Windows Security 4720 | Creator identity, account name, host, business reason | T1136.001 — Local Account |
| DET-04 | Account added to privileged local group | 4732 / related group events | Actor, target account, group, authorization | T1098 — Account Manipulation |
| DET-05 | Suspicious process execution review | Sysmon Event ID 1 | Process, parent, command line, user, hash, signer | T1059 — Command and Scripting Interpreter (only when applicable) |
| DET-06 | Linux SSH authentication failures | auth.log / journal | Source, target account, count, time pattern | T1110 — Brute Force |
| DET-07 | Linux successful SSH login after failures | auth log events | Account/source correlation and session context | T1078 — Valid Accounts (only if evidence supports) |
| DET-08 | Agent/log collection health | Wazuh agent status and event timestamps | Missing telemetry, last-seen time, service state | Defensive monitoring / ATT&CK mapping not required |

## DET-01 — Repeated Windows failed logons

**Objective:** identify a burst of failed authentication attempts that warrants review.

**Expected source:** Windows Security log, Event ID 4625.

**Analyst questions:**
- Which account was targeted?
- Is the source host / address expected?
- Are failures distributed across many accounts or concentrated on one?
- What is the logon type?
- Are there successful logons nearby in time?
- Could this be a user typo, stale service credential, or scheduled task?

**Validation:** use a dedicated lab account and a small number of intentional incorrect logons. Do not lock out real accounts or test against external systems.

**Evidence:** event details, query/filter, time window, screenshot, conclusion, and limitations.

## DET-02 — Success after failures

**Objective:** investigate whether failed attempts were followed by a successful authentication.

**Correlation keys:** account, source/workstation context, endpoint, and time window. Do not assume source IP will always be present or stable.

**Analyst questions:** Is the success from the same source? Is the logon type expected? Was MFA involved? Does the account owner recognize the activity?

## DET-03 — New local account

**Objective:** review local account creation events (4720).

**Analyst questions:** Who created the account? Was the action approved? Is the account enabled? Was it added to any groups? What happened immediately before and after?

## DET-04 — Privileged group membership change

**Objective:** identify and review a local group membership addition (for example, Event ID 4732 for a security-enabled local group).

**Analyst questions:** Which group changed? Which member was added? Who performed the change? Is there a change ticket or approved administrative task?

## DET-05 — Process creation

**Objective:** review Sysmon Event ID 1 for process execution context.

**Important:** process creation is high-volume telemetry. A process name alone is not enough to call an event malicious. Review parent process, command line, user, hashes, signer, host role, and surrounding events.

## DET-06 / DET-07 — Linux SSH activity

Review authentication events from the actual distribution and service configuration. Log formats vary. Correlate source, target user, timestamps, success/failure, and surrounding system activity.

## Detection quality checklist

- [ ] Telemetry source confirmed
- [ ] Expected event observed on endpoint
- [ ] Event ingested by Wazuh
- [ ] Rule/alert behaviour recorded
- [ ] Benign explanation considered
- [ ] Test is reproducible
- [ ] False-positive limitations documented
- [ ] Evidence saved and redacted

## ATT&CK mapping caution

ATT&CK technique mapping describes observed behaviour; it does not prove adversary intent. Use a mapping only when the event and investigation context support it. For background, consult [MITRE ATT&CK](https://attack.mitre.org/).
