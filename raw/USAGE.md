# USAGE GUIDE — How to Deploy FABLE on Other Models

> This guide explains the deployment strategies, when to use each, and how
> to get the best results from the FABLE behavioral system.

## Deployment Strategies

Paths below are relative to the repository root. The historical quality and
token estimates describe the original source material; they are not validated
measurements of this distribution.

### Strategy 0: Verbatim Leaked Prompt (Maximum Steering Power)
Give the model the actual leaked Fable 5 system prompt verbatim.
The `FABLE-VERBATIM*.md` files here are excerpts with continuation placeholders,
not the full prompts. Use the distilled prompt or installed skills for a
complete local starting point.
**Best for:** Claude Opus 4.8 specifically (proven via head-to-head test)
**Token cost:** ~40,000 tokens
**Expected quality:** 90-95%

### Strategy 1: Distilled Prompt Only (Simplest)
Give the model [raw/FABLE.md](FABLE.md) as its system prompt.
**Best for:** Quick setup, models with strong instruction following
**Token cost:** ~3,000 tokens
**Expected quality:** 70-80%

### Strategy 2: System Prompt + Relevant Modules (Recommended)
Give the model `raw/FABLE.md` plus relevant instructions from
[`skills/`](../skills/). The core supporting guides are in
[`skills/fable-core/references/`](../skills/fable-core/references/).
**Token cost:** ~3,000 + ~1,500 per module
**Expected quality:** 80-90%

### Strategy 3: Full Behavioral Database (Maximum Fidelity)
`raw/FABLE.md` + relevant skills + the curated
[behavioral examples](examples/behavioral-examples.md).
**Token cost:** ~15,000-30,000 tokens
**Expected quality:** 90-95%

### Strategy 4: Web Design Mode
`raw/FABLE.md` + the [web-design skill](../skills/fable-web-design/SKILL.md),
which links its design reference and procedural guides, including
scroll-driven video.

## Deployment Examples

### Claude Code (CLAUDE.md)
Place `raw/FABLE.md` content in your project's `CLAUDE.md` file. Claude Code
automatically reads it as behavioral instructions.

### Cursor / Windsurf
- Cursor: create a project rule in `.cursor/rules/fable.mdc` using the editor's
  rule command, choose its activation mode, and use `raw/FABLE.md` as the body.
  Plain `.md` files in `.cursor/rules/` are ignored. See
  [Cursor rules](https://cursor.com/docs/rules).
- Windsurf/Cascade: create a workspace rule through the editor's Rules panel,
  choose when it activates, and use `raw/FABLE.md` as its content. See
  [Cascade rules](https://docs.windsurf.com/windsurf/cascade/memories) for the
  current editor's locations and activation options.

### API

Install the official `anthropic` Python SDK in your own Python 3.10+ project
environment and set `ANTHROPIC_API_KEY` privately. Run this example from the repository root.
It makes a billed API request; the skill installer itself makes no API calls.
The example uses a current ID from Anthropic's
[model overview](https://platform.claude.com/docs/en/models/overview).

```python
from pathlib import Path

import anthropic

client = anthropic.Anthropic()
fable_prompt = Path("raw/FABLE.md").read_text(encoding="utf-8")
response = client.messages.create(
    model="claude-opus-5-5",
    max_tokens=8192,
    system=fable_prompt,
    messages=[{"role": "user", "content": "Your task"}]
)
```

## What Makes This Work

The behavioral patterns with most impact (in order):
1. "Act, don't ask" — biggest differentiator
2. "Finish what you start" — prevents "I'll do X next" pattern
3. "Verify, don't assume" — actually test work
4. "Lead with outcome" — result-first communication
5. "Research before asking" — eliminates unnecessary questions
6. "Minimal code" — no unnecessary comments or abstractions

## Limitations
- CANNOT make a weak model strong — FABLE enhances behavior, not capability
- CANNOT replicate Fable 5's training — reasoning depth comes from weights
- DOES make any capable model behave more like Fable 5
- DOES eliminate common anti-patterns (over-asking, not finishing, hedging)
