# Develop Android Baseline Profiles: field notes

## Decision boundaries

| Situation | Action |
| --- | --- |
| Hot-path isolated cost | Use a controlled microbenchmark and exclude unrelated setup. |
| User journey latency | Use end-to-end measurement with realistic data and release behavior. |
| Memory or power claim | Use the relevant measurement tool and repeated workload; do not infer it from elapsed time alone. |

## Practice task

Generate a profile for launch, opening a trip and starting a recording.

Before changing code, write the observable expected result and identify the component owning
state, resources and failure recovery. Inspect the smallest complete path that can explain the
task; avoid a repository-wide rewrite. Use the workflow in SKILL.md to choose the actual fix.

## Build a verification plan

1. Capture the original condition with a minimal fixture, screen state or device scenario.
2. Check the following domain-specific acceptance boundaries:
- Debug-only or uninstalled profiles are not credited with release improvements.
- Measurements distinguish profile effects from warm caches.
- Generated journeys exercise useful code rather than only opening the launcher.
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

- [Primary reference 1](https://developer.android.com/topic/performance/baselineprofiles)
- [Primary reference 2](https://developer.android.com/topic/performance/baselineprofiles/measure-baselineprofile)

Treat these as entry points, not frozen API guarantees. Follow the documentation for the project's
actual versions and record retrieval dates for volatile restrictions or distribution policies.
