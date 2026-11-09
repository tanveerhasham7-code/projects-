# Purple Team Three-Machine Cybersecurity Lab
## Windows Endpoint + Ubuntu Server + Kali Linux

An advanced, isolated purple-team portfolio project that connects offensive security simulation with defensive monitoring, detection engineering, incident response, and reporting.

This project uses three separate virtual machines:

1. **Windows Endpoint** — the monitored workstation and primary investigation target.
2. **Ubuntu Server** — a monitored Linux server that provides a controlled service and centralized lab role.
3. **Kali Linux** — the authorized security-testing and adversary-simulation machine.

The objective is not simply to run attack tools. The objective is to understand the behavior, generate observable telemetry, detect it, investigate it, explain the evidence, and recommend defensive improvements.

> **Safety boundary:** Use an isolated host-only/internal virtual network and systems you own. Do not bridge the attacker VM to public or third-party targets. Do not use real credentials, malware, destructive payloads, persistence, credential dumping, or denial-of-service. This project uses harmless, reversible simulations and test accounts only.

## Why this is more advanced

The earlier Wazuh project focused on building a SIEM home lab. The Threat Hunting project focused on detection logic and analyst hunts. This project combines all three systems into an end-to-end purple-team exercise:
- Model a small enterprise environment.
- Establish baseline telemetry on Windows and Ubuntu.
- Simulate safe, observable behaviors from Kali.
- Identify which events are generated on each target.
- Confirm whether Wazuh collects and correlates the events.
- Write or adapt detections.
- Investigate alerts and distinguish expected activity from suspicious activity.
- Measure detection gaps and produce a professional report.

## Architecture

```text
                 ISOLATED HOST-ONLY / INTERNAL NETWORK
                 Example subnet: 192.168.56.0/24
                 (Use your own non-conflicting lab subnet)

      +--------------------+       +----------------------+
      | Kali Linux         |       | Windows Endpoint     |
      | Authorized tester  |------>| Wazuh agent          |
      | Nmap / curl /      |       | Sysmon + Security log|
      | safe test scripts  |       | Test account         |
      +--------------------+       +----------------------+
                 |
                 | controlled lab traffic
                 v
      +--------------------+
      | Ubuntu Server      |
      | SSH / web service  |
      | Wazuh agent        |
      | Authentication log |
      +--------------------+

      Wazuh Manager / Indexer / Dashboard:
      Place on an existing trusted lab VM or a separate host.
      Do not assume the Ubuntu target is also the Wazuh manager.
```

The three machines are the lab endpoints. Wazuh management may run on a separate existing machine or a separately provisioned management VM. Keep management access restricted to the lab network.

## Project status

**Documentation and practical plans are prepared.** No scans, connections, alerts, detections, or investigations are claimed as completed. Add screenshots and measured results only after running each exercise.

## Start here — required order

1. Read `docs/00-project-overview.md`.
2. Read `docs/01-lab-safety-and-network-design.md`.
3. Complete `docs/02-hardware-and-vm-planning.md`.
4. Inventory your existing VMs before creating or reinstalling anything.
5. Complete `docs/03-build-and-baseline.md`.
6. Verify endpoint telemetry and agent health.
7. Perform the safe exercises in `exercises/` one at a time.
8. Record evidence in `evidence/` and update the exercise result.
9. Complete the capstone and final report.

## Project modules

| Module | Main focus |
|---|---|
| 00 | Project overview and terminology |
| 01 | Isolation, network design, safety |
| 02 | Hardware and VM planning |
| 03 | Build, inventory, and baseline |
| 04 | Wazuh telemetry and agent health |
| 05 | Windows event and Sysmon visibility |
| 06 | Ubuntu service and authentication visibility |
| 07 | Kali reconnaissance in the lab |
| 08 | Safe authentication-failure simulation |
| 09 | Web request and access-log analysis |
| 10 | Detection engineering and tuning |
| 11 | Incident investigation and reporting |
| 12 | Purple-team capstone |

## What you will produce

- Three-machine network and asset inventory.
- Baseline records for Windows and Ubuntu.
- Kali test activity log.
- Detection specifications and rule candidates.
- Screenshots of real events and alerts.
- Two or more investigation reports.
- Detection validation matrix.
- Final purple-team report with limitations and recommendations.

## Evidence policy

Every exercise has one of these states: Planned, Ready, Attempted, Passed, Failed, Inconclusive. "Passed" means the expected telemetry and detection outcome were actually observed and recorded. A successful tool command alone does not prove detection success.

## Skills demonstrated

Linux administration • Windows logging • Sysmon • Wazuh SIEM • Network fundamentals • Nmap fundamentals • HTTP and SSH log analysis • Detection engineering • Threat hunting • Incident response • MITRE ATT&CK • Evidence handling • Technical reporting
