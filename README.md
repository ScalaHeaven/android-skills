# Android development skills — 84

Набір містить усі 84 запропоновані скіли у 12 напрямах. Інструкції скілів написані
англійською для використання агентами; цей опис і каталог напрямів — українською.

## Склад

- 84 окремі каталоги з SKILL.md, YAML-метаданими та agents/openai.yaml.
- 84 предметні довідкові ресурси references/field-notes.md.
- 7 допоміжних Python-скриптів зі стандартною бібліотекою.
- Каталог, результати структурної перевірки та 17 перевірок скриптів у _bundle/.
- Три практичні перевірки скілів із чесно зазначеними межами середовища.

## Встановлення в Codex

Розпакуйте архів. Скопіюйте потрібні каталоги скілів безпосередньо до каталогу
skills у вашому CODEX_HOME, якщо його задано. Типовий шлях:

- Linux/macOS: ~/.codex/skills/<skill-name>/SKILL.md
- Windows: %USERPROFILE%\.codex\skills\<skill-name>\SKILL.md

Збережіть agents/, references/ і scripts/ поряд із SKILL.md. Не додавайте ще один
рівень каталогу навколо скіла. Якщо таке ім'я вже існує, порівняйте версії перед
заміною. Каталог _bundle та цей опис не є скілами й встановлення не потребують.
Оновіть сесію Codex після встановлення. Викликайте скіл як $develop-jetpack-compose
або за відповідною задачею. Скіли автономні й не залежать від інших скілів набору.

## Перевірка розпакованого архіву

Потрібен Python 3.10 або новіший:

```bash
python3 _bundle/verify_bundle.py
python3 _bundle/test_helpers.py
```

На Windows використайте python або py -3 замість python3. Перевірка хешів
виявляє відсутні або змінені файли, але не є підтвердженням авторства архіву.
Скрипти скілів читають локальні дані; вони не запускають Gradle, не керують
пристроями й не публікують застосунки.

## Межі перевірки

Структура та локальні посилання перевірені для всіх 84 скілів. Сім скриптів
перевірені на 17 синтетичних сценаріях із коректними й некоректними даними.
Практичні приклади не є повним Android-проєктом. Android-збірки, UI-тести та
перевірки на фізичних пристроях для них не виконувалися. Підтримку конкретного
Android API та актуальні правила магазинів потрібно звіряти під час застосування.

## Каталог

### 1. Архітектура та проєктування

- `design-android-architecture` — Design Android architecture.
- `design-android-state-management` — Design Android state management.
- `develop-android-dependency-injection` — Develop Android dependency injection.
- `document-android-architecture` — Document Android architecture.
- `modularize-android-project` — Modularize an Android project.
- `plan-android-application` — Plan an Android application.
- `review-android-architecture` — Review Android architecture.

### 2. Kotlin, coroutines і lifecycle

- `audit-android-lifecycle` — Audit Android lifecycle ownership.
- `develop-android-coroutines` — Develop Android coroutines.
- `develop-android-flow` — Develop Android Flow.
- `handle-android-process-death` — Handle Android process death.
- `refactor-android-code` — Refactor Android code.
- `review-android-kotlin` — Review Kotlin for Android.
- `validate-android-concurrency` — Validate Android concurrency.

### 3. Compose та інтерфейс

- `develop-android-animation` — Develop Android animations.
- `develop-android-design-system` — Develop an Android design system.
- `develop-android-forms` — Develop Android forms.
- `develop-android-navigation` — Develop Android navigation.
- `develop-compose-lists-paging` — Develop Compose lists and paging.
- `develop-jetpack-compose` — Develop Jetpack Compose screens.
- `review-compose-correctness` — Review Compose correctness.

### 4. Адаптивність і доступність

