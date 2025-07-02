# ────────────────────────────────────────────────────────────────
# scripts/build_agents_prompt.py
# ────────────────────────────────────────────────────────────────
#!/usr/bin/env python3
"""
Generate a prompt telling Codex to refine AGENTS.md
based on remaining failures.
"""
import json, sys, pathlib, textwrap

src = pathlib.Path(sys.argv[1])
out = pathlib.Path(sys.argv[2])

fails = []
if src.exists():
    for line in src.read_text().splitlines():
        rec = json.loads(line)
        if not rec.get("passed", False):
            fails.append(rec["instance_id"])

prompt = textwrap.dedent(f"""
    You are an automated coding agent working in this repository.
    Open AGENTS.md and improve its guidelines so that GPT-4.1-mini
    can fix the remaining SWE-bench-Lite failures below.

    Remaining failing instances (count {len(fails)}):
    {', '.join(fails[:50])}{' ...' if len(fails) > 50 else ''}

    • Add concrete strategies or patterns that address these failures.
    • Keep existing good advice; append or refine instead of deleting.
    • Include short example diffs if helpful.
    • Save and exit the file when finished.
""").strip()

out.write_text(prompt + "\n")
print(f"prompt written to {out}")
