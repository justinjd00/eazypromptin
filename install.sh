#!/usr/bin/env bash
# Install the eazypromptin skill for local coding agents.
#
#   curl -fsSL https://raw.githubusercontent.com/justinjd00/eazypromptin/main/install.sh | bash
#
# By default installs to every agent folder that exists on this machine:
#   ~/.claude/skills   (Claude Code; also read by Cursor, Copilot, opencode)
#   ~/.agents/skills   (Codex, Cursor, Gemini CLI, GitHub Copilot, opencode)
# Options:
#   --claude    only ~/.claude/skills
#   --agents    only ~/.agents/skills
#   --all       both, creating folders that don't exist yet
#   --project   install into ./.claude/skills and ./.agents/skills of the current directory
#   --ref <x>   install from a branch or tag (default: main)
set -euo pipefail

REPO="justinjd00/eazypromptin"
REF="main"
MODE="auto"
SCOPE="user"

while [ $# -gt 0 ]; do
  case "$1" in
    --claude) MODE="claude" ;;
    --agents) MODE="agents" ;;
    --all) MODE="all" ;;
    --project) SCOPE="project" ;;
    --ref) REF="$2"; shift ;;
    -h|--help) sed -n '2,16p' "$0"; exit 0 ;;
    *) echo "unknown option: $1" >&2; exit 1 ;;
  esac
  shift
done

if [ "$SCOPE" = "project" ]; then BASE="$PWD"; CLAUDE_DIR="$BASE/.claude/skills"; AGENTS_DIR="$BASE/.agents/skills";
else BASE="$HOME"; CLAUDE_DIR="$HOME/.claude/skills"; AGENTS_DIR="$HOME/.agents/skills"; fi

TARGETS=()
case "$MODE" in
  claude) TARGETS=("$CLAUDE_DIR") ;;
  agents) TARGETS=("$AGENTS_DIR") ;;
  all) TARGETS=("$CLAUDE_DIR" "$AGENTS_DIR") ;;
  auto)
    [ -d "$(dirname "$CLAUDE_DIR")" ] && TARGETS+=("$CLAUDE_DIR")
    [ -d "$(dirname "$AGENTS_DIR")" ] && TARGETS+=("$AGENTS_DIR")
    [ ${#TARGETS[@]} -eq 0 ] && TARGETS=("$CLAUDE_DIR" "$AGENTS_DIR")
    ;;
esac

TMP="$(mktemp -d)"
trap 'rm -rf "$TMP"' EXIT
echo "Downloading $REPO@$REF ..."
curl -fsSL "https://codeload.github.com/$REPO/tar.gz/$REF" | tar -xz -C "$TMP"
SRC="$(find "$TMP" -maxdepth 3 -type d -path '*/skills/eazypromptin' | head -n1)"
[ -f "$SRC/SKILL.md" ] || { echo "skill not found in download" >&2; exit 1; }

for dir in "${TARGETS[@]}"; do
  mkdir -p "$dir"
  rm -rf "$dir/eazypromptin"
  cp -R "$SRC" "$dir/eazypromptin"
  echo "Installed to $dir/eazypromptin"
done
echo "Done. Start a new session and say: /eazypromptin  (or just ask to build out a prompt)."
