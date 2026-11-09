# 08 — Safe Authentication-Failure Simulation

## Objective
Generate a small, controlled number of failed authentication events against a dedicated lab-only account, then confirm whether Ubuntu records them and whether Wazuh collects them.

## Safety conditions
- Use only your own isolated Ubuntu VM.
- Create a dedicated temporary test account if needed.
- Do not use a real password or a password used elsewhere.
- Do not use Hydra, password lists, spraying, or automated brute-force tools.
- Limit the exercise to three deliberately incorrect attempts, performed manually.
- Stop immediately if you see account lockout or unexpected impact.

## Procedure
1. Confirm the Ubuntu address and SSH service.
2. Confirm the test account is permitted to log in over SSH in this isolated lab.
3. Record the start time.
4. From Kali, initiate an SSH login to the Ubuntu VM.
5. Enter an intentionally incorrect lab-only password no more than three times.
6. Stop and close the client.
7. Inspect the Ubuntu authentication log or journal.
8. Search Wazuh for the matching event.
9. Record whether an alert fired and why.

## Expected learning
Understand the difference between an authentication event, a collected log, a rule match, and an actionable alert.

## Cleanup
Remove or disable the temporary account if it was created for this exercise. Do not delete logs needed for evidence.

## Result
Not tested. Add the actual result and sanitized screenshots after practice.
