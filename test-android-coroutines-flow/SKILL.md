---
name: test-android-coroutines-flow
description: "Test coroutine scheduling, cancellation and Flow emissions deterministically. Use for virtual-time, race and event delivery regressions."
---

# Test Android coroutines and Flow

## Establish the contract

Read repository instructions and the existing implementation first. Read existing tests, fixture ownership, environment setup and the contract the user scenario requires.
Record the requested outcome, current behavior and constraints. Inspect minSdk, targetSdk,
compileSdk and installed library/toolchain versions where they affect the task. Verify volatile
API restrictions, compatibility tables and release policies in current primary documentation.
Preserve the project's chosen stack unless a concrete limitation warrants changing it.

## Execute the workflow

1. Use the coroutine test library compatible with the project and share the test scheduler across injected dispatchers.
2. Start collectors deliberately and specify which emissions or state transitions matter.
3. Advance virtual time intentionally and distinguish runCurrent, time advancement and draining pending work.
4. Test cancellation cleanup, failing children, subscriber gaps and repeated subscription.
5. Keep never-ending collectors in a managed test background scope and assert no stranded jobs.

## Verify completion

- Real sleeps do not substitute for scheduling control.
- Unconfined test behavior does not hide a production ordering defect.
- Collectors are started before testing events that can be lost.

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
