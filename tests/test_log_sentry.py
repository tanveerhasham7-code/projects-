import unittest

from log_sentry import analyze_lines, render_report


class LogSentryTests(unittest.TestCase):
    def test_counts_failed_and_successful_events(self):
        lines = [
            "Oct 26 host sshd[1]: Failed password for admin from 203.0.113.10 port 1234 ssh2",
            "Oct 26 host sshd[2]: Accepted publickey for student from 192.0.2.1 port 2222 ssh2",
        ]
        report = analyze_lines(lines)
        self.assertEqual(report.failed, 1)
        self.assertEqual(report.successful, 1)
        self.assertEqual(report.unrecognized, 0)

    def test_groups_failures_by_ip_and_user(self):
        lines = [
            "Failed password for admin from 203.0.113.10 port 1001 ssh2",
            "Failed password for admin from 203.0.113.10 port 1002 ssh2",
            "Failed password for root from 203.0.113.10 port 1003 ssh2",
        ]
        report = analyze_lines(lines)
        self.assertEqual(report.failed_by_ip["203.0.113.10"], 3)
        self.assertEqual(report.failed_by_user["admin"], 2)

    def test_unrecognized_lines_are_counted(self):
        report = analyze_lines(["some unrelated service message"])
        self.assertEqual(report.unrecognized, 1)

    def test_report_flags_threshold(self):
        lines = [
            "Failed password for admin from 203.0.113.10 port 1001 ssh2",
            "Failed password for admin from 203.0.113.10 port 1002 ssh2",
        ]
        report = analyze_lines(lines)
        output = render_report(report, threshold=2)
        self.assertIn("203.0.113.10: 2 failures", output)

    def test_invalid_threshold_is_rejected(self):
        report = analyze_lines([])
        with self.assertRaises(ValueError):
            render_report(report, threshold=0)


if __name__ == "__main__":
    unittest.main()
