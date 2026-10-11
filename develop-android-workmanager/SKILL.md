---
name: develop-android-workmanager
description: "Implement reliable deferred Android work with WorkManager. Use for durable uploads, constrained tasks, retries and unique work chains."
---

# Develop Android WorkManager jobs

## Establish the contract

Read repository instructions and the existing implementation first. Read the merged manifest, task entry points, permissions and the current OS/target-SDK execution restrictions.
Record the requested outcome, current behavior and constraints. Inspect minSdk, targetSdk,
compileSdk and installed library/toolchain versions where they affect the task. Verify volatile
API restrictions, compatibility tables and release policies in current primary documentation.
Preserve the project's chosen stack unless a concrete limitation warrants changing it.

## Execute the workflow

1. Define work identity, constraints, input size, outputs and restart-safe progress.
2. Use unique work and an explicit replacement/append policy suited to business semantics.
3. Make workers idempotent, cancellation-aware and independent of screen objects.
4. Separate retryable failures from terminal failures and bound backoff; read current limits for long-running workers.
5. Test duplicate enqueue, constraints changing, interruption and repeated execution with realistic persistent state.

## Verify completion

- Work can resume safely after process recreation.
- Large payloads are stored externally and passed by reference.
- Cancellation does not mark incomplete business work as successful.

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
