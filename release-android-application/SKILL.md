---
name: release-android-application
description: "Prepare Android signed releases, test tracks and staged rollout with current distribution requirements. Use for version publishing and release readiness."
---

# Release an Android application

## Establish the contract

Read repository instructions and the existing implementation first. Read Gradle wrapper, toolchains, plugins, variants, repository policy and signing references without printing secrets.
Record the requested outcome, current behavior and constraints. Inspect minSdk, targetSdk,
compileSdk and installed library/toolchain versions where they affect the task. Verify volatile
API restrictions, compatibility tables and release policies in current primary documentation.
Preserve the project's chosen stack unless a concrete limitation warrants changing it.

## Execute the workflow

1. Verify version codes, artifact identity, signing lineage and the target distribution channel.
2. Check current store requirements, permissions declarations and data forms against actual app behavior.
3. Run release smoke tests and retain mapping/native symbols and reproducible build metadata.
4. Prepare review notes, migration communication and a staged rollout/stop plan where supported.
5. Publish only within user-authorized scope and monitor crash, ANR and essential business metrics after rollout.

## Verify completion

- Signing keys are never embedded in the distributable skill or diagnostics.
- Target-SDK and policy dates are verified at release time.
- Halting rollout is distinguished from reverting already installed application versions.

Discover available tasks with the project wrapper before using variant-specific examples. Use gradlew.bat on Windows. Check exit codes and reports; do not equate Gradle sync with verification.
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
