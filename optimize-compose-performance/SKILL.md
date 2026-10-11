---
name: optimize-compose-performance
description: "Optimize measured Compose composition, layout and drawing costs. Use for scrolling jank and rendering regressions."
---

# Optimize Compose performance

## Establish the contract

Read repository instructions and the existing implementation first. Read measurement scenarios, build variants, compilation state, device conditions and raw traces/results.
Record the requested outcome, current behavior and constraints. Inspect minSdk, targetSdk,
compileSdk and installed library/toolchain versions where they affect the task. Verify volatile
API restrictions, compatibility tables and release policies in current primary documentation.
Preserve the project's chosen stack unless a concrete limitation warrants changing it.

## Execute the workflow

1. Capture a benchmark or trace for the affected interaction before changing code.
2. Identify state-read scope, unnecessary work, layout passes and per-frame allocations.
3. Move expensive invariant work out of recomposition and defer state reads to the appropriate phase when useful.
4. Inspect list keys, unstable parameters and compiler reports without blindly adding Stable/Immutable annotations.
5. Rebenchmark with matching device and compilation conditions and preserve visual/accessibility behavior.

## Verify completion

- Reduced recomposition count alone is not claimed as faster UI.
- Annotations reflect real immutability guarantees.
- No premature caching retains excessive data or stale inputs.

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
