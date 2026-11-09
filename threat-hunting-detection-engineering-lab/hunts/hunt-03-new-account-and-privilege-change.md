# Hunt 03 — New Account and Privilege Change

## Question
Were accounts created or added to privileged groups during the selected period?

## Hypothesis
Unexpected account creation followed by group membership change may indicate persistence or privilege escalation, but approved administration can produce the same events.

## Data required
Windows Security 4720, 4728, 4732 and relevant account/group fields. Verify audit policy and event collection first.

## Procedure
1. Search the selected time window for account creation.
2. Search for group membership changes in the same period.
3. Correlate target account, actor, host, and timestamps.
4. Compare with an approved change record or known lab action.
5. Check whether the account is enabled and what group was modified, where telemetry permits.
6. Document the conclusion and missing context.

## Safe validation
Only in an isolated Windows VM that you own, create a clearly named temporary test account if permitted, observe the relevant event, and remove the account after recording evidence. Do not alter a real or shared machine.

## Outcome
Not tested. Add evidence after completing the exercise.
