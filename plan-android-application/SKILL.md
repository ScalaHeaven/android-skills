---
name: plan-android-application
description: "Plan Android product requirements, user journeys, platform constraints and delivery milestones. Use for a new app, substantial feature specification or feasibility assessment."
---

# Plan an Android application

## Establish the contract

Read repository instructions and the existing implementation first. Read module build files, representative vertical slices, data contracts and existing architecture decisions.
Record the requested outcome, current behavior and constraints. Inspect minSdk, targetSdk,
compileSdk and installed library/toolchain versions where they affect the task. Verify volatile
API restrictions, compatibility tables and release policies in current primary documentation.
Preserve the project's chosen stack unless a concrete limitation warrants changing it.

## Execute the workflow

1. Extract actors, journeys, data sensitivity, offline needs and measurable acceptance criteria.
2. Inventory device classes, distribution channels, minSdk/targetSdk constraints and required hardware; separate supported API access from privileged capabilities.
3. Create a feature-to-screen-to-data map and identify permission, service and external backend dependencies.
4. Compare implementation options by uncertainty, maintainability and operational cost; schedule prototypes for unresolved platform constraints.
5. Produce staged milestones with dependency order, verification environments and explicit out-of-scope features.

## Verify completion

- Every requirement maps to an observable acceptance condition.
- High-risk hardware/background assumptions have a prototype or an explicitly unverified status.
- Estimate ranges include integration, device QA and release work.

Use the project Gradle wrapper to inspect projects and affected compilation tasks. Review dependency edges and trace at least one read and write end to end.
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
