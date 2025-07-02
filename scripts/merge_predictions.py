# ────────────────────────────────────────────────────────────────
# scripts/merge_predictions.py
# ────────────────────────────────────────────────────────────────
#!/usr/bin/env python3
"""
Merge NEW predictions into master JSONL.
Old patch keeps unless NEW supplies the same instance_id.
"""
import json, sys, pathlib

new_path  = pathlib.Path(sys.argv[1])
master_path = pathlib.Path(sys.argv[2])

def load(path: pathlib.Path):
    if not path.exists():
        return {}
    return {json.loads(l)["instance_id"]: json.loads(l)
            for l in path.read_text().splitlines()}

merged = load(master_path)
merged.update(load(new_path))        # NEW wins on duplicates

master_path.write_text("\n".join(json.dumps(v) for v in merged.values()))
print(f"merged {len(merged)} predictions into {master_path}")
