---
name: develop-android-app-links
description: "Implement verified App Links, deep links and intent entry points. Use for shared URLs, external navigation and link verification failures."
---

# Develop Android App Links

## Establish the contract

Read repository instructions and the existing implementation first. Read the merged manifest, task entry points, permissions and the current OS/target-SDK execution restrictions.
Record the requested outcome, current behavior and constraints. Inspect minSdk, targetSdk,
compileSdk and installed library/toolchain versions where they affect the task. Verify volatile
API restrictions, compatibility tables and release policies in current primary documentation.
Preserve the project's chosen stack unless a concrete limitation warrants changing it.

## Execute the workflow

1. Define accepted hosts, schemes, paths and validated argument formats.
2. Configure manifest filters and domain association for the actual signing certificates and variants.
3. Route external input through authentication and authorization checks before displaying protected content.
4. Provide useful back-stack and invalid-link behavior; avoid unsafe broad URI or intent forwarding.
5. Verify links on relevant OS versions and test malformed, unverified, signed-out and duplicate entry cases.

## Verify completion

- App-link verification uses release or appropriate test certificate fingerprints.
- Untrusted URL parameters do not authorize access.
- Unknown or malformed links fail safely without crashing.

Use a specified adb device serial for device commands. Separate process termination, user force-stop, reboot and battery restrictions; they have different execution semantics.
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
