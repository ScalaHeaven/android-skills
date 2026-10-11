---
name: develop-android-file-storage
description: "Implement Android scoped storage, SAF, MediaStore and content URI access. Use for import/export, file permissions and large streamed media."
---

# Develop Android file storage

## Establish the contract

Read repository instructions and the existing implementation first. Read repository contracts, DTOs, schemas, transaction boundaries, retry policies and storage ownership.
Record the requested outcome, current behavior and constraints. Inspect minSdk, targetSdk,
compileSdk and installed library/toolchain versions where they affect the task. Verify volatile
API restrictions, compatibility tables and release policies in current primary documentation.
Preserve the project's chosen stack unless a concrete limitation warrants changing it.

## Execute the workflow

1. Select app-private storage, a document picker or MediaStore from ownership and user-access requirements.
2. Treat content URIs as provider handles, not filesystem paths; inspect supported seek and metadata operations.
3. Acquire persistable URI permission only when supported and required by the workflow.
4. Stream with bounded memory, close handles and handle provider cancellation, unavailable documents and insufficient space.
5. Test imported cloud documents, restart access, revoked grants and partial-output cleanup.

## Verify completion

- No blanket storage permission replaces an available scoped workflow.
- Success is reported only after output completion.
- Filename and MIME information from providers are treated as untrusted metadata.

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