- `audit-android-accessibility` — Audit Android accessibility.
- `audit-android-window-insets` — Audit Android window insets.
- `develop-adaptive-android-ui` — Develop adaptive Android UI.
- `develop-android-views` — Develop Android Views.
- `localize-android-application` — Localize an Android application.
- `migrate-views-to-compose` — Migrate Views to Compose.
- `test-android-ui-configurations` — Test Android UI configurations.

### 5. Дані та мережа

- `design-android-offline-first` — Design offline-first Android data.
- `develop-android-data-sync` — Develop Android data synchronization.
- `develop-android-datastore` — Develop Android DataStore.
- `develop-android-file-storage` — Develop Android file storage.
- `develop-android-networking` — Develop Android networking.
- `develop-android-realtime-networking` — Develop Android realtime networking.
- `develop-android-room` — Develop Android Room storage.

### 6. Фонова робота й інтеграція

- `choose-android-background-api` — Choose Android background APIs.
- `develop-android-alarms` — Develop Android alarms.
- `develop-android-app-links` — Develop Android App Links.
- `develop-android-foreground-services` — Develop Android foreground services.
- `develop-android-ipc` — Develop Android IPC.
- `develop-android-notifications` — Develop Android notifications.
- `develop-android-workmanager` — Develop Android WorkManager jobs.

### 7. Тестування

- `debug-android-flaky-tests` — Debug flaky Android tests.
- `design-android-test-strategy` — Design Android test strategy.
- `test-android-compose-ui` — Test Android Compose UI.
- `test-android-coroutines-flow` — Test Android coroutines and Flow.
- `test-android-data-layer` — Test Android data layers.
- `test-android-device-scenarios` — Test Android device scenarios.
- `test-android-unit` — Test Android units and ViewModels.

### 8. Продуктивність і ресурси

- `audit-android-memory` — Audit Android memory.
- `benchmark-android-application` — Benchmark an Android application.
- `develop-android-baseline-profiles` — Develop Android Baseline Profiles.
- `optimize-android-battery` — Optimize Android battery use.
- `optimize-android-startup` — Optimize Android startup.
- `optimize-compose-performance` — Optimize Compose performance.
- `profile-android-performance` — Profile Android performance.

### 9. Безпека та приватність

- `audit-android-components` — Audit Android exported components.
- `audit-android-data-security` — Audit Android data security.
- `audit-android-network-security` — Audit Android network security.
- `audit-android-permissions` — Audit Android permissions.
- `audit-android-privacy` — Audit Android privacy.
- `develop-android-authentication` — Develop Android authentication.
- `threat-model-android-app` — Threat-model an Android app.

### 10. Збірка, CI та реліз

- `audit-android-release-build` — Audit Android release builds.
- `develop-android-gradle-build` — Develop Android Gradle builds.
- `maintain-android-ci` — Maintain Android continuous integration.
- `maintain-android-dependencies` — Maintain Android dependencies.
- `maintain-android-static-analysis` — Maintain Android static analysis.
- `optimize-android-build` — Optimize Android builds.
- `release-android-application` — Release an Android application.

### 11. Сумісність та експлуатація

- `audit-android-api-compatibility` — Audit Android API compatibility.
- `debug-android-crashes-anrs` — Debug Android crashes and ANRs.
- `design-android-resilience` — Design Android resilience.
- `develop-android-observability` — Develop Android observability.
- `migrate-android-target-sdk` — Migrate Android target SDK.
- `triage-android-production-issues` — Triage Android production issues.
- `validate-android-device-compatibility` — Validate Android device compatibility.

### 12. Апаратні й спеціалізовані API

- `develop-android-audio-media` — Develop Android audio and media.
- `develop-android-camera` — Develop Android CameraX features.
- `develop-android-connectivity` — Develop Android device connectivity.
- `develop-android-location` — Develop Android location features.
- `develop-android-native-rust` — Develop Android native Rust integration.
- `develop-android-on-device-ml` — Develop Android on-device ML.
- `develop-android-sensors` — Develop Android sensor pipelines.
