---
name: audit-android-memory
description: "Diagnose Android leaks, allocation pressure and OOM across JVM and native memory. Use for growing memory use or crashes after repeated navigation."
---

# Audit Android memory

## Establish the contract

Read repository instructions and the existing implementation first. Read measurement scenarios, build variants, compilation state, device conditions and raw traces/results.
Record the requested outcome, current behavior and constraints. Inspect minSdk, targetSdk,
compileSdk and installed library/toolchain versions where they affect the task. Verify volatile
API restrictions, compatibility tables and release policies in current primary documentation.
Preserve the project's chosen stack unless a concrete limitation warrants changing it.

## Execute the workflow

1. Choose a repeatable scenario and distinguish Java heap, native heap, graphics and mapped memory.
2. Capture retained-object evidence or allocation profiles after suitable settling and collection conditions.
3. Trace reference ownership through callbacks, caches, Views, coroutines and JNI global references.
4. Bound caches and buffers and fix incorrect ownership rather than forcing GC as a repair.
5. Repeat the scenario and inspect retained objects plus peak memory with the same device/build.

## Verify completion

- One RSS reading is not treated as proof of a leak.
- Large assets use appropriate decoding and bounded lifetime.
- Fixes release native and managed resources exactly once.

Preserve raw samples, device/build identity, warmup, compilation mode and thermal conditions. Alternate run order where feasible and report contradictory or noisy results.
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
