# Hunt 01 — Repeated Authentication Failures

## Question
Are repeated failed authentication attempts occurring against one or more accounts in the lab?

## Hypothesis
A high number of failures grouped by account, source, and time window may indicate password guessing, but user error, stale services, and automation can produce similar patterns.

## Data required
Windows Security event 4625 and/or Linux SSH authentication logs. Confirm the source host and fields available in your SIEM.

## Procedure
1. Select a bounded time window.
2. Search failed authentication events.
3. Group by account, source address, host, and logon type where available.
4. Compare counts and timing with the normal lab baseline.
5. Review nearby successful logons and account-lockout events.
6. Identify whether activity is expected and who owns the source system.
7. Record evidence and confidence; do not label it malicious from volume alone.

## Evidence to capture
- Search time range and query
- Representative raw event
- Event count and grouping
- Related successful/locked-out events
- Sanitized screenshot
- Analyst conclusion and limitations

## Outcome
Not tested. Complete after running the hunt against real lab telemetry.
