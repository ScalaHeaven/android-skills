---
name: maintain-android-ci
description: "Build Android CI with reproducible toolchains, tests and emulator artifacts. Use for workflow creation and CI-only build/test failures."
---

# Maintain Android continuous integration

## Establish the contract

Read repository instructions and the existing implementation first. Read Gradle wrapper, toolchains, plugins, variants, repository policy and signing references without printing secrets.
Record the requested outcome, current behavior and constraints. Inspect minSdk, targetSdk,
compileSdk and installed library/toolchain versions where they affect the task. Verify volatile
API restrictions, compatibility tables and release policies in current primary documentation.
Preserve the project's chosen stack unless a concrete limitation warrants changing it.

## Execute the workflow

1. Pin compatible JDK, SDK and Gradle setup and read the repository-required tasks.
2. Separate fast checks from device scenarios while preserving required merge gates.
3. Use reproducible emulator/device configurations and bounded startup/test timeouts.
4. Cache supported dependency/build state without persisting secrets or treating stale cache as authoritative.
5. Retain test XML, useful logs and failure artifacts, and validate workflow changes against actual task execution.

## Verify completion

- CI does not expose signing credentials in logs or artifacts.
- Task success is not inferred from missing test reports.
- Device failures include enough evidence to reproduce configuration.

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
