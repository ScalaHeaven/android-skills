---
name: audit-android-lifecycle
description: "Audit Activity, Fragment, Compose and ViewModel resource lifetimes. Use for crashes after navigation, duplicate listeners and resources active on stopped screens."
---

# Audit Android lifecycle ownership

## Establish the contract

Read repository instructions and the existing implementation first. Read state holders, coroutine scopes, dispatchers, listener adapters and resource owners.
Record the requested outcome, current behavior and constraints. Inspect minSdk, targetSdk,
compileSdk and installed library/toolchain versions where they affect the task. Verify volatile
API restrictions, compatibility tables and release policies in current primary documentation.
Preserve the project's chosen stack unless a concrete limitation warrants changing it.

## Execute the workflow

1. Build an ownership table for views, callbacks, receivers, coroutines and native resources.
2. Distinguish Fragment lifecycle from viewLifecycleOwner and navigation entry lifetime.
3. Inspect registration/unregistration symmetry and callbacks arriving after stop or disposal.
4. Choose lifecycle collection and cleanup mechanisms that match the feature rather than always using onDestroy.
5. Exercise rotation, back navigation, multi-window and repeated foreground transitions; count active resources.

## Verify completion

- Each registration has one explicit cleanup owner.
- A removed Fragment view cannot be mutated by late results.
- Re-entering a screen does not multiply collectors or listeners.

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
