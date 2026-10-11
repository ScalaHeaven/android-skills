---
name: profile-android-performance
description: "Diagnose Android CPU, scheduling, rendering and I/O bottlenecks using profilers and Perfetto. Use for slow interactions and unexplained performance regressions."
---

# Profile Android performance

## Establish the contract

Read repository instructions and the existing implementation first. Read measurement scenarios, build variants, compilation state, device conditions and raw traces/results.
Record the requested outcome, current behavior and constraints. Inspect minSdk, targetSdk,
compileSdk and installed library/toolchain versions where they affect the task. Verify volatile
API restrictions, compatibility tables and release policies in current primary documentation.
Preserve the project's chosen stack unless a concrete limitation warrants changing it.

## Execute the workflow

1. Define a measurable user scenario and capture device, build, thermal and compilation conditions.
2. Reproduce with a representative release/profileable build and collect the appropriate trace.
3. Locate critical-path work, blocked threads, expensive frame phases and resource contention.
4. Form one evidence-backed hypothesis and make a bounded change.
5. Repeat the same scenario and report distributions and environmental limits rather than a single attractive run.

## Verify completion

- Tracing overhead is considered when interpreting results.
- Main-thread waiting is distinguished from main-thread computation.
- Trace evidence supports the specific optimization claim.

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
