---
name: develop-android-native-rust
description: "Integrate Rust with Android NDK/JNI and audit ABI, ownership and callbacks. Use for native libraries, JNI crashes and release packaging."
---

# Develop Android native Rust integration

## Establish the contract

Read repository instructions and the existing implementation first. Read actual hardware capabilities, units, timestamps, runtime support, ownership and device-level constraints.
Record the requested outcome, current behavior and constraints. Inspect minSdk, targetSdk,
compileSdk and installed library/toolchain versions where they affect the task. Verify volatile
API restrictions, compatibility tables and release policies in current primary documentation.
Preserve the project's chosen stack unless a concrete limitation warrants changing it.

## Execute the workflow

1. Inventory NDK/toolchain versions, supported ABIs and the current JVM-to-native contract.
2. Define explicit ownership of handles, strings, arrays and buffers; prevent use-after-free and double disposal.
3. Catch Rust panics before crossing FFI and translate failures without leaving pending JNI exceptions unnoticed.
4. Attach native callback threads correctly, manage local/global references and coordinate shutdown with in-flight calls.
5. Verify minified release packaging, symbolization, ELF alignment/page-size compatibility and device lifecycle stress.

## Verify completion

- JNIEnv and local references are not reused across arbitrary threads.
- Native shutdown cannot race an active operation without a defined protocol.
- ZIP inventory alone does not establish native load compatibility.

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
