#!/usr/bin/env python3
"""
Cleaner & Formatter for Overnight Free Fleet Raw Outputs.
Strips CLI headers/reasoning boxes and formats clean files into reports/
"""

import re
from pathlib import Path

RUN_DIR = Path("/home/kitti/Projects/Activities-me/ai-training-school/runs/2026-08-20-overnight-fleet")
STAGING_DIR = RUN_DIR / "staging"
REPORTS_DIR = RUN_DIR / "reports"

def clean_output(text: str) -> str:
    # Strip CLI header warnings & reasoning box
    text = re.sub(r"^(?:Warning:.*?|.*?tirith security.*?)\n+", "", text, flags=re.DOTALL)
    # Strip ┌─ Reasoning ─── ... └────── or reasoning text if present
    text = re.sub(r"┌─ Reasoning ─+.*?└─+.*?\n", "", text, flags=re.DOTALL)
    # Strip leading tool lines / git diff headers if model printed patch style
    text = re.sub(r"^.*?@@ -\d+,\d+ \+\d+,\d+ @@\n", "", text, flags=re.DOTALL)
    # Remove leading '+' from lines if model hallucinated a diff format
    lines = []
    for line in text.splitlines():
        if line.startswith("+") and not line.startswith("+++"):
            lines.append(line[1:])
        else:
            lines.append(line)
    return "\n".join(lines).strip()

def process():
    for raw_file in STAGING_DIR.glob("*.raw.md"):
        content = raw_file.read_text(encoding="utf-8")
        clean = clean_output(content)
        clean_file = REPORTS_DIR / raw_file.name.replace(".raw.md", ".clean.md")
        clean_file.write_text(clean, encoding="utf-8")
        print(f"✅ Cleaned {raw_file.name} -> {clean_file.name} ({len(clean):,} chars)")

if __name__ == "__main__":
    process()
