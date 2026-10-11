---
name: develop-android-audio-media
description: "Implement Android recording, playback, audio focus and routing. Use for speech capture, media playback and interrupted audio sessions."
---

# Develop Android audio and media

## Establish the contract

Read repository instructions and the existing implementation first. Read actual hardware capabilities, units, timestamps, runtime support, ownership and device-level constraints.
Record the requested outcome, current behavior and constraints. Inspect minSdk, targetSdk,
compileSdk and installed library/toolchain versions where they affect the task. Verify volatile
API restrictions, compatibility tables and release policies in current primary documentation.
Preserve the project's chosen stack unless a concrete limitation warrants changing it.

## Execute the workflow

1. Define actual format, sample rate, channels, latency and quality requirements; avoid claiming resampling restores lost information.
2. Select AudioRecord/AudioTrack or higher-level media APIs according to control and lifecycle needs.
3. Implement audio focus, route/device changes and interruption behavior with current platform constraints.
4. Use bounded buffers, explicit ownership and error handling for underrun, permission loss and device disconnect.
5. Test wired/Bluetooth routes, calls, screen-off behavior and real-device capture quality.

## Verify completion

- Audio resources and workers stop cleanly on every exit path.
- The delivered format is measured rather than assumed from a requested configuration.
- Background recording follows applicable service and permission requirements.

Use replay fixtures for algorithm correctness and physical devices for quality, timing, routing and power claims. Record actual delivered rates, formats and error conditions.
Choose tests that observe a real failure or acceptance condition; avoid tests that merely mirror
the implementation. Reproduce a reported regression before fixing it when feasible. State any
missing device, backend or signing environment instead of claiming unexecuted checks passed.

## Use the bundled reference

Read [field-notes.md](references/field-notes.md) for decision boundaries, a concrete task and
its verification plan. Use its primary-source links to resolve version-specific questions.
Keep this skill standalone; related installed skills are optional assistance, not prerequisites.

## Return evidence

Report the resulting behavior, changed artifacts and why the decision fits the contract.
Include executed checks and their actual outcomes, then any material unverified cases.
For reviews, give source locations, impact and a bounded repair. For plans, give acceptance
criteria and dependencies. For performance work, include measurement conditions and raw results.
Keep credentials and sensitive user data out of reports. Continue authorized implementation
and verification; do not add an approval step for routine reversible work.
