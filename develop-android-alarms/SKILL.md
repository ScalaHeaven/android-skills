---
name: develop-android-alarms
description: "Implement exact and inexact Android alarms with appropriate permission and timing semantics. Use for reminders and genuine time-critical user features."
---

# Develop Android alarms

## Establish the contract

Read repository instructions and the existing implementation first. Read the merged manifest, task entry points, permissions and the current OS/target-SDK execution restrictions.
Record the requested outcome, current behavior and constraints. Inspect minSdk, targetSdk,
compileSdk and installed library/toolchain versions where they affect the task. Verify volatile
API restrictions, compatibility tables and release policies in current primary documentation.
Preserve the project's chosen stack unless a concrete limitation warrants changing it.

## Execute the workflow

1. Determine whether exact wall-clock timing is a user requirement or merely a convenient implementation.
2. Select clock basis and wake behavior; distinguish elapsed duration from local calendar time.
3. Check current exact-alarm eligibility and access rules and define a fallback when unavailable.
4. Use stable PendingIntent identity and explicit cancellation/rescheduling after edits.
5. Test time-zone/time changes, reboot handling, denied access and Doze behavior relevant to the feature.

## Verify completion

- Repeated scheduling does not produce duplicate reminders.
- Local-time events handle daylight-saving transitions deliberately.
- Exact alarms are not used to emulate unrestricted background polling.

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
