# Develop Android foreground services: field notes

## Decision boundaries

| Situation | Action |
| --- | --- |
| Deferrable durable operation | Evaluate persistent scheduling and restart-safe work. |
| User-visible ongoing task | Check service eligibility, type, launch path and user stop behavior. |
| Precise calendar reminder | Verify exactness is a real requirement, then check access and fallback semantics. |

## Practice task

Record a user-started trip with location while the screen is off.

Before changing code, write the observable expected result and identify the component owning
state, resources and failure recovery. Inspect the smallest complete path that can explain the
task; avoid a repository-wide rewrite. Use the workflow in SKILL.md to choose the actual fix.

## Build a verification plan

1. Capture the original condition with a minimal fixture, screen state or device scenario.
2. Check the following domain-specific acceptance boundaries:
- Denied permission or ineligible launch produces a recoverable UI outcome.
- Stopping releases sensor, audio, location and wake resources.
- Service presence is not claimed to guarantee immunity to process termination.
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

- [Primary reference 1](https://developer.android.com/develop/background-work/services/fgs)
- [Primary reference 2](https://developer.android.com/develop/background-work/services/fgs/changes)

Treat these as entry points, not frozen API guarantees. Follow the documentation for the project's
actual versions and record retrieval dates for volatile restrictions or distribution policies.
