# Develop Android Room storage: field notes

## Decision boundaries

| Situation | Action |
| --- | --- |
| Remote write retried | Require a defined idempotency contract or expose uncertain completion. |
| Locally accepted edit | Persist enough state to recover after restart and represent sync status explicitly. |
| Large external file | Use bounded streaming and provider handles; do not assume a content URI is a local path. |

## Practice task

Add altitude samples to an installed trip database while preserving existing trips.

Before changing code, write the observable expected result and identify the component owning
state, resources and failure recovery. Inspect the smallest complete path that can explain the
task; avoid a repository-wide rewrite. Use the workflow in SKILL.md to choose the actual fix.

## Build a verification plan

1. Capture the original condition with a minimal fixture, screen state or device scenario.
2. Check the following domain-specific acceptance boundaries:
- Queries handle empty, duplicate and boundary data correctly.
- Migration tests verify content preservation, not just database opening.
- Large results use bounded loading rather than unbounded entity materialization.
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

- [Primary reference 1](https://developer.android.com/training/data-storage/room)
- [Primary reference 2](https://developer.android.com/training/data-storage/room/migrating-db)

Treat these as entry points, not frozen API guarantees. Follow the documentation for the project's
actual versions and record retrieval dates for volatile restrictions or distribution policies.

## Helper input and interpretation

Use exported Room schema files with database.entities. Structural differences are hints; execute populated migration tests to verify correctness.

Use `python3 scripts/compare_schemas.py --help` for exact positional inputs. Invalid input is an error; an inventory without findings is not proof of runtime correctness.
