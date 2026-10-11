# Release an Android application: field notes

## Decision boundaries

| Situation | Action |
| --- | --- |
| Toolchain upgrade | Verify version compatibility and migration notes before selecting a version. |
| Release-only failure | Test the actual shrunk/signed variant and retain mapping/native symbols. |
| Distribution action | Prepare reviewable artifacts; publish only when the user has authorized that external action. |

## Practice task

Prepare a signed trip-recorder release for an internal test track.

Before changing code, write the observable expected result and identify the component owning
state, resources and failure recovery. Inspect the smallest complete path that can explain the
task; avoid a repository-wide rewrite. Use the workflow in SKILL.md to choose the actual fix.

## Build a verification plan

1. Capture the original condition with a minimal fixture, screen state or device scenario.
2. Check the following domain-specific acceptance boundaries:
- Signing keys are never embedded in the distributable skill or diagnostics.
- Target-SDK and policy dates are verified at release time.
- Halting rollout is distinguished from reverting already installed application versions.
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

- [Primary reference 1](https://developer.android.com/studio/publish)
- [Primary reference 2](https://support.google.com/googleplay/android-developer/)

Treat these as entry points, not frozen API guarantees. Follow the documentation for the project's
actual versions and record retrieval dates for volatile restrictions or distribution policies.
