# ────────────────────────────────────────────────────────────────
# scripts/merge_predictions.py
# ────────────────────────────────────────────────────────────────
#!/usr/bin/env python3
"""
Merge NEW predictions into master predictions.jsonl.
Keeps old patch unless NEW has same instance_id.
"""
import json, sys, pathlib
new_p = pathlib.Path(sys.argv[1]); master_p = pathlib.Path(sys.argv[2])
def read(path):
    return {json.loads(l)["instance_id"]: json.loads(l)
            for l in path.read_text().splitlines()} if path.exists() else {}
combined = read(master_p); combined.update(read(new_p))
master_p.write_text("\n".join(json.dumps(v) for v in combined.values()))
print(f"merged {len(combined)} predictions into {master_p}")

