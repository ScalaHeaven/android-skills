---
name: localize-android-application
description: "Implement Android translations, plurals, formatting and RTL. Use for adding locales, resource auditing or locale-specific display failures."
---

# Localize an Android application

## Establish the contract

Read repository instructions and the existing implementation first. Read window constraints, resource qualifiers, inset consumers, themes and accessibility semantics.
Record the requested outcome, current behavior and constraints. Inspect minSdk, targetSdk,
compileSdk and installed library/toolchain versions where they affect the task. Verify volatile
API restrictions, compatibility tables and release policies in current primary documentation.
Preserve the project's chosen stack unless a concrete limitation warrants changing it.

## Execute the workflow

1. Inventory visible strings, content descriptions, embedded images and concatenated messages.
2. Move translatable content to resources with context and stable placeholder contracts.
3. Use plural and locale-aware number/date formatting; distinguish device locale from explicit user settings.
4. Handle RTL direction, mixed-script text and locale-aware input without reversing semantically fixed graphics.
5. Test pseudolocales, long translations, English plurals and runtime language changes.

## Verify completion

- Translation placeholders match their argument types and order.
- No sentence is assembled from independently translated fragments.
- Layout and accessibility labels work in long-text and RTL configurations.

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
