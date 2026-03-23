# Bug 2023823 Triage Analysis

**Generated:** 2026-03-21
**Bug URL:** https://bugzilla.mozilla.org/show_bug.cgi?id=2023823

## Bug Information

- **Summary:** MSE audio track desyncs from video on loop seek via ended event, while manual seek to same timestamp works correctly
- **Reporter:** alex.servanis@proton.me (external)
- **Status:** UNCONFIRMED
- **Product:** Core
- **Component:** Audio/Video: Playback
- **Severity:** -- (unset)
- **Priority:** -- (unset)
- **Created:** 2026-03-17 (4 days ago)
- **Security Sensitive:** No

## Research Summary and Key Findings

The reporter observes that YouTube videos (~30 minutes long) using the `loop` attribute exhibit audio/video desynchronization when the video loops back to the beginning. The specific symptom is that the video track seeks correctly to 0:00 while the audio lands at an incorrect position (approximately the 14-minute mark in their example). Three failure modes are described: audio offset (~14 min), complete silence, or mid-video glitch. A manual seek to the same timestamp immediately corrects the sync. The reporter concludes this is a race condition in how MSE coordinates audio and video `SourceBuffer` seeks during looping.

The reporter's platform is Microsoft Surface Pro 6, Windows 10, Firefox 148. No crash IDs, no attachments, no `about:support` data, and no test case were provided.

Mozilla engineer **jmathies** (jmathies@mozilla.com) responded on 2026-03-17, requesting two diagnostic items: (1) test with `media.seamless-looping-video` disabled in `about:config`, and (2) capture media playback logs via `about:logging`. A needinfo was set on the reporter. The reporter cleared the needinfo on 2026-03-18 but no follow-up comment with diagnostic data appears to have been provided.

**Related bugs found:**

