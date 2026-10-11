---
name: validate-android-concurrency
description: "Find Android races, callback ordering errors and unsafe shared state. Use for intermittent bugs in coroutine, sensor, network or native callback pipelines."
---

# Validate Android concurrency

## Establish the contract

Read repository instructions and the existing implementation first. Read state holders, coroutine scopes, dispatchers, listener adapters and resource owners.
Record the requested outcome, current behavior and constraints. Inspect minSdk, targetSdk,
compileSdk and installed library/toolchain versions where they affect the task. Verify volatile
API restrictions, compatibility tables and release policies in current primary documentation.
Preserve the project's chosen stack unless a concrete limitation warrants changing it.

## Execute the workflow

1. Enumerate threads, coroutine scopes, shared mutable state and callback ordering guarantees.
2. Write invariants for ownership, update ordering and maximum in-flight work.
3. Construct adverse interleavings: cancel-before-register, late response, simultaneous update and double disposal.
4. Choose confinement, atomic operations, Mutex or serialization based on the invariant; avoid locks around suspending external calls.
5. Use controlled fakes or schedulers to reproduce failures and verify cleanup under repeated execution.

## Verify completion

- Cancellation and registration cannot leave an orphan callback.
- Stale results cannot overwrite a newer accepted state.
- Native/JVM thread assumptions are supported by implementation evidence.

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
