# Build and Validation Plan

This is the execution checklist. Mark an item complete only after performing it and recording evidence.

## Phase 0 — Host readiness

- [ ] Confirm host OS and version.
- [ ] Confirm CPU model, core count, and hardware virtualization support.
- [ ] Confirm available disk space and virtualization platform.
- [ ] Record host specifications in the lab journal.
- [ ] Create a dedicated lab folder and backup important files.

## Phase 1 — Wazuh server

- [ ] Create Ubuntu Server VM using the resource plan in [architecture.md](architecture.md).
- [ ] Apply updates and configure a non-root administrative account.
- [ ] Install Wazuh all-in-one using the current official Quickstart guide.
- [ ] Save the installed Wazuh version and installation date.
- [ ] Verify manager, indexer, and dashboard services.
- [ ] Sign in to the dashboard and capture a redacted screenshot.
- [ ] Take a clean VM snapshot.

**Acceptance criteria:** dashboard is reachable from the trusted lab network; required Wazuh services are healthy; no credentials are stored in the repository.

## Phase 2 — Windows endpoint

- [ ] Install Sysmon from Microsoft's official Sysinternals source.
- [ ] Select and document a reputable Sysmon configuration; record its source and version.
- [ ] Confirm Sysmon service and event channel are active.
- [ ] Install and enrol the Wazuh agent.
- [ ] Configure collection of the required Windows Security and Sysmon channels.
- [ ] Confirm the endpoint appears active in Wazuh.
- [ ] Generate a harmless test event and locate it in the dashboard.
- [ ] Record event channel, Event ID, timestamp, and agent identity (redacted).

**Acceptance criteria:** a known test event from Windows is visible in Wazuh with the expected endpoint and timestamp.

## Phase 3 — Linux endpoint

- [ ] Create or select a Linux endpoint inside the lab.
- [ ] Install and enrol the Wazuh agent.
- [ ] Confirm authentication log collection for the distribution.
- [ ] Confirm the endpoint appears active.
- [ ] Generate a controlled authentication test using a lab-only account.
- [ ] Locate the event in Wazuh and record the relevant fields.

**Acceptance criteria:** a known Linux authentication event is visible in Wazuh.

## Phase 4 — Detection validation

- [ ] Select one use case from [detection-use-cases.md](detection-use-cases.md).
- [ ] Record expected telemetry and expected alert behaviour before testing.
- [ ] Run only the harmless, authorized test steps.
- [ ] Record actual result, timestamp, rule ID/level, and relevant fields.
- [ ] Investigate whether the alert is meaningful or a false positive.
- [ ] Save a redacted screenshot and complete an incident / test report.
- [ ] Mark the use case Validated only when evidence supports it.

## Phase 5 — Portfolio release

- [ ] Update project status and environment versions.
- [ ] Add architecture and dashboard screenshots.
- [ ] Add at least two fully documented investigations.
- [ ] Add detection validation results and limitations.
- [ ] Review all files for secrets, personal data, and unredacted identifiers.
- [ ] Update the main project README with actual completed work only.

## Validation record

| Field | Value |
|---|---|
| Test ID | |
| Date/time + timezone | |
| Endpoint | |
| Telemetry source | |
| Expected event | |
| Actual event / alert | |
| Rule ID and level | |
| Result | Planned / Passed / Failed / Inconclusive |
| Evidence path | |
| Analyst notes | |

## Troubleshooting order

1. Is the endpoint powered on and connected to the intended lab network?
2. Is the Wazuh agent service running?
3. Does the agent show as connected in the dashboard?
4. Is the relevant Windows event channel or Linux log source enabled?
5. Does the endpoint itself contain the expected event?
6. Is the agent configured to collect that source?
7. Is the event arriving but not generating an alert? Check decoder/rule coverage and alert thresholds.

Do not label a detection broken until you confirm that the underlying event is being collected.
