---
name: develop-android-networking
description: "Implement Android HTTP APIs, serialization and network error handling. Use for API clients, uploads, timeouts and network robustness."
---

# Develop Android networking

## Establish the contract

Read repository instructions and the existing implementation first. Read repository contracts, DTOs, schemas, transaction boundaries, retry policies and storage ownership.
Record the requested outcome, current behavior and constraints. Inspect minSdk, targetSdk,
compileSdk and installed library/toolchain versions where they affect the task. Verify volatile
API restrictions, compatibility tables and release policies in current primary documentation.
Preserve the project's chosen stack unless a concrete limitation warrants changing it.

## Execute the workflow

1. Identify the API contract, authentication boundary, timeout needs and expected payload sizes.
2. Keep DTOs distinct from domain models where schema evolution or validation requires it.
3. Map transport, HTTP, parsing and business failures without swallowing cancellation.
4. Retry only operations whose semantics allow it; use server-supported idempotency for repeated writes.
5. Test malformed responses, slow/disconnected networks, expired sessions and partial uploads.

## Verify completion

- Sensitive headers and bodies are not exposed in logs.
- Timeouts and retries have finite budgets.
- Parsing rejects invalid required data rather than creating plausible corrupt records.

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
