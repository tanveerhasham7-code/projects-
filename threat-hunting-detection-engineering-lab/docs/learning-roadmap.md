# Learning Roadmap: Beginner to Advanced

## Module 1 — Detection foundations
**Theory:** distinguish an asset, event, log, telemetry source, indicator, alert, incident, and detection. Understand that a detection is a testable statement about observable behavior, not a verdict that an attacker exists.

**Practice:** choose one Windows event and document its provider, event ID, timestamp, host, user, process, and outcome. Find the same event in the endpoint log and SIEM if available.

**Deliverable:** telemetry glossary and one event walkthrough.

## Module 2 — Data sources and quality
**Theory:** Windows Security auditing, Sysmon, Linux authentication logs, endpoint agent health, time synchronization, event loss, parsing, normalization, and retention.

**Practice:** inventory data sources on the existing lab. Confirm which host generates each event and whether the event reaches Wazuh. Record missing fields and time differences.

**Deliverable:** data-source matrix.

## Module 3 — Detection logic
**Theory:** matching conditions, event sequences, aggregation, thresholds, time windows, allowlists, exclusions, severity, confidence, and alert fatigue.

**Practice:** write a detection specification before writing a rule. Define behavior, required fields, data source, logic, expected benign matches, and known blind spots.

**Deliverable:** one detection specification and one rule candidate.

## Module 4 — Sigma
**Theory:** Sigma is a generic, YAML-based format for describing log detections. A Sigma rule is not automatically active in Wazuh; it must be translated or implemented in a supported backend and tested against the actual event schema.

**Practice:** inspect the starter rules in sigma/. Validate YAML locally with an appropriate YAML parser if installed. Review field names against the events your environment actually collects.

**Deliverable:** reviewed rule with backend/adaptation notes.

## Module 5 — Threat hunting
**Theory:** hypothesis-led hunting, baselines, scoping, pivots, timelines, context, and documenting inconclusive results.

**Practice:** choose one hunt in hunts/. State what evidence would support or weaken the hypothesis. Search only your own lab telemetry.

**Deliverable:** completed hunt worksheet.

## Module 6 — Validation and tuning
**Theory:** test cases, expected telemetry, observed telemetry, false positives, false negatives, coverage gaps, regression testing, and detection confidence.

**Practice:** run only the safe, explicitly described lab actions in validation/. Capture the resulting event and alert. If the event does not appear, troubleshoot collection before changing detection logic.

**Deliverable:** validation record with screenshots.

## Module 7 — Capstone
Create a small detection pack of at least three documented detections, complete two hunt reports, record test outcomes, and present limitations and next steps.

## Recommended study rhythm
Study the theory for one module, perform its practical exercise, write the evidence record, and only then move forward. Do not mark a module complete merely because you read it.
