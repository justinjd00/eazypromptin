#!/usr/bin/env python3
"""Build distributable artefacts for eazypromptin from skills/eazypromptin.

Outputs (in dist/):
  eazypromptin.zip               claude.ai / Claude desktop upload (Settings > Capabilities > Skills)
  eazypromptin.skill             same archive, opens with "Save skill" in Claude apps
  eazypromptin-full.md           one-file system prompt for any model with a large context (API, Claude Projects, LM Studio...)
  chat/instructions.md           short core instructions (< 8000 chars) for ChatGPT Custom GPTs, Gemini Gems, Mistral agents...
  chat/eazypromptin-knowledge.md all reference files in one document, to upload as the knowledge file next to instructions.md

Run:  python3 scripts/build.py          (build)
      python3 scripts/build.py --check  (fail if dist/ is out of date; used in CI)
"""
from __future__ import annotations

import io
import re
import sys
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SKILL = ROOT / "skills" / "eazypromptin"
DIST = ROOT / "dist"
CHAT_INSTRUCTIONS_SRC = ROOT / "scripts" / "chat-instructions.md"
CHAT_LIMIT = 8000  # ChatGPT Custom GPT instruction limit
FIXED_TIME = (2026, 1, 1, 0, 0, 0)  # deterministic archives


def skill_files() -> list[Path]:
    return sorted(p for p in SKILL.rglob("*") if p.is_file() and not p.name.startswith("."))


def strip_frontmatter(text: str) -> str:
    return re.sub(r"\A---\n.*?\n---\n", "", text, count=1, flags=re.S).lstrip()


def build_zip() -> bytes:
    buf = io.BytesIO()
    with zipfile.ZipFile(buf, "w", zipfile.ZIP_DEFLATED) as zf:
        for p in skill_files():
            info = zipfile.ZipInfo(f"eazypromptin/{p.relative_to(SKILL).as_posix()}", FIXED_TIME)
            info.compress_type = zipfile.ZIP_DEFLATED
            info.external_attr = 0o644 << 16
            zf.writestr(info, p.read_bytes())
    return buf.getvalue()


def reference_docs() -> list[Path]:
    refs = SKILL / "references"
    top = sorted(p for p in refs.glob("*.md"))
    domains = sorted(p for p in (refs / "domains").glob("*.md") if not p.name.startswith("_"))
    return top + domains


def build_knowledge() -> str:
    parts = [
        "# EazyPromptin: reference library\n",
        "This document bundles every reference file of the eazypromptin skill. "
        "When the instructions say to read `references/<file>`, find the section headed "
        "`FILE: references/<file>` below.\n",
    ]
    for p in reference_docs():
        rel = p.relative_to(SKILL).as_posix()
        parts.append(f"\n\n---\n\n## FILE: {rel}\n\n{p.read_text(encoding='utf-8').strip()}\n")
    return "".join(parts)


def build_full() -> str:
    core = strip_frontmatter((SKILL / "SKILL.md").read_text(encoding="utf-8"))
    preface = (
        "<!-- Generated from skills/eazypromptin by scripts/build.py. Use as a system prompt. -->\n"
        "All files this prompt refers to as `references/...` are included at the end of this prompt "
        "under headings `FILE: references/...`. You have no file system unless your environment provides one; "
        "if it does not, deliver briefs and prompts in your replies instead of writing files.\n\n"
    )
    return preface + core.strip() + "\n\n" + build_knowledge()


def outputs() -> dict[Path, bytes]:
    z = build_zip()
    chat = CHAT_INSTRUCTIONS_SRC.read_text(encoding="utf-8")
    if len(chat) > CHAT_LIMIT:
        sys.exit(f"scripts/chat-instructions.md is {len(chat)} chars; limit is {CHAT_LIMIT}")
    return {
        DIST / "eazypromptin.zip": z,
        DIST / "eazypromptin.skill": z,
        DIST / "eazypromptin-full.md": build_full().encode(),
        DIST / "chat" / "instructions.md": chat.encode(),
        DIST / "chat" / "eazypromptin-knowledge.md": build_knowledge().encode(),
    }


def zip_members(data: bytes) -> dict[str, bytes]:
    with zipfile.ZipFile(io.BytesIO(data)) as zf:
        return {n: zf.read(n) for n in zf.namelist()}


def same_content(path: Path, data: bytes) -> bool:
    """Compare archives by their members: deflate output differs between zlib versions."""
    current = path.read_bytes()
    if path.suffix in {".zip", ".skill"}:
        try:
            return zip_members(current) == zip_members(data)
        except zipfile.BadZipFile:
            return False
    return current == data


def main() -> None:
    check = "--check" in sys.argv
    stale = []
    for path, data in outputs().items():
        if check:
            if not path.exists() or not same_content(path, data):
                stale.append(path.relative_to(ROOT).as_posix())
        else:
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_bytes(data)
            print(f"wrote {path.relative_to(ROOT)} ({len(data):,} bytes)")
    if check:
        if stale:
            sys.exit("dist/ is out of date, run python3 scripts/build.py:\n  " + "\n  ".join(stale))
        print("dist/ is up to date")


if __name__ == "__main__":
    main()
