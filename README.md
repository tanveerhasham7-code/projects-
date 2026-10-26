# LogSentry — Security Log Analyzer 🛡️

LogSentry is a beginner-friendly Python project that reads **local authentication logs** and highlights patterns that may deserve investigation. It helps students practice Python, regular expressions, log analysis, and basic security monitoring (a core SOC skill).

> **Safety and scope:** LogSentry only reads the file you provide. It does not connect to computers, scan networks, block IP addresses, or prove that an event is malicious. Review alerts in context before taking action.

## Features

- Counts failed and successful SSH-style authentication events
- Groups failed logins by source IP address
- Flags IP addresses with repeated failures based on a configurable threshold
- Counts failed attempts against usernames
- Prints a readable summary
- Includes synthetic sample logs and unit tests
- Uses only the Python standard library

## Requirements

- Python 3.9+
- No third-party packages

## Run it

Analyze the included sample log:

```bash
python log_sentry.py --file sample_auth.log
```

Change the repeated-failure threshold (default is 5):

```bash
python log_sentry.py --file sample_auth.log --threshold 3
```

Run automated tests:

```bash
python -m unittest discover -s tests -v
```

## Example output

The exact counts depend on the contents of the log file.

```text
LogSentry - Authentication Log Summary
Events analyzed: 10
Failed logins: 6
Successful logins: 2
Other/unrecognized lines: 2

Sources with repeated failed logins (threshold: 5):
  203.0.113.10: 5 failures

Most targeted usernames:
  admin: 3 failed attempts
```

The documentation IP range `203.0.113.0/24` is reserved for examples; the sample data is synthetic and does not describe real activity.

## What it looks for

LogSentry recognizes common SSH-style messages containing:
- `Failed password`
- `Invalid user` alongside a failed-password event
- `Accepted password` or `Accepted publickey`

Log formats differ between Linux distributions and services. Unrecognized formats are counted but not interpreted.

## Project structure

```text
projects-/
├── README.md
├── log_sentry.py
├── sample_auth.log
└── tests/
    └── test_log_sentry.py
```

## Skills demonstrated

Python • Regular expressions • Log parsing • Security monitoring • Basic incident triage • Unit testing • CLI tools

## Suggested next steps

1. Add JSON or CSV report export.
2. Add support for another documented log format.
3. Create a small dashboard for results.
4. Compare alerts against a known benign sample and document false positives.

Created as a learning project by **Tanveer Hassham**, cybersecurity student.
