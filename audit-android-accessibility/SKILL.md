---
name: audit-android-accessibility
description: "Audit Android UI with TalkBack, semantics, focus, text scaling and contrast. Use for accessibility fixes and release usability review."
---

# Audit Android accessibility

## Establish the contract

Read repository instructions and the existing implementation first. Read window constraints, resource qualifiers, inset consumers, themes and accessibility semantics.
Record the requested outcome, current behavior and constraints. Inspect minSdk, targetSdk,
compileSdk and installed library/toolchain versions where they affect the task. Verify volatile
API restrictions, compatibility tables and release policies in current primary documentation.
Preserve the project's chosen stack unless a concrete limitation warrants changing it.

## Execute the workflow

1. Inspect semantic roles, names, state descriptions, actions and traversal groups.
2. Walk the primary task using TalkBack and keyboard/switch input where supported.
3. Check touch targets, contrast, large fonts and non-color-only status communication.
4. Prevent duplicate announcements from decorative icons and ensure custom controls expose equivalent actions.
5. Retest affected flows with both accessibility services and normal touch interaction.

## Verify completion

- Every important action has a meaningful accessible name and role.
- Focus order matches the task and does not trap the user.
- Dynamic errors and state changes remain understandable without seeing the screen.

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
