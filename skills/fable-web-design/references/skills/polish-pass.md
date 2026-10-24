# Polish Pass: End-of-Design Quality Gate

Run a comprehensive quality check before delivery. A polished design and
unpolished design are the same idea executed at different levels of care.

## Phase 1: Confirm Scope
Determine what to polish: the HTML file just finished, or the current main
deliverable. If the design is clearly mid-flight, ask whether to polish now.

## Phase 2: Launch Review Checks (run sequentially)

Run these four checks in order:

### A. Accessibility Audit
- Contrast and color (WCAG AA minimums, color-only signaling)
- Semantic HTML and structure (headings, button vs div, labels, ARIA)
- Keyboard navigation and focus (reachability, tab order, visible focus)
- Motion, forms (prefers-reduced-motion, flash limits, error specificity,
  hit-target size)

### B. AI Slop Check
Apply the [AI Slop Check criteria](ai-slop-check.md).

### C. Hierarchy & Rhythm Review
- **Hierarchy**: primary/secondary/tertiary differentiation, 5-second test
- **Rhythm**: spacing scale discipline, type scale discipline, repetition,
  strategic variation, alignment

### D. Interaction States Pass
- Inventory every interactive element
- For each: default, hover, active, disabled, focus, loading
- Transitions (0.15-0.3s for state changes, longer for entry/exit)
- Feedback for actions (success/error confirmation)

## Phase 3: Fix
Fix every blocker and quality issue. Apply polish recommendations when
they don't conflict with user's stated direction.

## Phase 4: Re-verify
Quick re-check on high-risk areas. Did contrast fixes maintain visual style?
Did focus rings overlap? Did hierarchy adjustments make primary CTA feel primary?

## Phase 5: Final Summary
- Verdict: "Ready to ship" / "Ready after user reviews" / "Needs more iteration"
- Blockers fixed (count by category)
- Open decisions for user sign-off
- Out of scope: noticed but didn't touch
