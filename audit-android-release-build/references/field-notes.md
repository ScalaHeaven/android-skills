# Audit Android release builds: field notes

## Decision boundaries

| Situation | Action |
| --- | --- |
| Toolchain upgrade | Verify version compatibility and migration notes before selecting a version. |
| Release-only failure | Test the actual shrunk/signed variant and retain mapping/native symbols. |
| Distribution action | Prepare reviewable artifacts; publish only when the user has authorized that external action. |

## Practice task

Diagnose a Rust JNI method that disappears only in a minified release build.

Before changing code, write the observable expected result and identify the component owning
state, resources and failure recovery. Inspect the smallest complete path that can explain the
task; avoid a repository-wide rewrite. Use the workflow in SKILL.md to choose the actual fix.

## Build a verification plan

1. Capture the original condition with a minimal fixture, screen state or device scenario.
2. Check the following domain-specific acceptance boundaries:
- ZIP native inventory is not mistaken for ELF/page-alignment verification.
- Keep rules are minimal and justified by actual dynamic access.
- Debug and release differences are explicitly tested.
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

- [Primary reference 1](https://developer.android.com/topic/performance/app-optimization)
- [Primary reference 2](https://developer.android.com/guide/practices/page-sizes)

Treat these as entry points, not frozen API guarantees. Follow the documentation for the project's
actual versions and record retrieval dates for volatile restrictions or distribution policies.

## Helper input and interpretation

Accept APK or AAB ZIP containers. Read native ABI/library inventory without extracting files. Verify signatures, ELF page alignment and APK ZIP alignment separately with appropriate Android tooling.

Use `python3 scripts/inspect_apk.py --help` for exact positional inputs. Invalid input is an error; an inventory without findings is not proof of runtime correctness.
