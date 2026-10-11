---
name: modularize-android-project
description: "Define and implement Android Gradle module boundaries. Use for growing projects, dependency cycles, slow development builds or isolated feature delivery."
---

# Modularize an Android project

## Establish the contract

Read repository instructions and the existing implementation first. Read module build files, representative vertical slices, data contracts and existing architecture decisions.
Record the requested outcome, current behavior and constraints. Inspect minSdk, targetSdk,
compileSdk and installed library/toolchain versions where they affect the task. Verify volatile
API restrictions, compatibility tables and release policies in current primary documentation.
Preserve the project's chosen stack unless a concrete limitation warrants changing it.

## Execute the workflow

1. Inventory existing module dependencies, build timings and ownership; establish why modularization is needed.
2. Group code by cohesive responsibilities and change patterns, separating reusable infrastructure from features.
3. Define minimal public APIs and enforce an acyclic dependency direction; avoid a universal shared module.
4. Move a vertical slice including resources, tests and DI bindings; verify variant and namespace assumptions.
5. Measure affected build paths and document module rules before further extraction.

## Verify completion

- No dependency cycles or accidental feature-to-feature internals access remain.
- Resources, manifest merging and release variants still build.
- Module count is justified by actual isolation or build benefits.

Use the project Gradle wrapper to inspect projects and affected compilation tasks. Review dependency edges and trace at least one read and write end to end.
Choose tests that observe a real failure or acceptance condition; avoid tests that merely mirror
the implementation. Reproduce a reported regression before fixing it when feasible. State any
missing device, backend or signing environment instead of claiming unexecuted checks passed.

## Use the bundled reference

Read [field-notes.md](references/field-notes.md) for decision boundaries, a concrete task and
its verification plan. Use its primary-source links to resolve version-specific questions.
Keep this skill standalone; related installed skills are optional assistance, not prerequisites.

## Run the helper

Run `python3 scripts/analyze_graph.py MODULE_GRAPH.json` from this skill directory, replacing the input
placeholders with actual paths and quoting paths with spaces. On Windows use the available Python
launcher (`python` or `py -3`). The script uses the standard library, reads local inputs and does
not run Gradle, alter devices or contact services. Read its `--help` and the input notes below.

Provide an explicit adjacency object, for example {":app":[":data"],":data":[]}. Exit 1 reports cycles or referenced undeclared modules; exit 2 reports invalid input. Resolve variant-specific edges separately.

## Return evidence

Report the resulting behavior, changed artifacts and why the decision fits the contract.
Include executed checks and their actual outcomes, then any material unverified cases.
For reviews, give source locations, impact and a bounded repair. For plans, give acceptance
criteria and dependencies. For performance work, include measurement conditions and raw results.
Keep credentials and sensitive user data out of reports. Continue authorized implementation
and verification; do not add an approval step for routine reversible work.
