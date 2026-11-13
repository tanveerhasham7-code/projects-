#!/usr/bin/env python3
"""Create a SHA-256 inventory of files under a directory without modifying them."""
from __future__ import annotations

import argparse
import hashlib
import json
import os
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


def sha256_file(path: Path, chunk_size: int = 1024 * 1024) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        while True:
            chunk = handle.read(chunk_size)
            if not chunk:
                break
            digest.update(chunk)
    return digest.hexdigest()


def build_manifest(root: Path, output: Path | None = None) -> dict[str, Any]:
    root = root.resolve()
    if not root.is_dir():
        raise NotADirectoryError(f"Evidence path is not a directory: {root}")

    entries: list[dict[str, Any]] = []
    errors: list[dict[str, str]] = []

    for current, dirs, filenames in os.walk(root, followlinks=False):
        dirs[:] = sorted(
            name for name in dirs
            if not (Path(current) / name).is_symlink()
        )
        for filename in sorted(filenames):
            path = Path(current) / filename
            if path.is_symlink():
                errors.append({"path": str(path.relative_to(root)), "error": "symbolic link skipped"})
                continue
            if output is not None and path.resolve() == output.resolve():
                continue
            try:
                stat = path.stat()
                entries.append({
                    "relative_path": str(path.relative_to(root)),
                    "size_bytes": stat.st_size,
                    "modified_time_utc": datetime.fromtimestamp(
                        stat.st_mtime, tz=timezone.utc
                    ).isoformat(),
                    "sha256": sha256_file(path),
                })
            except OSError as exc:
                errors.append({"path": str(path.relative_to(root)), "error": str(exc)})

    return {
        "manifest_format": "dfir-evidence-manifest-v1",
        "generated_at_utc": datetime.now(timezone.utc).isoformat(),
        "root_directory": str(root),
        "hash_algorithm": "SHA-256",
        "files_hashed": len(entries),
        "errors_count": len(errors),
        "files": entries,
        "errors": errors,
        "limitations": [
            "This is a file inventory, not a forensic acquisition.",
            "Filesystem metadata can change and does not establish file authenticity.",
            "The tool does not preserve volatile system state or prove chain of custody.",
            "The generated manifest must itself be stored and protected separately.",
        ],
    }


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Create a read-only SHA-256 inventory for a directory."
    )
    parser.add_argument("directory", type=Path, help="Directory containing evidence copies")
    parser.add_argument("--output", type=Path, help="Write JSON manifest to this separate path")
    args = parser.parse_args()

    try:
        manifest = build_manifest(args.directory, args.output)
    except (OSError, NotADirectoryError) as exc:
        print(f"Error: {exc}", file=sys.stderr)
        return 2

    rendered = json.dumps(manifest, indent=2) + "\n"
    if args.output:
        try:
            args.output.parent.mkdir(parents=True, exist_ok=True)
            args.output.write_text(rendered, encoding="utf-8")
        except OSError as exc:
            print(f"Error writing manifest: {exc}", file=sys.stderr)
            return 2
        print(f"Manifest written: {args.output}")
    else:
        print(rendered, end="")

    print(
        f"Files hashed: {manifest['files_hashed']} | "
        f"Errors: {manifest['errors_count']}",
        file=sys.stderr,
    )
    return 1 if manifest["errors_count"] else 0


if __name__ == "__main__":
    raise SystemExit(main())
