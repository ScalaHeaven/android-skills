---
name: develop-android-navigation
description: "Implement Android navigation, back-stack behavior and restoration using the project navigation stack. Use for routes, nested flows, deep-link destinations or duplicate screens."
---

# Develop Android navigation

## Establish the contract

Read repository instructions and the existing implementation first. Read theme, composable boundaries, state collection, installed Compose/navigation versions and semantic trees.
Record the requested outcome, current behavior and constraints. Inspect minSdk, targetSdk,
compileSdk and installed library/toolchain versions where they affect the task. Verify volatile
API restrictions, compatibility tables and release policies in current primary documentation.
Preserve the project's chosen stack unless a concrete limitation warrants changing it.

## Execute the workflow

1. Read the installed navigation library and model destination identity, graph scopes and entry points.
2. Pass small validated identifiers rather than large mutable objects; define missing-argument behavior.
3. Specify back, up, repeated tap, login redirect and multiple entry semantics before coding.
4. Scope state holders to the correct entry and restore navigation consistently with saved application state.
5. Test deep entry, restored stack, nested navigation and back gestures on supported platform versions.

## Verify completion

- Back navigation returns to the intended previous context.
- Repeated actions do not unintentionally duplicate destinations.
- Deep links cannot bypass required authorization checks.

Run existing Compose UI tests and inspect representative previews. Verify interaction semantics; use screenshots for actual rendering questions, not as a substitute for behavior.
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
