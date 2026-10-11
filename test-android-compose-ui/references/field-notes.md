# Test Android Compose UI: field notes

## Decision boundaries

| Situation | Action |
| --- | --- |
| Pure transformation | Use deterministic local tests and boundary values. |
| Framework behavior | Use instrumentation on relevant runtime boundaries; a fake is insufficient proof. |
| Hardware quality | Use target physical devices and preserve raw fixture/evaluation conditions. |

## Practice task

Test that a failed form submission retains text and displays a retryable error.

Before changing code, write the observable expected result and identify the component owning
state, resources and failure recovery. Inspect the smallest complete path that can explain the
task; avoid a repository-wide rewrite. Use the workflow in SKILL.md to choose the actual fix.

## Build a verification plan

1. Capture the original condition with a minimal fixture, screen state or device scenario.
2. Check the following domain-specific acceptance boundaries:
- Tests assert behavior rather than the exact number of internal recompositions.
- Semantics reflect real accessibility where possible.
- External asynchronous work has an explicit synchronization mechanism.
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

- [Primary reference 1](https://developer.android.com/develop/ui/compose/testing)
- [Primary reference 2](https://developer.android.com/develop/ui/compose/testing/synchronization)

Treat these as entry points, not frozen API guarantees. Follow the documentation for the project's
actual versions and record retrieval dates for volatile restrictions or distribution policies.
