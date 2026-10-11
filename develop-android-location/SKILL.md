---
name: develop-android-location
description: "Implement Android location providers, freshness, accuracy and background tracking. Use for GNSS/network location, trip recording and stale-position bugs."
---

# Develop Android location features

## Establish the contract

Read repository instructions and the existing implementation first. Read actual hardware capabilities, units, timestamps, runtime support, ownership and device-level constraints.
Record the requested outcome, current behavior and constraints. Inspect minSdk, targetSdk,
compileSdk and installed library/toolchain versions where they affect the task. Verify volatile
API restrictions, compatibility tables and release policies in current primary documentation.
Preserve the project's chosen stack unless a concrete limitation warrants changing it.

## Execute the workflow

1. Define accuracy, latency and power needs and choose platform or Play services APIs according to supported devices.
2. Check provider/service availability and permissions, including approximate access and background/foreground-service rules.
3. Validate position age using appropriate monotonic timing and inspect accuracy and mock indicators according to the use case.
4. Own subscriptions explicitly and handle unavailable providers, stale last-known fixes and user stop.
5. Test reproducible mock routes separately from real-device indoor/outdoor, handover and screen-off recording.

## Verify completion

- Network-derived location is not described as a guaranteed direct cell-tower coordinate API.
- Missing Play services or GNSS has a defined fallback where supported.
- Accuracy and freshness are not inferred merely from receiving a callback.

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
