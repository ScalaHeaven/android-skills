---
name: develop-android-flow
description: "Build Android Flow, StateFlow and SharedFlow pipelines with explicit sharing, replay and lifecycle behavior. Use for stale UI, duplicated subscriptions or dropped events."
---

# Develop Android Flow

## Establish the contract

Read repository instructions and the existing implementation first. Read state holders, coroutine scopes, dispatchers, listener adapters and resource owners.
Record the requested outcome, current behavior and constraints. Inspect minSdk, targetSdk,
compileSdk and installed library/toolchain versions where they affect the task. Verify volatile
API restrictions, compatibility tables and release policies in current primary documentation.
Preserve the project's chosen stack unless a concrete limitation warrants changing it.

## Execute the workflow

1. Classify the stream as state, events or a cold computation and identify its upstream owner.
2. Choose sharing start policy and replay from delivery requirements; stateIn does not provide durable storage.
3. Place transformations and flowOn deliberately; avoid retaining heavyweight data in replay caches.
4. Collect UI streams with the relevant lifecycle APIs and close callbackFlow listeners with awaitClose.
5. Verify multiple collectors, subscription gaps, rapid input, cancellation and backpressure behavior.

## Verify completion

- State collectors obtain a coherent current state.
- Hot-flow event loss or replay behavior is documented and tested where material.
- Restarting collection does not accidentally register duplicate hardware listeners.

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
