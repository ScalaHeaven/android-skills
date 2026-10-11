---
name: document-android-architecture
description: "Write Android architecture decisions, module contracts and data-flow documentation grounded in current code. Use for onboarding, ADRs or architecture changes."
---

# Document Android architecture

## Establish the contract

Read repository instructions and the existing implementation first. Read module build files, representative vertical slices, data contracts and existing architecture decisions.
Record the requested outcome, current behavior and constraints. Inspect minSdk, targetSdk,
compileSdk and installed library/toolchain versions where they affect the task. Verify volatile
API restrictions, compatibility tables and release policies in current primary documentation.
Preserve the project's chosen stack unless a concrete limitation warrants changing it.

## Execute the workflow

1. Read implementation and build files; separate observed behavior from planned changes.
2. Select decisions that affect maintenance: state ownership, synchronization, lifetime, module boundaries and platform constraints.
3. Write concise ADRs with context, alternatives, decision and consequences rather than restating API tutorials.
4. Draw only diagrams that explain dependency direction or complex state transitions; name actual modules and components.
5. Cross-check examples, paths and commands against the project and assign review triggers for volatile claims.

## Verify completion

- Documentation distinguishes current, planned and unverified behavior.
- Links and component names resolve to actual project artifacts.
- A reader can locate a feature, its state owner and its verification route.

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
