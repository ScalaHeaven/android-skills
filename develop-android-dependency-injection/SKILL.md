---
name: develop-android-dependency-injection
description: "Implement Android dependency injection and review scopes with Hilt, Dagger or manual containers. Use for object lifetime bugs, test replacement or DI setup."
---

# Develop Android dependency injection

## Establish the contract

Read repository instructions and the existing implementation first. Read module build files, representative vertical slices, data contracts and existing architecture decisions.
Record the requested outcome, current behavior and constraints. Inspect minSdk, targetSdk,
compileSdk and installed library/toolchain versions where they affect the task. Verify volatile
API restrictions, compatibility tables and release policies in current primary documentation.
Preserve the project's chosen stack unless a concrete limitation warrants changing it.

## Execute the workflow

1. Read the existing DI mechanism and identify constructors, bindings, qualifiers and component owners.
2. Match each dependency lifetime to the data it owns; reject Activity or View references in longer-lived objects.
3. Choose constructor injection where possible and explicit factories for runtime arguments.
4. Provide replaceable boundaries for tests without global mutable registries.
5. Verify creation, disposal, component recreation and production/test binding completeness.

## Verify completion

- Scoped instances have deliberate identity and no shorter-lived Context capture.
- Missing or ambiguous bindings fail during appropriate build checks.
- Tests can replace external I/O without altering production lifetime semantics.

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
