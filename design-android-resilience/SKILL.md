---
name: design-android-resilience
description: "Design Android recovery under process loss, storage pressure and dependency failure. Use for robust long-running and offline features."
---

# Design Android resilience

## Establish the contract

Read repository instructions and the existing implementation first. Read supported runtime matrix, release identities, telemetry definitions and reproducible incident evidence.
Record the requested outcome, current behavior and constraints. Inspect minSdk, targetSdk,
compileSdk and installed library/toolchain versions where they affect the task. Verify volatile
API restrictions, compatibility tables and release policies in current primary documentation.
Preserve the project's chosen stack unless a concrete limitation warrants changing it.

## Execute the workflow

1. List interruption points and the minimum state required to resume each operation.
2. Separate authoritative durable data from reconstructible caches and in-memory progress.
3. Make partial writes atomic or recoverable and define corruption/disk-full behavior.
4. Use finite retries, deadlines and explicit degradation rather than endless loading.
5. Inject failures around commits, resource acquisition and external acceptance to verify recovery.

## Verify completion

- Success cannot be reported before its durability contract is satisfied.
- Recovery does not duplicate accepted external actions.
- Fallbacks are visible when they affect data quality or user expectations.

Exercise the oldest supported runtime and changed behavior boundaries. Report local, emulator, physical-device and deployed evidence separately.
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
