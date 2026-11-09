# 04 — Wazuh Telemetry and Agent Health

## Purpose
Confirm that endpoint data is actually reaching Wazuh before performing security exercises. An installed agent is not proof that events are being collected.

## Checks
1. Open the Wazuh Dashboard.
2. Inspect the agent list and record the Windows and Ubuntu agent status.
3. Record the last keep-alive time and agent version where shown.
4. On each endpoint, inspect the agent service state.
5. Identify the configured event channels or log files being monitored.
6. Generate only normal benign activity and check whether the corresponding event appears in Wazuh.
7. Record event timestamp, agent, data source, and relevant fields.

## Troubleshooting order
- Is the endpoint powered on?
- Is the agent service running?
- Can the endpoint reach the manager over the intended lab network?
- Is the agent registered and showing the expected status?
- Is the event source configured for collection?
- Does the event exist locally?
- Is parsing or indexing delayed?

Do not change several settings at once. Make one change, record it, and test again.

## Completion evidence
A sanitized screenshot of the agent list and one real event from each endpoint. Record any unavailable telemetry honestly.
