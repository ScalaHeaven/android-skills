# Develop Android Gradle builds: field notes

## Decision boundaries

| Situation | Action |
| --- | --- |
| Toolchain upgrade | Verify version compatibility and migration notes before selecting a version. |
| Release-only failure | Test the actual shrunk/signed variant and retain mapping/native symbols. |
| Distribution action | Prepare reviewable artifacts; publish only when the user has authorized that external action. |

## Practice task

Add a staging flavor with a separate endpoint and application ID.

Before changing code, write the observable expected result and identify the component owning
state, resources and failure recovery. Inspect the smallest complete path that can explain the
task; avoid a repository-wide rewrite. Use the workflow in SKILL.md to choose the actual fix.

## Build a verification plan

1. Capture the original condition with a minimal fixture, screen state or device scenario.
2. Check the following domain-specific acceptance boundaries:
- Dependencies are pinned or locked according to project policy.
- Signing material and local machine paths are not committed.
- Variant behavior is demonstrated through generated outputs or builds.
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

- [Primary reference 1](https://developer.android.com/build)
- [Primary reference 2](https://developer.android.com/build/build-variants)

Treat these as entry points, not frozen API guarantees. Follow the documentation for the project's
actual versions and record retrieval dates for volatile restrictions or distribution policies.

## Helper input and interpretation

Read build-file paths and literal SDK hints without executing Gradle. Resolve variables and convention plugins separately.

Use `python3 scripts/project_inventory.py --help` for exact positional inputs. Invalid input is an error; an inventory without findings is not proof of runtime correctness.
