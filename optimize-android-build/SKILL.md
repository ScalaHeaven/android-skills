---
name: optimize-android-build
description: "Diagnose Android Gradle build latency and improve incremental/cache behavior. Use for slow local iteration or CI build regressions."
---

# Optimize Android builds

## Establish the contract

Read repository instructions and the existing implementation first. Read Gradle wrapper, toolchains, plugins, variants, repository policy and signing references without printing secrets.
Record the requested outcome, current behavior and constraints. Inspect minSdk, targetSdk,
compileSdk and installed library/toolchain versions where they affect the task. Verify volatile
API restrictions, compatibility tables and release policies in current primary documentation.
Preserve the project's chosen stack unless a concrete limitation warrants changing it.

## Execute the workflow

1. Define clean, incremental or no-change build workloads and collect matching timings.
2. Inspect configuration, task execution, dependency resolution and annotation-processing costs.
3. Fix eager configuration and unnecessary task inputs using supported Gradle patterns.
4. Evaluate configuration/build caches and module changes with correctness under cache reuse.
5. Compare repeated workloads and avoid claiming a cache hit is equivalent to faster cold compilation.

## Verify completion

- Cached builds reproduce the same outputs and do not leak credentials.
- Optimization does not disable required verification tasks.
- Memory/parallelism settings match the actual machine and workload.

Discover available tasks with the project wrapper before using variant-specific examples. Use gradlew.bat on Windows. Check exit codes and reports; do not equate Gradle sync with verification.
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
