# Active Directory SOC Monitoring Lab

**Track:** Blue Team / Junior SOC Analyst  
**Level:** Beginner to Intermediate, with advanced detection extensions  
**Primary focus:** Windows domain identity monitoring, authentication telemetry, privileged access, detection engineering and incident investigation  
**Status:** Project blueprint and documentation published. Practical exercises are planned and must be completed by the author before being marked verified.

## 1. Project overview

This project is an isolated Active Directory training environment designed to teach how a SOC analyst monitors and investigates identity-related activity in a Windows domain.

The lab will generate legitimate, controlled activity using test accounts and test systems. Windows Security events will be collected and reviewed to understand how normal administration appears in logs and how suspicious patterns can be detected.

The project connects directly to the theory module in the Learning Journey repository:

[Active Directory Security for SOC Analysts — Learning Journey](https://github.com/tanveerhasham7-code/learning-journey/tree/main/active-directory-security)

### What this project aims to demonstrate

- Understanding a small Windows domain and its identity components.
- Enabling and validating relevant Windows audit policies.
- Generating controlled account, group and authentication events.
- Collecting and searching Windows event logs.
- Building detection hypotheses for suspicious identity activity.
- Investigating alerts with evidence, timelines and context.
- Writing clear SOC case reports and recommendations.

**Important:** Publishing this blueprint does not mean the lab has been deployed, detections have fired, or an integration has been validated. Add screenshots, exported events and test results only after personally performing the exercises.

## 2. Learning objectives

By completing the project, the author should be able to:

1. Explain the roles of a domain controller, domain, OU, user, computer and security group.
2. Identify the source computer and meaning of important Windows Security events.
3. Distinguish the actor performing a directory change from the account/object being changed.
4. Investigate successful and failed domain logons.
5. Review account creation, enablement, password reset and group membership changes.
6. Recognize suspicious privileged account behavior.
7. Correlate events across a timeline and multiple systems.
8. Build and tune basic SIEM detections.
9. Explain false positives and detection limitations.
10. Produce a professional incident report supported by evidence.

## 3. Lab architecture

### 3.1 Recommended components

| Component | Purpose | Notes |
|---|---|---|
| Windows Server VM | Domain Controller with AD DS and DNS | Use a supported evaluation image in an isolated lab |
| Windows client VM | Domain-joined endpoint | Use test users only |
| Analyst host / VM | Review logs and document findings | Keep evidence sanitized |
| Wazuh (optional) | Central log collection, alerting and investigation | Configure only after basic event generation is understood |
| Sysmon (optional) | Additional endpoint process and network telemetry | Use a documented configuration and validate event collection |

The lab can begin with two virtual machines: one domain controller and one Windows client. The analyst can review exported event logs from the host. Add a separate SIEM only when the basic domain and event flow are working.

### 3.2 Network safety

- Use a private or host-only virtual network for the domain lab.
- Do not expose the domain controller's AD services directly to the public internet.
- Do not use real personal, university or workplace credentials.
- Use fictional test users and non-sensitive data.
- Take VM snapshots before configuration changes.
- Keep the lab separate from production networks.
- Do not run password spraying, destructive actions, malware or denial-of-service tests.
- Never upload passwords, hashes, tokens, private keys or unredacted personal data.

### 3.3 Logical topology

```text
             Isolated Virtual Network
                       |
          +------------+-------------+
          |                          |
  +-------v--------+         +-------v--------+
  | Windows Server |         | Windows Client |
  | Domain Control |         | Domain Joined  |
  | AD DS + DNS    |         | Test User      |
  +-------+--------+         +-------+--------+
          |                          |
          +------------+-------------+
                       |
             Windows Security Events
                       |
              +--------v---------+
              | Analyst / Wazuh  |
              | Search, Triage,  |
              | Timeline, Report |
              +------------------+
```

This is a proposed architecture, not a record of a running or validated environment.

## 4. Build phases

### Phase 1 — Prepare the environment

- Confirm host virtualization support and available resources.
- Create an isolated virtual network.
- Prepare Windows Server and Windows client VMs.
- Record OS editions, versions, VM names and network settings.
- Take clean snapshots.

**Exit criteria:** Both VMs boot, communicate only as intended within the lab, and the topology is documented.

### Phase 2 — Configure the test domain

- Install AD DS and DNS on the Windows Server VM.
- Create a clearly fictional test domain, for example `corp.example.test`.
- Create a small OU structure for users, workstations and test service identities.
- Create standard test users and non-privileged test groups.
- Join the Windows client to the domain.
- Verify domain DNS and authentication.

**Exit criteria:** The client is domain-joined and a test user can sign in. Save sanitized verification evidence.

### Phase 3 — Configure security auditing

Enable the required advanced audit subcategories through an appropriate test GPO or local policy. At minimum, plan to review:

- Account Logon.
- Logon/Logoff.
- Account Management.
- Detailed Tracking (where required).
- Policy Change.
- Directory Service Access or Directory Service Changes where appropriate and supported.

Audit policy names, event generation and event locations can vary by Windows version and configuration. Validate the actual events rather than assuming a setting worked.

**Exit criteria:** A controlled test action generates the expected event, and the event's source computer and fields are understood.

### Phase 4 — Collect and review events

Start with Event Viewer on the relevant computer. Export a small, relevant EVTX sample after each exercise. If Wazuh is used, document the agent, manager, collection configuration, decoder/rule behavior and actual event arrival.

**Exit criteria:** The analyst can search for an event by ID, identify the source and explain the relevant fields.

### Phase 5 — Detection and investigation

Create detection logic from the use cases in Section 6. Begin with simple event searches; add correlation only after validating the data and time fields.

**Exit criteria:** Each detection has a written hypothesis, required telemetry, test cases, tuning notes and an investigation guide. Mark a detection validated only when a real lab test supports that claim.

### Phase 6 — Reporting and review

For each exercise, create a short case note with evidence, timeline, assessment, limitations and recommendations.

**Exit criteria:** A reviewer can reproduce the reasoning from the saved, sanitized evidence.

## 5. Windows Security event reference

Event IDs are starting points, not complete detections. The source computer and audit configuration matter.

| Event ID | Meaning | Typical investigation |
|---|---|---|
| 4624 | Successful logon | Account, logon type, source and destination |
| 4625 | Failed logon | Failure reason, source, target and pattern |
| 4648 | Logon using explicit credentials | Process and context using supplied credentials |
| 4672 | Special privileges assigned to new logon | Privileged session context |
| 4688 | Process creation | Process execution, if configured |
| 4720 | User account created | Creator, new account and approval |
| 4722 | User account enabled | Actor and reason for enabling |
| 4723 | Attempt to change password | Account and context |
| 4724 | Attempt to reset password | Reset actor and target |
| 4725 | User account disabled | Offboarding or containment validation |
| 4726 | User account deleted | Change authorization |
| 4728 / 4729 | Member added to / removed from a global security group | Group membership change |
| 4732 / 4733 | Member added to / removed from a local security group | Local group change |
| 4740 | User account locked out | Caller/source context and preceding failures |
| 4768 | Kerberos TGT requested | Domain authentication |
| 4769 | Kerberos service ticket requested | Service access patterns |
| 4771 | Kerberos pre-authentication failed | Authentication failure analysis |
| 4776 | NTLM credentials validated | NTLM activity |
| 1102 | Security audit log cleared | High-priority audit-log integrity investigation |

Some events are DC-side, while others are generated on the computer where the action or logon occurs. Always record the event source computer. Consult Microsoft event documentation for the Windows version in use.

## 6. Detection use cases

Each use case below is a detection design, not a claim that an alert has already been produced.

### AD-01 — Repeated authentication failures

- **Hypothesis:** Repeated failures against one or more accounts may indicate password guessing, a stale credential or a misconfigured service.
- **Telemetry:** 4625, source address, target account, target computer, logon type and status/substatus.
- **Logic:** Group failures by source and target over a measured time window; compare with a baseline; enrich with asset and account criticality.
- **Triage:** Check whether the source is a known application, VPN, scheduled task or user endpoint. Look for subsequent success.
- **False positives:** Mistyped passwords, expired saved credentials, service misconfiguration and scheduled tasks.

### AD-02 — Failures followed by a successful logon

- **Hypothesis:** A successful authentication after a cluster of failures may deserve review.
- **Telemetry:** 4625 and 4624 with account, source, target, logon type and timestamp.
- **Logic:** Correlate related failures and success within a documented time window. Do not assume source equality if NAT, proxies or multiple systems are involved.
- **Triage:** Confirm the user, device, authentication method, business context and subsequent activity.
- **False positives:** User mistakes, password changes and legitimate account recovery.

### AD-03 — New user account created

- **Hypothesis:** An account created outside the normal identity lifecycle may be unauthorized.
- **Telemetry:** 4720 and nearby enablement, password reset, group-change and first-logon events.
- **Logic:** Alert on account creation by unexpected actors, outside approved windows or with unusual initial group membership.
- **Triage:** Identify creator, target account, ticket/approval, OU, groups and first sign-in.
- **False positives:** Approved onboarding, testing and automation.

### AD-04 — Privileged group membership changed

- **Hypothesis:** A new member in a sensitive group can materially increase access.
- **Telemetry:** 4728, 4732 and related events, group name/SID, member, actor, DC and timestamp.
- **Logic:** Maintain an environment-specific list of sensitive groups; enrich with approved administrators and change windows.
- **Triage:** Validate the actor, member, group, ticket and activity after the change.
- **False positives:** Approved administration, role changes and emergency access.

### AD-05 — Account lockout

- **Hypothesis:** Repeated authentication failures have caused an account lockout that may indicate attack activity or a misconfigured client.
- **Telemetry:** 4740 and related 4625 events.
- **Logic:** Correlate lockout with caller/source information and preceding failures.
- **Triage:** Identify the system generating attempts and whether other accounts are affected.
- **False positives:** Old passwords in mobile devices, services or mapped drives.

### AD-06 — Unusual privileged account logon

- **Hypothesis:** A privileged identity authenticating from an unusual endpoint, at an unusual time or with an unexpected logon type may indicate misuse.
- **Telemetry:** 4624, 4672, account/group inventory, endpoint identity and baseline context.
- **Logic:** Compare privileged logons with approved administrative workstations, expected systems and normal activity.
- **Triage:** Validate administrator activity, source endpoint, destination, session and actions performed.
- **False positives:** On-call work, maintenance and emergency administration.

### AD-07 — NTLM authentication outside expected use

- **Hypothesis:** NTLM use from a system or account expected to use Kerberos may indicate legacy dependency or suspicious authentication.
- **Telemetry:** 4776 and relevant endpoint/domain authentication records.
- **Logic:** Baseline NTLM by host, account and application; alert on unexpected changes.
- **Triage:** Identify application dependency and assess whether the activity is expected.
- **False positives:** Legacy applications, workgroup devices and compatibility scenarios.

### AD-08 — Security audit log cleared

- **Hypothesis:** Clearing the Windows Security log can reduce visibility and requires investigation.
- **Telemetry:** 1102, actor, host and surrounding administrative events.
- **Logic:** Alert on the event and preserve surrounding logs from central collection.
- **Triage:** Validate maintenance context, actor authorization and whether collection stopped or other logs were affected.
- **False positives:** Authorized troubleshooting or maintenance, which should still be documented.

## 7. Investigation playbook

Use this checklist for identity-related alerts.

1. **Validate the record:** Confirm event ID, provider, source computer, timestamp and required fields.
2. **Identify the actor and target:** Separate Subject/actor fields from Target/account/object fields.
3. **Classify the identity:** Standard user, privileged user, service account or computer account.
4. **Understand the asset:** Determine whether the endpoint is a workstation, server or domain controller.
5. **Build a timeline:** Search relevant authentication, account-management and process events before and after the alert.
6. **Check the baseline:** Compare the activity with known normal behavior and the account's role.
7. **Verify authorization:** Check approved change tickets, maintenance windows or administrator confirmation.
8. **Scope the activity:** Search for related users, endpoints, sources and group changes.
9. **Assess impact:** Determine what access may have been gained or what systems may have been affected.
10. **Escalate and document:** Follow the organization's incident policy and preserve relevant evidence.

### Evidence to preserve

- Original event record or sanitized EVTX export.
- Event ID, provider, channel and source computer.
- Timestamp and timezone.
- Actor and target identifiers.
- Source address and logon type, when present.
- Relevant SIEM query and time range.
- Timeline of related activity.
- Approval/change record reference (do not publish confidential ticket details).
- Analyst assessment, confidence and unresolved questions.

## 8. Practical exercise backlog

All exercises begin as **Planned**. Update their status only after doing the work and saving evidence.

| ID | Exercise | Expected evidence | Initial status |
|---|---|---|---|
| LAB-01 | Record VM and isolated network topology | Sanitized topology and VM details | Planned |
| LAB-02 | Configure test domain and join client | Domain/client verification output | Planned |
| LAB-03 | Create a test user and inspect account events | Relevant event and field explanation | Planned |
| LAB-04 | Perform controlled failed and successful logons | 4625/4624 event samples | Planned |
| LAB-05 | Review a test account lockout | 4740 and related failure timeline | Planned |
| LAB-06 | Reset a test account password | Relevant event and actor/target analysis | Planned |
| LAB-07 | Add/remove a test group member | Group event and membership before/after | Planned |
| LAB-08 | Inspect an approved test GPO change | Policy setting and change evidence | Planned |
| LAB-09 | Review privileged group membership | Sanitized membership audit | Planned |
| LAB-10 | Search domain authentication events in Wazuh (optional) | Query, event arrival and screenshots | Planned |
| LAB-11 | Investigate a synthetic suspicious identity scenario | Timeline and case report | Planned |
| LAB-12 | Tune one detection and document false positives | Rule logic, test cases and tuning notes | Planned |

### Exercise completion template

Copy this template for each lab:

```markdown
## LAB-XX — Exercise name

**Date/time and timezone:**  
**Environment:**  
**Objective:**  
**Authorization/scope:** Own isolated lab  
**Steps performed:**
1.
2.
3.

**Expected result:**  
**Actual result:**  
**Evidence files:**  
**Relevant event IDs:**  
**What the evidence means:**  
**Problems or limitations:**  
**Status:** Planned / In Progress / Verified
```

A screenshot without context is weak evidence. Explain what it shows, where the event came from and why it matters.

## 9. Suggested repository structure

As the project grows, use this structure. Add files only when their content exists; do not create empty evidence or claim completed tests.

```text
active-directory-soc-monitoring-lab/
├── README.md
├── docs/
│   ├── ARCHITECTURE.md
│   ├── DOMAIN-BUILD-GUIDE.md
│   ├── AUDIT-POLICY.md
│   ├── EVENT-REFERENCE.md
│   ├── DETECTION-USE-CASES.md
│   └── INVESTIGATION-RUNBOOK.md
├── detections/
│   ├── README.md
│   └── examples/
├── queries/
│   ├── README.md
│   └── wazuh/
├── evidence/
│   ├── README.md
│   └── sanitized/
├── reports/
│   └── CASE-REPORT-TEMPLATE.md
└── lab-notes/
    └── TEMPLATE.md
```

Do not upload raw domain database files, credential material, unredacted EVTX logs or private organizational data. Review all evidence before publishing.

## 10. Portfolio report template

For a completed investigation, use:

- **Case ID:**
- **Alert/detection:**
- **Severity and rationale:**
- **Analyst / date:**
- **Summary:**
- **Affected identity and assets:**
- **Timeline (with timezone):**
- **Evidence collected:**
- **Investigation steps:**
- **Findings:**
- **Assessment:** Benign / Suspicious / Confirmed incident / Inconclusive
- **Scope and impact:**
- **Actions taken and approvals:**
- **Recommendations:**
- **Detection gaps and lessons learned:**
- **Evidence references:**

## 11. Success criteria

The project can be described as practically completed only when:

- The isolated domain and client are configured and documented.
- Required audit settings are enabled and validated.
- The relevant events are generated and correctly sourced.
- At least three detection use cases are tested with documented results.
- At least one investigation timeline and case report are completed.
- False positives and limitations are explained.
- Evidence is sanitized and reproducible.

## 12. Learning references

- [Microsoft Learn — Active Directory Domain Services](https://learn.microsoft.com/en-us/windows-server/identity/ad-ds/)
- [Microsoft Learn — Advanced Security Audit Policy Settings](https://learn.microsoft.com/en-us/windows/security/threat-protection/auditing/advanced-security-audit-policy-settings)
- [Microsoft Learn — Windows Security Auditing](https://learn.microsoft.com/en-us/windows/security/threat-protection/auditing/basic-audit-policy-recommendations)
- [Microsoft Learn — Kerberos Authentication Overview](https://learn.microsoft.com/en-us/windows-server/security/kerberos/kerberos-authentication-overview)
- [Wazuh Documentation](https://documentation.wazuh.com/current/)
- [MITRE ATT&CK — Enterprise](https://attack.mitre.org/)

---

## Current project status

**Published:** Project plan, proposed architecture, event reference, detection hypotheses, investigation workflow and practical backlog.  
**Not yet verified:** VM deployment, domain configuration, audit policy, event collection, Wazuh integration, detection execution and practical evidence.

The next update should be based on the author's real lab outputs, screenshots and investigation notes.
