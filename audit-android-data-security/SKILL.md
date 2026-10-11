---
name: audit-android-data-security
description: "Audit Android secrets, Keystore, backup and stored sensitive data. Use for local confidentiality, key management and accidental data exposure."
---

# Audit Android data security

## Establish the contract

Read repository instructions and the existing implementation first. Read exported interfaces, trust boundaries, credentials, sensitive data and release manifest/network configuration.
Record the requested outcome, current behavior and constraints. Inspect minSdk, targetSdk,
compileSdk and installed library/toolchain versions where they affect the task. Verify volatile
API restrictions, compatibility tables and release policies in current primary documentation.
Preserve the project's chosen stack unless a concrete limitation warrants changing it.

## Execute the workflow

1. Classify stored data and identify backup, export, logging and crash-report copies.
2. Choose platform key protection and encryption based on actual threat model and library support.
3. Inspect key lifetime, authentication requirements, invalidation and reinstall/restore behavior.
4. Check that secrets are absent from source, resources and client-distributed configuration where confidentiality is required.
5. Test access failure, key invalidation and cleanup without silently destroying recoverable user data.

## Verify completion

- Keystore use is not claimed to protect data after all possible device compromises.
- Backup behavior matches the sensitivity and restoration contract.
- Cryptographic choices use established APIs rather than custom primitives.

Use merged release configuration and controlled negative cases. Separate a scanner hint, confirmed reachable issue and hypothetical threat; do not label every exported component vulnerable.
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
