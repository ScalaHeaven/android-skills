---
name: review-android-architecture
description: "Audit existing Android architecture for coupling, data ownership, lifetime and testability problems. Use for project reviews or architecture-related regressions."
---

# Review Android architecture

## Establish the contract

Read repository instructions and the existing implementation first. Read module build files, representative vertical slices, data contracts and existing architecture decisions.
Record the requested outcome, current behavior and constraints. Inspect minSdk, targetSdk,
compileSdk and installed library/toolchain versions where they affect the task. Verify volatile
API restrictions, compatibility tables and release policies in current primary documentation.
Preserve the project's chosen stack unless a concrete limitation warrants changing it.

## Execute the workflow

1. Map modules, entry points, repositories, state holders and dependencies from source rather than naming conventions.
2. Follow a representative read, write and cancellation path; inspect error propagation and competing sources of truth.
3. Identify platform leakage into business code, cyclical dependencies and objects retained beyond their owners.
4. Rank findings by a concrete failure scenario and evidence; distinguish requirements from stylistic preferences.
5. Propose bounded fixes with regression checks and explain any migration cost.

## Verify completion

- Each finding includes a source location and user-visible consequence.
- Recommendations respect existing constraints and do not mandate a rewrite.
- A before/after dependency or data-flow example makes the fix reviewable.

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
