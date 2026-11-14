# LogSentry — SSH Authentication Log Analyzer

A Python command-line tool for defensive analysis of local SSH-style authentication logs. It summarizes failed and successful logins, groups failures by source IP and username, and highlights sources meeting a configurable count threshold.

## Project status

Source code, synthetic sample data, documentation, and unit tests are included. Run the commands below on your own machine before describing the tests or tool as personally executed. No live SOC deployment or real-world attack detection is claimed.

## Features

- Parses common SSH authentication success and failure messages
- Validates IPv4 addresses before counting events
- Groups failed attempts by source IP and username
- Summarizes successful logins by source IP
- Configurable repeated-failure count threshold
- Handles unreadable files with a clear error
- Uses Python standard-library modules only

## Requirements

- Python 3.10 or newer
- No third-party packages

## Run

From this directory:

```bash
python log_sentry.py --file sample_auth.log
python log_sentry.py --file sample_auth.log --threshold 3
```

## Run unit tests

```bash
python -m unittest discover -s tests -v
```

Tests are provided; results are not represented as passing until the commands have actually been run.

## Detection interpretation

A source IP meeting the threshold is a lead for analyst review, not proof of brute force or compromise. Correlate with timestamps, successful logons, user and asset context, and other approved identity or endpoint telemetry.

**Important limitation:** the current threshold is counted across the entire supplied file. It is not a rolling five-minute or fifteen-minute detection window. A large historical file can produce a threshold finding even when failures were spread over a long period. Treat this as a basic log-summary exercise, not a production brute-force detection. A future improvement is timestamp-aware window aggregation and correlation of failures followed by a successful login.

## Input and privacy

The parser is designed for common SSH-style messages; other formats may be counted as unrecognized. Use synthetic or authorized logs only. Sanitize usernames, IPs, hostnames, timestamps, and other identifying details before publishing evidence.

## Structure

```text
log-sentry/
├── README.md
├── log_sentry.py
├── sample_auth.log
└── tests/
    └── test_log_sentry.py
```

## SOC analyst learning outcomes

- Distinguish authentication successes from failures
- Identify repeated activity by source IP and target account
- Explain why a threshold alone is insufficient evidence
- Document detection limitations and recommend improvements
- Handle security logs responsibly and protect sensitive data
