# SOC Alert Investigation Workflow

Use this workflow for every alert or notable event. The goal is to show structured analyst reasoning, not simply take a screenshot.

## 1. Prepare

- Confirm the lab is authorized and the data is synthetic or belongs to your own systems.
- Record the alert ID, rule ID, severity/level, timestamp, endpoint, and source.
- Preserve the original event details before changing filters or configuration.

## 2. Triage

Classify the alert as:
- **True positive:** observed activity matches the detection intent and is suspicious in context.
- **Benign positive:** detection correctly identified an event, but the activity is authorized or expected.
- **False positive:** the rule fired on activity outside its intended detection condition.
- **Inconclusive:** available telemetry is insufficient to decide.

Do not use "true positive" as a synonym for "confirmed compromise."

## 3. Scope

Establish:
- Which host and account are involved?
- What happened, and when?
- Is there a source address, process, parent process, or logon type?
- Are there related events on the same endpoint?
- Is the activity isolated or repeated?
- What telemetry is missing?

## 4. Build a timeline

Normalize timestamps to a single timezone and preserve the original timezone. Include the event source and why each entry matters.

| Time (with timezone) | Source | Event | Analyst interpretation |
|---|---|---|---|
| | | | |

## 5. Map behaviour

Use MITRE ATT&CK only when supported by evidence. Include technique ID, technique name, and a short justification. Leave it unmapped when evidence is insufficient.

## 6. Recommend response

For a home lab, recommendations may include:
- Verify the activity with the account owner / lab operator.
- Disable or reset a test account if the scenario warrants it.
- Review group membership and recent authentication history.
- Isolate a lab VM from the lab network if a controlled scenario requires it.
- Preserve relevant logs and document any containment action.

Do not claim an action was taken if you only recommended it.

## 7. Close and learn

Record disposition, confidence, evidence gaps, tuning ideas, and what should be tested next. A strong report explains both what is known and what cannot be concluded.
