---
name: develop-android-coroutines
description: "Implement lifecycle-aware Android coroutine work with structured concurrency. Use for blocking UI, leaked jobs, cancellation or dispatcher problems."
---

# Develop Android coroutines

## Establish the contract

Read repository instructions and the existing implementation first. Read state holders, coroutine scopes, dispatchers, listener adapters and resource owners.
Record the requested outcome, current behavior and constraints. Inspect minSdk, targetSdk,
compileSdk and installed library/toolchain versions where they affect the task. Verify volatile
API restrictions, compatibility tables and release policies in current primary documentation.
Preserve the project's chosen stack unless a concrete limitation warrants changing it.

## Execute the workflow

1. Identify the operation owner and whether work should survive the screen, app backgrounding or process termination.
2. Inject dispatchers at I/O boundaries and keep suspend APIs main-safe; never assume suspend makes blocking work safe.
3. Use child jobs under deliberate scopes; distinguish failure propagation from independent supervised operations.
4. Preserve CancellationException and ensure callback adapters unregister and resume at most once.
5. Test cancellation during I/O, screen removal and partial completion; release resources in finally blocks.

## Verify completion

- No unowned GlobalScope or arbitrary application job solves a screen-lifetime problem.
- Blocking CPU/I/O work runs on an appropriate dispatcher.
- Cancellation releases resources and does not become a displayed business error.

Run the relevant JVM test task using injected dispatchers. Add lifecycle/device checks only for the platform behavior the change actually depends on.
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
