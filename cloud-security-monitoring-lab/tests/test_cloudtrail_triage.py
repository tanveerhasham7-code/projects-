import sys
import unittest
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(PROJECT_ROOT / "scripts"))

from cloudtrail_triage import analyze_events, event_findings, load_jsonl  # noqa: E402


class CloudTrailTriageTests(unittest.TestCase):
    def test_failed_console_login_is_flagged(self):
        event = {
            "eventName": "ConsoleLogin",
            "responseElements": {"ConsoleLogin": "Failure"},
            "userIdentity": {"type": "IAMUser", "userName": "demo"},
        }
        findings = event_findings(event)
        self.assertIn("CLOUD-AUTH-001", [item["rule_id"] for item in findings])

    def test_iam_access_key_creation_is_flagged(self):
        findings = event_findings({"eventName": "CreateAccessKey"})
        self.assertIn("CLOUD-IAM-003", [item["rule_id"] for item in findings])

    def test_public_ingress_is_flagged(self):
        event = {
            "eventName": "AuthorizeSecurityGroupIngress",
            "requestParameters": {
                "ipPermissions": {"ipRanges": [{"cidrIp": "0.0.0.0/0"}]}
            },
        }
        findings = event_findings(event)
        self.assertIn("CLOUD-NET-001", [item["rule_id"] for item in findings])

    def test_private_ingress_is_not_flagged_by_public_rule(self):
        event = {
            "eventName": "AuthorizeSecurityGroupIngress",
            "requestParameters": {
                "ipPermissions": {"ipRanges": [{"cidrIp": "10.0.0.0/8"}]}
            },
        }
        findings = event_findings(event)
        self.assertNotIn("CLOUD-NET-001", [item["rule_id"] for item in findings])

    def test_sample_file_has_events_and_findings(self):
        events, errors = load_jsonl(PROJECT_ROOT / "sample_data" / "cloudtrail-events.jsonl")
        report = analyze_events(events)
        self.assertEqual(errors, [])
        self.assertEqual(report["events_analyzed"], 5)
        self.assertGreaterEqual(report["findings_count"], 4)


if __name__ == "__main__":
    unittest.main()
