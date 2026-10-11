---
name: develop-android-observability
description: "Implement Android structured logs, metrics and diagnostic evidence with privacy controls. Use for production diagnosis and monitoring design."
---

# Develop Android observability

## Establish the contract

Read repository instructions and the existing implementation first. Read supported runtime matrix, release identities, telemetry definitions and reproducible incident evidence.
Record the requested outcome, current behavior and constraints. Inspect minSdk, targetSdk,
compileSdk and installed library/toolchain versions where they affect the task. Verify volatile
API restrictions, compatibility tables and release policies in current primary documentation.
Preserve the project's chosen stack unless a concrete limitation warrants changing it.

## Execute the workflow

1. Define questions the telemetry must answer and minimize collected fields.
2. Add bounded structured events for state transitions, failures and important latency measurements.
3. Use correlation identifiers that avoid exposing user identity or sensitive payloads.
4. Redact credentials, location and personal content where not essential; define retention and sampling.
5. Test offline buffering, reporting failures and release log behavior without affecting the primary app task.

## Verify completion

- Telemetry failure cannot block critical user operations.
- Release diagnostics omit secrets and raw sensitive data.
- Metric definitions identify units, boundaries and sampling biases.

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
