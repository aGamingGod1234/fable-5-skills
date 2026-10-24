---
name: fable-plan-mode
description: >
  Plan a change before implementation. Use when the user requests a plan,
  design, or architectural approach, or when a multi-file task needs
  exploration before choosing an implementation.
---

# Plan Mode

## When to Plan
- Task requires understanding multiple files/systems not yet read
- Task involves architectural decisions
- Task spans 3+ files and you don't know the codebase structure
- User explicitly asks to "plan," "design," "think through"
- You're unsure where to start

## When NOT to Plan
- Simple bug fixes where you already know the file
- Small changes to 1-2 files with clear requirements
- User gives specific instructions
- Follow-up work where you already explored

## The Planning Process

### Phase 1: Understand Requirements
What problem does this solve? What are the constraints? What does success look like?

### Phase 2: Explore Thoroughly
Read provided files, find existing patterns, understand architecture, identify
similar features as reference, trace code paths.

### Phase 3: Design Solution
Create approach based on findings, consider trade-offs, follow existing patterns.
What could go wrong? What are edge cases?

### Phase 4: Write the Plan
- Begin with Context: why this change is being made
- Include only the recommended approach, not all alternatives
- Name critical files to be modified
- Reference existing functions/utilities with file paths
- Include verification section: how to test end-to-end

## Plan Quality Checklist
- [ ] Context explains why, not just what
- [ ] Steps ordered by dependency
- [ ] Critical files named
- [ ] Existing patterns/utilities referenced
- [ ] Verification steps included
- [ ] Edge cases addressed
- [ ] No unnecessary alternatives listed

## After Planning
Execute systematically, mark tasks completed as you go, update the plan if
discoveries change it, don't re-litigate decisions.
