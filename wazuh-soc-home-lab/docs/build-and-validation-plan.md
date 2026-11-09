# Existing Lab Audit and Validation Plan

The author reports that the Wazuh lab is already installed and has been used for practice. **Do not reinstall or rebuild it by default.** First inspect the current environment, capture its configuration, and document prior work. Mark an item complete only after checking it in the actual lab and recording evidence.

## Phase 0 — Audit the existing environment

- [ ] Confirm host OS and version.
- [ ] Confirm CPU model, core count, and hardware virtualization support.
- [ ] Confirm available disk space and virtualization platform.
- [ ] Record host specifications in the lab journal.
- [ ] Create a dedicated lab folder and backup important files.
- [ ] Record what practical exercises have already been attempted, even if they were not documented at the time.
- [ ] Collect existing screenshots, alert examples, notes, and terminal output where available.

## Phase 1 — Verify the existing Wazuh server

- [ ] Identify the existing Wazuh server VM / host and its OS.
- [ ] Record the installed Wazuh version and installation date if known.
- [ ] Check current Wazuh services and dashboard health.
- [ ] Record the existing VM resource allocation.
- [ ] Verify manager, indexer, and dashboard services.
- [ ] Sign in to the dashboard and capture a redacted screenshot.
- [ ] Take a clean VM snapshot.

**Acceptance criteria:** existing dashboard is reachable from the trusted lab network; required Wazuh services are healthy; version and configuration details are documented; no credentials are stored in the repository.

## Phase 2 — Audit the existing Windows endpoint

- [ ] Check whether Sysmon is already installed; record its version and configuration source.
- [ ] Confirm Sysmon service and event channel are active.
- [ ] Check whether the Wazuh agent is already installed and enrolled; record its version.
- [ ] Configure collection of the required Windows Security and Sysmon channels.
- [ ] Confirm the endpoint appears active in Wazuh.
- [ ] Generate a harmless test event and locate it in the dashboard.
- [ ] Record event channel, Event ID, timestamp, and agent identity (redacted).

**Acceptance criteria:** a known test event from Windows is visible in Wazuh with the expected endpoint and timestamp.

## Phase 3 — Audit the existing Linux endpoint

- [ ] Identify the Linux endpoint already used in the lab and record its distribution/version.
- [ ] Check whether the Wazuh agent is already installed and enrolled; record its version.
- [ ] Confirm authentication log collection for the distribution.
- [ ] Confirm the endpoint appears active.
- [ ] Generate a controlled authentication test using a lab-only account.
- [ ] Locate the event in Wazuh and record the relevant fields.

**Acceptance criteria:** a known Linux authentication event is visible in Wazuh.

## Phase 4 — Reconstruct previous practice and validate detections

- [ ] List the exercises and alerts you remember testing previously.
- [ ] Recover any existing screenshots, saved alerts, notes, or terminal output.
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
