---
name: develop-android-authentication
description: "Implement Android Credential Manager, passkeys and OAuth/OIDC session handling. Use for login, account switching and token lifecycle integration."
---

# Develop Android authentication

## Establish the contract

Read repository instructions and the existing implementation first. Read exported interfaces, trust boundaries, credentials, sensitive data and release manifest/network configuration.
Record the requested outcome, current behavior and constraints. Inspect minSdk, targetSdk,
compileSdk and installed library/toolchain versions where they affect the task. Verify volatile
API restrictions, compatibility tables and release policies in current primary documentation.
Preserve the project's chosen stack unless a concrete limitation warrants changing it.

## Execute the workflow

1. Select authentication from backend capabilities and current credential-provider support.
2. For OAuth/OIDC use established authorization flows, browser-based authorization and PKCE where applicable; validate redirect and state contracts.
3. Store and refresh session credentials with deliberate lifetime and concurrency ownership.
4. Separate successful authentication from authorization of each protected operation.
5. Test cancellation, account switch, logout, revoked session and interrupted redirects without leaking tokens.

## Verify completion

- No client-embedded secret is treated as confidential.
- Concurrent refreshes cannot corrupt the accepted session.
- Logout removes local session access and handles pending authenticated work.

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
