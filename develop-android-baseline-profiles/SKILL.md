---
name: develop-android-baseline-profiles
description: "Generate and validate Baseline Profiles for important Android user journeys. Use for startup and runtime optimization in release builds."
---

# Develop Android Baseline Profiles

## Establish the contract

Read repository instructions and the existing implementation first. Read measurement scenarios, build variants, compilation state, device conditions and raw traces/results.
Record the requested outcome, current behavior and constraints. Inspect minSdk, targetSdk,
compileSdk and installed library/toolchain versions where they affect the task. Verify volatile
API restrictions, compatibility tables and release policies in current primary documentation.
Preserve the project's chosen stack unless a concrete limitation warrants changing it.

## Execute the workflow

1. Verify plugin, AGP, library and target-device support using the current project versions.
2. Select representative critical journeys and generate profiles with stable navigation and data.
3. Inspect generated artifacts and confirm they are packaged in the intended release variant.
4. Measure matching builds with explicitly chosen compilation modes to isolate profile benefit.
5. Maintain regeneration triggers when journeys or dependency versions change.

## Verify completion

- Debug-only or uninstalled profiles are not credited with release improvements.
- Measurements distinguish profile effects from warm caches.
- Generated journeys exercise useful code rather than only opening the launcher.

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
