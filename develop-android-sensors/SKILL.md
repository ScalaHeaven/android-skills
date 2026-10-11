---
name: develop-android-sensors
description: "Implement Android IMU and sensor acquisition with timestamps, batching and coordinate handling. Use for motion tracking and sensor lifecycle issues."
---

# Develop Android sensor pipelines

## Establish the contract

Read repository instructions and the existing implementation first. Read actual hardware capabilities, units, timestamps, runtime support, ownership and device-level constraints.
Record the requested outcome, current behavior and constraints. Inspect minSdk, targetSdk,
compileSdk and installed library/toolchain versions where they affect the task. Verify volatile
API restrictions, compatibility tables and release policies in current primary documentation.
Preserve the project's chosen stack unless a concrete limitation warrants changing it.

## Execute the workflow

1. Detect actual sensor type/capabilities and define required versus optional data.
2. Interpret units, device axes and event timestamps; distinguish sensor time from wall-clock time.
3. Keep callbacks short, copy data before asynchronous retention and process on an owned bounded pipeline.
4. Choose rate, batching and listener lifecycle from quality/power needs; check current rate and background restrictions.
5. Test replayed fixtures plus real-device orientation, missing sensors, jitter and screen-off behavior.

## Verify completion

- SensorEvent arrays are not retained as immutable snapshots without copying.
- Requested sampling rate is not treated as guaranteed delivered rate.
- Coordinate conversions and timestamp synchronization have numerical checks.

Use replay fixtures for algorithm correctness and physical devices for quality, timing, routing and power claims. Record actual delivered rates, formats and error conditions.
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
