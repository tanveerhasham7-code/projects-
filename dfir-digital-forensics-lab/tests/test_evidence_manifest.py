import hashlib
import sys
import tempfile
import unittest
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(PROJECT_ROOT / "scripts"))

from evidence_manifest import build_manifest  # noqa: E402


class EvidenceManifestTests(unittest.TestCase):
    def test_hash_matches_independent_sha256(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            sample = root / "evidence.txt"
            content = b"synthetic forensic evidence"
            sample.write_bytes(content)

            manifest = build_manifest(root)
            expected = hashlib.sha256(content).hexdigest()

            self.assertEqual(manifest["files_hashed"], 1)
            self.assertEqual(manifest["files"][0]["sha256"], expected)
            self.assertEqual(manifest["errors_count"], 0)

    def test_manifest_excludes_output_file(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            (root / "a.txt").write_text("one", encoding="utf-8")
            output = root / "manifest.json"
            manifest = build_manifest(root, output)
            self.assertEqual(manifest["files_hashed"], 1)

    def test_rejects_non_directory(self):
        with tempfile.TemporaryDirectory() as temp:
            path = Path(temp) / "file.txt"
            path.write_text("x", encoding="utf-8")
            with self.assertRaises(NotADirectoryError):
                build_manifest(path)


if __name__ == "__main__":
    unittest.main()
