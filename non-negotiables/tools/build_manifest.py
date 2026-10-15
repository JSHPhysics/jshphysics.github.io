#!/usr/bin/env python3
"""Validate every topic file in data/ and write data/manifest.json.

Run this after adding or editing a topic file:
    python3 tools/build_manifest.py
"""

import glob
import json
import os
import sys

# Import the validator from the same folder
sys.path.insert(0, os.path.dirname(__file__))
from validate import validate_file  # noqa: E402


def main():
    root = os.path.join(os.path.dirname(__file__), "..")
    data_dir = os.path.join(root, "data")

    paths = sorted(glob.glob(os.path.join(data_dir, "*.json")))
    paths = [path for path in paths if not path.endswith("manifest.json")]

    entries = []
    failed = False

    for path in paths:
        problems = validate_file(path)
        if problems:
            failed = True
            print(f"FAIL {os.path.basename(path)}")
            for problem in problems:
                print(f"  - {problem}")
            continue

        with open(path, encoding="utf-8") as handle:
            topic = json.load(handle)

        entries.append({
            "id": topic["id"],
            "file": os.path.basename(path),
            "title": topic["title"],
            "order": topic["order"],
            "types": len(topic["types"]),
        })

    if failed:
        print("Manifest not written: fix the problems above first.")
        return 1

    # Sort by order so the manifest reads naturally
    entries.sort(key=lambda entry: entry["order"])

    manifest = {"topics": entries}
    manifest_path = os.path.join(data_dir, "manifest.json")
    with open(manifest_path, "w", encoding="utf-8") as handle:
        json.dump(manifest, handle, indent=2, ensure_ascii=False)
        handle.write("\n")

    total_types = sum(entry["types"] for entry in entries)
    print(f"Wrote manifest with {len(entries)} topics, {total_types} types, {total_types * 7} questions.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
