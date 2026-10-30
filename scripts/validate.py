#!/usr/bin/env python3
"""Validate skills/*/SKILL.md against the Agent Skills spec (agentskills.io) and check references resolve."""
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
errors = []

for skill_md in sorted((ROOT / "skills").glob("*/SKILL.md")):
    folder = skill_md.parent
    text = skill_md.read_text(encoding="utf-8")
    m = re.match(r"\A---\n(.*?)\n---\n", text, re.S)
    if not m:
        errors.append(f"{skill_md}: missing frontmatter")
        continue
    fm = m.group(1)
    name = re.search(r"^name:\s*(.+)$", fm, re.M)
    desc = re.search(r"^description:\s*(.+)$", fm, re.M)
    if not name or name.group(1).strip() != folder.name:
        errors.append(f"{skill_md}: name must equal folder name '{folder.name}'")
    elif not re.fullmatch(r"[a-z0-9]+(-[a-z0-9]+)*", name.group(1).strip()) or len(name.group(1).strip()) > 64:
        errors.append(f"{skill_md}: invalid name")
    if not desc or not (1 <= len(desc.group(1).strip()) <= 1024):
        errors.append(f"{skill_md}: description missing or longer than 1024 chars ({len(desc.group(1)) if desc else 0})")
    lines = text.count("\n")
    if lines > 500:
        errors.append(f"{skill_md}: {lines} lines, spec recommends < 500")
    for ref in set(re.findall(r"`((?:references/)?domains/[\w-]+\.md|references/[\w/-]+\.md)`", text)):
        path = folder / (ref if ref.startswith("references/") else "references/" + ref)
        if not path.exists():
            errors.append(f"{skill_md}: referenced file missing: {ref}")

if errors:
    print("\n".join(errors))
    sys.exit(1)
print("skills valid")
