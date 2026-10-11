---
name: develop-android-room
description: "Design Room entities, queries, transactions and schema migrations. Use for local databases, query correctness or upgrading installed data."
---

# Develop Android Room storage

## Establish the contract

Read repository instructions and the existing implementation first. Read repository contracts, DTOs, schemas, transaction boundaries, retry policies and storage ownership.
Record the requested outcome, current behavior and constraints. Inspect minSdk, targetSdk,
compileSdk and installed library/toolchain versions where they affect the task. Verify volatile
API restrictions, compatibility tables and release policies in current primary documentation.
Preserve the project's chosen stack unless a concrete limitation warrants changing it.

## Execute the workflow

1. Model keys, relationships, nullability and constraints from product invariants.
2. Inspect query plans and indexes for actual read/write patterns; avoid premature indexing.
3. Define transactions for multi-record invariants and keep network calls outside database transactions.
4. Export versioned schemas and provide every supported migration path without accidental destructive fallback.
5. Test migration on populated old schemas and validate retained values, indexes and foreign keys.

## Verify completion

- Queries handle empty, duplicate and boundary data correctly.
- Migration tests verify content preservation, not just database opening.
- Large results use bounded loading rather than unbounded entity materialization.

Use realistic data and inject failures before and after commit/remote acceptance. Test upgrades against populated old data and distinguish mock server checks from actual backend compatibility.
Choose tests that observe a real failure or acceptance condition; avoid tests that merely mirror
the implementation. Reproduce a reported regression before fixing it when feasible. State any
missing device, backend or signing environment instead of claiming unexecuted checks passed.

## Use the bundled reference

Read [field-notes.md](references/field-notes.md) for decision boundaries, a concrete task and
its verification plan. Use its primary-source links to resolve version-specific questions.
Keep this skill standalone; related installed skills are optional assistance, not prerequisites.

## Run the helper

Run `python3 scripts/compare_schemas.py OLD_ROOM_SCHEMA.json NEW_ROOM_SCHEMA.json` from this skill directory, replacing the input
placeholders with actual paths and quoting paths with spaces. On Windows use the available Python
launcher (`python` or `py -3`). The script uses the standard library, reads local inputs and does
not run Gradle, alter devices or contact services. Read its `--help` and the input notes below.

Use exported Room schema files with database.entities. Structural differences are hints; execute populated migration tests to verify correctness.

## Return evidence

Report the resulting behavior, changed artifacts and why the decision fits the contract.
Include executed checks and their actual outcomes, then any material unverified cases.
For reviews, give source locations, impact and a bounded repair. For plans, give acceptance
criteria and dependencies. For performance work, include measurement conditions and raw results.
Keep credentials and sensitive user data out of reports. Continue authorized implementation
and verification; do not add an approval step for routine reversible work.
