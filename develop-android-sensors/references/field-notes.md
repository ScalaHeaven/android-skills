# Develop Android sensor pipelines: field notes

## Decision boundaries

| Situation | Action |
| --- | --- |
| Public platform API | Verify permissions, runtime support and delivered behavior on target hardware. |
| Google service or optional runtime | Check availability and model/device compatibility, then define a fallback if supported. |
| Privileged/internal capability | Do not present it as ordinary app access; identify authorization and distribution constraints before proposing it. |

## Practice task

Feed accelerometer and gyroscope samples into a Rust navigation estimator.

Before changing code, write the observable expected result and identify the component owning
state, resources and failure recovery. Inspect the smallest complete path that can explain the
task; avoid a repository-wide rewrite. Use the workflow in SKILL.md to choose the actual fix.

## Build a verification plan

1. Capture the original condition with a minimal fixture, screen state or device scenario.
2. Check the following domain-specific acceptance boundaries:
- SensorEvent arrays are not retained as immutable snapshots without copying.
- Requested sampling rate is not treated as guaranteed delivered rate.
- Coordinate conversions and timestamp synchronization have numerical checks.
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

- [Primary reference 1](https://developer.android.com/develop/sensors-and-location/sensors/sensors_overview)
- [Primary reference 2](https://developer.android.com/develop/sensors-and-location/sensors/sensors_motion)

Treat these as entry points, not frozen API guarantees. Follow the documentation for the project's
actual versions and record retrieval dates for volatile restrictions or distribution policies.
