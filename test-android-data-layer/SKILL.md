---
name: test-android-data-layer
description: "Test Android repositories, API parsing, Room migrations and synchronization. Use for storage/network contract regressions."
---

# Test Android data layers

## Establish the contract

Read repository instructions and the existing implementation first. Read existing tests, fixture ownership, environment setup and the contract the user scenario requires.
Record the requested outcome, current behavior and constraints. Inspect minSdk, targetSdk,
compileSdk and installed library/toolchain versions where they affect the task. Verify volatile
API restrictions, compatibility tables and release policies in current primary documentation.
Preserve the project's chosen stack unless a concrete limitation warrants changing it.

## Execute the workflow

1. Define repository invariants independently of the implementation and choose local or device environments accordingly.
2. Use representative API fixtures including malformed fields and protocol errors.
3. Test transactions and migration paths on populated schemas with actual value assertions.
4. Exercise stale cache, partial writes, repeated sync and lost remote acknowledgments.
5. Report which checks use an actual backend or database versus a substitute.

## Verify completion

- Migration tests check records and constraints after upgrade.
- A mock API does not establish compatibility with the live backend.
- Failure injection demonstrates recovery rather than only exception propagation.

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
