---
name: develop-android-data-sync
description: "Implement durable Android synchronization queues, retries and conflicts. Use for queued uploads, outbox patterns and duplicate or lost writes."
---

# Develop Android data synchronization

## Establish the contract

Read repository instructions and the existing implementation first. Read repository contracts, DTOs, schemas, transaction boundaries, retry policies and storage ownership.
Record the requested outcome, current behavior and constraints. Inspect minSdk, targetSdk,
compileSdk and installed library/toolchain versions where they affect the task. Verify volatile
API restrictions, compatibility tables and release policies in current primary documentation.
Preserve the project's chosen stack unless a concrete limitation warrants changing it.

## Execute the workflow

1. Specify identity, revision and idempotency contracts shared with the backend.
2. Persist a durable outbox and commit local mutations and queue records consistently.
3. Claim work with recoverable ownership and handle interruption before and after remote acceptance.
4. Define bounded backoff, terminal errors, conflict resolution and user-visible retry behavior.
5. Test lost acknowledgments, replay, simultaneous edits, reordered delivery and app restart.

## Verify completion

- Repeated delivery cannot duplicate the accepted business action.
- A crash does not strand a claimed item indefinitely.
- Conflict handling preserves or exposes competing edits instead of silently dropping them.

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
