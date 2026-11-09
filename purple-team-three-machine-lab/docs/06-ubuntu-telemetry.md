# 06 — Ubuntu Server Telemetry: SSH and Web Logs

## Authentication telemetry
Ubuntu releases and configurations may record authentication events in the system journal, /var/log/auth.log, or another configured destination. Verify which source your VM actually uses.

Look for:
- SSH authentication failures.
- Successful SSH authentication.
- Invalid username attempts.
- Session opened or closed messages.
- Sudo activity, where configured and relevant.

## Web access telemetry
If you choose to install a simple web server such as Nginx or Apache, access logs can record:
- Client address.
- Request time.
- HTTP method and path.
- Response status.
- User-agent string.

A 404 response is not automatically an attack. A single unusual request is not proof of compromise.

## Practical verification
1. Identify the active authentication log source.
2. Open a normal local session or use your own test account.
3. Locate the corresponding authentication event.
4. If a web server is installed, make a harmless GET request from Kali to the Ubuntu lab address.
5. Locate the request in the server access log.
6. Check whether Wazuh receives the relevant log entries.
7. Record the exact source, timestamp, and fields.

Do not publish real usernames, secrets, or unnecessary personal data.
