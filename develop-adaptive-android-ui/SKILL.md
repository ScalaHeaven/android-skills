---
name: develop-adaptive-android-ui
description: "Adapt Android UI to available window space, tablets and foldable postures. Use for responsive layouts and multi-pane screen behavior."
---

# Develop adaptive Android UI

## Establish the contract

Read repository instructions and the existing implementation first. Read window constraints, resource qualifiers, inset consumers, themes and accessibility semantics.
Record the requested outcome, current behavior and constraints. Inspect minSdk, targetSdk,
compileSdk and installed library/toolchain versions where they affect the task. Verify volatile
API restrictions, compatibility tables and release policies in current primary documentation.
Preserve the project's chosen stack unless a concrete limitation warrants changing it.

## Execute the workflow

1. Read current window constraints and feature requirements; avoid using device marketing categories as layout rules.
2. Define compact and expanded navigation/content arrangements with meaningful breakpoints.
3. Preserve selection and screen state when switching between one and multiple panes.
4. Handle hinges, resizing, multi-window and external input where relevant.
5. Validate minimum usable sizes, long content and live window changes without restarting the feature.

## Verify completion

- Window resizing preserves the active task.
- Pane placement accounts for occlusion and available space.
- Large-screen UI uses space productively rather than stretching phone content.

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