- [1806060](https://bugzilla.mozilla.org/show_bug.cgi?id=1806060) — "Audio becomes out of sync after looping" (NEW, S3, 2022-12-16). Filed by Mozilla engineer jya (Jean-Yves Avenard). Reproduction: Facebook reel video, macOS Ventura + AirPods (Bluetooth). Unable to reproduce without BT headset; mozregression was requested but jya went inactive. Possibly related but may involve a different root cause (BT-specific audio timing vs. general MSE seek sync).

- [1498733](https://bugzilla.mozilla.org/show_bug.cgi?id=1498733) — "[Meta] Seamless media playback looping" (NEW, S3, meta keyword). Tracks all seamless looping work; last updated 2025-10-15 with 17 dependent bugs. This is the canonical tracking bug for the feature area.

No duplicate of the exact MSE-specific desync scenario was found in searches.

## Regression Timeline

No regression timeline provided. The reporter does not indicate this is a regression from a previously working version.

## Classification

| Signal | Detected | Evidence |
|--------|----------|----------|
| Clear STR | No | Steps are vague: "YouTube video ~30 minutes with loop attribute" — no specific URL, no reliable reproduction rate, no configuration steps |
| Test Case | No | No attached files, no inline reproduction code |
| Crash Stack | No | No crash signatures or stack traces |
| Fuzzing | No | No fuzzing indicators |

## Assessment

- **Suggested Severity:** S3
- **Suggested Priority:** --

### Assessment Reasoning

Audio/video desync on looping is a legitimate, non-trivial issue affecting user experience when watching looping content via MSE (which YouTube uses for adaptive streaming). The symptom is reproducible for the reporter but requires a specific ~30-minute video and the `loop` attribute, suggesting this is not a widespread S2-level regression. A workaround exists: manual seeking immediately corrects sync. This places the bug squarely in S3 territory.

The diagnostic gap is significant. The `media.seamless-looping-video` toggle requested by jmathies is the highest-value next step: if disabling it eliminates the desync, the bug is in the `LoopingDecodingState` path; if the desync persists, the bug lies in the traditional seek-to-zero path triggered when seamless looping is not active. Without this information and media logs, developers cannot reliably reproduce or diagnose the issue.

Priority is withheld pending diagnostic information. The meta bug [1498733](https://bugzilla.mozilla.org/show_bug.cgi?id=1498733) and the related open bug [1806060](https://bugzilla.mozilla.org/show_bug.cgi?id=1806060) (filed by a Mozilla engineer) suggest this feature area has known ongoing stability issues; a TODO comment in `MediaDecoderStateMachine.cpp` at the `mSeamlessLoopingAllowed` assignment point explicitly notes that video seamless looping may not yet be stable enough to always enable. This bug should depend on or be linked to the meta bug once its nature is clarified.

## Codebase Investigation

The seamless looping implementation lives primarily in [MediaDecoderStateMachine.cpp](https://searchfox.org/mozilla-central/source/dom/media/MediaDecoderStateMachine.cpp) via the `LoopingDecodingState` class (around line 820). This state handles audio and video EOS independently, requesting data from start position for each track separately (`RequestDataFromStartPosition`), and adjusting queue offsets so decoded timestamps increase monotonically across the loop boundary.

The pref gating is at line ~2970:
- Audio-only media: controlled by `media.seamless-looping`
- Video media: controlled by `media.seamless-looping-video`

A TODO comment at line 2966 reads: _"after we ensure video seamless looping is stable enough, then we can remove this to make the condition always true"_ — explicit acknowledgment of potential instability.

`MediaSourceDecoder` (in [dom/media/mediasource/MediaSourceDecoder.cpp](https://searchfox.org/mozilla-central/source/dom/media/mediasource/MediaSourceDecoder.cpp)) does not override any seamless looping behavior, so MSE media uses the same `LoopingDecodingState` path. However, the MSE demuxer (`MediaSourceDemuxer`) may respond differently to the seek-to-start requests, which is a plausible source of the audio/video desync.

The `eSeamlessLoopingSeeking` position update type in [MediaDecoder.cpp](https://searchfox.org/mozilla-central/source/dom/media/MediaDecoder.cpp) (~line 1003) detects a loop by observing `currentPosition < prevPosition` without an active seek request — this is the trigger for notifying the owner (`SeekStarted` / `SeekCompleted`).

The bug title references "loop seek via ended event" — for seamless looping, no `ended` event fires from the browser side (it's all demuxer-level). If the reporter is accurately describing an `ended` event firing, it may indicate seamless looping is not activating for their MSE content, and the sync issue lies in the non-seamless loop path (traditional `ended` → seek-to-0 via JS/HTML loop attribute handling).

## Suggested Investigation Areas

1. **[MediaDecoderStateMachine.cpp — LoopingDecodingState::HandleEndOfAudio / HandleEndOfVideo](https://searchfox.org/mozilla-central/source/dom/media/MediaDecoderStateMachine.cpp)** (~lines 1004–1079): Check whether the audio and video EOS events and their corresponding `RequestDataFromStartPosition` calls are properly coordinated for MSE media. A race where audio EOS arrives and seeks before video EOS (or vice versa) and they seek to different effective positions could explain the desync.

2. **[MediaSourceDemuxer.cpp](https://searchfox.org/mozilla-central/source/dom/media/mediasource/MediaSourceDemuxer.cpp)**: Examine how seek-to-start requests from `LoopingDecodingState` are handled for MSE. The MSE demuxer has a `SourceBuffer`-based architecture where audio and video tracks are managed separately; independent seeks could produce misaligned start positions.

3. **Whether seamless looping is even active for the reporter**: If `media.seamless-looping-video` is enabled but MSE causes it to fall back (e.g., duration is unknown or the resource is treated as infinite), the traditional `ended`-event-based loop path may be taken, which may have separate sync issues.

## Suggested Feedback Request

A follow-up comment should be posted (jmathies already asked, but the reporter cleared the needinfo without apparent data). The request should re-ask for:

1. Result of toggling `media.seamless-looping-video` to `false` in `about:config` — does the desync still occur?
2. Media playback logs from `about:logging` using the `media` preset with log settings:
   `MOZ_LOG=timestamp,MediaDecoder:5,AudioStream:5,MediaFormatReader:5`
3. A specific URL or minimal HTML test case to reproduce the issue

## Bugzilla Use Tracking

- Total Bugzilla Queries: 11
- Total Bugs Processed: 3 (2023823, 1806060, 1498733)
- Estimated Download Bandwidth Used: ~0.3 MB
- Inaccessible Bugs Due to Permissions: 0
