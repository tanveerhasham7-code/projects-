# 01 — DFIR Foundations

## 1. What is digital forensics?

Digital forensics is the disciplined identification, preservation, examination, analysis, and reporting of information stored or transmitted by digital systems. The goal is to produce findings that are repeatable, technically supported, and understandable to the intended audience.

Digital evidence may come from:
- Endpoints: desktops, laptops, servers, and mobile devices.
- Operating systems: event logs, registry, journals, configuration, and process data.
- Storage: filesystems, partitions, disk images, removable media.
- Memory: running processes, network connections, loaded modules, and other volatile state.
- Networks: packet captures, DNS, proxy, firewall, VPN, and flow records.
- Cloud platforms: identity events, audit logs, object access, and control-plane records.
- Applications: web server, database, email, authentication, and application logs.

## 2. What is incident response?

Incident response is the organized process used to prepare for, detect, analyze, contain, eradicate, and recover from security incidents. Digital forensics supports incident response by establishing what happened and preserving supporting evidence.

A commonly used lifecycle is:
1. Preparation.
2. Detection and analysis.
3. Containment, eradication, and recovery.
4. Post-incident activity and lessons learned.

Organizations may use different frameworks and phase names. Follow the incident-response policy in force for the environment.

## 3. DFIR roles

- **SOC analyst:** triages alerts and identifies events requiring deeper investigation.
- **Incident responder:** coordinates containment and recovery.
- **Forensic examiner:** acquires and examines evidence using documented procedures.
- **Threat hunter:** searches for activity that may not have generated an alert.
- **Incident commander:** coordinates people, priorities, communication, and decisions.
- **Legal/privacy/compliance teams:** advise on obligations, evidence handling, and notification.

In small teams, one person may perform several roles. Record who performed each action.

## 4. Key forensic principles

- **Integrity:** demonstrate that evidence has not changed unexpectedly.
- **Authenticity:** document where evidence came from and how it was collected.
- **Repeatability:** another qualified person should be able to follow the documented method.
- **Minimization:** collect only what is authorized and necessary.
- **Traceability:** connect each finding to a specific evidence item and analysis step.
- **Objectivity:** test alternative explanations and state uncertainty.

## 5. Important terms

- **Artifact:** a data item that may help explain system or user activity.
- **Acquisition:** collection of data from a source using a defined method.
- **Forensic image:** a bit-for-bit or otherwise defined copy of a storage source.
- **Volatile data:** information that may disappear when a system is powered off or changes state.
- **Working copy:** a verified duplicate used for examination.
- **Hash:** a fixed-length digest used to compare data integrity.
- **Timeline:** events arranged by time with source and context.
- **IOC:** indicator of compromise, such as a known malicious hash or domain; an IOC alone does not prove compromise.

## 6. Example

A SIEM alert reports an unusual PowerShell process. A disciplined investigation may:
1. Record the alert ID and time window.
2. Preserve relevant Windows event logs and endpoint telemetry according to policy.
3. Identify the user, host, process ancestry, command line, and network connections.
4. Correlate logon events, scheduled tasks, file creation, and DNS activity.
5. Determine whether the activity matches an approved administrative task.
6. Report confirmed observations separately from hypotheses.

## 7. Knowledge check

1. Why is an alert not automatically proof of compromise?
2. Why should originals be preserved?
3. What is the difference between acquisition and analysis?
4. Why must a report describe limitations?
