# Analyst incident-response runbook

## Validate
Confirm case fingerprint and original Wazuh alert. Check timestamp/timezone, agent health, rule ID/level, and fields. Treat AI output as a hypothesis and verify claims against source telemetry.

## Scope
Search adjacent events for the same account, source, host, process, and time window. Identify asset criticality. Check identity, endpoint, firewall, DNS, VPN, and authentication telemetry where authorized. Check for approved changes.

## Classify
Choose true positive, benign positive, false positive, duplicate, or inconclusive. Record evidence and confidence. A high risk score is not confirmation of compromise.

## Escalate and contain
Follow approved organizational policy. Disabling accounts, isolating endpoints, blocking IPs, or killing processes requires authorized human approval and an audit trail. Sentinel does not execute these actions.

## Recover and learn
Document eradication/recovery decisions, validate service health, preserve evidence, tune detections when justified, and record lessons learned.
