# SOC Investigation Report — [Case ID]

> Status: Draft template. Replace bracketed fields only after performing the investigation. Do not include secrets or unredacted personal data.

## 1. Case summary

| Field | Value |
|---|---|
| Case ID | [e.g. LAB-IR-001] |
| Analyst | Tanveer Hassham |
| Date opened | [date + timezone] |
| Alert / rule ID | [value] |
| Severity | [Wazuh level / local triage rating] |
| Endpoint | [redacted lab endpoint] |
| Disposition | [True positive / Benign positive / False positive / Inconclusive] |
| Confidence | [Low / Medium / High, with reason] |

## 2. Executive summary

[Summarize what was observed, why it was reviewed, and the outcome. Do not state "compromise" unless evidence supports it.]

## 3. Detection details

- Data source:
- Event ID / rule:
- Event timestamp:
- Account / process / source:
- Relevant fields:
- Search/filter used:

## 4. Investigation steps

1. [Step performed and result]
2. [Step performed and result]
3. [Step performed and result]

## 5. Timeline

| Timestamp + timezone | Source | Observation | Interpretation |
|---|---|---|---|
| | | | |

## 6. MITRE ATT&CK mapping

| Technique ID | Technique | Evidence supporting the mapping |
|---|---|---|
| | | |

Write "Not mapped" when evidence is insufficient.

## 7. Findings

### Confirmed facts
- [Only directly observed facts]

### Analyst assessment
- [Reasoned interpretation]

### Alternative / benign explanations
- [Potential expected activity and how it was assessed]

### Evidence gaps
- [Missing logs, fields, context, or limitations]

## 8. Response

- Actions actually performed:
- Recommendations:
- Escalation decision:

Clearly distinguish actions performed from recommendations only.

## 9. Evidence

- Screenshot paths:
- Sanitized event export:
- Relevant configuration / rule version:

## 10. Lessons learned and tuning

- What worked:
- What did not:
- False-positive considerations:
- Detection improvements:
- Follow-up test:
