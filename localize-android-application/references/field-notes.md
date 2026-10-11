# Localize an Android application: field notes

## Decision boundaries

| Situation | Action |
| --- | --- |
| Window changes live | Preserve the task and selected content while changing presentation. |
| Large font or long translation | Allow content growth and scrolling; avoid fixed text-height assumptions. |
| Assistive input | Expose role, state, name and actions; verify focus and traversal with the service. |

## Practice task

Add English trip statistics with correct plural forms and timestamps.

Before changing code, write the observable expected result and identify the component owning
state, resources and failure recovery. Inspect the smallest complete path that can explain the
task; avoid a repository-wide rewrite. Use the workflow in SKILL.md to choose the actual fix.

## Build a verification plan

1. Capture the original condition with a minimal fixture, screen state or device scenario.
2. Check the following domain-specific acceptance boundaries:
- Translation placeholders match their argument types and order.
- No sentence is assembled from independently translated fragments.
- Layout and accessibility labels work in long-text and RTL configurations.
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

- [Primary reference 1](https://developer.android.com/guide/topics/resources/localization)
- [Primary reference 2](https://developer.android.com/guide/topics/resources/pseudolocales)

Treat these as entry points, not frozen API guarantees. Follow the documentation for the project's
actual versions and record retrieval dates for volatile restrictions or distribution policies.
