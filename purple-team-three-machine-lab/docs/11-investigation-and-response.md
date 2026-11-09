# 11 — Investigation and Response Workflow

## 1. Triage
Record alert ID, time, host, user, source, rule name, severity, and raw event. Check whether the event is complete and correctly parsed.

## 2. Validate
Compare the alert with the original endpoint or service log. Confirm timestamps, host identity, and important fields.

## 3. Scope
Search for related activity on the same host, account, source, and time window. Check both Windows and Ubuntu only where relevant evidence exists.

## 4. Build a timeline
Order events by timestamp and preserve the original time zone. Include the source of each observation.

## 5. Consider benign explanations
Examples include an administrator's planned work, a mistyped password, software updates, health checks, or a user following a normal link.

## 6. Determine disposition
- True positive: behavior of concern is supported by evidence.
- Benign positive: the rule matched a real but expected activity.
- False positive: the rule matched an event that did not represent the intended behavior.
- Inconclusive: evidence is insufficient.
- No finding: the hunt found no relevant activity in the searched scope.

## 7. Recommend response
Recommend proportionate defensive actions. Do not claim an account was disabled, host isolated, or service blocked unless that action was actually performed and authorized.

## 8. Report
Use the case report template. Separate observed facts, analyst interpretation, and recommendations.
