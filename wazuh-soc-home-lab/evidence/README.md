# Evidence Library

Evidence is added only after the corresponding activity has been performed in the lab.

## Evidence quality rules

- Capture the relevant dashboard panel and the event details, not just the dashboard home page.
- Include date/time and timezone in the report.
- Redact passwords, tokens, email addresses, personal usernames, public IPs where sensitive, and unique machine identifiers.
- Keep original evidence locally; publish only sanitized copies.
- Name files consistently: `YYYY-MM-DD-phase-topic-01.png`.
- Link each screenshot from a report or validation record.
- Never create mock screenshots or claim that a planned test succeeded.

## Planned evidence milestones

| Milestone | Evidence to add | Status |
|---|---|---|
| Server online | Wazuh dashboard and service health | Pending |
| Windows connected | Agent active + endpoint identity redacted | Pending |
| Sysmon telemetry | Event ID 1 event details | Pending |
| Linux connected | Agent active + auth event | Pending |
| Detection validation | Alert details + test context | Pending |
| Investigation | Completed report + timeline | Pending |
