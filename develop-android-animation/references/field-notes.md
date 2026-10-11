# Develop Android animations: field notes

## Decision boundaries

| Situation | Action |
| --- | --- |
| Pure rendering | Pass immutable visible state and action callbacks; keep external work out of composable execution. |
| Owned effect | Choose keys from semantic restart conditions and arrange disposal. |
| Restorable interaction | Save a small reconstruction value and reload durable data; do not serialize resource objects. |

## Practice task

Animate recording controls that can be rapidly started and stopped.

Before changing code, write the observable expected result and identify the component owning
state, resources and failure recovery. Inspect the smallest complete path that can explain the
task; avoid a repository-wide rewrite. Use the workflow in SKILL.md to choose the actual fix.

## Build a verification plan

1. Capture the original condition with a minimal fixture, screen state or device scenario.
2. Check the following domain-specific acceptance boundaries:
- Rapid toggles converge to the latest intended state.
- Animation does not delay essential validation or accessibility state updates.
- No unbounded coroutine or drawing allocation is introduced.
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

- [Primary reference 1](https://developer.android.com/develop/ui/compose/animation)
- [Primary reference 2](https://developer.android.com/develop/ui/compose/animation/choose-api)

Treat these as entry points, not frozen API guarantees. Follow the documentation for the project's
actual versions and record retrieval dates for volatile restrictions or distribution policies.
