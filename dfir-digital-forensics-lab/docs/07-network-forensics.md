# 07 — Network Forensics

## 1. Network evidence sources

- PCAP/PCAPNG packet captures.
- DNS resolver logs.
- Firewall allow/deny records.
- Proxy and secure web gateway logs.
- VPN authentication and session logs.
- NetFlow/IPFIX or other flow records.
- IDS/IPS alerts.
- Cloud network flow logs.

Each source has different visibility, retention, clock precision, and blind spots.

## 2. Packet capture concepts

Understand Ethernet, ARP, IP, TCP, UDP, DNS, HTTP, TLS, and common application protocols. A packet capture may reveal endpoints, timing, protocol behavior, and sometimes payload data. Encryption limits payload visibility but does not remove all metadata.

## 3. Wireshark workflow

1. Verify the capture source and scope.
2. Record file hash and capture time range.
3. Identify protocols and top talkers.
4. Inspect DNS queries and responses.
5. Review TCP conversations, resets, retransmissions, and unusual connection patterns.
6. Correlate IPs and timestamps with endpoint and firewall logs.
7. Save display filters, packet numbers, and relevant excerpts.
8. Explain capture limitations, including missing traffic and clock differences.

Example display filters:

```text
dns
tcp.flags.syn == 1 && tcp.flags.ack == 0
http.request
tls.handshake.type == 1
ip.addr == 192.0.2.10
```

These are analysis filters, not proof of malicious activity.

## 4. Practical exercise

Use a PCAP you created in your own lab or a reputable training capture whose terms permit analysis. Do not capture other people's traffic or collect credentials.

- Calculate the PCAP SHA-256 hash.
- Identify capture duration and protocol distribution.
- Find three DNS queries and explain their context.
- Select one TCP conversation and describe its sequence.
- Correlate one endpoint address with a synthetic host event.
- Write a brief finding with packet references and limitations.
