---
name: develop-android-ipc
description: "Implement Android Binder, AIDL and ContentProvider contracts. Use for cross-process services, structured data sharing and IPC lifecycle bugs."
---

# Develop Android IPC

## Establish the contract

Read repository instructions and the existing implementation first. Read the merged manifest, task entry points, permissions and the current OS/target-SDK execution restrictions.
Record the requested outcome, current behavior and constraints. Inspect minSdk, targetSdk,
compileSdk and installed library/toolchain versions where they affect the task. Verify volatile
API restrictions, compatibility tables and release policies in current primary documentation.
Preserve the project's chosen stack unless a concrete limitation warrants changing it.

## Execute the workflow

1. Confirm IPC is required and define caller trust, protocol versioning and bounded payloads.
2. Enforce caller authorization at exported endpoints; do not trust an identifier supplied in the request.
3. Handle Binder thread-pool concurrency, remote death and reconnect without blocking main-thread interactions.
4. Design transactions and provider operations for resource ownership and backpressure.
5. Test unauthorized callers, oversized data, remote process loss and backward-compatible contract evolution.

## Verify completion

- Exported endpoints enforce intended permissions and identity checks.
- Remote death cannot leave permanently pending UI operations.
- Large binary data uses an appropriate handle or streaming contract.

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
