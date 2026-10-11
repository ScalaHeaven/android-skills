---
name: validate-android-device-compatibility
description: "Validate Android behavior across device classes, OEMs, ABIs and hardware capability differences. Use for device-specific failures and support planning."
---

# Validate Android device compatibility

## Establish the contract

Read repository instructions and the existing implementation first. Read supported runtime matrix, release identities, telemetry definitions and reproducible incident evidence.
Record the requested outcome, current behavior and constraints. Inspect minSdk, targetSdk,
compileSdk and installed library/toolchain versions where they affect the task. Verify volatile
API restrictions, compatibility tables and release policies in current primary documentation.
Preserve the project's chosen stack unless a concrete limitation warrants changing it.

## Execute the workflow

1. Map audience and feature needs to representative devices rather than an arbitrary brand list.
2. Check declared required features, optional hardware detection and native ABI packaging.
3. Include missing Play services, low RAM/storage and relevant vendor behavior where the product supports them.
4. Execute consistent functional scenarios and record exact model, build fingerprint and app artifact.
5. Separate reproducible app defects from documented platform limitations and provide meaningful feature degradation.

## Verify completion

- Optional hardware absence does not make unrelated features unusable.
- One successful emulator is not called universal device support.
- Unsupported configurations have explicit installation or runtime behavior.

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
