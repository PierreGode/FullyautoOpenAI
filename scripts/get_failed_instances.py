#!/usr/bin/env python3
"""
Extract still-failing instance IDs from instance_results.jsonl.
Writes one ID per line to output file.
Exit 0 when input JSONL missing → treated as first run.
"""
import json, sys, pathlib

src = pathlib.Path(sys.argv[1])
dst = pathlib.Path(sys.argv[2])

if not src.exists():
    print("no previous results – full run next")
    sys.exit(0)

fails = [
    json.loads(line)["instance_id"]
    for line in src.read_text().splitlines()
    if not json.loads(line).get("passed", False)
]

dst.write_text("\n".join(fails))
print(f"{len(fails)} failing instances listed in {dst}")
