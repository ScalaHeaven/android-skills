---
name: develop-android-realtime-networking
description: "Implement Android long-lived streams and connections with reconnection and backpressure. Use for WebSocket, event streams or realtime feeds."
---

# Develop Android realtime networking

## Establish the contract

Read repository instructions and the existing implementation first. Read repository contracts, DTOs, schemas, transaction boundaries, retry policies and storage ownership.
Record the requested outcome, current behavior and constraints. Inspect minSdk, targetSdk,
compileSdk and installed library/toolchain versions where they affect the task. Verify volatile
API restrictions, compatibility tables and release policies in current primary documentation.
Preserve the project's chosen stack unless a concrete limitation warrants changing it.

## Execute the workflow

1. Define connection ownership, authorization refresh, ordering and resumption semantics.
2. Use a bounded state machine for disconnected, connecting, active and retry states.
3. Apply jittered backoff with cancellation and a finite policy; do not infer reachability solely from network callbacks.
4. Bound inbound/outbound buffering and define loss or persistence behavior per message class.
5. Test network handover, duplicate delivery, background suspension, slow consumers and session expiry.

## Verify completion

- A stopped owner cannot start a delayed reconnect.
- Reconnect preserves protocol ordering or explicitly resynchronizes.
- No unbounded queue grows while the server or UI is unavailable.

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
