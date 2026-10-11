---
name: develop-compose-lists-paging
description: "Implement Compose lazy lists and Paging with stable identity and clear load states. Use for large lists, scroll restoration, repeated loads or paginated feeds."
---

# Develop Compose lists and paging

## Establish the contract

Read repository instructions and the existing implementation first. Read theme, composable boundaries, state collection, installed Compose/navigation versions and semantic trees.
Record the requested outcome, current behavior and constraints. Inspect minSdk, targetSdk,
compileSdk and installed library/toolchain versions where they affect the task. Verify volatile
API restrictions, compatibility tables and release policies in current primary documentation.
Preserve the project's chosen stack unless a concrete limitation warrants changing it.

## Execute the workflow

1. Define sort order, stable item IDs and refresh/append consistency rules.
2. Select eager or lazy rendering and Paging only when data volume and loading behavior warrant it.
3. Supply stable keys and appropriate content types; prevent per-item work from owning global state.
4. Represent refresh, append, empty and retry states without discarding useful cached content.
5. Test insertion, deletion, reordering, failed append and restored scroll with realistic data volume.

## Verify completion

- Item-local state follows identity through reordering.
- Paging retries do not duplicate accepted records.
- Restoration uses IDs or indices consistent with the current dataset.

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
