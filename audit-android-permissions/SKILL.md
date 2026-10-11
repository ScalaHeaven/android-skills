---
name: audit-android-permissions
description: "Audit Android permission necessity, request timing and denied/revoked behavior. Use for excessive permissions and permission-dependent crashes."
---

# Audit Android permissions

## Establish the contract

Read repository instructions and the existing implementation first. Read exported interfaces, trust boundaries, credentials, sensitive data and release manifest/network configuration.
Record the requested outcome, current behavior and constraints. Inspect minSdk, targetSdk,
compileSdk and installed library/toolchain versions where they affect the task. Verify volatile
API restrictions, compatibility tables and release policies in current primary documentation.
Preserve the project's chosen stack unless a concrete limitation warrants changing it.

## Execute the workflow

1. Map each manifest permission to an actual user feature and current platform requirements.
2. Prefer narrower APIs and user-mediated pickers where they satisfy the use case.
3. Request access in context and handle approximate, partial, one-time and denied grants where applicable.
4. Recheck prerequisites at protected operations and respond safely to revocation or settings changes.
5. Test clean install, denial, repeated denial, revocation and resumed app behavior.

## Verify completion

- Removing permission does not crash unrelated app features.
- Permission checks are not treated as permanently valid snapshots.
- Privileged or signature permissions are not advertised as available to ordinary apps.

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
