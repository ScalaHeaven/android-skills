---
name: develop-android-design-system
description: "Build Android design tokens, themes and reusable accessible components. Use for inconsistent UI, app-wide theming or shared component libraries."
---

# Develop an Android design system

## Establish the contract

Read repository instructions and the existing implementation first. Read theme, composable boundaries, state collection, installed Compose/navigation versions and semantic trees.
Record the requested outcome, current behavior and constraints. Inspect minSdk, targetSdk,
compileSdk and installed library/toolchain versions where they affect the task. Verify volatile
API restrictions, compatibility tables and release policies in current primary documentation.
Preserve the project's chosen stack unless a concrete limitation warrants changing it.

## Execute the workflow

1. Inventory actual UI patterns and establish semantic color, typography, spacing and interaction tokens.
2. Implement themes across light/dark modes and any chosen dynamic-color policy without encoding raw colors in feature code.
3. Define component APIs for states, actions, content and accessibility semantics.
4. Create previews covering enabled, disabled, loading, error, long text and large font configurations.
5. Validate contrast, layout behavior and compatibility when replacing existing components.

## Verify completion

- Component states have consistent focus and touch behavior.
- Tokens express meaning and do not merely duplicate literal values.
- Theme changes preserve readable text and visible interaction states.

Run existing Compose UI tests and inspect representative previews. Verify interaction semantics; use screenshots for actual rendering questions, not as a substitute for behavior.
Choose tests that observe a real failure or acceptance condition; avoid tests that merely mirror
the implementation. Reproduce a reported regression before fixing it when feasible. State any
missing device, backend or signing environment instead of claiming unexecuted checks passed.

## Use the bundled reference

Read [field-notes.md](references/field-notes.md) for decision boundaries, a concrete task and
its verification plan. Use its primary-source links to resolve version-specific questions.
Keep this skill standalone; related installed skills are optional assistance, not prerequisites.

## Return evidence

Report the resulting behavior, changed artifacts and why the decision fits the contract.
Include executed checks and their actual outcomes, then any material unverified cases.
For reviews, give source locations, impact and a bounded repair. For plans, give acceptance
criteria and dependencies. For performance work, include measurement conditions and raw results.
Keep credentials and sensitive user data out of reports. Continue authorized implementation
and verification; do not add an approval step for routine reversible work.
