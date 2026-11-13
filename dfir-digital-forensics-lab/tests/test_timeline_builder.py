import sys
import tempfile
import unittest
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(PROJECT_ROOT / "scripts"))

from timeline_builder import build_timeline  # noqa: E402


class TimelineBuilderTests(unittest.TestCase):
    def test_sorts_iso_timestamps(self):
        with tempfile.TemporaryDirectory() as temp:
            path = Path(temp) / "events.csv"
            path.write_text(
                "timestamp,source,event,details,evidence_id\n"
                "2026-11-10T09:10:00Z,host,second,detail,E2\n"
                "2026-11-10T09:00:00Z,host,first,detail,E1\n",
                encoding="utf-8",
            )
            rows, errors = build_timeline(path)
            self.assertEqual(errors, [])
            self.assertEqual([row["evidence_id"] for row in rows], ["E1", "E2"])

    def test_reports_missing_timestamp(self):
        with tempfile.TemporaryDirectory() as temp:
            path = Path(temp) / "events.csv"
            path.write_text(
                "timestamp,source,event,details\n,host,event,detail\n",
                encoding="utf-8",
            )
            rows, errors = build_timeline(path)
            self.assertEqual(rows, [])
            self.assertEqual(len(errors), 1)

    def test_requires_schema(self):
        with tempfile.TemporaryDirectory() as temp:
            path = Path(temp) / "events.csv"
            path.write_text("time,source\nnow,host\n", encoding="utf-8")
            rows, errors = build_timeline(path)
            self.assertEqual(rows, [])
            self.assertTrue(errors)


if __name__ == "__main__":
    unittest.main()
