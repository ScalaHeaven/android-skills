---
name: maintain-android-static-analysis
description: "Configure Android Lint, Detekt and formatting with meaningful enforcement. Use for CI lint failures and code quality configuration."
---

# Maintain Android static analysis

## Establish the contract

Read repository instructions and the existing implementation first. Read Gradle wrapper, toolchains, plugins, variants, repository policy and signing references without printing secrets.
Record the requested outcome, current behavior and constraints. Inspect minSdk, targetSdk,
compileSdk and installed library/toolchain versions where they affect the task. Verify volatile
API restrictions, compatibility tables and release policies in current primary documentation.
Preserve the project's chosen stack unless a concrete limitation warrants changing it.

## Execute the workflow

1. Inspect current tools, versions, rules, baselines and generated-code exclusions.
2. Enable rules that catch actual project risks and assign ownership for existing findings.
3. Fix root causes before adding narrow justified suppressions.
4. Keep formatting, Kotlin analysis and Android resource/API checks as distinct responsibilities.
5. Run the same tasks locally and in CI; verify release-specific lint configuration where relevant.

## Verify completion

- Broad baselines do not silently absorb new regressions.
- Suppressions state why the finding is inapplicable.
- Generated and vendored files are excluded without hiding owned source.

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
