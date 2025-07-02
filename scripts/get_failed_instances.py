# ────────────────────────────────────────────────────────────────
# scripts/get_failed_instances.py
# ────────────────────────────────────────────────────────────────
#!/usr/bin/env python3
"""
Extract still-failing instance IDs.
Usage:
    python get_failed_instances.py instance_results.jsonl output.txt
Exit 0 even if input missing (first run).
"""
import json, sys, pathlib
src = pathlib.Path(sys.argv[1])
dst = pathlib.Path(sys.argv[2])
if not src.exists():
    print("no previous results -> full run")
    sys.exit(0)
fail = [
    json.loads(l)["instance_id"]
    for l in src.read_text().splitlines()
    if not json.loads(l).get("passed", False)
]
dst.write_text("\n".join(fail))
print(f"{len(fail)} failing instances saved to {dst}")
