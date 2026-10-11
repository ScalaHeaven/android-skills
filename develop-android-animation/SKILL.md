---
name: develop-android-animation
description: "Implement interruptible Android and Compose animations. Use for state transitions, gestures, animated navigation or motion-related usability problems."
---

# Develop Android animations

## Establish the contract

Read repository instructions and the existing implementation first. Read theme, composable boundaries, state collection, installed Compose/navigation versions and semantic trees.
Record the requested outcome, current behavior and constraints. Inspect minSdk, targetSdk,
compileSdk and installed library/toolchain versions where they affect the task. Verify volatile
API restrictions, compatibility tables and release policies in current primary documentation.
Preserve the project's chosen stack unless a concrete limitation warrants changing it.

## Execute the workflow

1. Define the purpose, start/end states and interruption policy for each animation.
2. Select transition, visibility, value or gesture-driven APIs based on coordinated state requirements.
3. Keep animated presentation derived from authoritative product state; avoid timers that race navigation.
4. Support rapid reversals, removed composition and relevant reduced-animation settings.
5. Inspect frame timing on realistic devices and test final semantics when animations are skipped or interrupted.

## Verify completion

- Rapid toggles converge to the latest intended state.
- Animation does not delay essential validation or accessibility state updates.
- No unbounded coroutine or drawing allocation is introduced.

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
