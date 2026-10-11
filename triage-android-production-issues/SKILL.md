---
name: triage-android-production-issues
description: "Turn Android user reports and telemetry into reproducible defects and bounded fixes. Use for support incidents and post-release regressions."
---

# Triage Android production issues

## Establish the contract

Read repository instructions and the existing implementation first. Read supported runtime matrix, release identities, telemetry definitions and reproducible incident evidence.
Record the requested outcome, current behavior and constraints. Inspect minSdk, targetSdk,
compileSdk and installed library/toolchain versions where they affect the task. Verify volatile
API restrictions, compatibility tables and release policies in current primary documentation.
Preserve the project's chosen stack unless a concrete limitation warrants changing it.

## Execute the workflow

1. Collect version, device, timing, expected behavior and minimal reproduction without unnecessary personal data.
2. Correlate report with release changes and diagnostic evidence, marking hypotheses explicitly.
3. Prioritize by user impact, reach and workaround availability.
4. Reproduce at the relevant platform boundary and implement the smallest adequate fix.
5. Add a regression guard and define post-release observation criteria for resolution.

## Verify completion

- No claimed cause rests solely on a plausible anecdote.
- Sensitive logs are minimized and handled according to scope.
- Fix status distinguishes locally verified, device verified and deployed.

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
