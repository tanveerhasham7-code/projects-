# Professional Detection Engineering Workflow

A detection should be understandable, testable, and maintainable.

## 1. Define the behavior
Describe the suspicious behavior in plain language. Avoid starting with a tool-specific query.

## 2. State the hypothesis
Example: repeated failed logons against one account from one source within a short period may indicate password guessing. This is a hypothesis, not proof.

## 3. Identify telemetry
Specify the host, event provider, event ID, required fields, collection path, and retention requirements.

## 4. Write the detection specification
Document:
- Detection name and unique ID
- Threat behavior and rationale
- Data source and required fields
- Matching logic and time window
- Threshold and grouping keys
- Expected benign causes
- Exclusions and their justification
- Severity and confidence
- ATT&CK mapping, only when supported
- Known blind spots

## 5. Implement
Write a Sigma candidate or SIEM-specific rule. Confirm field names and operators against real collected events. Generic field names may need backend-specific mapping.

## 6. Validate
Define safe test cases before execution. Capture the raw event, normalized event, alert, and timestamps. Record both positive and negative tests.

## 7. Tune
Review benign matches. Add narrow exclusions only when justified. Avoid broad exclusions that hide real activity.

## 8. Release and maintain
Version the rule, document dependencies, assign an owner, track changes, and rerun regression tests after updates.

## Quality measures
- True positive: alert corresponds to the behavior being detected.
- False positive: alert matches benign activity.
- False negative: test behavior occurred but detection did not alert.
- Precision: proportion of alerts that are true positives in the evaluated set.
- Coverage gap: required telemetry or behavior is not observable.
- Detection latency: time between behavior and alert availability.

Do not report precision or detection latency without a defined test set and measured timestamps.
