# Debug flaky Android tests: field notes

## Decision boundaries

| Situation | Action |
| --- | --- |
| Pure transformation | Use deterministic local tests and boundary values. |
| Framework behavior | Use instrumentation on relevant runtime boundaries; a fake is insufficient proof. |
| Hardware quality | Use target physical devices and preserve raw fixture/evaluation conditions. |

## Practice task

Fix a Compose test that intermittently taps a loading screen before data arrives.

Before changing code, write the observable expected result and identify the component owning
state, resources and failure recovery. Inspect the smallest complete path that can explain the
task; avoid a repository-wide rewrite. Use the workflow in SKILL.md to choose the actual fix.

## Build a verification plan

1. Capture the original condition with a minimal fixture, screen state or device scenario.
2. Check the following domain-specific acceptance boundaries:
- Retries do not become the sole fix.
- Root-cause evidence distinguishes app defects from test infrastructure failures.
- XML reports preserve failed, skipped and errored cases separately.
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

- [Primary reference 1](https://developer.android.com/develop/ui/compose/testing/synchronization)
- [Primary reference 2](https://developer.android.com/training/testing/espresso/idling-resource)

Treat these as entry points, not frozen API guarantees. Follow the documentation for the project's
actual versions and record retrieval dates for volatile restrictions or distribution policies.

## Helper input and interpretation

Provide one or more JUnit report files or directories. Exit 1 indicates failures/errors; exit 2 indicates missing cases or invalid input reports. Repeated executions count separately.

Use `python3 scripts/summarize_test_reports.py --help` for exact positional inputs. Invalid input is an error; an inventory without findings is not proof of runtime correctness.
