---
name: test-android-ui-configurations
description: "Build a focused UI configuration matrix for font scale, orientation, themes and window sizes. Use for responsive regressions and visual QA."
---

# Test Android UI configurations

## Establish the contract

Read repository instructions and the existing implementation first. Read window constraints, resource qualifiers, inset consumers, themes and accessibility semantics.
Record the requested outcome, current behavior and constraints. Inspect minSdk, targetSdk,
compileSdk and installed library/toolchain versions where they affect the task. Verify volatile
API restrictions, compatibility tables and release policies in current primary documentation.
Preserve the project's chosen stack unless a concrete limitation warrants changing it.

## Execute the workflow

1. Select configurations from actual audience and known layout risks rather than an exhaustive Cartesian product.
2. Capture representative states with long content, loading and errors.
3. Exercise live configuration changes while preserving the active user task.
4. Combine semantic interaction assertions with screenshots where rendering itself matters.
5. Record exact emulator/device, display metrics, font scale and theme for reproducible findings.

## Verify completion

- Screenshot baselines are generated under controlled rendering conditions.
- Visual comparisons do not replace assertions about action behavior.
- Clipping and inaccessible primary controls have explicit regressions.

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
