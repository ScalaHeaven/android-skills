---
name: develop-android-gradle-build
description: "Configure Android AGP, Kotlin DSL, variants and version catalogs. Use for build setup, flavors and toolchain compatibility."
---

# Develop Android Gradle builds

## Establish the contract

Read repository instructions and the existing implementation first. Read Gradle wrapper, toolchains, plugins, variants, repository policy and signing references without printing secrets.
Record the requested outcome, current behavior and constraints. Inspect minSdk, targetSdk,
compileSdk and installed library/toolchain versions where they affect the task. Verify volatile
API restrictions, compatibility tables and release policies in current primary documentation.
Preserve the project's chosen stack unless a concrete limitation warrants changing it.

## Execute the workflow

1. Read wrapper, JDK, AGP, Kotlin and plugin constraints from the project and official compatibility guidance.
2. Define build types and flavors only for real delivery differences and keep variant-specific configuration explicit.
3. Centralize shared build logic through appropriate convention plugins and catalogs.
4. Inspect manifest/resource merging, namespaces and generated sources across affected variants.
5. Run actual Gradle tasks for affected debug, test and release variants without changing unrelated toolchain versions.

## Verify completion

- Dependencies are pinned or locked according to project policy.
- Signing material and local machine paths are not committed.
- Variant behavior is demonstrated through generated outputs or builds.

Discover available tasks with the project wrapper before using variant-specific examples. Use gradlew.bat on Windows. Check exit codes and reports; do not equate Gradle sync with verification.
Choose tests that observe a real failure or acceptance condition; avoid tests that merely mirror
the implementation. Reproduce a reported regression before fixing it when feasible. State any
missing device, backend or signing environment instead of claiming unexecuted checks passed.

## Use the bundled reference

Read [field-notes.md](references/field-notes.md) for decision boundaries, a concrete task and
its verification plan. Use its primary-source links to resolve version-specific questions.
Keep this skill standalone; related installed skills are optional assistance, not prerequisites.

## Run the helper

Run `python3 scripts/project_inventory.py PROJECT_DIRECTORY` from this skill directory, replacing the input
placeholders with actual paths and quoting paths with spaces. On Windows use the available Python
launcher (`python` or `py -3`). The script uses the standard library, reads local inputs and does
not run Gradle, alter devices or contact services. Read its `--help` and the input notes below.

Read build-file paths and literal SDK hints without executing Gradle. Resolve variables and convention plugins separately.

## Return evidence

Report the resulting behavior, changed artifacts and why the decision fits the contract.
Include executed checks and their actual outcomes, then any material unverified cases.
For reviews, give source locations, impact and a bounded repair. For plans, give acceptance
criteria and dependencies. For performance work, include measurement conditions and raw results.
Keep credentials and sensitive user data out of reports. Continue authorized implementation
and verification; do not add an approval step for routine reversible work.
