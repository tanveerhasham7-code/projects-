# 09 — Evidence-Led Investigation Methodology

## 1. Start with a question

Avoid collecting data without a purpose. Convert the alert or report into answerable questions:
- What activity is being investigated?
- Which systems and identities are in scope?
- What time window is relevant?
- What evidence sources can answer the question?
- What collection is authorized?

## 2. Hypothesis-led analysis

Create one or more hypotheses and identify evidence that would support or weaken each one.

Example:
- Hypothesis: a privileged account was used unexpectedly.
- Supporting evidence: sign-in from an unapproved source, unusual MFA context, privileged action, and no matching change record.
- Alternative explanation: approved emergency administration or a known VPN egress change.
- Needed evidence: identity-provider logs, change ticket, user confirmation through approved channels, endpoint telemetry.

Do not select only evidence that confirms the first hypothesis.

## 3. Facts, interpretations, and confidence

- **Fact:** directly observable in a source (for example, an event log records a process start).
- **Interpretation:** what the observation may mean in context.
- **Hypothesis:** an explanation that requires testing.
- **Confidence:** how strongly the available evidence supports the interpretation.

Explain confidence using source quality, corroboration, consistency, and gaps—not intuition alone.

## 4. Impact and scope

Identify affected systems, accounts, data, business services, and time range. State what was not examined. Distinguish confirmed access from suspected access and data exposure from confirmed exfiltration.

## 5. MITRE ATT&CK

ATT&CK can help describe adversary behaviors and organize detection coverage. Map only when the observed behavior supports the technique. Record the specific evidence and avoid mapping an event name to a technique without context.

## 6. Reporting structure

1. Executive summary.
2. Scope and authorization.
3. Case and evidence identifiers.
4. Timeline.
5. Findings with source references.
6. Analysis and alternative explanations.
7. Impact and confidence.
8. Containment and recovery actions.
9. Limitations and evidence gaps.
10. Recommendations and lessons learned.

## 7. Professional writing

Use clear language. Include exact times with timezone. Identify the source for every important claim. Do not expose secrets or unnecessary personal data. Do not claim that an incident is confirmed if the evidence supports only suspicious activity.
