---
name: design-android-offline-first
description: "Design Android data flows that remain useful without connectivity. Use for local-first repositories, cached UI and offline editing."
---

# Design offline-first Android data

## Establish the contract

Read repository instructions and the existing implementation first. Read repository contracts, DTOs, schemas, transaction boundaries, retry policies and storage ownership.
Record the requested outcome, current behavior and constraints. Inspect minSdk, targetSdk,
compileSdk and installed library/toolchain versions where they affect the task. Verify volatile
API restrictions, compatibility tables and release policies in current primary documentation.
Preserve the project's chosen stack unless a concrete limitation warrants changing it.

## Execute the workflow

1. Define which operations are available offline and how freshness is shown to users.
2. Choose a local authoritative read model and separate network refresh from visible data reads.
3. Specify queued writes, pending status and conflict ownership with backend contracts.
4. Use bounded synchronization triggered by meaningful signals rather than treating connectivity as proof of server reachability.
5. Verify cold launch offline, stale cache, partial refresh and recovery after process termination.

## Verify completion

- UI remains useful with previously stored data during a failed refresh.
- Pending changes cannot silently disappear.
- Freshness and conflict behavior are explicit product decisions.

Use realistic data and inject failures before and after commit/remote acceptance. Test upgrades against populated old data and distinguish mock server checks from actual backend compatibility.
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
