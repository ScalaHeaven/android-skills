---
name: audit-android-privacy
description: "Audit Android personal-data collection, SDK flows, retention and disclosure consistency. Use for privacy reviews and store data declarations."
---

# Audit Android privacy

## Establish the contract

Read repository instructions and the existing implementation first. Read exported interfaces, trust boundaries, credentials, sensitive data and release manifest/network configuration.
Record the requested outcome, current behavior and constraints. Inspect minSdk, targetSdk,
compileSdk and installed library/toolchain versions where they affect the task. Verify volatile
API restrictions, compatibility tables and release policies in current primary documentation.
Preserve the project's chosen stack unless a concrete limitation warrants changing it.

## Execute the workflow

1. Trace data collection from app and SDKs to storage, analytics and backend recipients.
2. Identify purpose, necessity, retention and deletion behavior for each data category.
3. Reduce collection and redact diagnostics while keeping sufficient operational evidence.
4. Compare actual behavior with consent flows, privacy text and current store declaration requirements.
5. Test opt-out, account deletion and SDK initialization timing; mark legal interpretation separately from technical evidence.

## Verify completion

- Declarations reflect SDK behavior as well as first-party code.
- Sensitive raw logs are not included in ordinary telemetry.
- Deleted data and retained backups have an explicit product policy.

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
