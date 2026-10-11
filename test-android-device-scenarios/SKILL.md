---
name: test-android-device-scenarios
description: "Exercise Android lifecycle, permissions, network and process behavior on devices or emulators. Use for integration QA beyond JVM tests."
---

# Test Android device scenarios

## Establish the contract

Read repository instructions and the existing implementation first. Read existing tests, fixture ownership, environment setup and the contract the user scenario requires.
Record the requested outcome, current behavior and constraints. Inspect minSdk, targetSdk,
compileSdk and installed library/toolchain versions where they affect the task. Verify volatile
API restrictions, compatibility tables and release policies in current primary documentation.
Preserve the project's chosen stack unless a concrete limitation warrants changing it.

## Execute the workflow

1. Select device/OS configurations from actual behavior boundaries and record build variant.
2. Prepare repeatable state and define expected outcomes for each scenario.
3. Test recreation, genuine background process termination, permission denial/revocation and interrupted connectivity separately.
4. Use UI Automator, instrumentation and scoped ADB operations with an explicit target device.
5. Restore changed test settings and record screenshots/logs only as needed for evidence.

## Verify completion

- Force-stop, task dismissal and process death are not treated as equivalent.
- Emulator success is not reported as validation of GNSS, BLE or vendor power behavior.
- Test state changes do not affect an unintended attached device.

Run only meaningful affected checks, retain test XML and list skipped/unavailable cases. A passing local substitute does not establish behavior of an untested external system.
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
