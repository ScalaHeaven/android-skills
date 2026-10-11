---
name: audit-android-window-insets
description: "Audit edge-to-edge, system bars, cutouts and IME in Android UI. Use for clipped controls, doubled padding or keyboard overlap."
---

# Audit Android window insets

## Establish the contract

Read repository instructions and the existing implementation first. Read window constraints, resource qualifiers, inset consumers, themes and accessibility semantics.
Record the requested outcome, current behavior and constraints. Inspect minSdk, targetSdk,
compileSdk and installed library/toolchain versions where they affect the task. Verify volatile
API restrictions, compatibility tables and release policies in current primary documentation.
Preserve the project's chosen stack unless a concrete limitation warrants changing it.

## Execute the workflow

1. Inventory edge-to-edge setup and each layer consuming status, navigation, cutout or IME insets.
2. Trace inset propagation across Scaffold, navigation hosts, dialogs and embedded Views.
3. Choose ownership for each inset and avoid adding the same padding twice.
4. Distinguish drawing behind system bars from keeping interactive content safely reachable.
5. Test gesture and button navigation, keyboard visibility, landscape, cutouts and supported target-SDK behavior.

## Verify completion

- Focused input and primary actions remain reachable with the keyboard.
- System bar contrast and icon appearance are readable.
- Screens do not accumulate extra padding through nested containers.

Record width, height, density, font scale, locale, theme and navigation mode. Compare the same content states and exercise configuration changes during the task.
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
