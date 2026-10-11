---
name: optimize-android-startup
description: "Measure and improve Android cold and warm startup and usable-screen latency. Use for slow launch or eager initialization regressions."
---

# Optimize Android startup

## Establish the contract

Read repository instructions and the existing implementation first. Read measurement scenarios, build variants, compilation state, device conditions and raw traces/results.
Record the requested outcome, current behavior and constraints. Inspect minSdk, targetSdk,
compileSdk and installed library/toolchain versions where they affect the task. Verify volatile
API restrictions, compatibility tables and release policies in current primary documentation.
Preserve the project's chosen stack unless a concrete limitation warrants changing it.

## Execute the workflow

1. Define launch mode and distinguish initial display from fully useful content.
2. Measure startup under controlled compilation, storage and cache conditions.
3. Trace application, provider, DI and first-screen initialization along the critical path.
4. Defer nonessential work and preserve ordering for required dependencies; avoid merely hiding a blank wait behind a splash.
5. Repeat measurements and verify first interaction and deep-entry correctness.

## Verify completion

- Cold and warm measurements are not mixed into one comparison.
- Deferred work does not immediately create post-launch jank.
- Startup improvement includes a defined user-ready condition.

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
