# Develop Android Flow: field notes

## Decision boundaries

| Situation | Action |
| --- | --- |
| Screen-owned operation | Tie cancellation to the actual owner and verify cleanup when the screen disappears. |
| Durable business action | Persist its intent or result; an in-memory coroutine scope cannot survive process death. |
| Callback adapter | Test late callbacks, cancellation during registration and exactly one cleanup operation. |

## Practice task

Expose location state to two screens while sharing a single upstream registration.

Before changing code, write the observable expected result and identify the component owning
state, resources and failure recovery. Inspect the smallest complete path that can explain the
task; avoid a repository-wide rewrite. Use the workflow in SKILL.md to choose the actual fix.

## Build a verification plan

1. Capture the original condition with a minimal fixture, screen state or device scenario.
2. Check the following domain-specific acceptance boundaries:
- State collectors obtain a coherent current state.
- Hot-flow event loss or replay behavior is documented and tested where material.
- Restarting collection does not accidentally register duplicate hardware listeners.
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

- [Primary reference 1](https://developer.android.com/kotlin/flow/stateflow-and-sharedflow)
- [Primary reference 2](https://kotlinlang.org/docs/flow.html)

Treat these as entry points, not frozen API guarantees. Follow the documentation for the project's
actual versions and record retrieval dates for volatile restrictions or distribution policies.
