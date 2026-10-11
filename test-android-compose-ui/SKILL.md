---
name: test-android-compose-ui
description: "Write Compose UI tests for semantics, user actions and screen state. Use for interaction regressions and composable behavior."
---

# Test Android Compose UI

## Establish the contract

Read repository instructions and the existing implementation first. Read existing tests, fixture ownership, environment setup and the contract the user scenario requires.
Record the requested outcome, current behavior and constraints. Inspect minSdk, targetSdk,
compileSdk and installed library/toolchain versions where they affect the task. Verify volatile
API restrictions, compatibility tables and release policies in current primary documentation.
Preserve the project's chosen stack unless a concrete limitation warrants changing it.

## Execute the workflow

1. Select the composable or navigation boundary under test and provide deterministic state/dependencies.
2. Query by user-facing semantics or intentional stable test tags; inspect merged versus unmerged trees where relevant.
3. Perform real UI actions and assert user-visible behavior, focus or accessible state.
4. Use test synchronization or the animation clock instead of arbitrary sleeps.
5. Exercise loading, errors, keyboard input and relevant navigation/restoration behavior.

## Verify completion

- Tests assert behavior rather than the exact number of internal recompositions.
- Semantics reflect real accessibility where possible.
- External asynchronous work has an explicit synchronization mechanism.

Run only meaningful affected checks, retain test XML and list skipped/unavailable cases. A passing local substitute does not establish behavior of an untested external system.
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
