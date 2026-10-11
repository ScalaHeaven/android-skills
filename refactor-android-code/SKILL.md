---
name: refactor-android-code
description: "Refactor Android implementations while preserving observable behavior, lifecycle and compatibility. Use for bounded cleanup, duplicated platform glue or oversized components."
---

# Refactor Android code

## Establish the contract

Read repository instructions and the existing implementation first. Read state holders, coroutine scopes, dispatchers, listener adapters and resource owners.
Record the requested outcome, current behavior and constraints. Inspect minSdk, targetSdk,
compileSdk and installed library/toolchain versions where they affect the task. Verify volatile
API restrictions, compatibility tables and release policies in current primary documentation.
Preserve the project's chosen stack unless a concrete limitation warrants changing it.

## Execute the workflow

1. Identify the concrete maintenance problem and record behavior, public APIs and saved-data contracts.
2. Create characterization checks for risky lifecycle or I/O paths before moving logic.
3. Extract pure transformations and platform adapters; keep ownership and dispatcher boundaries explicit.
4. Change one responsibility at a time and preserve navigation, permissions, serialization and DI contracts.
5. Run focused checks and inspect release behavior if reflection, resources or JNI names changed.

## Verify completion

- No architectural rewrite is smuggled into a local cleanup.
- Resource lifetimes and persisted formats remain deliberate.
- The diff demonstrates reduced complexity with preserved behavior.

Run the relevant JVM test task using injected dispatchers. Add lifecycle/device checks only for the platform behavior the change actually depends on.
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
