# CHANGELOG

## Unreleased
- Fix fresh installs and honor Claude Code's `CLAUDE_CONFIG_DIR` override.
- Restore the advertised `fable-plan-mode` skill from the existing planning guide.
- Check all skill entrypoints before installing, and make supporting references reachable.
- Move the core version field into portable skill metadata and describe shipped reference content accurately.
- Add installer and distribution checks on Linux and macOS.
- Correct usage-guide paths, identify prompt excerpts, and update the API example's model ID.

## v1.0.0 (2026-07-05)
- Initial release: 18 skills, 51 files
- Merged from: HalalifyMusic/fable-mode, kpab/claude-fable-5-skills,
  unclecatvn/rigorous-execution-skill, cyrus-tt/fable5-system-prompt,
  Rodbourn's retiring principal engineer methodology
- Based on: FABLE.md distillation + 3,800+ line verbatim prompt
- Source data: 72 session traces, 953 CoT traces, Boeing 747 trace
- Includes measured playbook: 1,307 Fable turns vs 10,470 Opus turns
