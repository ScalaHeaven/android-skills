---
name: audit-android-components
description: "Audit Android activities, services, receivers, providers, intents and PendingIntents. Use for exported entry-point and cross-app security review."
---

# Audit Android exported components

## Establish the contract

Read repository instructions and the existing implementation first. Read exported interfaces, trust boundaries, credentials, sensitive data and release manifest/network configuration.
Record the requested outcome, current behavior and constraints. Inspect minSdk, targetSdk,
compileSdk and installed library/toolchain versions where they affect the task. Verify volatile
API restrictions, compatibility tables and release policies in current primary documentation.
Preserve the project's chosen stack unless a concrete limitation warrants changing it.

## Execute the workflow

1. Inspect source and merged release manifests, including library-added components.
2. Identify reachable inputs and protections for each exported endpoint.
3. Validate caller identity, URI grants, intent parameters and forwarding behavior at trust boundaries.
4. Review PendingIntent mutability, identity collisions and nested intent handling.
5. Demonstrate relevant access with a controlled test caller and verify fixed behavior.

## Verify completion

- Manifest scanner hints are confirmed against merged manifests and runtime behavior.
- An exported launcher is not automatically treated as a vulnerability.
- Provider access and temporary URI grants expose only intended data.

Use merged release configuration and controlled negative cases. Separate a scanner hint, confirmed reachable issue and hypothetical threat; do not label every exported component vulnerable.
Choose tests that observe a real failure or acceptance condition; avoid tests that merely mirror
the implementation. Reproduce a reported regression before fixing it when feasible. State any
missing device, backend or signing environment instead of claiming unexecuted checks passed.

## Use the bundled reference

Read [field-notes.md](references/field-notes.md) for decision boundaries, a concrete task and
its verification plan. Use its primary-source links to resolve version-specific questions.
Keep this skill standalone; related installed skills are optional assistance, not prerequisites.

## Run the helper

Run `python3 scripts/inspect_manifest.py MERGED_MANIFEST.xml` from this skill directory, replacing the input
placeholders with actual paths and quoting paths with spaces. On Windows use the available Python
launcher (`python` or `py -3`). The script uses the standard library, reads local inputs and does
not run Gradle, alter devices or contact services. Read its `--help` and the input notes below.

Use text XML from the merged release manifest. Binary APK manifests need Android tooling first. This inventories declarations; it does not infer exposure defaults or prove vulnerabilities.

## Return evidence

Report the resulting behavior, changed artifacts and why the decision fits the contract.
Include executed checks and their actual outcomes, then any material unverified cases.
For reviews, give source locations, impact and a bounded repair. For plans, give acceptance
criteria and dependencies. For performance work, include measurement conditions and raw results.
Keep credentials and sensitive user data out of reports. Continue authorized implementation
and verification; do not add an approval step for routine reversible work.
