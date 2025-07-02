# ────────────────────────────────────────────────────────────────
# scripts/build_agents_prompt.py
# ────────────────────────────────────────────────────────────────
#!/usr/bin/env python3
"""
Create a natural-language prompt telling Codex to improve AGENTS.md
based on failing instances.
Usage:
    python build_agents_prompt.py instance_results.jsonl output_prompt.txt
"""
import json, sys, pathlib, textwrap
src = pathlib.Path(sys.argv[1]); out = pathlib.Path(sys.argv[2])
failed = []
if src.exists():
    for l in src.read_text().splitlines():
        rec = json.loads(l)
        if not rec.get("passed", False):
            failed.append(rec["instance_id"])
prompt = textwrap.dedent(f"""
    You are a coding agent editing this repository. Open the file AGENTS.md
    and improve its guidelines so that GPT-4.1-mini can fix the remaining
    SWE-bench Lite failures listed below.

    Remaining failing instances (total {len(failed)}):
    {', '.join(failed[:50])}
    {'...' if len(failed) > 50 else ''}

    • For each common error pattern you can infer, add a concrete strategy.
    • Add at least one worked example diff if appropriate.
    • Do NOT remove existing good advice; append or refine instead.
    • Save and exit the file when done.
""").strip()
out.write_text(prompt + "\n")
print(f"prompt written to {out}")
