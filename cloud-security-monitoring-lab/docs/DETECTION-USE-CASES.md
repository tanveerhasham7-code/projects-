# Detection Use Cases and Investigation Notes

These are starter analytics for learning. They are intentionally transparent, narrow rules—not production-ready detections. Validate field availability and semantics against the CloudTrail event version and services in your own environment.

## CLOUD-AUTH-001 — Failed console sign-in

- **Signal:** `eventName=ConsoleLogin` and a failure in `responseElements.ConsoleLogin` or `errorCode`.
- **Why it matters:** Repeated failures may indicate password guessing, stale automation, or a user typing an incorrect password.
- **Triage:** Group by principal and source IP; inspect count and time window; compare with successful logins; verify expected VPN or corporate egress.
- **False positives:** Mistyped passwords, password manager issues, expired credentials, approved testing.
- **Escalate when:** Failures are followed by a successful login, involve privileged identities, or originate from an unexpected source.

## CLOUD-AUTH-002 — Console sign-in without MFA

- **Signal:** `ConsoleLogin` with `additionalEventData.MFAUsed=No`.
- **Triage:** Confirm whether the identity is human or service-related, review MFA policy, and inspect adjacent activity.
- **Limitation:** Event fields and MFA reporting can vary. Validate the field before enabling an alert.

## CLOUD-IAM-001 — Root account activity

- **Signal:** `ConsoleLogin` where `userIdentity.type=Root`.
- **Triage:** Identify the action, time, source, and business justification. Root use should be tightly controlled.
- **False positives:** Approved account administration or emergency access.

## CLOUD-IAM-002 — IAM permissions changed

- **Signal:** IAM policy attachment or policy-version events such as `AttachUserPolicy`, `PutRolePolicy`, or `CreatePolicyVersion`.
- **Triage:** Identify actor and target principal; inspect policy document and effective permissions; compare with approved change records; search for follow-on activity.
- **High-risk clue:** Unexpected attachment of broad administrative permissions.
- **False positives:** Approved onboarding, deployment, and infrastructure-as-code changes.

## CLOUD-IAM-003 — New access key

- **Signal:** `CreateAccessKey`.
- **Triage:** Verify owner, purpose, age, storage location, and whether a key rotation was planned. Review subsequent API calls by the new identity.
- **Response:** Follow the organization's credential-revocation process if unauthorized. Do not paste secret access keys into tickets or this repository.

## CLOUD-NET-001 — Public IPv4 ingress

- **Signal:** `AuthorizeSecurityGroupIngress` with an IPv4 range of `0.0.0.0/0`.
- **Triage:** Identify security group, protocol, port range, resource exposure, duration, and change owner.
- **False positives:** Intentionally public services, temporary approved changes, or rules that are restricted by other controls.
- **Response:** If unauthorized, use the approved change process to restrict or remove the rule and verify service impact.

## Correlation ideas for future work

- Multiple failed sign-ins followed by a success for the same principal or source.
- IAM permission expansion followed by access-key creation or unusual API calls.
- Public ingress change followed by activity against the affected workload.
- New identity credentials followed by activity from a new region or unfamiliar source.

## MITRE ATT&CK mapping

Mapping depends on observed behavior and context. Do not force a technique mapping when evidence is insufficient. Potential investigative references include Valid Accounts (T1078) and External Remote Services (T1133) only when the event sequence supports those interpretations. Cloud control-plane actions should be mapped carefully and documented with the specific evidence.

## Analyst rule-validation record

For every detection, record: source fields, query/rule version, test event, expected result, actual result, false-positive scenarios, owner, and last validation date. A rule that matches synthetic data is not yet a validated production detection.
