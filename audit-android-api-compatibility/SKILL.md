---
name: audit-android-api-compatibility
description: "Audit Android minSdk, targetSdk, API guards and fallback behavior. Use for older-device crashes and platform API adoption."
---

# Audit Android API compatibility

## Establish the contract

Read repository instructions and the existing implementation first. Read supported runtime matrix, release identities, telemetry definitions and reproducible incident evidence.
Record the requested outcome, current behavior and constraints. Inspect minSdk, targetSdk,
compileSdk and installed library/toolchain versions where they affect the task. Verify volatile
API restrictions, compatibility tables and release policies in current primary documentation.
Preserve the project's chosen stack unless a concrete limitation warrants changing it.

## Execute the workflow

1. Inventory SDK levels, desugaring, library minimums and guarded platform entry points.
2. Distinguish API availability from target-SDK behavior changes and service/library capabilities.
3. Place compatible fallbacks at boundaries and avoid loading unsupported classes before guards apply.
4. Review resource qualifiers, permission differences and unavailable hardware independently of API level.
5. Test oldest supported runtime plus behavior boundaries introduced by affected APIs.

## Verify completion

- Newer API references cannot execute through unguarded initialization.
- Fallback behavior meets a defined user contract.
- Compile success is not reported as runtime compatibility proof.

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
