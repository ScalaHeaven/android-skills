---
name: threat-model-android-app
description: "Model Android assets, attackers, trust boundaries and abuse cases. Use for sensitive apps, new integrations or security architecture reviews."
---

# Threat-model an Android app

## Establish the contract

Read repository instructions and the existing implementation first. Read exported interfaces, trust boundaries, credentials, sensitive data and release manifest/network configuration.
Record the requested outcome, current behavior and constraints. Inspect minSdk, targetSdk,
compileSdk and installed library/toolchain versions where they affect the task. Verify volatile
API restrictions, compatibility tables and release policies in current primary documentation.
Preserve the project's chosen stack unless a concrete limitation warrants changing it.

## Execute the workflow

1. Inventory sensitive records, credentials, hardware access and exported entry points.
2. Define realistic attacker capabilities including another local app, hostile network, compromised account and device access.
3. Trace data across app, OS, SDK and backend boundaries and list concrete misuse cases.
4. Prioritize mitigations by impact and feasibility; distinguish local controls from server authorization.
5. Produce a bounded risk register with verification evidence and residual assumptions.

## Verify completion

- Threats are tied to actual assets and reachable interfaces.
- Rooted-device resistance is not confused with normal app sandbox guarantees.
- Integrity signals do not replace authorization or fraud analysis.

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
