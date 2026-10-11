# Android development skills — 84

This collection contains all 84 proposed skills across 12 categories. The skill
instructions, this overview and the category catalog are written in English.

## Contents

- 84 separate directories with SKILL.md, YAML metadata and agents/openai.yaml.
- 84 domain-specific reference files at references/field-notes.md.
- 7 helper Python scripts using the standard library.
- A catalog, structural validation results and 17 script checks in _bundle/.
- Three practical skill checks with explicitly stated environment limitations.

## Installation in Codex

Extract the archive. Copy the desired skill directories directly into the skills
directory under CODEX_HOME, if set. The default paths are:

- Linux/macOS: ~/.codex/skills/<skill-name>/SKILL.md
- Windows: %USERPROFILE%\.codex\skills\<skill-name>\SKILL.md

Keep agents/, references/ and scripts/ alongside SKILL.md. Do not add an extra
directory level around a skill. If a skill with the same name already exists,
compare versions before replacing it. The _bundle directory and this overview
are not skills and do not need to be installed.
Refresh your Codex session after installation. Invoke a skill by name, such as
$develop-jetpack-compose, or through a relevant task. Each skill is standalone
and does not depend on other skills in this collection.

## Verifying the extracted archive

Python 3.10 or later is required:

```bash
python3 _bundle/verify_bundle.py
python3 _bundle/test_helpers.py
```

On Windows, use python or py -3 instead of python3. Hash verification detects
missing or modified files but does not authenticate the archive's authorship.
The skill scripts read local data; they do not run Gradle, control devices or
publish applications.

## Validation limits

Structure and local links have been checked for all 84 skills. The seven scripts
have been checked against 17 synthetic scenarios with valid and invalid data.
The practical examples do not constitute a complete Android project. Android
builds, UI tests and physical-device checks have not been run for these examples.
Verify support for specific Android APIs and current app store policies when
using the skills.

## Catalog

### 1. Architecture and design

- `design-android-architecture` — Design Android architecture.
- `design-android-state-management` — Design Android state management.
- `develop-android-dependency-injection` — Develop Android dependency injection.
- `document-android-architecture` — Document Android architecture.
- `modularize-android-project` — Modularize an Android project.
- `plan-android-application` — Plan an Android application.
- `review-android-architecture` — Review Android architecture.

### 2. Kotlin, coroutines and lifecycle

- `audit-android-lifecycle` — Audit Android lifecycle ownership.
- `develop-android-coroutines` — Develop Android coroutines.
- `develop-android-flow` — Develop Android Flow.
- `handle-android-process-death` — Handle Android process death.
- `refactor-android-code` — Refactor Android code.
- `review-android-kotlin` — Review Kotlin for Android.
- `validate-android-concurrency` — Validate Android concurrency.

### 3. Compose and UI

- `develop-android-animation` — Develop Android animations.
- `develop-android-design-system` — Develop an Android design system.
- `develop-android-forms` — Develop Android forms.
- `develop-android-navigation` — Develop Android navigation.
- `develop-compose-lists-paging` — Develop Compose lists and paging.
- `develop-jetpack-compose` — Develop Jetpack Compose screens.
- `review-compose-correctness` — Review Compose correctness.

### 4. Adaptivity and accessibility

- `audit-android-accessibility` — Audit Android accessibility.
- `audit-android-window-insets` — Audit Android window insets.
- `develop-adaptive-android-ui` — Develop adaptive Android UI.
- `develop-android-views` — Develop Android Views.
- `localize-android-application` — Localize an Android application.
- `migrate-views-to-compose` — Migrate Views to Compose.
- `test-android-ui-configurations` — Test Android UI configurations.

### 5. Data and networking

- `design-android-offline-first` — Design offline-first Android data.
- `develop-android-data-sync` — Develop Android data synchronization.
- `develop-android-datastore` — Develop Android DataStore.
- `develop-android-file-storage` — Develop Android file storage.
- `develop-android-networking` — Develop Android networking.
- `develop-android-realtime-networking` — Develop Android realtime networking.
- `develop-android-room` — Develop Android Room storage.

### 6. Background work and integration

- `choose-android-background-api` — Choose Android background APIs.
- `develop-android-alarms` — Develop Android alarms.
- `develop-android-app-links` — Develop Android App Links.
- `develop-android-foreground-services` — Develop Android foreground services.
- `develop-android-ipc` — Develop Android IPC.
- `develop-android-notifications` — Develop Android notifications.
- `develop-android-workmanager` — Develop Android WorkManager jobs.

### 7. Testing

- `debug-android-flaky-tests` — Debug flaky Android tests.
- `design-android-test-strategy` — Design Android test strategy.
- `test-android-compose-ui` — Test Android Compose UI.
- `test-android-coroutines-flow` — Test Android coroutines and Flow.
- `test-android-data-layer` — Test Android data layers.
- `test-android-device-scenarios` — Test Android device scenarios.
- `test-android-unit` — Test Android units and ViewModels.

### 8. Performance and resources

- `audit-android-memory` — Audit Android memory.
- `benchmark-android-application` — Benchmark an Android application.
- `develop-android-baseline-profiles` — Develop Android Baseline Profiles.
- `optimize-android-battery` — Optimize Android battery use.
- `optimize-android-startup` — Optimize Android startup.
- `optimize-compose-performance` — Optimize Compose performance.
- `profile-android-performance` — Profile Android performance.

### 9. Security and privacy

- `audit-android-components` — Audit Android exported components.
- `audit-android-data-security` — Audit Android data security.
- `audit-android-network-security` — Audit Android network security.
- `audit-android-permissions` — Audit Android permissions.
- `audit-android-privacy` — Audit Android privacy.
- `develop-android-authentication` — Develop Android authentication.
- `threat-model-android-app` — Threat-model an Android app.

### 10. Builds, CI and releases

- `audit-android-release-build` — Audit Android release builds.
- `develop-android-gradle-build` — Develop Android Gradle builds.
- `maintain-android-ci` — Maintain Android continuous integration.
- `maintain-android-dependencies` — Maintain Android dependencies.
- `maintain-android-static-analysis` — Maintain Android static analysis.
- `optimize-android-build` — Optimize Android builds.
- `release-android-application` — Release an Android application.

### 11. Compatibility and operations

- `audit-android-api-compatibility` — Audit Android API compatibility.
- `debug-android-crashes-anrs` — Debug Android crashes and ANRs.
- `design-android-resilience` — Design Android resilience.
- `develop-android-observability` — Develop Android observability.
- `migrate-android-target-sdk` — Migrate Android target SDK.
- `triage-android-production-issues` — Triage Android production issues.
- `validate-android-device-compatibility` — Validate Android device compatibility.

### 12. Hardware and specialized APIs

- `develop-android-audio-media` — Develop Android audio and media.
- `develop-android-camera` — Develop Android CameraX features.
- `develop-android-connectivity` — Develop Android device connectivity.
- `develop-android-location` — Develop Android location features.
- `develop-android-native-rust` — Develop Android native Rust integration.
- `develop-android-on-device-ml` — Develop Android on-device ML.
- `develop-android-sensors` — Develop Android sensor pipelines.
