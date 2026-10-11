---
name: design-android-state-management
description: "Design Android UI state, user actions and effect delivery. Use for ViewModel state machines, repeated navigation, lost messages or inconsistent screen state."
---

# Design Android state management

## Establish the contract

Read repository instructions and the existing implementation first. Read module build files, representative vertical slices, data contracts and existing architecture decisions.
Record the requested outcome, current behavior and constraints. Inspect minSdk, targetSdk,
compileSdk and installed library/toolchain versions where they affect the task. Verify volatile
API restrictions, compatibility tables and release policies in current primary documentation.
Preserve the project's chosen stack unless a concrete limitation warrants changing it.

## Execute the workflow

1. List stable screen states and transitions for loading, content, empty, error and pending actions.
2. Choose a single state owner; derive display state from durable data and expose immutable snapshots.
3. Model actions explicitly and define cancellation, deduplication and stale-response handling.
4. Classify effects by delivery semantics: durable outcome, acknowledged message or transient best-effort signal; do not promise exactly-once delivery from a channel.
5. Verify collector interruption, recreation and process restoration against the required semantics.

## Verify completion

- Concurrent actions cannot produce impossible combinations of screen flags.
- Important outcomes survive collector absence through state or persisted data.
- Navigation and messages are neither blindly replayed nor silently dropped.

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
