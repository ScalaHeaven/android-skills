---
name: design-android-test-strategy
description: "Design risk-based Android unit, integration, device and UI testing. Use for new projects, coverage gaps or expensive unreliable test suites."
---

# Design Android test strategy

## Establish the contract

Read repository instructions and the existing implementation first. Read existing tests, fixture ownership, environment setup and the contract the user scenario requires.
Record the requested outcome, current behavior and constraints. Inspect minSdk, targetSdk,
compileSdk and installed library/toolchain versions where they affect the task. Verify volatile
API restrictions, compatibility tables and release policies in current primary documentation.
Preserve the project's chosen stack unless a concrete limitation warrants changing it.

## Execute the workflow

1. Map user journeys to failure impact, change frequency and platform dependence.
2. Choose the cheapest test level that can observe the actual risk; use device tests for real framework behavior.
3. Define external boundaries, fixtures, realistic datasets and which contracts need backend verification.
4. Allocate OS/device configurations by boundary behavior rather than duplicating every unit test across all devices.
5. Write a verification plan with owners, reproducibility requirements and explicit untested hardware cases.

## Verify completion

- Coverage percentage does not substitute for important behavior assertions.
- Mocks do not redefine the contract being tested.
- Each expensive device test protects a distinct platform risk.

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
