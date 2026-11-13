#!/usr/bin/env python3
"""Normalize and sort a simple CSV event timeline by ISO-8601 timestamp."""
from __future__ import annotations

import argparse
import csv
import sys
from pathlib import Path

REQUIRED_FIELDS = ("timestamp", "source", "event", "details")


def build_timeline(input_path: Path) -> tuple[list[dict[str, str]], list[str]]:
    rows: list[dict[str, str]] = []
    errors: list[str] = []
    with input_path.open("r", encoding="utf-8-sig", newline="") as handle:
        reader = csv.DictReader(handle)
        if reader.fieldnames is None:
            return [], ["CSV file is empty or has no header"]
        missing = [field for field in REQUIRED_FIELDS if field not in reader.fieldnames]
        if missing:
            return [], [f"Missing required CSV columns: {', '.join(missing)}"]

        for line_number, row in enumerate(reader, start=2):
            timestamp = (row.get("timestamp") or "").strip()
            if not timestamp:
                errors.append(f"line {line_number}: timestamp is empty; row skipped")
                continue
            # Lexical ordering is reliable only when timestamps use one normalized
            # ISO-8601 format and timezone (prefer UTC with Z).
            rows.append({
                "timestamp": timestamp,
                "source": (row.get("source") or "").strip(),
                "event": (row.get("event") or "").strip(),
                "details": (row.get("details") or "").strip(),
                "evidence_id": (row.get("evidence_id") or "").strip(),
            })

    rows.sort(key=lambda item: item["timestamp"])
    return rows, errors


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("input", type=Path, help="CSV containing timeline events")
    parser.add_argument("--output", type=Path, help="Output sorted timeline CSV")
    args = parser.parse_args()

    if not args.input.is_file():
        print(f"Input file not found: {args.input}", file=sys.stderr)
        return 2

    try:
        rows, errors = build_timeline(args.input)
    except OSError as exc:
        print(f"Could not read input: {exc}", file=sys.stderr)
        return 2

    fields = ["timestamp", "source", "event", "details", "evidence_id"]
    if args.output:
        try:
            args.output.parent.mkdir(parents=True, exist_ok=True)
            with args.output.open("w", encoding="utf-8", newline="") as handle:
                writer = csv.DictWriter(handle, fieldnames=fields)
                writer.writeheader()
                writer.writerows(rows)
        except OSError as exc:
            print(f"Could not write output: {exc}", file=sys.stderr)
            return 2
        print(f"Timeline written: {args.output}")
    else:
        writer = csv.DictWriter(sys.stdout, fieldnames=fields)
        writer.writeheader()
        writer.writerows(rows)

    for error in errors:
        print(f"Warning: {error}", file=sys.stderr)
    print(f"Events included: {len(rows)}", file=sys.stderr)
    return 1 if errors else 0


if __name__ == "__main__":
    raise SystemExit(main())
