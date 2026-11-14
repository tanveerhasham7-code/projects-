# Microsoft Sentinel SOC Lab — SIEM, KQL, Detection Engineering and Incident Response

**Track:** SOC Analyst / Cloud Security Operations / Blue Team  
**Level:** Beginner to Advanced  
**Status:** Detailed project blueprint published. Azure deployment, data ingestion, analytics rules, playbooks and incident investigations are not yet verified.

## 1. Project overview
Build a Microsoft Sentinel training environment to learn cloud SIEM operations from the analyst perspective. The project covers Azure resource foundations, Log Analytics Workspace, Sentinel setup, data connectors, KQL hunting, analytics rules, incidents, entity mapping, workbooks, automation and incident response.

Companion theory: [Microsoft Sentinel for SOC Analysts — Learning Journey](https://github.com/tanveerhasham7-code/learning-journey/tree/main/microsoft-sentinel).

**Portfolio integrity:** This repository currently documents the architecture, staged build, queries, detection hypotheses, exercises and report templates. It does not claim that an Azure workspace has been deployed, live logs have been ingested, alerts have fired or playbooks have run. Add your own sanitized evidence after performing the exercises.

## 2. Learning outcomes
1. Explain Azure tenant, subscription, resource group and workspace relationships.
2. Plan and configure an authorized Sentinel workspace.
3. Understand data connectors, tables and ingestion validation.
4. Write KQL from beginner to intermediate/advanced hunting patterns.
5. Design analytics rules and entity mappings.
6. Triage alerts and investigate incidents.
7. Design workbooks and SOC reporting.
8. Design safe automation using Sentinel automation rules and Logic Apps.
9. Document governance, access, cost and operational health.
10. Produce evidence-based incident reports.

## 3. Proposed architecture

~~~text
Identity / Endpoint / Azure / Network / Applications
                    |
              Data connectors
                    |
                    v
          Log Analytics Workspace
             Tables and records
                    |
             KQL investigation
                    |
          Analytics / Detection rules
                    |
                  Alerts
                    |
                Incidents
                    |
          SOC analyst investigation
              /             \
         Workbooks      Automation rules
                              |
                         Logic Apps
                         playbooks
~~~

This is a proposed design, not a deployed environment.

## 4. Prerequisites and cost controls
- An Azure tenant and subscription that you are authorized to use.
- Review current Sentinel pricing, regional availability, trial/free eligibility and retention charges before creating resources.
- Set a budget and billing alert where supported.
- Use sample or synthetic data for initial exercises.
- Never connect employer or third-party logs without written authorization.
- Use least-privilege RBAC and MFA.
- Redact tenant IDs, subscription IDs, usernames, IP addresses and sensitive event content from public screenshots.
- Document resource cleanup and remove unused paid resources after the lab.

## 5. Staged implementation plan

### Phase 0 — Azure and cost planning
Document tenant/subscription concepts, region, resource group, expected data sources, expected volume, access model, retention and cleanup.
**Validation:** Dated cost and architecture plan.

### Phase 1 — Workspace and Sentinel
Create or select an authorized resource group, deploy a Log Analytics Workspace and enable Sentinel following current Microsoft documentation.
**Validation:** Redacted workspace/Sentinel configuration and access notes.

### Phase 2 — Data connector
Choose one approved source or supported sample-data option. Configure prerequisites and validate the destination table.
**Validation:** Connector status plus query evidence showing records and expected fields.

### Phase 3 — KQL fundamentals
Write queries using where, project, extend, summarize, order by, bin, joins and time filters. Adapt examples to actual schemas.
**Validation:** At least five queries with results and plain-language explanations.

### Phase 4 — Hunting and detection
Define a hypothesis, verify telemetry, write a KQL query, test with safe/sample data, tune false positives and document limitations.
**Validation:** Detection specification, query, test notes and review outcome.

### Phase 5 — Incidents and entity mapping
Configure a safe analytics rule where authorized, inspect resulting alerts/incidents and validate entity mapping.
**Validation:** Redacted alert/incident evidence or clearly labelled sample scenario.

### Phase 6 — Workbooks
Design a SOC dashboard for incident trends, severity, top detections and data-source health.
**Validation:** Workbook design or sanitized screenshot and description.

### Phase 7 — Automation
Design a non-destructive playbook for enrichment and analyst notification. Use least privilege and require human approval for disruptive actions.
**Validation:** Workflow diagram, permissions and test evidence if implemented.

### Phase 8 — Investigation and operations
Complete a synthetic incident report. Review access, retention, connector health, ingestion, costs and cleanup.
**Validation:** Timeline, case report, operational checklist and cleanup record.

## 6. KQL query starter pack

These are learning examples. Confirm the table exists and inspect its schema before running. A missing table or field requires connector/schema investigation, not blind copying.

### Query 1 — Inspect recent sign-ins

~~~kusto
SigninLogs
| where TimeGenerated > ago(24h)
| take 20
~~~

### Query 2 — Count sign-ins by result

~~~kusto
SigninLogs
| where TimeGenerated > ago(24h)
| summarize Total = count() by ResultType
| order by Total desc
~~~

### Query 3 — Top source IPs

~~~kusto
SigninLogs
| where TimeGenerated > ago(24h)
| summarize Attempts = count() by IPAddress
| top 20 by Attempts desc
~~~

### Query 4 — Review audit activity

~~~kusto
AuditLogs
| where TimeGenerated > ago(24h)
| project TimeGenerated, ActivityDisplayName, Category, Result
| order by TimeGenerated desc
~~~

### Query 5 — Bucket activity by hour

~~~kusto
SigninLogs
| where TimeGenerated > ago(7d)
| summarize Events = count() by bin(TimeGenerated, 1h)
| order by TimeGenerated asc
~~~

**Query caution:** Table availability, field names, result semantics and access depend on connector and environment. Validate with actual workspace data.

## 7. Detection use-case backlog

All use cases below are hypotheses, not deployed or validated analytics rules.

### SENT-DET-01 — Repeated sign-in failures
- **Source:** SigninLogs.
- **Hypothesis:** Repeated failures against one identity may indicate password guessing or an account issue.
- **Review:** Account, IP, device, authentication method, result, MFA and later successful sign-ins.
- **False positives:** Mistyped passwords, expired credentials, user device changes.

### SENT-DET-02 — Unusual successful sign-in after failures
- **Source:** SigninLogs.
- **Hypothesis:** A successful sign-in after a failure burst from an unusual context needs review.
- **Review:** Time sequence, source, device, risk signals and user baseline.
- **False positives:** User typo followed by correct password, approved testing.

### SENT-DET-03 — Privileged role assignment
- **Source:** AuditLogs and relevant Entra role activity.
- **Hypothesis:** Unexpected privileged role assignment may create elevated access.
- **Review:** Initiating identity, target, role, approval and change record.
- **False positives:** Approved identity administration.

### SENT-DET-04 — Suspicious cloud resource change
- **Source:** AzureActivity.
- **Hypothesis:** High-impact resource or network configuration changes outside an approved window need investigation.
- **Review:** Caller, operation, resource, result, time and change approval.
- **False positives:** Planned deployment and maintenance.

### SENT-DET-05 — Endpoint alert correlation
- **Source:** Defender-related tables when integrated and available.
- **Hypothesis:** Related endpoint alerts across one device may represent a larger incident.
- **Review:** Device, user, process, alert timeline and response status.
- **False positives:** Duplicate or correlated benign detections.

### SENT-DET-06 — Data source health gap
- **Source:** Heartbeat or connector/agent health data where available.
- **Hypothesis:** A critical source stops reporting and creates a monitoring blind spot.
- **Review:** Last event, agent status, maintenance and network health.
- **False positives:** Planned shutdown and maintenance.

## 8. Practical exercise backlog

All tasks begin as Planned. Mark Verified only after you perform them and inspect actual evidence.

| ID | Exercise | Evidence expected | Status |
|---|---|---|---|
| MS-LAB-01 | Draw Azure resource hierarchy | Tenant/subscription/resource plan | Planned |
| MS-LAB-02 | Review pricing and eligibility | Dated cost notes | Planned |
| MS-LAB-03 | Plan workspace and region | Sanitized architecture | Planned |
| MS-LAB-04 | Deploy workspace and enable Sentinel (if authorized) | Redacted setup evidence | Planned |
| MS-LAB-05 | Review RBAC and least privilege | Role/scope notes | Planned |
| MS-LAB-06 | Explore connector catalog | Connector inventory | Planned |
| MS-LAB-07 | Connect approved source/sample data | Connector and table evidence | Planned |
| MS-LAB-08 | Inspect table schema | Column and type notes | Planned |
| MS-LAB-09 | Write five basic KQL queries | Query text and results | Planned |
| MS-LAB-10 | Build a hunting query | Hypothesis, query and interpretation | Planned |
| MS-LAB-11 | Draft analytics rule | Rule specification and test plan | Planned |
| MS-LAB-12 | Triage sample alert/incident | Triage notes | Planned |
| MS-LAB-13 | Design entity mapping and workbook | Design or screenshots | Planned |
| MS-LAB-14 | Design a non-destructive playbook | Workflow and permission notes | Planned |
| MS-LAB-15 | Investigate synthetic incident | Timeline and case report | Planned |
| MS-LAB-16 | Review cost and clean up | Cleanup evidence | Planned |

## 9. Detection specification template

~~~yaml
detection_id: SENT-DET-EXAMPLE
name: Example cloud identity behavior
status: experimental
hypothesis: Describe behavior requiring investigation.
data_sources:
  - SigninLogs
required_fields:
  - TimeGenerated
  - UserPrincipalName
  - IPAddress
  - ResultType
logic_summary: Describe the KQL logic and time window.
false_positives:
  - Approved administrative or user activity
limitations:
  - Requires validated connector coverage and field semantics
response:
  - Validate identity, source, device, timeline and business context
~~~

## 10. SOC investigation playbook
1. Validate the alert rule and raw query results.
2. Confirm workspace, source table, time range and timestamps.
3. Validate mapped account, host, IP and cloud resource entities.
4. Pivot across identity, endpoint, Azure activity and network sources.
5. Build a timeline and assess scope.
6. Check approved changes, maintenance and user context.
7. Preserve query text and sanitized evidence.
8. Record confirmed facts, assumptions and gaps separately.
9. Escalate and recommend response under organizational policy.
10. Close with findings, confidence and detection improvements.

## 11. Incident report template

~~~markdown
# Microsoft Sentinel Incident Report
Incident reference:
Date/time and timezone:
Analyst:
Summary:
Severity and rationale:
Affected accounts/assets:
Timeline:
Workspace/tables/queries:
Evidence references:
Findings:
Alternative explanations:
Scope and impact:
Actions and approvals:
Assessment: Benign / Suspicious / Confirmed / Inconclusive
Recommendations:
Limitations and lessons learned:
~~~

## 12. Suggested repository structure

~~~text
microsoft-sentinel-soc-lab/
├── README.md
├── docs/
│   ├── ARCHITECTURE.md
│   ├── AZURE-PREREQUISITES-AND-COST.md
│   ├── DATA-CONNECTORS.md
│   ├── KQL-GUIDE.md
│   ├── INCIDENT-RESPONSE.md
│   └── GOVERNANCE-AND-OPERATIONS.md
├── queries/
│   ├── identity/
│   ├── azure-activity/
│   └── endpoint/
├── detections/
│   ├── README.md
│   └── specifications/
├── workbooks/
│   └── README.md
├── playbooks/
│   └── README.md
├── evidence/
│   └── README.md
└── reports/
    └── INCIDENT-REPORT-TEMPLATE.md
~~~

Add query files and exported configurations only when they are useful and safe to publish. Never commit secrets, tenant identifiers or unredacted logs.

## 13. Success criteria
- Authorized environment and cost plan documented.
- Workspace and Sentinel deployment evidenced if performed.
- At least one source or sample dataset queried.
- Five KQL queries explained.
- One hunting hypothesis documented and tested.
- One analytics rule specification tested safely.
- One alert/incident triage completed.
- Workbook and playbook designs documented.
- One synthetic incident report completed.
- Access, retention, cost and cleanup reviewed.

## 14. References
- [Microsoft Sentinel documentation](https://learn.microsoft.com/en-us/azure/sentinel/)
- [Kusto Query Language](https://learn.microsoft.com/en-us/kusto/query/)
- [Log Analytics Workspace overview](https://learn.microsoft.com/en-us/azure/azure-monitor/logs/log-analytics-workspace-overview)
- [Sentinel data connectors](https://learn.microsoft.com/en-us/azure/sentinel/connect-data-sources)
- [Sentinel analytics rules](https://learn.microsoft.com/en-us/azure/sentinel/detect-threats-built-in)
- [Sentinel automation](https://learn.microsoft.com/en-us/azure/sentinel/automation/automation)
- [Microsoft Sentinel pricing](https://azure.microsoft.com/en-us/pricing/details/microsoft-sentinel/)

## Current status
**Published:** Project blueprint, architecture, staged implementation plan, KQL starter pack, six detection hypotheses, 16 practical exercises, investigation playbook and report templates.  
**Pending validation:** Azure workspace deployment, connector setup, data ingestion, KQL results, analytics rules, incidents, workbooks, playbooks and practical evidence.