# Bug 1955841 Triage Analysis

**Generated:** 2026-03-21
**Bug URL:** https://bugzilla.mozilla.org/show_bug.cgi?id=1955841

## Bug Information

- **Summary:** Video and Audio gets out of sync if 2x is used on youtube
- **Reporter:** joaolvcm@gmail.com (external contributor)
- **Status:** NEW
- **Product:** Core
- **Component:** Audio/Video: Playback
- **Severity/Priority:** S4 / P3
- **Created:** 2025-03-23 (~12 months ago)
- **Security Sensitive:** No
- **Pending Needinfo:** isorropisths@hotmail.com (requested by jmathies@mozilla.com on 2026-03-22)

## Research Summary and Key Findings

The bug reports progressive audio/video desynchronization on YouTube when the "hold to use 2x speed" feature is triggered repeatedly (3–10 times). Each speed-change cycle accumulates additional drift; seeking the video resets it (padenot confirmed this is because seeking recreates the entire audio pipeline, effectively resetting whatever was accumulating).

The issue has been confirmed by alice0775 (reliable external reporter), alwu@mozilla.com, and padenot@mozilla.com. Multiple users across Windows 10/11, macOS, Linux (Mint, Arch, Fedora), and Android have reported it. AMD GPU correlation was raised (comments 11, 20) but refuted by an Intel iGPU user (comment 14) — the issue is platform-agnostic.

