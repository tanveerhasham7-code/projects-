#!/usr/bin/env python3
"""Wazuh custom integration adapter: stdin alert JSON -> Sentinel webhook."""
import json
import os
import sys
import urllib.request
import urllib.error

def main():
    endpoint = os.environ.get("AI_SOC_WEBHOOK_URL", "http://127.0.0.1:8080/webhook/wazuh")
    token = os.environ.get("AI_SOC_WEBHOOK_TOKEN", "")
    if not token:
        raise SystemExit("AI_SOC_WEBHOOK_TOKEN is not configured")
    alert = json.loads(sys.stdin.read())
    request = urllib.request.Request(
        endpoint,
        data=json.dumps(alert).encode("utf-8"),
        headers={"Content-Type": "application/json", "X-Webhook-Token": token},
        method="POST",
    )
    try:
        with urllib.request.urlopen(request, timeout=10) as response:
            if response.status >= 300:
                raise SystemExit(f"Sentinel returned HTTP {response.status}")
    except (urllib.error.URLError, TimeoutError) as exc:
        raise SystemExit(f"Could not deliver alert to Sentinel: {exc}")

if __name__ == "__main__":
    main()
