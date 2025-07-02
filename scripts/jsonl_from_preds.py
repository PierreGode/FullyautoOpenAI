# ────────────────────────────────────────────────────────────────
# scripts/jsonl_from_preds.py
# ────────────────────────────────────────────────────────────────
#!/usr/bin/env python3
"""
Convert SWE-agent preds.json → JSONL for SWE-bench harness.
Usage:
    python jsonl_from_preds.py input_preds.json output.jsonl
"""
import json, sys, pathlib
inp = pathlib.Path(sys.argv[1])
out = pathlib.Path(sys.argv[2])
preds = json.loads(inp.read_text())
lines = [
    json.dumps({
        "instance_id": k,
        "model":       "gpt-4.1-mini",
        "prediction":  v["model_patch"]
    }) for k, v in preds.items()
]
out.write_text("\n".join(lines))
print(f"✓ wrote {len(lines)} lines to {out}")
