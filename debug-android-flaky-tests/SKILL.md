---
name: debug-android-flaky-tests
description: "Diagnose intermittent Android test failures without masking them. Use for CI-only failures, timing sensitivity and unstable UI tests."
---

# Debug flaky Android tests

## Establish the contract

Read repository instructions and the existing implementation first. Read existing tests, fixture ownership, environment setup and the contract the user scenario requires.
Record the requested outcome, current behavior and constraints. Inspect minSdk, targetSdk,
compileSdk and installed library/toolchain versions where they affect the task. Verify volatile
API restrictions, compatibility tables and release policies in current primary documentation.
Preserve the project's chosen stack unless a concrete limitation warrants changing it.

## Execute the workflow

1. Collect original failure, seed, device configuration, test order and artifacts.
2. Reproduce by isolating and then varying order, parallelism and resource pressure.
3. Inspect asynchronous work, shared state, uncontrolled time and leaked lifecycle resources.
4. Replace timing guesses with explicit synchronization and eliminate cross-test state contamination.
5. Rerun the relevant adverse condition and quantify the observation window; keep unexplained failures visible.

## Verify completion

- Retries do not become the sole fix.
- Root-cause evidence distinguishes app defects from test infrastructure failures.
- XML reports preserve failed, skipped and errored cases separately.

Run only meaningful affected checks, retain test XML and list skipped/unavailable cases. A passing local substitute does not establish behavior of an untested external system.
Choose tests that observe a real failure or acceptance condition; avoid tests that merely mirror
the implementation. Reproduce a reported regression before fixing it when feasible. State any
missing device, backend or signing environment instead of claiming unexecuted checks passed.

## Use the bundled reference

Read [field-notes.md](references/field-notes.md) for decision boundaries, a concrete task and
its verification plan. Use its primary-source links to resolve version-specific questions.
Keep this skill standalone; related installed skills are optional assistance, not prerequisites.

## Run the helper

Run `python3 scripts/summarize_test_reports.py REPORT_DIRECTORY_OR_XML` from this skill directory, replacing the input
placeholders with actual paths and quoting paths with spaces. On Windows use the available Python
launcher (`python` or `py -3`). The script uses the standard library, reads local inputs and does
not run Gradle, alter devices or contact services. Read its `--help` and the input notes below.

Provide one or more JUnit report files or directories. Exit 1 indicates failures/errors; exit 2 indicates missing cases or invalid input reports. Repeated executions count separately.

## Return evidence

Report the resulting behavior, changed artifacts and why the decision fits the contract.
Include executed checks and their actual outcomes, then any material unverified cases.
For reviews, give source locations, impact and a bounded repair. For plans, give acceptance
criteria and dependencies. For performance work, include measurement conditions and raw results.
Keep credentials and sensitive user data out of reports. Continue authorized implementation
and verification; do not add an approval step for routine reversible work.
