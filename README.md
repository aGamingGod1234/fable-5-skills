# FABLE 5 Skills for Claude Code

**FABLE** (Framework for Agentic Behavioral Language Excellence) — the most complete collection of Claude Fable 5's behavioral patterns, distilled into installable Claude Code skills.

Built from Claude Fable 5's leaked system prompts (3,800+ lines verbatim), 72 Claude Code session traces, 953 chain-of-thought traces, and measured behavioral data across 382 sessions. 

The verbatim files in `raw/` are incomplete excerpts with continuation
placeholders. For complete local instructions, use the distilled `raw/FABLE.md`
or the installable skills below.

## Install

Requires Bash and the standard `cp` and `mkdir` commands (Linux, macOS, or WSL).
Claude Code must be installed separately.

```bash
git clone https://github.com/SoulSniper-V2/fable-5-skills.git
cd fable-5-skills
bash install.sh
```

The installer creates `~/.claude/skills/` when needed and copies all 18 skills,
including their supporting files. If you use a custom Claude Code configuration
directory, run it with the same `CLAUDE_CONFIG_DIR`:

```bash
CLAUDE_CONFIG_DIR="/path/to/claude-config" bash install.sh
```

Re-running updates files supplied by this repository. Back up any edits to those
files first; unrelated skills and extra files are kept. If a required `SKILL.md`
is missing, the installer stops before writing any skills.

Open Claude Code and type `/fable-core` or `/fable-plan-mode` to verify discovery.
See the [Claude Code skills documentation](https://code.claude.com/docs/en/skills)
for invocation and supported skill locations.

Or copy individual skills from inside the cloned repository:
```bash
mkdir -p "${CLAUDE_CONFIG_DIR:-$HOME/.claude}/skills"
cp -R skills/fable-core "${CLAUDE_CONFIG_DIR:-$HOME/.claude}/skills/"
cp -R skills/fable-web-design "${CLAUDE_CONFIG_DIR:-$HOME/.claude}/skills/"
```

Or tell Claude Code: "Install skills from https://github.com/SoulSniper-V2/fable-5-skills into my ~/.claude/skills/"

## Skills (18 total)

| Skill | What it does |
|-------|-------------|
| `fable-core` | Three Laws, communication style, engineering principles, action safety |
| `fable-act-when-ready` | Decision thresholds: sufficiency over completeness |
| `fable-no-gold-plating` | No unrequested refactors, no speculative abstractions |
| `fable-scope-guard` | Read-request-type-first: diagnose vs change |
| `fable-effort-calibrator` | Match effort level to task class |
| `fable-autonomous` | Autonomous mode: priority order, what to act on/not do |
| `fable-autonomous-continuation` | Long-run discipline, turn-ending check, checkpoint placement |
| `fable-debugging` | Reproduce → isolate → understand → fix minimal → verify |
| `fable-code-review` | PR review: correctness, altitude, efficiency, security |
| `fable-adversarial-review` | Post-completion self-critique: falsify the work |
| `fable-grounded-progress` | Evidence rule: every claim points to a tool result |
| `fable-plan-mode` | 4-phase planning process, quality checklist |
| `fable-regrounding-summary` | Final reports that stand alone |
| `fable-multi-agent` | When to spawn subagents, writing effective prompts |
| `fable-subagent-orchestration` | Fresh-context verifiers, handoff template |
| `fable-markdown-memory` | File-based lesson memory across sessions |
| `fable-skill-refactorer` | Audit existing skills: guardrails vs compensation |
| `fable-web-design` | Condensed design reference + 15 procedural guides, including scroll-driven video |

## Principles

1. Skills encode behavior, not knowledge — when and how to apply what the model already knows
2. Progressive disclosure: load what's needed, when it's needed (~100 tokens at startup per skill)
3. Every rule must have a reason — understand it and you apply it in unenumerated situations
4. Measured improvements > claimed improvements — playbook backs every claim with session data
5. Best of all open-source Fable skill repos merged into one — nothing held back

## Source Data

| Source | Location |
|--------|----------|
| 63 JSONL session traces | [armand0e/claude-fable-5-claude-code](https://huggingface.co/datasets/armand0e/claude-fable-5-claude-code) |
| 4,665 CoT traces | [Glint-Research/Fable-5-traces](https://huggingface.co/datasets/Glint-Research/Fable-5-traces) |
| Boeing 747 trace (31MB) | [victor/fable-5-boeing-747-trace](https://huggingface.co/datasets/victor/fable-5-boeing-747-trace) |
| Leaked system prompts | [asgeirtj/system_prompts_leaks](https://github.com/asgeirtj/system_prompts_leaks) |
| CL4R1T4S archive | [Ss1024sS/CL4R1T4S](https://github.com/Ss1024sS/CL4R1T4S) |

## License

MIT
