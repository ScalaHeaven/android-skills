# Develop Android authentication: field notes

## Decision boundaries

| Situation | Action |
| --- | --- |
| Untrusted local caller | Validate identity and authorization at the exposed endpoint. |
| Remote content | Limit privileges and validate protocol/origin assumptions. |
| Sensitive diagnostics | Minimize and redact data before collection; keep security tests within the authorized target. |

## Practice task

Add passkey login with an existing backend and safe account switching.

Before changing code, write the observable expected result and identify the component owning
state, resources and failure recovery. Inspect the smallest complete path that can explain the
task; avoid a repository-wide rewrite. Use the workflow in SKILL.md to choose the actual fix.

## Build a verification plan

1. Capture the original condition with a minimal fixture, screen state or device scenario.
2. Check the following domain-specific acceptance boundaries:
- No client-embedded secret is treated as confidential.
- Concurrent refreshes cannot corrupt the accepted session.
- Logout removes local session access and handles pending authenticated work.
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

- [Primary reference 1](https://developer.android.com/identity/sign-in/credential-manager)
- [Primary reference 2](https://www.rfc-editor.org/rfc/rfc8252)

Treat these as entry points, not frozen API guarantees. Follow the documentation for the project's
actual versions and record retrieval dates for volatile restrictions or distribution policies.