A code-level TODO in [AudioStream.cpp](https://searchfox.org/mozilla-central/source/dom/media/AudioStream.cpp#493) directly describes the bug mechanism (see Codebase Investigation below). The root cause appears to be residual unprocessed samples remaining in the SoundTouch timestretcher pipeline after switching from non-1.0 back to 1.0 playback rate, which then corrupt timing on subsequent speed changes.

**Related bugs:**
- [1971227](https://bugzilla.mozilla.org/show_bug.cgi?id=1971227) — RESOLVED DUPLICATE: YouTube desync via 2x spacebar hold
- [1979560](https://bugzilla.mozilla.org/show_bug.cgi?id=1979560) — RESOLVED DUPLICATE: YouTube sync after fast forward
- [1972545](https://bugzilla.mozilla.org/show_bug.cgi?id=1972545) — NEW S4: lemonde.fr desync after fast forward (filed by Mozilla's Julien Wajsberg [:julienw])
- [2007762](https://bugzilla.mozilla.org/show_bug.cgi?id=2007762) — NEW S3/P3: YouTube desync on speed toggle (Arch Linux / PipeWire)
- [1938766](https://bugzilla.mozilla.org/show_bug.cgi?id=1938766) — UNCONFIRMED (Dec 2024, predates triage bug): "Video/Audio out of sync after accelerating the playback rate" — possibly the same root cause at higher speeds (4x); intermittent behavior reported

## Regression Timeline

- **Regressor identified:** [Bug 1752345](https://bugzilla.mozilla.org/show_bug.cgi?id=1752345) — "Make AudioStream.cpp real-time safe on macOS" (landed Feb 2022, Firefox 98). Filed and fixed by padenot@mozilla.com. This change made playback rate/pitch changes wait-free using an SPSC queue and refactored the audio callback pipeline.
- **Regression window confirmed by alice0775:** hg pushlog from c4339dd5 to f85620f9 (autoland, 2022). Alice added the `regressed_by: 1752345` field on 2025-03-24.
- **Reporter tested older versions:** Confirmed present in Firefox 118 and 101, consistent with a regression from early 2022.
- **ESR status:** Firefox ESR 115 and 128 marked `wontfix` (set via release bot). Firefox 136–139 marked affected.
- **Bug 1938766** (filed Dec 2024) may represent the first public report of this issue, though it was UNCONFIRMED and had an intermittent reproduction.

## Classification

| Signal | Detected | Evidence |
|--------|----------|----------|
| Clear STR | Yes | Hold mouse on YouTube to trigger 2x, repeat 3–10 times; confirmed by alice0775 and alwu@mozilla.com |
| Test Case | No | No standalone minimal test case; reporter shared a profiler link |
| Crash Stack | No | Not a crash |
| Fuzzing | No | Community-reported |

## Assessment

- **Suggested Severity:** S3 (upgrade from S4)
- **Suggested Priority:** P3 (keep)

### Assessment Reasoning

The current S4 rating underestimates impact. This is a confirmed regression affecting YouTube — the most widely used video platform — through a standard interaction (the "hold for 2x" feature). Two bugs have been duplicated against it, and active reports span all major desktop and mobile platforms from unrelated users across more than a year. The issue isn't rare or platform-specific.

A workaround exists (seeking resets sync), so S3 is appropriate: "Blocks non-critical functionality, workarounds in Firefox exist." A crash or total playback failure would warrant S2. The issue is not a good first bug given the audio pipeline complexity.

P3 (backlog) remains appropriate; this is a regression but does not block critical paths and has a usable workaround. The fact that padenot couldn't prioritize it and jmathies delegated the needinfo suggests it's not being treated as urgent, which aligns with P3.

## Codebase Investigation

### Relevant Files Examined

- [dom/media/AudioStream.cpp](https://searchfox.org/mozilla-central/source/dom/media/AudioStream.cpp) — Core audio stream implementation, timestretcher pipeline, FrameHistory, DataCallback
- [dom/media/AudioStream.h](https://searchfox.org/mozilla-central/source/dom/media/AudioStream.h) — AudioStream and AudioClock declarations

### Findings

The root cause is visible in `AudioStream::GetUnprocessed()` at lines 473–505. When playback rate returns to 1.0, this function is called to flush the SoundTouch timestretcher pipeline. However, an explicit TODO at line 493 acknowledges the issue:

```cpp
// TODO: There might be still unprocessed samples in the stretcher.
// We should either remove or flush them so they won't be in the output
// next time we switch a playback rate other than 1.0.
mTimeStretcher->numUnprocessedSamples().copy_and_verify([](auto samples) {
  NS_WARNING_ASSERTION(samples == 0, "no samples");
});
```

The flow that causes the desync:
1. User triggers 2x speed → `GetTimeStretched()` feeds audio frames through the SoundTouch timestretcher
2. User releases mouse → rate returns to 1.0 → `GetUnprocessed()` flushes available output samples from the stretcher
3. Residual *unprocessed input* samples remain inside the stretcher but are not cleared
4. Next 2x trigger: the stretcher starts with stale samples already queued, shifting the timing relationship between audio and video frames
5. Each cycle accumulates more drift → progressive desync observed by users

The workaround of seeking works because seeking destroys and recreates the media sink (confirmed by padenot in comment 8: "we recreate the whole thing so we effectively 'reset' whatever issue was accumulating").

The `UpdatePlaybackRateIfNeeded()` function (line 583) sets the new tempo/rate on the timestretcher but does not flush it first. The `FrameHistory` class's `GetPosition()` also accumulates position based on frames served at each rate — residual samples at the wrong rate would corrupt this calculation.

### Suggested Investigation Areas

1. **`AudioStream::GetUnprocessed()` (line 473)** — Implement the TODO: when the timestretcher has unprocessed input samples after flushing output, call `mTimeStretcher->clear()` or equivalent to discard them before deleting the timestretcher or returning to 1.0-rate processing.
2. **`AudioStream::UpdatePlaybackRateIfNeeded()` (line 583)** — Consider whether the timestretcher should be flushed/reset before applying a new rate, not just after. This would prevent stale state from one rate affecting the next.
3. **`FrameHistory::Append()`** — Verify that the history accounting correctly handles the frames associated with residual unprocessed samples (they are consumed by audio hardware timing but may not map correctly to a rendered video frame).

## Bugzilla Use Tracking

- Total Bugzilla Queries: 16
- Total Bugs Processed: 8 (1955841, 1752345, 1971227, 1972545, 1979560, 1938766, 1980236, 2007762)
- Estimated Download Bandwidth Used: ~0.3 MB
- Inaccessible Bugs Due to Permissions: 0
