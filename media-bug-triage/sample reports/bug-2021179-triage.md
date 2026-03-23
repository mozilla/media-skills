# Bug 2021179 Triage Analysis

**Generated:** 2026-03-21
**Bug URL:** https://bugzilla.mozilla.org/show_bug.cgi?id=2021179

## Bug Information

- **Summary:** When scrolling through Instagram reels on Mozilla Firefox, after a few reels; I start hearing a static sound in my sound. After a few more reels, the sound becomes mute and the entire website lags.
- **Reporter:** Jacob Kelley (xjacobkelleyx@gmail.com) — new external contributor
- **Status:** UNCONFIRMED
- **Product:** Core
- **Component:** Audio/Video: cubeb
- **Severity / Priority:** -- / --
- **Created:** 2026-03-05 (16 days ago)
- **CC:** alice0775@gmail.com (prolific external media reporter), tim.w.connors@gmail.com

## Research Summary and Key Findings

The reporter describes a progressive audio failure pattern when scrolling Instagram Reels in Firefox on Windows: audio first becomes static, then fully mutes, and eventually no audio works across any browser tab or external application — a system-wide failure. Chrome is unaffected.

Mozilla engineer jmathies triaged this on 2026-03-14, moved the bug to the `Audio/Video: cubeb` component, and identified the likely root cause: **cubeb audio streams are not being released when Instagram Reels' video/audio elements scroll out of view**. Each new reel creates a new WASAPI audio stream, but the old ones are not closed. When WASAPI runs out of available resources, audio fails globally across the Windows session.

The reporter responded on 2026-03-19 with a Firefox performance profile ([profile link](https://share.firefox.dev/4bAiUY9)) and about:support data. Key system details from about:support:

- Firefox 148.0.2 on Windows 10 (build 19045)
- NVIDIA GeForce RTX 5070 Ti; 63.8 GB RAM
- **Hardware compositing is disabled** (`layers.acceleration.disabled: true`)
- WebRender in software mode; hardware video decoding unsupported
- Log entry: `"CompositorDevice does not exist."`
- Extensions: AdBlock, uBlock Origin, Return YouTube Dislike, YouTube Redux, Augmented Steam

The disabled hardware acceleration increases CPU load for video decode and display, but is likely not a direct cause of the audio stream leak. It may, however, exacerbate lag symptoms since each reel video is decoded entirely in software.

**Related bugs:**

- [1959613](https://bugzilla.mozilla.org/show_bug.cgi?id=1959613) — "Audio stream remains open when playback paused" (Core / cubeb, S4, UNCONFIRMED, 2025-04-10). Demonstrates the same underlying mechanism on Windows with a simpler repro: play/pause a YouTube video, then a WASAPI exclusive-mode application fails with "Audio device in use". This is the closest known analog.
- [1974718](https://bugzilla.mozilla.org/show_bug.cgi?id=1974718) — "Maintains too many open connections to pipewire (and pulseaudio) sound server on Linux" (Core / Audio/Video: Playback, S3/P3, UNCONFIRMED, 2025-06-30). The Linux equivalent: file descriptor exhaustion in pipewire-pulse after extended use of Firefox, caused by unreleased audio connections. Root cause is the same pattern.
- Both bugs now reference 2021179 in their `see_also` fields (added by jmathies).

No crash signatures are associated with this bug. No duplicate candidates found.

## Regression Timeline

Not reported as a regression. No baseline comparison provided. The reporter notes that Chrome handles the same scenario without issue, suggesting this is a pre-existing Firefox behavior difference rather than a newly introduced regression.

## Classification

| Signal | Detected | Evidence |
|--------|----------|----------|
| Clear STR | Yes (conditional) | Steps provided; requires Instagram account, ~10 reels of scrolling |
| Test Case | No | No standalone HTML/JS test case attached |
| Crash Stack | No | Not a crash — resource exhaustion |
| Fuzzing | No | — |

## Assessment

- **Suggested Severity:** S2
- **Suggested Priority:** P2

### Assessment Reasoning

The system-wide audio loss is the defining characteristic here. When Firefox exhausts WASAPI audio resources, no application on the system can play audio until Firefox is restarted — this goes beyond Firefox-only impact and constitutes a serious degradation of the user's computing environment. The S2 designation ("Major functionality impaired, high impact, no satisfactory workaround") is appropriate because restarting the browser is the only remedy, and the issue can arise during normal browsing of a high-traffic site (Instagram). The current S4 on the simpler-to-reproduce related bug 1959613 may warrant reassessment given this broader impact evidence.

P2 is warranted given that a Mozilla engineer has already identified the root cause and related bugs exist to anchor the work. This is not a fringe case: Instagram Reels is one of the most widely used video-scrolling interfaces on the web, and any site using multiple `<audio>`/`<video>` elements in rapid succession (TikTok, YouTube Shorts) could trigger the same exhaustion path. The underlying mechanism — cubeb WASAPI streams not being released on element removal or pause — is a genuine platform-level resource management gap.

## Codebase Investigation

Not performed. jmathies has already identified the relevant code area (cubeb's WASAPI backend, stream lifecycle management). The relevant source is in `media/libcubeb/src/cubeb_wasapi.cpp` and its stream destruction/release paths. The related bug 1959613 has a concrete repro for the same mechanism and may be the better vehicle for a targeted fix.

## Suggested Investigation Areas

- [cubeb_wasapi.cpp](https://searchfox.org/mozilla-central/source/media/libcubeb/src/cubeb_wasapi.cpp) — WASAPI stream lifecycle, specifically whether `cubeb_stream_stop` / stream destruction is reliably called when media elements are removed from the DOM or scrolled out of view
- DOM media element teardown path — verify that destroying a `<video>` or `<audio>` element always triggers cubeb stream release, even when the element was never explicitly paused
- Bug 1959613 STR (play/pause WASAPI exclusive) is a controlled repro for the same underlying mechanism and can be used to validate any fix

## Bugzilla Use Tracking

- Total Bugzilla Queries: 7
- Total Bugs Processed: 5 (2021179, 1974718, 1959613, 1953698, 1991116)
- Estimated Download Bandwidth Used: ~0.2 MB
- Inaccessible Bugs Due to Permissions: 0
