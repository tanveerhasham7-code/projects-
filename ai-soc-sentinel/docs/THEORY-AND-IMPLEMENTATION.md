# Theory and implementation notes

## 1. SIEM and alert pipelines
A SIEM centralizes telemetry, parses events, applies detection rules, and creates alerts. Wazuh provides endpoint monitoring, log analysis, rule matching, and alert generation. Sentinel consumes selected alerts after Wazuh has detected them; it does not replace SIEM collection or decoding.

## 2. Why deterministic detection comes first
A rule-based baseline is reproducible and explainable. It uses Wazuh rule level, groups, and observable fields. It works even if the model is unavailable. A high rule level can still be a false positive and depends on local rule configuration.

## 3. Normalization
Sources represent the same concept using different field names. Normalization creates a stable schema: timestamp, rule ID/level, agent, source IP, user, process, and ATT&CK technique. Production systems should preserve original evidence in restricted storage; this starter stores a compact case record.

## 4. Risk scoring
Risk is prioritization, not probability of compromise. This implementation begins with Wazuh level and adds bounded points for indicators. Mature scoring should include asset criticality, identity privilege, exposure, threat intelligence, detection confidence, business impact, and false-positive history.

## 5. AI triage
The LLM summarizes evidence and suggests read-only checks. It can hallucinate or be manipulated by strings in logs. Safeguards:
- event values are explicitly untrusted data;
- the prompt forbids following embedded instructions;
- only a minimized field set is sent;
- strict JSON and confidence validation are applied;
- AI cannot lower deterministic critical severity;
- the model has no shell, tools, SIEM write access, or response credentials.

AI confidence is not a calibrated probability. Validate thresholds on labeled data before operational use.

## 6. Policy gate and human oversight
The policy gate—not the model—decides whether email is sent. Automatic side effects are limited to audit storage and notification. An analyst validates context, checks related telemetry, classifies the event, and follows approved playbooks.

## 7. Email and audit
Email is a notification channel, not proof of compromise. Avoid secrets and unnecessary personal data. SQLite fingerprints suppress exact duplicates in this single-instance starter; they do not provide distributed exactly-once processing.

## 8. Evaluation metrics
Measure precision, recall, false-positive rate, alert-to-email latency, duplicate suppression, schema-validity rate, analyst acceptance, and time-to-triage. Maintain labeled benign, suspicious, and ambiguous examples.
