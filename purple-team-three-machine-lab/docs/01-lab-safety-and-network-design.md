# 01 — Lab Safety and Network Design

## 1. Isolation is mandatory

Use a Host-only or Internal Network in your hypervisor. Do not use Bridged networking for Kali during these exercises. NAT may provide internet access but does not by itself guarantee that the VMs are isolated from your home or office network. Prefer a dedicated host-only/internal segment with no route to production networks.

Never scan public IP addresses, campus networks, workplace networks, neighbors' devices, or systems you do not own or have explicit permission to test.

## 2. Example addressing plan

This is an example only. Check for conflicts before using it.

| Machine | Example address | Role |
|---|---:|---|
| Kali | 192.168.56.10 | Authorized test workstation |
| Windows | 192.168.56.20 | Monitored endpoint |
| Ubuntu | 192.168.56.30 | Monitored server |
| Wazuh manager | Existing management address | SIEM management |

Use static DHCP reservations or static addresses only if you understand your virtual network. Record the actual addresses in your private lab notes. Do not publish sensitive addresses if you do not want them public.

## 3. Network checks

Before any test:
- Confirm all three VMs use the intended isolated network.
- Confirm Kali can reach only the intended lab targets.
- Confirm the management interface is not exposed publicly.
- Confirm host firewall rules restrict unnecessary inbound access.
- Take VM snapshots before configuration changes.
- Use dedicated lab-only test accounts and non-reused passwords.

## 4. Allowed activities in this project

- Ping or basic connectivity checks between lab VMs.
- Nmap service discovery against the explicitly listed lab IPs only.
- Harmless HTTP GET requests to the lab web service.
- A small number of deliberately incorrect logins against a lab-only account, within the exercise limits.
- Normal PowerShell process creation and benign commands for Sysmon visibility.
- Reviewing logs, queries, alerts, and configuration.

## 5. Out of scope

- Denial-of-service or stress testing.
- Password spraying, brute-force tools, or credential guessing at scale.
- Exploitation of real vulnerabilities.
- Malware, ransomware, payload delivery, or persistence.
- Credential dumping, token theft, or bypassing security controls.
- Scanning beyond the isolated lab subnet.

## 6. Emergency stop

If traffic reaches an unintended network, stop the test immediately, disconnect Kali's virtual network adapter, and inspect the hypervisor network configuration before continuing.
