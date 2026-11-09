# 09 — HTTP Request and Access-Log Analysis

## Objective
Send a few harmless HTTP GET requests from Kali to a web service on Ubuntu and trace the requests through server access logs and Wazuh.

## Preconditions
An intentionally installed lab web service must be running on Ubuntu. If no web service exists, document this as a prerequisite; do not assume one is installed.

## Safe procedure
1. Confirm the web service is listening on the Ubuntu lab interface.
2. Record the exact base URL and test time.
3. From Kali, request the home page using curl.
4. Request one clearly nonexistent path to generate a normal 404 response.
5. Stop after these two requests.
6. Inspect the server access log.
7. Search Wazuh for the matching records if the access log is configured for collection.

Example commands (replace the placeholder):
```bash
curl -i http://<UBUNTU_LAB_IP>/
curl -i http://<UBUNTU_LAB_IP>/purple-team-lab-not-found
```

## Analysis
Explain method, path, status code, client address, user-agent, timestamp, and whether the behavior is expected. A 404 is a normal web response and does not by itself indicate malicious activity.

## Result
Not tested. Record actual server and SIEM observations after practice.
