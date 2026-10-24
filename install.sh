#!/bin/bash
# Install FABLE skills to Claude Code's personal skills directory.
set -euo pipefail
SCRIPT_DIR="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd)"
SKILLS_DIR="${CLAUDE_CONFIG_DIR:-$HOME/.claude}/skills"

SKILLS=(
  "fable-core"
  "fable-code-review"
  "fable-debugging"
  "fable-autonomous"
  "fable-autonomous-continuation"
  "fable-web-design"
  "fable-multi-agent"
  "fable-plan-mode"
  "fable-effort-calibrator"
  "fable-grounded-progress"
  "fable-act-when-ready"
  "fable-scope-guard"
  "fable-no-gold-plating"
  "fable-regrounding-summary"
  "fable-adversarial-review"
  "fable-markdown-memory"
  "fable-subagent-orchestration"
  "fable-skill-refactorer"
)

# Check the whole distribution before changing an existing installation.
for skill in "${SKILLS[@]}"; do
  if [[ ! -f "$SCRIPT_DIR/skills/$skill/SKILL.md" ]]; then
    echo "Missing skill: $skill/SKILL.md. Use a complete repository checkout." >&2
    exit 1
  fi
done

echo "Installing FABLE 5 Skills to $SKILLS_DIR..."
echo ""

mkdir -p "$SKILLS_DIR"
for skill in "${SKILLS[@]}"; do
  mkdir -p "$SKILLS_DIR/$skill"
  cp -R "$SCRIPT_DIR/skills/$skill/." "$SKILLS_DIR/$skill/"
  echo "  + $skill"
done

echo ""
echo "Done. Open Claude Code and type /fable-core to verify."
