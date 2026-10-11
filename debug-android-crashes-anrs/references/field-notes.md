# Debug Android crashes and ANRs: field notes

## Decision boundaries

| Situation | Action |
| --- | --- |
| API not present | Guard access and define a supported fallback rather than catching arbitrary exceptions. |
| Vendor-only failure | Record model and system build and reproduce the relevant power/resource behavior. |
| Production report | Match artifact and symbols first; keep hypotheses separate from confirmed causes. |

## Practice task

Diagnose an ANR while stopping a recorder that waits for native worker shutdown.

Before changing code, write the observable expected result and identify the component owning
state, resources and failure recovery. Inspect the smallest complete path that can explain the
task; avoid a repository-wide rewrite. Use the workflow in SKILL.md to choose the actual fix.

## Build a verification plan

1. Capture the original condition with a minimal fixture, screen state or device scenario.
2. Check the following domain-specific acceptance boundaries:
- Missing symbols or mappings are acknowledged before drawing precise conclusions.
- ANRs are not all attributed to long computation; waiting and deadlocks are considered.
- A null guard does not hide violated required invariants.
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

- [Primary reference 1](https://developer.android.com/topic/performance/vitals/anr)
- [Primary reference 2](https://developer.android.com/ndk/guides/debug)

Treat these as entry points, not frozen API guarantees. Follow the documentation for the project's
actual versions and record retrieval dates for volatile restrictions or distribution policies.
