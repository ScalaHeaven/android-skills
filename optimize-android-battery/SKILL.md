---
name: optimize-android-battery
description: "Analyze Android power use from background work, radios, sensors and wake locks. Use for battery drain and long-running recording optimization."
---

# Optimize Android battery use

## Establish the contract

Read repository instructions and the existing implementation first. Read measurement scenarios, build variants, compilation state, device conditions and raw traces/results.
Record the requested outcome, current behavior and constraints. Inspect minSdk, targetSdk,
compileSdk and installed library/toolchain versions where they affect the task. Verify volatile
API restrictions, compatibility tables and release policies in current primary documentation.
Preserve the project's chosen stack unless a concrete limitation warrants changing it.

## Execute the workflow

1. Define workload duration and device conditions; separate active user tasks from idle behavior.
2. Inspect wake locks, callback frequency, network batching and scheduler activity.
3. Reduce redundant work and tune sampling/batching against measured quality requirements.
4. Verify power behavior under screen-off, connectivity changes and relevant battery modes.
5. Report measurement method and tradeoffs; do not extrapolate precise battery life from CPU time alone.

## Verify completion

- Wake locks have explicit timeout or cleanup ownership.
- Sampling reductions preserve the required recording accuracy.
- OEM-dependent behavior is tested or clearly unverified.

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
