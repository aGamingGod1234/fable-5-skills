# Contributing

## Adding a Skill

1. Create a new directory under `skills/`
2. Add a `SKILL.md` with YAML frontmatter (`name`, `description`) + body
3. Keep SKILL.md body under 500 lines — move detail to `references/`
4. Description must be trigger-rich — Claude matches requests against it
5. Test with Haiku, Sonnet, and Opus if possible

## Distribution Checks

Add new skills to the `SKILLS` array in `install.sh` and the README inventory.
Link supporting Markdown files from the skill's `SKILL.md`, using paths relative
to that file so each skill remains independently installable.

Before submitting a change, run these checks with Bash and Python 3.9 or newer:

```bash
bash -n install.sh
python3 -B -m unittest discover -s tests -v
```

The tests invoke the installer in temporary directories. They check fresh and
repeat installs, incomplete checkouts, failure reporting, the documented skill
inventory, and reachable supporting files. They do not call a model or modify
your personal Claude Code configuration. CI runs the same checks on Linux and
macOS. Model-based evaluation remains a separate check of the skill's behavior.

## Skill Quality Bar

- Every rule must have a reason stated
- Progressive disclosure: supporting files load on demand
- No capability compensation (hand-holding for older models)
- One concept per skill — don't bundle unrelated behaviors
- Ground every claim in observed behavior from traces
