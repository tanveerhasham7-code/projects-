import unittest
from app.engine import normalize_alert, deterministic_triage, apply_policy, event_fingerprint

class EngineTests(unittest.TestCase):
    def test_critical_rule_stays_critical_even_if_ai_says_low(self):
        event = normalize_alert({"rule": {"id": "999", "level": 14, "description": "critical test"}})
        decision = apply_policy(deterministic_triage(event), {"severity": "low", "confidence": 1.0}, 70)
        self.assertEqual(decision["severity"], "critical")
        self.assertTrue(decision["notify_analyst"])

    def test_high_risk_triggers_notification(self):
        event = normalize_alert({"rule": {"id": "5710", "level": 12, "description": "authentication_failed"}})
        self.assertTrue(apply_policy(deterministic_triage(event), None, 70)["notify_analyst"])

    def test_low_severity_does_not_trigger_notification(self):
        event = normalize_alert({"rule": {"id": "1", "level": 2, "description": "service started"}})
        self.assertFalse(apply_policy(deterministic_triage(event), None, 70)["notify_analyst"])

    def test_ai_can_raise_but_not_lower_score(self):
        event = normalize_alert({"rule": {"id": "2", "level": 3, "description": "unusual activity"}})
        det = deterministic_triage(event)
        decision = apply_policy(det, {"severity": "high", "confidence": 0.95}, 70)
        self.assertGreaterEqual(decision["risk_score"], det["risk_score"])
        self.assertTrue(decision["notify_analyst"])

    def test_high_severity_cannot_be_downgraded_by_ai(self):
        event = normalize_alert({"rule": {"id": "10", "level": 10, "description": "high priority"}})
        det = deterministic_triage(event)
        decision = apply_policy(det, {"severity": "low", "confidence": 1.0}, 70)
        self.assertEqual(decision["severity"], "high")
        self.assertTrue(decision["notify_analyst"])

    def test_medium_severity_floor_is_preserved(self):
        event = normalize_alert({"rule": {"id": "7", "level": 7, "description": "medium priority"}})
        decision = apply_policy(deterministic_triage(event), None, 70)
        self.assertEqual(decision["severity"], "medium")

    def test_fingerprint_is_stable(self):
        event = normalize_alert({"id": "abc", "rule": {"id": "10", "level": 8}})
        self.assertEqual(event_fingerprint(event), event_fingerprint(event))

if __name__ == "__main__":
    unittest.main()
