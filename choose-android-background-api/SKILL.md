---
name: choose-android-background-api
description: "Select Android execution mechanisms for deferred, user-visible or time-sensitive work. Use before introducing WorkManager, services or alarms."
---

# Choose Android background APIs

## Establish the contract

Read repository instructions and the existing implementation first. Read the merged manifest, task entry points, permissions and the current OS/target-SDK execution restrictions.
Record the requested outcome, current behavior and constraints. Inspect minSdk, targetSdk,
compileSdk and installed library/toolchain versions where they affect the task. Verify volatile
API restrictions, compatibility tables and release policies in current primary documentation.
Preserve the project's chosen stack unless a concrete limitation warrants changing it.

## Execute the workflow

1. Classify user initiation, durability, timing precision, data access and expected execution duration.
2. Check current OS and target-SDK rules for the required operation and permissions.
3. Choose lifecycle coroutines for owned in-process work, persistent schedulers for deferrable work and services only for qualifying ongoing work.
4. Record why alternatives fail requirements; do not use WorkManager as a guarantee of precise periodic timing.
5. Create a lifecycle and execution acceptance matrix including process loss, battery constraints and user cancellation.

## Verify completion

- The chosen mechanism satisfies platform eligibility, not just compilation.
- Timing promises match scheduler guarantees.
- No component is used merely to keep the process alive.

Use a specified adb device serial for device commands. Separate process termination, user force-stop, reboot and battery restrictions; they have different execution semantics.
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
