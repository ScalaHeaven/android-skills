---
name: audit-android-release-build
description: "Audit Android release R8, resources, signing and native packaging. Use when debug works but release fails or before delivery."
---

# Audit Android release builds

## Establish the contract

Read repository instructions and the existing implementation first. Read Gradle wrapper, toolchains, plugins, variants, repository policy and signing references without printing secrets.
Record the requested outcome, current behavior and constraints. Inspect minSdk, targetSdk,
compileSdk and installed library/toolchain versions where they affect the task. Verify volatile
API restrictions, compatibility tables and release policies in current primary documentation.
Preserve the project's chosen stack unless a concrete limitation warrants changing it.

## Execute the workflow

1. Build the exact release variant and inspect its merged configuration and packaged contents.
2. Verify reflection, serialization and JNI entry points under shrinking using targeted keep rules.
3. Inspect required ABIs, native library alignment and current page-size compatibility requirements.
4. Validate signing configuration, debuggability, network overrides and intended resources without exposing private keys.
5. Install representative release outputs and exercise critical flows; preserve mapping and symbol artifacts for diagnosis.

## Verify completion

- ZIP native inventory is not mistaken for ELF/page-alignment verification.
- Keep rules are minimal and justified by actual dynamic access.
- Debug and release differences are explicitly tested.

Discover available tasks with the project wrapper before using variant-specific examples. Use gradlew.bat on Windows. Check exit codes and reports; do not equate Gradle sync with verification.
Choose tests that observe a real failure or acceptance condition; avoid tests that merely mirror
the implementation. Reproduce a reported regression before fixing it when feasible. State any
missing device, backend or signing environment instead of claiming unexecuted checks passed.

## Use the bundled reference

Read [field-notes.md](references/field-notes.md) for decision boundaries, a concrete task and
its verification plan. Use its primary-source links to resolve version-specific questions.
Keep this skill standalone; related installed skills are optional assistance, not prerequisites.

## Run the helper

Run `python3 scripts/inspect_apk.py APP.apk` from this skill directory, replacing the input
placeholders with actual paths and quoting paths with spaces. On Windows use the available Python
launcher (`python` or `py -3`). The script uses the standard library, reads local inputs and does
not run Gradle, alter devices or contact services. Read its `--help` and the input notes below.

Accept APK or AAB ZIP containers. Read native ABI/library inventory without extracting files. Verify signatures, ELF page alignment and APK ZIP alignment separately with appropriate Android tooling.

## Return evidence

Report the resulting behavior, changed artifacts and why the decision fits the contract.
Include executed checks and their actual outcomes, then any material unverified cases.
For reviews, give source locations, impact and a bounded repair. For plans, give acceptance
criteria and dependencies. For performance work, include measurement conditions and raw results.
Keep credentials and sensitive user data out of reports. Continue authorized implementation
and verification; do not add an approval step for routine reversible work.
