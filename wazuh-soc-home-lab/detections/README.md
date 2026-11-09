# Detection Engineering Workspace

This folder will hold version-controlled detection artefacts after the environment is deployed.

## Planned artefacts

- Wazuh custom rules (XML), with rule IDs, descriptions, levels, and rationale.
- Sample event records that are synthetic and sanitized.
- Test cases describing expected match / non-match behaviour.
- Tuning notes and false-positive analysis.
- ATT&CK mappings with justification.

## Rule development standard

Each rule contribution must document:
1. Data source and required event fields.
2. Detection hypothesis and expected behaviour.
3. Rule ID and rule logic.
4. Positive test and negative / benign test.
5. Actual result from the lab, with evidence link.
6. Known limitations and tuning notes.

No custom rule is marked tested until it has been loaded successfully and validated against observed telemetry. Avoid copying unverified rule snippets into production systems. Start with the built-in Wazuh rules and document what they detect before writing custom rules.

**Current status:** no custom rules have been validated in this lab yet.
