# 07 — Kali Safe Reconnaissance

## Theory
Reconnaissance is the process of learning what services are exposed on a target. In a defensive lab, a limited service inventory helps you compare expected exposure with actual exposure.

Nmap can identify hosts, open ports, and service information. Results depend on network conditions, firewalls, privileges, and scan options. A scan result is not proof that a service is vulnerable.

## Preconditions
- Confirm the isolated network.
- Confirm the exact Ubuntu and Windows lab IP addresses.
- Obtain authorization for both targets (your own VMs).
- Record the start time and test operator.
- Keep the scan limited to one named target at a time.

## Safe first exercise
From Kali, run a basic connectivity check against the Ubuntu lab address. Then perform a limited TCP service scan against that one address only.

Example command pattern:
```bash
nmap -sT --top-ports 20 <UBUNTU_LAB_IP>
```

Replace the placeholder with the actual Ubuntu lab IP. Do not run this against an internet address or an unknown subnet.

## Analysis
- Which ports are open?
- Does each open port correspond to an intended service?
- Does the service match the asset inventory?
- Is the service reachable only inside the lab?
- Did Ubuntu logs or network telemetry record the activity?
- Did Wazuh create an alert? If not, is that expected based on installed rules and data sources?

## Evidence
Save the command, target, timestamp, output, Ubuntu-side evidence, and Wazuh result. Redact private details before publishing.
