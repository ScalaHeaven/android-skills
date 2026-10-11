---
name: test-android-unit
description: "Write Android JVM tests for business logic, ViewModels and state transformations. Use for isolated regressions and deterministic correctness checks."
---

# Test Android units and ViewModels

## Establish the contract

Read repository instructions and the existing implementation first. Read existing tests, fixture ownership, environment setup and the contract the user scenario requires.
Record the requested outcome, current behavior and constraints. Inspect minSdk, targetSdk,
compileSdk and installed library/toolchain versions where they affect the task. Verify volatile
API restrictions, compatibility tables and release policies in current primary documentation.
Preserve the project's chosen stack unless a concrete limitation warrants changing it.

## Execute the workflow

1. Identify an observable contract and isolate external time, storage and networking.
2. Use stateful fakes for meaningful boundary behavior rather than asserting every internal call.
3. Test success, invalid input, dependency failure and relevant boundary values.
4. Verify state transitions and final outputs without depending on incidental scheduling or implementation structure.
5. Run focused tests and check whether the assertion would fail under the original defect.

## Verify completion

- Tests do not require Android framework objects unless their behavior is relevant.
- A failing test reports the broken contract clearly.
- Fixtures avoid nondeterministic clock, locale and random values.

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
