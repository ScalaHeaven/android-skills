---
name: develop-android-foreground-services
description: "Implement eligible Android foreground services with correct types, permissions and stop behavior. Use for ongoing recording, location or media operations."
---

# Develop Android foreground services

## Establish the contract

Read repository instructions and the existing implementation first. Read the merged manifest, task entry points, permissions and the current OS/target-SDK execution restrictions.
Record the requested outcome, current behavior and constraints. Inspect minSdk, targetSdk,
compileSdk and installed library/toolchain versions where they affect the task. Verify volatile
API restrictions, compatibility tables and release policies in current primary documentation.
Preserve the project's chosen stack unless a concrete limitation warrants changing it.

## Execute the workflow

1. Validate foreground-service eligibility and current launch restrictions for OS and target SDK.
2. Declare the applicable service type and permissions and handle denied prerequisites before starting.
3. Enter foreground promptly with a meaningful notification and user stop action.
4. Persist required task state separately from service memory; define restart behavior without assuming continuous execution.
5. Test background transitions, revoked permission, user stop, process loss and applicable time limits.

## Verify completion

- Denied permission or ineligible launch produces a recoverable UI outcome.
- Stopping releases sensor, audio, location and wake resources.
- Service presence is not claimed to guarantee immunity to process termination.

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
