# Modularize an Android project: field notes

## Decision boundaries

| Situation | Action |
| --- | --- |
| Small cohesive app | Use clear boundaries inside one module first; extract modules only for concrete isolation benefits. |
| Complex business rules | Consider an independently testable domain layer when complexity or reuse justifies it. |
| Unknown platform feasibility | Prototype the public API and permission path before treating the feature as deliverable. |

## Practice task

Extract trip storage from a single-module app without introducing circular feature dependencies.

Before changing code, write the observable expected result and identify the component owning
state, resources and failure recovery. Inspect the smallest complete path that can explain the
task; avoid a repository-wide rewrite. Use the workflow in SKILL.md to choose the actual fix.

## Build a verification plan

1. Capture the original condition with a minimal fixture, screen state or device scenario.
2. Check the following domain-specific acceptance boundaries:
- No dependency cycles or accidental feature-to-feature internals access remain.
- Resources, manifest merging and release variants still build.
- Module count is justified by actual isolation or build benefits.
3. Add an adverse case for interruption or unavailable inputs when the feature depends on them.
4. Check a supported successful path to ensure the repair does not disable the feature.
5. Record exact commands, device/runtime and artifacts. If a required environment is unavailable,
   provide an executable test plan and mark that outcome unverified.

## Evidence worksheet

| Field | Record |
| --- | --- |
| Contract | User action, initial state and expected observable result |
| Environment | Artifact/variant, toolchain, runtime, relevant device capability |
| Reproduction | Steps or fixture, expected result and actual result |
| Change | Responsibility modified and reason |
| Verification | Executed checks, reports and failures/skips |
| Limit | Untested conditions and next concrete validation |

## Primary documentation

- [Primary reference 1](https://developer.android.com/topic/modularization)
- [Primary reference 2](https://docs.gradle.org/current/userguide/multi_project_builds.html)

Treat these as entry points, not frozen API guarantees. Follow the documentation for the project's
actual versions and record retrieval dates for volatile restrictions or distribution policies.

## Helper input and interpretation

Provide an explicit adjacency object, for example {":app":[":data"],":data":[]}. Exit 1 reports cycles or referenced undeclared modules; exit 2 reports invalid input. Resolve variant-specific edges separately.

Use `python3 scripts/analyze_graph.py --help` for exact positional inputs. Invalid input is an error; an inventory without findings is not proof of runtime correctness.
