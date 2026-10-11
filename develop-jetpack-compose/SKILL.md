---
name: develop-jetpack-compose
description: "Implement Compose screens with explicit state ownership and reusable UI contracts. Use for new composables, screen features or Compose integration."
---

# Develop Jetpack Compose screens

## Establish the contract

Read repository instructions and the existing implementation first. Read theme, composable boundaries, state collection, installed Compose/navigation versions and semantic trees.
Record the requested outcome, current behavior and constraints. Inspect minSdk, targetSdk,
compileSdk and installed library/toolchain versions where they affect the task. Verify volatile
API restrictions, compatibility tables and release policies in current primary documentation.
Preserve the project's chosen stack unless a concrete limitation warrants changing it.

## Execute the workflow

1. Read the existing theme, state holder and supported Compose versions before choosing APIs.
2. Separate route/state collection from stateless rendering; accept state and action callbacks at screen boundaries.
3. Hoist state to its lowest correct shared owner and use saved state only where restoration is required.
4. Implement loading, error, empty and content cases plus previewable representative states.
5. Verify semantics, user actions, recomposition safety and resource cleanup on screen disposal.

## Verify completion

- Composable execution does not directly perform I/O or navigation.
- Reusable components expose deliberate Modifier and event contracts.
- All material screen states can be exercised independently.

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
