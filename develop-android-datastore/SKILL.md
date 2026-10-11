---
name: develop-android-datastore
description: "Implement DataStore settings and migrations from SharedPreferences. Use for preference concurrency, typed settings and durable small configuration."
---

# Develop Android DataStore

## Establish the contract

Read repository instructions and the existing implementation first. Read repository contracts, DTOs, schemas, transaction boundaries, retry policies and storage ownership.
Record the requested outcome, current behavior and constraints. Inspect minSdk, targetSdk,
compileSdk and installed library/toolchain versions where they affect the task. Verify volatile
API restrictions, compatibility tables and release policies in current primary documentation.
Preserve the project's chosen stack unless a concrete limitation warrants changing it.

## Execute the workflow

1. Choose Preferences or typed storage according to schema and validation needs.
2. Ensure store instances and file ownership comply with the library process model; choose a supported multiprocess mechanism when needed.
3. Make updates atomic and avoid read-modify-write races outside update operations.
4. Define default, corruption, migration and unknown-enum behavior without resetting unrelated values.
5. Test concurrent updates, legacy migration and restart persistence.

## Verify completion

- Migration preserves valid existing user choices.
- No heavy business dataset is forced into a settings store.
- Failure handling distinguishes unavailable storage from a legitimate default.

Use realistic data and inject failures before and after commit/remote acceptance. Test upgrades against populated old data and distinguish mock server checks from actual backend compatibility.
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
