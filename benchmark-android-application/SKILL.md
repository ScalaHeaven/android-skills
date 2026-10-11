---
name: benchmark-android-application
description: "Create Android Microbenchmark and Macrobenchmark experiments with reproducible comparisons. Use for performance claims and regression checks."
---

# Benchmark an Android application

## Establish the contract

Read repository instructions and the existing implementation first. Read measurement scenarios, build variants, compilation state, device conditions and raw traces/results.
Record the requested outcome, current behavior and constraints. Inspect minSdk, targetSdk,
compileSdk and installed library/toolchain versions where they affect the task. Verify volatile
API restrictions, compatibility tables and release policies in current primary documentation.
Preserve the project's chosen stack unless a concrete limitation warrants changing it.

## Execute the workflow

1. Select a metric and scenario that represent the user or hot path; choose micro versus end-to-end measurement.
2. Control device, build, compilation, datasets, warmup, thermal state and run order.
3. Keep setup and assertions outside the measured region where appropriate.
4. Collect repeated raw results, traces and relevant distribution statistics; avoid treating emulator timing as representative device performance.
5. Compare changes with a predeclared practical threshold and rerun contradictory results before drawing a conclusion.

## Verify completion

- Results identify the exact artifacts and environment compared.
- Outliers are explained rather than silently discarded.
- A median change alone is not a statistical significance claim.

Preserve raw samples, device/build identity, warmup, compilation mode and thermal conditions. Alternate run order where feasible and report contradictory or noisy results.
Choose tests that observe a real failure or acceptance condition; avoid tests that merely mirror
the implementation. Reproduce a reported regression before fixing it when feasible. State any
missing device, backend or signing environment instead of claiming unexecuted checks passed.

## Use the bundled reference

Read [field-notes.md](references/field-notes.md) for decision boundaries, a concrete task and
its verification plan. Use its primary-source links to resolve version-specific questions.
Keep this skill standalone; related installed skills are optional assistance, not prerequisites.

## Run the helper

Run `python3 scripts/compare_samples.py BEFORE.json AFTER.json` from this skill directory, replacing the input
placeholders with actual paths and quoting paths with spaces. On Windows use the available Python
launcher (`python` or `py -3`). The script uses the standard library, reads local inputs and does
not run Gradle, alter devices or contact services. Read its `--help` and the input notes below.

Normalize each dataset as {"metric":"startup","unit":"ms","samples":[101,104,99],"context":{"device":"test-device","variant":"release","compilation":"record-mode"}}. Preserve original results. This computes descriptive medians, not significance; positive changes mean larger values.

## Return evidence

Report the resulting behavior, changed artifacts and why the decision fits the contract.
Include executed checks and their actual outcomes, then any material unverified cases.
For reviews, give source locations, impact and a bounded repair. For plans, give acceptance
criteria and dependencies. For performance work, include measurement conditions and raw results.
Keep credentials and sensitive user data out of reports. Continue authorized implementation
and verification; do not add an approval step for routine reversible work.
