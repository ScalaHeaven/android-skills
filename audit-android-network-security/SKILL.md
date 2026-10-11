---
name: audit-android-network-security
description: "Audit Android TLS, cleartext, WebView and network security configuration. Use for unsafe transport or untrusted embedded content."
---

# Audit Android network security

## Establish the contract

Read repository instructions and the existing implementation first. Read exported interfaces, trust boundaries, credentials, sensitive data and release manifest/network configuration.
Record the requested outcome, current behavior and constraints. Inspect minSdk, targetSdk,
compileSdk and installed library/toolchain versions where they affect the task. Verify volatile
API restrictions, compatibility tables and release policies in current primary documentation.
Preserve the project's chosen stack unless a concrete limitation warrants changing it.

## Execute the workflow

1. Inventory endpoints, trust configuration, debug overrides and WebView origins.
2. Verify certificate/hostname validation and prevent permissive trust managers from reaching release builds.
3. Restrict cleartext and WebView capabilities to required behavior; inspect file access, JavaScript bridges and mixed content.
4. Evaluate pinning only with a rotation/recovery threat-model rationale rather than assuming it is universally beneficial.
5. Test rejected certificates and hostile navigation in a controlled environment.

## Verify completion

- Debug trust exceptions cannot bypass release verification.
- Web content cannot call privileged app bridges without appropriate origin/trust constraints.
- Security findings include a reachable misuse path and practical fix.

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
