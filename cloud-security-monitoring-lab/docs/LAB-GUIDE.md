# Cloud Security Monitoring Lab — Guided Practical

Work through the sections in order. The local exercises require only Python. AWS exercises are optional and must use an account and resources you own.

## Part 1 — Foundations

### AWS shared responsibility

AWS is responsible for security **of** the cloud infrastructure; customers remain responsible for security **in** the cloud according to the services they use. Customer responsibilities commonly include identity permissions, data handling, workload configuration, and network exposure. The exact split varies by service.

### Core services and concepts

- **IAM:** identities, roles, policies, and permissions.
- **CloudTrail:** records account activity and API events.
- **Management events:** control-plane operations such as creating users or changing security groups.
- **Region:** a geographic AWS location; many resources and event records are region-scoped.
- **Security group:** a stateful virtual firewall for supported network resources.
- **MFA:** an additional authentication factor.
- **GuardDuty:** a managed threat-detection service that analyzes supported data sources. It is not required for this local project and may incur charges.

## Part 2 — Local lab (no AWS account required)

1. Install Python 3.9 or newer.
2. Clone or download this repository.
3. Run: `python scripts/cloudtrail_triage.py sample_data/cloudtrail-events.jsonl`.
4. Save a JSON report: `python scripts/cloudtrail_triage.py sample_data/cloudtrail-events.jsonl --json-out findings.json`.
5. Run tests: `python -m unittest discover -s tests -v`.
6. Open the sample file and manually trace each finding to its source event.
7. Record which findings are high or medium severity and explain why severity alone does not prove compromise.

### Questions to answer

- Which events change identity permissions?
- Which event creates a new credential?
- Which event may expose a resource to all IPv4 addresses?
- What additional evidence would you need before declaring an incident?
- Which findings could be legitimate administrative work?

## Part 3 — Optional AWS setup

Before proceeding, review current AWS pricing, free-tier eligibility, CloudTrail configuration, and data-retention costs. Do not enable paid services without understanding the charges.

1. Use a dedicated lab account, not a production account.
2. Protect the root identity with MFA; do not use root for daily administration.
3. Create a least-privilege lab identity or role.
4. Enable and verify a CloudTrail trail for the required management events.
5. Configure delivery to a private S3 bucket with appropriate access controls and encryption.
6. Confirm that a harmless, approved lab management event appears in the trail.
7. Export only a small, sanitized event sample for local analysis.

Do not publish account IDs, personal email addresses, access keys, session tokens, or raw sensitive logs.

## Part 4 — Controlled exercises

### Exercise A: IAM change review

In the dedicated lab account, make a harmless and reversible IAM change using a test identity. Find the matching CloudTrail event. Record event name, actor, target, time, and change purpose. Revert the change after verification.

### Exercise B: Authentication review

Review sign-in events for the test identity. Do not attempt password guessing or repeated failed logins. Use naturally generated lab events or the synthetic sample to learn the event structure.

### Exercise C: Network exposure analysis

Use the synthetic `AuthorizeSecurityGroupIngress` event to understand the public CIDR rule. Do not expose a real service to the internet for this exercise. If you need a live test, use a disposable resource, a non-sensitive port, strict time limits, and remove the rule immediately; synthetic data is safer and sufficient for the learning objective.

### Exercise D: Incident timeline

Build a timeline from at least three related events. For each event, write what is known, what is inferred, and what remains unknown. Avoid presenting assumptions as facts.

## Part 5 — Investigation workflow

1. **Validate:** confirm event integrity, timestamp, source, and account context.
2. **Scope:** identify principal, affected resource, region, and related events.
3. **Enrich:** compare with approved changes, identity inventory, and expected locations.
4. **Assess:** determine likelihood and impact; state confidence and evidence gaps.
5. **Contain:** follow the account owner's approved response process. Do not revoke credentials or change production permissions without authorization.
6. **Recover:** restore known-good configuration and verify service health.
7. **Learn:** document root cause, detection gaps, and preventive actions.

## Part 6 — Evidence and completion

Keep evidence in a local private folder until sanitized. Capture command output, test results, and relevant event excerpts. Remove account identifiers, usernames, public IPs if sensitive, and all secrets before publishing.

Update the checklist in the project README only after completing each item. A local synthetic test is useful evidence of code behavior, but it is not evidence of a live AWS detection.
