# Develop Android location features: field notes

## Decision boundaries

| Situation | Action |
| --- | --- |
| Public platform API | Verify permissions, runtime support and delivered behavior on target hardware. |
| Google service or optional runtime | Check availability and model/device compatibility, then define a fallback if supported. |
| Privileged/internal capability | Do not present it as ordinary app access; identify authorization and distribution constraints before proposing it. |

## Practice task

Prevent a stale last-known location from starting a trip at the wrong point.

Before changing code, write the observable expected result and identify the component owning
state, resources and failure recovery. Inspect the smallest complete path that can explain the
task; avoid a repository-wide rewrite. Use the workflow in SKILL.md to choose the actual fix.

## Build a verification plan

1. Capture the original condition with a minimal fixture, screen state or device scenario.
2. Check the following domain-specific acceptance boundaries:
- Network-derived location is not described as a guaranteed direct cell-tower coordinate API.
- Missing Play services or GNSS has a defined fallback where supported.
- Accuracy and freshness are not inferred merely from receiving a callback.
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

- [Primary reference 1](https://developer.android.com/develop/sensors-and-location/location)
- [Primary reference 2](https://developers.google.com/location-context/fused-location-provider)

Treat these as entry points, not frozen API guarantees. Follow the documentation for the project's
actual versions and record retrieval dates for volatile restrictions or distribution policies.
