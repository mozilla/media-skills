# Bugzilla Wrangler Report — Media Scope

---

## Session Info

| Field | Value |
|-------|-------|
| **Date** | 2026-03-18 |
| **Scope Profile** | `media` — Core: Audio/Video, Audio/Video: cubeb, Audio/Video: GMP, Audio/Video: MediaStreamGraph, Audio/Video: Playback, Audio/Video: Recording, Audio/Video: Web Codecs, Web Audio |
| **Seed Timeframe** | 2025-12-18 → 2026-03-18 (last 3 months, default) |
| **Seed Count** | 46 (33 created + 13 changed = 46 unique, after filtering `intermittent-failure` bugs) |
| **Seed Mode** | mixed-seed (33 created + 13 changed = 46 unique) |
| **Cache** | Fresh — generated this session (`reports/wrangler_cache_media.json`) |

---

## Seed Info

### Full Seed List (by priority)

**P1**
- [2023094](https://bugzilla.mozilla.org/show_bug.cgi?id=2023094) AppLocker Publisher rules don't work when loading DLLs with USER_RESTRICTED token (GMP) — S3, ASSIGNED

**P2**
- [2022993](https://bugzilla.mozilla.org/show_bug.cgi?id=2022993) Crash in [@ syscall | std::sys::pal::unix::futex::futex_wait] — S2, ASSIGNED
- [2011679](https://bugzilla.mozilla.org/show_bug.cgi?id=2011679) [Meta] Bluetooth device related issues with audio and video — S2, NEW
- [2023159](https://bugzilla.mozilla.org/show_bug.cgi?id=2023159) 28.4 - 15.12% ve-av1-q wallclock regression (OSX) — S2, NEW
- [2023568](https://bugzilla.mozilla.org/show_bug.cgi?id=2023568) Use a single rlbox sandbox for all soundtouch instances — S2, NEW
- [2023515](https://bugzilla.mozilla.org/show_bug.cgi?id=2023515) Crash in [@ libc.so | libart.so | JNI::CallVoidMethodA] (Android) — S2, NEW
- [2011539](https://bugzilla.mozilla.org/show_bug.cgi?id=2011539) Crash in [@ mozilla::AudioDecoderInputTrack::EnsureTimeStretcher] — S2, ASSIGNED
- [2017567](https://bugzilla.mozilla.org/show_bug.cgi?id=2017567) Handle more TimeUnit overflow cases in MSE — S3, NEW
- [2016484](https://bugzilla.mozilla.org/show_bug.cgi?id=2016484) High-bitrate AV1 freezes: DAV1DDecoder busy-waits on EAGAIN — S2, NEW
- [1984064](https://bugzilla.mozilla.org/show_bug.cgi?id=1984064) Android 14 emulator has many mochitest media failures on debug — S2, ASSIGNED
- [1978703](https://bugzilla.mozilla.org/show_bug.cgi?id=1978703) AV1 video stuttering with media.ffvpx-hw.enabled set to true — S3, REOPENED
- [2016501](https://bugzilla.mozilla.org/show_bug.cgi?id=2016501) crash at null in [@ mozilla::EncoderAgent::Dry] (WebCodecs) — S3, NEW

**P3**
- [2021805](https://bugzilla.mozilla.org/show_bug.cgi?id=2021805) Firefox mutes YouTube for a second on Wheel-Click a Tweet — S3, UNCONFIRMED
- [2023447](https://bugzilla.mozilla.org/show_bug.cgi?id=2023447) High power consumption when playing YouTube videos — S3, UNCONFIRMED
- [2013720](https://bugzilla.mozilla.org/show_bug.cgi?id=2013720) Screen saver activates when streaming video in Firefox on Linux Mint — S3, UNCONFIRMED
- [2009596](https://bugzilla.mozilla.org/show_bug.cgi?id=2009596) [HDR/Windows] Intel Iris Xe (Alder Lake Mobile) doesn't show HDR — S3, NEW
- [2023379](https://bugzilla.mozilla.org/show_bug.cgi?id=2023379) [meta] Media Related Sleep Issues — S3, NEW
- [2016587](https://bugzilla.mozilla.org/show_bug.cgi?id=2016587) Nvidia Tegra Video HW Decoding Regression with Firefox 142+ — S3, NEW
- [2007762](https://bugzilla.mozilla.org/show_bug.cgi?id=2007762) Audio/video desync when toggling playback speed on YouTube (PipeWire) — S3, NEW
- [2023388](https://bugzilla.mozilla.org/show_bug.cgi?id=2023388) Cubeb Pain Points — S2, NEW
- [2020653](https://bugzilla.mozilla.org/show_bug.cgi?id=2020653) Disconnecting AirPods no longer pauses media (YouTube) unlike Safari — S3, UNCONFIRMED
- [2018819](https://bugzilla.mozilla.org/show_bug.cgi?id=2018819) No way to add exceptions to Autoplay default permissions — S3, UNCONFIRMED
- [2023046](https://bugzilla.mozilla.org/show_bug.cgi?id=2023046) Firefox crashes with crafted Ogg file (negative timeDenom assertion) — S3, UNCONFIRMED
- [2009624](https://bugzilla.mozilla.org/show_bug.cgi?id=2009624) HDR video transfer function mismatch on Qualcomm Snapdragon X1 — S3, NEW
- [2021122](https://bugzilla.mozilla.org/show_bug.cgi?id=2021122) HEVC video doesn't play in flatpak builds — S3, NEW
- [2020823](https://bugzilla.mozilla.org/show_bug.cgi?id=2020823) h264 video not decoded with hardware in flatpak build — S3, NEW
- [2012285](https://bugzilla.mozilla.org/show_bug.cgi?id=2012285) [NVIDIA] Fails to create headless HW accelerated GL context — S3, UNCONFIRMED
- [2017271](https://bugzilla.mozilla.org/show_bug.cgi?id=2017271) Video choppy on Coursera.org after 12 hours — S3, NEW
- [2008781](https://bugzilla.mozilla.org/show_bug.cgi?id=2008781) Bluetooth audio stuttering when playing a video — S3, UNCONFIRMED
- [2020532](https://bugzilla.mozilla.org/show_bug.cgi?id=2020532) Strange msgs at FF startup (cubeb) — S3, UNCONFIRMED
- [2009171](https://bugzilla.mozilla.org/show_bug.cgi?id=2009171) Freeze after Bluetooth disconnect on Windows 11 (fails to rebind audio sink) — S3, UNCONFIRMED
- [1953883](https://bugzilla.mozilla.org/show_bug.cgi?id=1953883) Firefox doesn't play YouTube videos in Flatpak, AppImage does (SteamOS) — S3, UNCONFIRMED
- [1999168](https://bugzilla.mozilla.org/show_bug.cgi?id=1999168) VideoDecoder.isConfigSupported() returns false for HEVC on Windows — S3, NEW
- [1541471](https://bugzilla.mozilla.org/show_bug.cgi?id=1541471) [meta] Implement spec-compliant HTMLMediaElement.captureStream — S3, NEW
- [1942421](https://bugzilla.mozilla.org/show_bug.cgi?id=1942421) Enable H265 Decoder on Windows for WebCodecs — S3, NEW
- [1978703](https://bugzilla.mozilla.org/show_bug.cgi?id=1978703) AV1 video stuttering with media.ffvpx-hw.enabled — S3, REOPENED
- [1986315](https://bugzilla.mozilla.org/show_bug.cgi?id=1986315) AAC in MP4, channel index 7 (7.1) rendered incorrectly — S3, NEW
- [1999639](https://bugzilla.mozilla.org/show_bug.cgi?id=1999639) audiodg process uses multiple GB RAM when playing audio file N times quickly — S3, NEW
- [2002910](https://bugzilla.mozilla.org/show_bug.cgi?id=2002910) Replace user interaction with explicit control that allows video playback — S3, UNCONFIRMED
- [1987266](https://bugzilla.mozilla.org/show_bug.cgi?id=1987266) Tabs freeze and crash on background play on secondary screen — S3, UNCONFIRMED
- [1984763](https://bugzilla.mozilla.org/show_bug.cgi?id=1984763) MOZ_CRASH: MozPromise::ThenValue from 'RecvFlush' destroyed without resolve/reject — S3, NEW

**Priority Unknown (--)**
- [2023254](https://bugzilla.mozilla.org/show_bug.cgi?id=2023254) Fix lifetimes for RemoteMediaDataEncoderChild and RemoteCDMChild — S3, ASSIGNED
- [2016952](https://bugzilla.mozilla.org/show_bug.cgi?id=2016952) Crash in [@ OOM | small] — S3, UNCONFIRMED
- [2018005](https://bugzilla.mozilla.org/show_bug.cgi?id=2018005) Firefox crashes gnome desktop process causing a SIGSEGV — S3, UNCONFIRMED
- [1883738](https://bugzilla.mozilla.org/show_bug.cgi?id=1883738) Assertion failure: d3d11.IsEnabled() at DeviceManagerDx.cpp:81 — S3, REOPENED

**P4/P5**
- [2021505](https://bugzilla.mozilla.org/show_bug.cgi?id=2021505) Check bit depth for codec (WebCodecs) — S4, NEW

---

### Seed Creation Timeline

Seed bugs from Query A (created in window) break down as follows:

```
Dec 2025  |  #  |
Jan 2026  |  ########## (9)  |
Feb 2026  |  ######## (8)    |
Mar 2026  |  ################ (16) |
```

Query B added 13 older bugs recently changed (all created before the window — reaching back to 2019 in the case of the captureStream meta). The March spike reflects active triage and new meta-bug creation.

---

## Theme 1 — Bluetooth Audio Device Issues

**User-facing impact:** Firefox users with Bluetooth headphones, earbuds (AirPods, Pixel Buds, Bose, generic BT devices) on Windows, macOS, Android, and Linux experience a wide range of failures: audio stuttering, desync between audio and video, muting when clicking elsewhere, failure to resume after disconnect, and complete audio dropout when toggling devices. This cluster has been accumulating reports since 2018, and a meta-bug was created in January 2026 acknowledging the scope of the problem.

### Breadcrumbs

| Bug ID | Summary | Severity | Status | Last Changed |
|--------|---------|----------|--------|--------------|
| [2011679](https://bugzilla.mozilla.org/show_bug.cgi?id=2011679) | [Meta] Bluetooth device related issues with audio and video | S2 | NEW | 2026-03-18 |
| [2008781](https://bugzilla.mozilla.org/show_bug.cgi?id=2008781) | Bluetooth audio stuttering when playing a video | S3 | UNCONFIRMED | 2026-03-04 |
| [2009171](https://bugzilla.mozilla.org/show_bug.cgi?id=2009171) | Freeze of audio/video after Bluetooth disconnect on Windows 11 (fails to rebind audio sink) | S3 | UNCONFIRMED | 2026-03-05 |
| [2020653](https://bugzilla.mozilla.org/show_bug.cgi?id=2020653) | Disconnecting AirPods no longer pauses media (YouTube) unlike Safari | S3 | UNCONFIRMED | 2026-03-14 |
| [2021805](https://bugzilla.mozilla.org/show_bug.cgi?id=2021805) | Firefox mutes YouTube for a second on Wheel-Click a Tweet | S3 | UNCONFIRMED | 2026-03-17 |
| [1987257](https://bugzilla.mozilla.org/show_bug.cgi?id=1987257) | Audio desynchronized between left/right AirPods Pro 2 on macOS 15 | S3 | UNCONFIRMED | 2026-03-14 |
| [1999582](https://bugzilla.mozilla.org/show_bug.cgi?id=1999582) | Short BT audio hiccup when reloading or closing another tab | S3 | UNCONFIRMED | 2026-03-14 |
| [1973353](https://bugzilla.mozilla.org/show_bug.cgi?id=1973353) | Delayed video start/resume by Bluetooth | S2 | UNCONFIRMED | 2026-03-11 |
| [1937317](https://bugzilla.mozilla.org/show_bug.cgi?id=1937317) | Videos stop playing if headphones removed during playback (regression) | S3 | NEW | 2026-01-21 |
| [1936931](https://bugzilla.mozilla.org/show_bug.cgi?id=1936931) | Video desyncs with audio after YouTube ads with BT headphones | S3 | UNCONFIRMED | 2026-01-21 |
| [1835986](https://bugzilla.mozilla.org/show_bug.cgi?id=1835986) | Audio and video stutter on Android with Bluetooth output (BT codec issue) | S3 | NEW | 2026-01-21 |
| [1901224](https://bugzilla.mozilla.org/show_bug.cgi?id=1901224) | Videos pausing with Bose 45 BT headphones | S3 | NEW | 2026-03-15 |
| [2007835](https://bugzilla.mozilla.org/show_bug.cgi?id=2007835) | Audio stutters with Pixel Buds Pro 2 BT earbuds | S3 | UNCONFIRMED | 2026-01-21 |
| [2008968](https://bugzilla.mozilla.org/show_bug.cgi?id=2008968) | YouTube stutters at start and on seeking when BT device is audio output | S3 | UNCONFIRMED | 2026-01-21 |
| [1957088](https://bugzilla.mozilla.org/show_bug.cgi?id=1957088) | sesame.com — can't hear AI talking in voice demo with BT headphones (site-report) | S3 | NEW | 2026-02-05 |

### Timeline Narrative

Reports of Bluetooth audio failures stretch back to 2018 ([1492488](https://bugzilla.mozilla.org/show_bug.cgi?id=1492488)). The meta-bug [2011679](https://bugzilla.mozilla.org/show_bug.cgi?id=2011679) was created on 2026-01-21 consolidating 23 open issues. The meta itself is S2/P2 but has no assignee. The problems span cubeb (audio backend), Playback, and have webcompat cross-over (site-report on sesame.com). The `regression` keyword on [1937317](https://bugzilla.mozilla.org/show_bug.cgi?id=1937317) (videos stop playing on headphone removal) is particularly concerning.

> **Stagnation callout:** The meta bug [2011679](https://bugzilla.mozilla.org/show_bug.cgi?id=2011679) is S2, created Jan 2026, with no assignee and no current active work tracked. Multiple underlying S3 bugs have had no activity in >30 days, and several have been open since 2018-2023 with no resolution.

---

## Theme 2 — Crash: AudioDecoderInputTrack::EnsureTimeStretcher (Windows, Topcrash)

**User-facing impact:** Firefox crashes on Windows during audio/video playback, specifically when the time-stretcher (soundtouch, used for variable playback speed) is invoked from the audio pipeline. This is marked as a `topcrash` and has an active assignee. A related bug ([2023568](https://bugzilla.mozilla.org/show_bug.cgi?id=2023568)) proposes consolidating all soundtouch rlbox sandbox instances as part of the fix.

### Breadcrumbs

| Bug ID | Summary | Severity | Status | Last Changed |
|--------|---------|----------|--------|--------------|
| [2011539](https://bugzilla.mozilla.org/show_bug.cgi?id=2011539) | Crash in [@ mozilla::AudioDecoderInputTrack::EnsureTimeStretcher] | S2 | ASSIGNED | 2026-03-16 |
| [2023568](https://bugzilla.mozilla.org/show_bug.cgi?id=2023568) | Use a single rlbox sandbox for all soundtouch instances (fix work) | S2 | NEW | 2026-03-17 |
| [2017567](https://bugzilla.mozilla.org/show_bug.cgi?id=2017567) | Handle more TimeUnit overflow cases in MSE (related pipeline robustness) | S3 | NEW | 2026-03-17 |
| [1984763](https://bugzilla.mozilla.org/show_bug.cgi?id=1984763) | MOZ_CRASH: MozPromise::ThenValue from 'RecvFlush' destroyed without resolve/reject | S3 | NEW | 2026-03-16 |

### Socorro Crash Data

[mozilla::AudioDecoderInputTrack::EnsureTimeStretcher](https://crashes.mozilla.org/signatures?q=signature%3A%22mozilla%3A%3AAudioDecoderInputTrack%3A%3AEnsureTimeStretcher%22)

- **Volume (visible sample):** 14 crashes retrieved, all from 2026-03-14 to 2026-03-17
- **Top platform:** Windows NT (Windows 10 and Windows 11)
- **Versions affected:** Firefox 148.0.2 (release) and 149.0b8 (beta)
- **Process type:** main process
- **Trend:** Date-windowed comparison was inconclusive (CLI date filter returned no results for prior window); currently active in both release and beta

### Timeline Narrative

Bug filed 2026-01-20, quickly gained `topcrash` status. The fix direction involves restructuring soundtouch sandbox usage ([2023568](https://bugzilla.mozilla.org/show_bug.cgi?id=2023568), S2/P2 filed 2026-03-16). Active assignee. Still crashing in 148.0.2 release as of 2026-03-17.

---

## Theme 3 — Crash: cubeb futex_wait (Linux/ESR)

**User-facing impact:** Firefox crashes on Linux systems — particularly on Debian, Fedora, and Kali Linux — in the cubeb audio backend's futex synchronization path. The bug is S2/P2 and ASSIGNED. Notably, the ESR channel is heavily represented, suggesting this hits a broader Linux enterprise/power-user audience.

### Breadcrumbs

| Bug ID | Summary | Severity | Status | Last Changed |
|--------|---------|----------|--------|--------------|
| [2022993](https://bugzilla.mozilla.org/show_bug.cgi?id=2022993) | Crash in [@ syscall \| std::sys::pal::unix::futex::futex_wait] | S2 | ASSIGNED | 2026-03-18 |
| [2023388](https://bugzilla.mozilla.org/show_bug.cgi?id=2023388) | Cubeb Pain Points (tracks several cubeb robustness issues) | S2 | NEW | 2026-03-15 |
| [2018955](https://bugzilla.mozilla.org/show_bug.cgi?id=2018955) | WebRTC playout fails silently when default output operates at 768 kHz | S3 | NEW | 2026-03-16 |
| [1999639](https://bugzilla.mozilla.org/show_bug.cgi?id=1999639) | audiodg process uses multiple GB of RAM when audio file played rapidly (Windows cubeb) | S3 | NEW | 2026-03-16 |
| [2007762](https://bugzilla.mozilla.org/show_bug.cgi?id=2007762) | Audio/video desync toggling playback speed on YouTube (Arch Linux / PipeWire) | S3 | NEW | 2026-03-15 |

### Socorro Crash Data

[syscall | std::sys::pal::unix::futex::futex_wait](https://crashes.mozilla.org/signatures?q=signature%3A%22syscall+%7C+std%3A%3Asys%3A%3Apal%3A%3Aunix%3A%3Afutex%3A%3Afutex_wait%22)

- **Volume (visible sample):** 49 crashes retrieved, clustered 2026-03-17 to 2026-03-18
- **Top platform:** Linux (Debian 6.12, Fedora 6.18, Kali 6.18)
- **Versions affected:** Firefox 148.0.2 (release), 147.0.3, 140.7.0esr, 140.8.0esr — **ESR is prominently affected**
- **Process type:** main (audio-related thread)
- **Trend:** Date-windowed comparison inconclusive; sample shows active crash rate today

### Timeline Narrative

Filed 2026-03-12, immediately triaged as S2/P2 and ASSIGNED. The crash is in Rust stdlib futex code used by cubeb's threading. The companion bug [2023388](https://bugzilla.mozilla.org/show_bug.cgi?id=2023388) "Cubeb Pain Points" was filed 2026-03-15 to track broader cubeb reliability concerns. ESR users are disproportionately affected.

---

## Theme 4 — AV1 Decoder Performance and Freeze

**User-facing impact:** Users experience AV1 video freezes, stuttering, and performance regressions across platforms. The freeze scenario is particularly severe: the DAV1D decoder busy-waits on EAGAIN rather than draining frames, causing the video pipeline to halt on high-bitrate content. A hardware-accelerated AV1 path (`media.ffvpx-hw`) also has a long-standing stutter regression that was reopened after an incomplete fix.

### Breadcrumbs

| Bug ID | Summary | Severity | Status | Last Changed |
|--------|---------|----------|--------|--------------|
| [2016484](https://bugzilla.mozilla.org/show_bug.cgi?id=2016484) | High-bitrate AV1 freezes: DAV1DDecoder busy-waits on EAGAIN instead of draining | S2 | NEW | 2026-03-15 |
| [2023159](https://bugzilla.mozilla.org/show_bug.cgi?id=2023159) | 15.12% ve-av1-q wallclock regression on macOS (perf-alert, regression) | S2 | NEW | 2026-03-17 |
| [1978703](https://bugzilla.mozilla.org/show_bug.cgi?id=1978703) | AV1 video stuttering with media.ffvpx-hw.enabled=true (56 comments, REOPENED) | S3 | REOPENED | 2026-03-16 |
| [1708504](https://bugzilla.mozilla.org/show_bug.cgi?id=1708504) | [meta] Media Triage (2016484 is a dep) | meta | NEW | 2026-03-15 |
| [2017567](https://bugzilla.mozilla.org/show_bug.cgi?id=2017567) | Handle more TimeUnit overflow cases in MSE | S3 | NEW | 2026-03-17 |

### Timeline Narrative

[2016484](https://bugzilla.mozilla.org/show_bug.cgi?id=2016484) was filed 2026-02-12 with a root cause identified (busy-wait loop in DAV1D), no assignee yet. [2023159](https://bugzilla.mozilla.org/show_bug.cgi?id=2023159) is a fresh perf-alert (filed 2026-03-13) showing a 15% AV1 wallclock regression on macOS introduced around March 9. [1978703](https://bugzilla.mozilla.org/show_bug.cgi?id=1978703) has accumulated 56 comments and was reopened, indicating a prior fix attempt was insufficient. The combination of a freeze bug, a performance regression, and a long-standing HW-accelerated stutter makes AV1 the most multi-faceted playback problem in the current window.

> **Stagnation callout:** [2016484](https://bugzilla.mozilla.org/show_bug.cgi?id=2016484) is S2, filed 2026-02-12, with no assignee and no activity in >30 days.

---

## Theme 5 — Media Sleep / Screensaver Inhibition

**User-facing impact:** Firefox fails to suppress OS sleep, display sleep, or screensaver activation during video playback (screensaver fires mid-stream on Linux; display sleeps during YouTube on Windows; macOS coreaudiod stays active preventing sleep). In the reverse direction, playback fails to recover correctly after the system wakes from sleep (video choppy, audio silent, or playback continues on the lock screen). A new meta-bug was just created to consolidate these reports.

### Breadcrumbs

| Bug ID | Summary | Severity | Status | Last Changed |
|--------|---------|----------|--------|--------------|
| [2023379](https://bugzilla.mozilla.org/show_bug.cgi?id=2023379) | [meta] Media Related Sleep Issues (16 deps) | S3 | NEW | 2026-03-15 |
| [2013720](https://bugzilla.mozilla.org/show_bug.cgi?id=2013720) | Screen saver activates when streaming video on Linux Mint | S3 | UNCONFIRMED | 2026-03-16 |
| [1984927](https://bugzilla.mozilla.org/show_bug.cgi?id=1984927) | Display goes to sleep while watching YouTube videos | S3 | NEW | 2026-03-14 |
| [1821102](https://bugzilla.mozilla.org/show_bug.cgi?id=1821102) | Firefox keeps coreaudiod active, prevents sleep on macOS | S3 | UNCONFIRMED | 2026-03-15 |
| [1977132](https://bugzilla.mozilla.org/show_bug.cgi?id=1977132) | Media playback resumes on Windows lock screen after waking from sleep (parity-chrome) | S3 | NEW | 2026-03-15 |
| [1961596](https://bugzilla.mozilla.org/show_bug.cgi?id=1961596) | Unmuted video does not play after computer sleep on macOS | S3 | UNCONFIRMED | 2026-03-15 |
| [1869101](https://bugzilla.mozilla.org/show_bug.cgi?id=1869101) | After sleep, video is very slow and choppy — doesn't happen in Edge | S3 | UNCONFIRMED | 2026-03-15 |
| [1519935](https://bugzilla.mozilla.org/show_bug.cgi?id=1519935) | Windows Sleep mode causes all video to unexpectedly stop after waking | S3 | NEW | 2026-03-15 |
| [2011578](https://bugzilla.mozilla.org/show_bug.cgi?id=2011578) | Firefox stops audio playback when monitor goes to sleep | S3 | RESOLVED | 2026-03-17 |

### Timeline Narrative

The oldest bug ([1519935](https://bugzilla.mozilla.org/show_bug.cgi?id=1519935)) dates to 2019. The meta [2023379](https://bugzilla.mozilla.org/show_bug.cgi?id=2023379) was freshly created 2026-03-14 — a positive sign that someone is organizing this space. [2011578](https://bugzilla.mozilla.org/show_bug.cgi?id=2011578) was recently RESOLVED (2026-03-17), showing some momentum. However, the bulk of the meta's 16 deps remain open and largely unassigned. The cross-platform nature (Windows, macOS, Linux) and presence of `parity-chrome` on [1977132](https://bugzilla.mozilla.org/show_bug.cgi?id=1977132) indicate user-visible competitive impact.

> **Stagnation callout:** Several S3 bugs in this theme (1519935, 1821102, 1869101) have had no resolution for 2–5 years and had only cosmetic "triage batch" updates in this window. The meta is new but the underlying issues are old.

---

## Theme 6 — AppLocker / GMP Plugin Loading Breakage (Windows Security)

**User-facing impact:** On Windows systems using AppLocker Publisher Rules with `USER_RESTRICTED` or lower access tokens (common in managed/enterprise environments), Firefox fails to load DLLs for the GMP (plugin) system. This breaks Widevine/EME-protected content (DRM streaming) and potentially other codec plugins. The parent crash bug [1830431](https://bugzilla.mozilla.org/show_bug.cgi?id=1830431) has 44 comments and blocks other security-related bugs.

### Breadcrumbs

| Bug ID | Summary | Severity | Status | Last Changed |
|--------|---------|----------|--------|--------------|
| [2023094](https://bugzilla.mozilla.org/show_bug.cgi?id=2023094) | AppLocker Publisher rules don't work with USER_RESTRICTED token (DLL loading) | S3 | ASSIGNED (mjf) | 2026-03-17 |
| [1830431](https://bugzilla.mozilla.org/show_bug.cgi?id=1830431) | Crash in [@ mozilla::gmp::GMPLoader::Load] (44 comments, parent crash) | S3 | NEW | 2026-03-13 |
| [2016501](https://bugzilla.mozilla.org/show_bug.cgi?id=2016501) | crash at null in [@ mozilla::EncoderAgent::Dry] (WebCodecs, ai-involved testcase) | S3 | NEW | 2026-03-10 |

### Timeline Narrative

[2023094](https://bugzilla.mozilla.org/show_bug.cgi?id=2023094) is P1, meaning fix is targeted for the current release cycle. It blocks [1830431](https://bugzilla.mozilla.org/show_bug.cgi?id=1830431), which has been open since 2023 with a broad dependency tree touching DRM loading and sandbox security. The fact that this is P1/ASSIGNED gives confidence that it's being actively addressed. The 14 comments on [2023094](https://bugzilla.mozilla.org/show_bug.cgi?id=2023094) indicate ongoing engineering discussion.

---

## Theme 7 — Linux Flatpak / Container Codec Failures

**User-facing impact:** Firefox running inside Flatpak containers (Steam Deck / SteamOS, standard Flatpak on Fedora/Debian) cannot hardware-decode H.264 or HEVC video, and fails to play YouTube in environments where the AppImage build works fine. This is a growing concern as SteamOS adoption increases.

### Breadcrumbs

| Bug ID | Summary | Severity | Status | Last Changed |
|--------|---------|----------|--------|--------------|
| [1867638](https://bugzilla.mozilla.org/show_bug.cgi?id=1867638) | [meta] Steam Deck related issues (Arch Linux flatpak distribution) — 16 deps | meta | NEW | 2026-03-04 |
| [2021122](https://bugzilla.mozilla.org/show_bug.cgi?id=2021122) | HEVC video doesn't play in flatpak builds | S3 | NEW | 2026-03-11 |
| [2020823](https://bugzilla.mozilla.org/show_bug.cgi?id=2020823) | h264 video not decoded with hardware in flatpak build | S3 | NEW | 2026-03-11 |
| [1953883](https://bugzilla.mozilla.org/show_bug.cgi?id=1953883) | Firefox doesn't play YouTube videos in Flatpak, AppImage does (SteamOS) | S3 | UNCONFIRMED | 2026-03-16 |

### Timeline Narrative

The Steam Deck meta [1867638](https://bugzilla.mozilla.org/show_bug.cgi?id=1867638) was created in late 2023 and has accumulated 16 dependencies. Two fresh bugs ([2021122](https://bugzilla.mozilla.org/show_bug.cgi?id=2021122) and [2020823](https://bugzilla.mozilla.org/show_bug.cgi?id=2020823)) were filed in March 2026, indicating users are still hitting these issues as Flatpak becomes more prevalent. No assignees. The fix likely requires VA-API or codec library availability improvements in the Flatpak sandbox.

---

## Theme 8 — HDR Video on Windows (Emerging)

**User-facing impact:** HDR video fails to display correctly on specific Windows hardware — Intel Iris Xe (Alder Lake Mobile) shows no HDR at all, and Qualcomm Snapdragon X1 shows incorrect HDR transfer function mapping. A meta-bug was created in January 2026 to track follow-ups.

### Breadcrumbs

| Bug ID | Summary | Severity | Status | Last Changed |
|--------|---------|----------|--------|--------------|
| [2012848](https://bugzilla.mozilla.org/show_bug.cgi?id=2012848) | [meta] HDR video support on Windows follow-ups (7 deps) | meta | NEW | 2026-03-13 |
| [2009596](https://bugzilla.mozilla.org/show_bug.cgi?id=2009596) | [HDR/Windows] Intel Iris Xe (Alder Lake Mobile) doesn't show HDR video | S3 | NEW | 2026-03-16 |
| [2009624](https://bugzilla.mozilla.org/show_bug.cgi?id=2009624) | HDR transfer function mismatch on Qualcomm Snapdragon X1 (Windows 11) | S3 | NEW | 2026-03-12 |

### Timeline Narrative

The meta [2012848](https://bugzilla.mozilla.org/show_bug.cgi?id=2012848) has 7 open dependencies and lives under Graphics: Color Management (cross-component from Audio/Video). No assignees on any of the tracked bugs. Filed in January 2026, last changed March 2026. As Windows on ARM and Alder Lake laptops become more common, this will affect more users.

> **Stagnation callout:** All three bugs (including S3 regressions on modern hardware) have had no activity in >30 days.

---

## Emerging Theme — captureStream Now Live on Nightly

**Positive momentum:** The long-running meta [1541471](https://bugzilla.mozilla.org/show_bug.cgi?id=1541471) for spec-compliant `HTMLMediaElement.captureStream` is nearing completion. The pref `media.captureStream.enabled` was enabled on Nightly ([2017708](https://bugzilla.mozilla.org/show_bug.cgi?id=2017708) RESOLVED, 2026-03-06), and the core implementation ([2007596](https://bugzilla.mozilla.org/show_bug.cgi?id=2007596)) landed. The `webcompat:platform-bug` keyword on the meta signals real-world site breakage that was fixed. Remaining open work includes a local file edge case ([917187](https://bugzilla.mozilla.org/show_bug.cgi?id=917187)) and a DecodedStream refactor ([2009488](https://bugzilla.mozilla.org/show_bug.cgi?id=2009488)).

---

## Closing

### Ranked Signal Summary

| Rank | Theme | Breadcrumbs | Meta-bug | Top Severity | Notes |
|------|-------|-------------|----------|--------------|-------|
| 1 | Bluetooth Audio Device Issues | 23+ | [2011679](https://bugzilla.mozilla.org/show_bug.cgi?id=2011679) (S2) | S2 | No assignee; 8-year accumulation; `regression` present |
| 2 | Crash: AudioDecoderInputTrack::EnsureTimeStretcher | 4 | — | S2 | `topcrash`; ASSIGNED; Windows release+beta; fix in progress |
| 3 | Crash: cubeb futex_wait (Linux/ESR) | 5 | — | S2 | 49 Socorro crashes; ESR heavily affected; ASSIGNED |
| 4 | AV1 Decoder Performance & Freeze | 5 | [1708504](https://bugzilla.mozilla.org/show_bug.cgi?id=1708504) | S2 | Freeze (no assignee, stagnant) + perf regression + reopened stutter |
| 5 | Media Sleep / Screensaver Inhibition | 9+ | [2023379](https://bugzilla.mozilla.org/show_bug.cgi?id=2023379) (S3) | S3 | Fresh meta; long-stagnant deps; cross-platform; parity-chrome |
| 6 | AppLocker / GMP Plugin Loading | 3 | — | S3 | P1 ASSIGNED; enterprise impact; DRM breakage |
| 7 | Linux Flatpak Codec Issues | 4 | [1867638](https://bugzilla.mozilla.org/show_bug.cgi?id=1867638) | S3 | SteamOS growing; fresh bugs; no assignees |
| 8 | HDR Video on Windows | 3 | [2012848](https://bugzilla.mozilla.org/show_bug.cgi?id=2012848) | S3 | Stagnant; 7 deps; ARM + Intel hardware |

---

### Resources Used

| Resource | Details |
|----------|---------|
| Bugzilla REST API | 5 batch requests (seed Query A, seed Query B, Bluetooth deps, Sleep/HDR deps, misc deps) |
| socorro-cli | 4 signature searches (AudioDecoderInputTrack, futex_wait, trend windows) |
| WebFetch (Bugzilla) | Additional batch for captureStream deps, webcompat site-reports, GMP parent bugs |
| Total bugs examined | ~120 across all depths |
| Cache file | `reports/wrangler_cache_media.json` |

---

### Suggestions for Improving This Skill

1. **Socorro date filtering:** The `--date` flag syntax may need documentation — date-windowed trend queries returned no results while the undated query returned 49 crashes. Adding a syntax check or example to the skill prompt would help.
2. **cc_count consistently null:** The Bugzilla REST API returned `null` for `cc_count` on nearly all bugs in this run, making the signal-scoring proxy unusable. The skill should fall back gracefully and note its absence rather than silently omitting it.
3. **Automatically correlate crash bugs to soundtouch/rlbox sibling bugs:** In this run, [2011539](https://bugzilla.mozilla.org/show_bug.cgi?id=2011539) and [2023568](https://bugzilla.mozilla.org/show_bug.cgi?id=2023568) are clearly related but not linked via Bugzilla deps. A heuristic for component + keyword proximity could surface these.
4. **HDR meta lives in Graphics, not Audio/Video:** The dep crawl surfaced [2012848](https://bugzilla.mozilla.org/show_bug.cgi?id=2012848) because it's `blocks`-linked from a seed bug, but searching only the media components would miss it as a primary signal. Cross-component crawling is working well.

---

> *"The game is afoot — and the clues are in the comment threads."*
> — A detective who stared at Bugzilla for too long

---

*Report generated: 2026-03-18 | Scope: media | Tool: bugzilla-wrangler*
