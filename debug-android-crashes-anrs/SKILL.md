---
name: debug-android-crashes-anrs
description: "Diagnose Android JVM/native crashes and Application Not Responding reports. Use for stack traces, tombstones and blocked-thread failures."
---

# Debug Android crashes and ANRs

## Establish the contract

Read repository instructions and the existing implementation first. Read supported runtime matrix, release identities, telemetry definitions and reproducible incident evidence.
Record the requested outcome, current behavior and constraints. Inspect minSdk, targetSdk,
compileSdk and installed library/toolchain versions where they affect the task. Verify volatile
API restrictions, compatibility tables and release policies in current primary documentation.
Preserve the project's chosen stack unless a concrete limitation warrants changing it.

## Execute the workflow

1. Match report to exact version, variant, obfuscation mapping and native symbols.
2. Group by failure mechanism and user scenario rather than merely top stack frame.
3. For ANRs inspect all relevant threads, locks, Binder calls and main-thread critical paths.
4. For native crashes inspect symbolized frames, ownership and memory corruption possibilities without trusting the final frame as root cause.
5. Produce a minimal reproduction and fix with a regression check or explicit device validation requirement.

## Verify completion

- Missing symbols or mappings are acknowledged before drawing precise conclusions.
- ANRs are not all attributed to long computation; waiting and deadlocks are considered.
- A null guard does not hide violated required invariants.

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
