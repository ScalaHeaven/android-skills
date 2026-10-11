---
name: develop-android-views
description: "Implement and maintain Android XML Views, Fragments and RecyclerView. Use for existing View-based apps and mixed UI projects."
---

# Develop Android Views

## Establish the contract

Read repository instructions and the existing implementation first. Read window constraints, resource qualifiers, inset consumers, themes and accessibility semantics.
Record the requested outcome, current behavior and constraints. Inspect minSdk, targetSdk,
compileSdk and installed library/toolchain versions where they affect the task. Verify volatile
API restrictions, compatibility tables and release policies in current primary documentation.
Preserve the project's chosen stack unless a concrete limitation warrants changing it.

## Execute the workflow

1. Read view lifecycle, layout hierarchy and binding setup before modifying a screen.
2. Keep binding references within the Fragment view lifetime and avoid asynchronous mutation after destruction.
3. Use RecyclerView identity, diffing and payload updates that match actual model equality.
4. Handle layout constraints, resource qualifiers, insets and keyboard behavior explicitly.
5. Test view recreation, recycled holders, delayed callbacks and accessible interaction.

## Verify completion

- Bindings are cleared and listeners removed at the correct lifetime boundary.
- Recycled items reset all relevant state.
- Layout changes remain correct across supported resource configurations.

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
