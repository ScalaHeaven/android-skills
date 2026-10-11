---
name: review-compose-correctness
description: "Audit Compose remember keys, effects, mutable state and identity bugs. Use for stale callbacks, repeated requests, lost item state or unsafe composition side effects."
---

# Review Compose correctness

## Establish the contract

Read repository instructions and the existing implementation first. Read theme, composable boundaries, state collection, installed Compose/navigation versions and semantic trees.
Record the requested outcome, current behavior and constraints. Inspect minSdk, targetSdk,
compileSdk and installed library/toolchain versions where they affect the task. Verify volatile
API restrictions, compatibility tables and release policies in current primary documentation.
Preserve the project's chosen stack unless a concrete limitation warrants changing it.

## Execute the workflow

1. Trace state reads and writes and identify values that must trigger recomposition.
2. Check remember and effect keys against actual invalidation requirements and item identity.
3. Inspect LaunchedEffect, DisposableEffect and rememberUpdatedState for cancellation, cleanup and current callbacks.
4. Replace unobservable in-place mutations with supported state updates; do not use stability annotations to hide mutable contracts.
5. Exercise reordered items, changed arguments, conditional composition and disposal to expose stale behavior.

## Verify completion

- Effects restart only when their semantic inputs change.
- Listeners are removed on disposal and callbacks observe current values.
- Stable keys represent item identity rather than list position.

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
