# Bugzilla Wrangler Report — Media (Core)
**Generated:** 2026-03-25

---

## Session Info

| Field | Value |
|-------|-------|
| **Date** | 2026-03-25 |
| **Scope profile** | `media` — Core: Audio/Video, Audio/Video: cubeb, Audio/Video: GMP, Audio/Video: MediaStreamGraph, Audio/Video: Playback, Audio/Video: Recording, Audio/Video: Web Codecs, Web Audio |
| **Seed timeframe** | 2025-12-25 → 2026-03-25 (default 3-month window) |
| **Seed count** | 41 unique (post-filter) |
| **Seed mode** | mixed-seed (33 created + 8 unique changed = 41 total unique) |
| **Cache freshness** | Live fetch (default window — cache bypassed) |
| **Socorro enrichment** | **Unavailable** — TLS certificate error (`OSStatus -26276`) prevented connection to `crash-stats.mozilla.org`. Crash volume and trend data could not be collected. Recommend re-running crash lookups manually at [crash-stats.mozilla.org](https://crash-stats.mozilla.org) for signatures listed in the Crashes section below. |

---

## Seed Info

### Seed Bugs (prioritized by severity)

**S2 — 5 bugs**

| Bug | Summary | Component | Status |
|-----|---------|-----------|--------|
| [2011679](https://bugzilla.mozilla.org/show_bug.cgi?id=2011679) | [Meta] Bluetooth device related issues with audio and video | Audio/Video | NEW |
| [2016484](https://bugzilla.mozilla.org/show_bug.cgi?id=2016484) | High-bitrate AV1 freezes: DAV1DDecoder busy-waits on dav1d EAGAIN | Audio/Video: Playback | NEW |
| [2022993](https://bugzilla.mozilla.org/show_bug.cgi?id=2022993) | Crash in [@ syscall \| std::sys::pal::unix::futex::futex_wait] | Audio/Video: cubeb | ASSIGNED (kinetik) |
| [2023515](https://bugzilla.mozilla.org/show_bug.cgi?id=2023515) | Crash in [@ libc.so \| libmozglue.so \| libart.so \| _JNIEnv::CallVoidMethodA] | Audio/Video: Playback | NEW (topcrash) |
| [2023970](https://bugzilla.mozilla.org/show_bug.cgi?id=2023970) | about:support can leak PII via audio device names | Web Audio | NEW |

**S3 — 33 bugs**

| Bug | Summary | Component | Status |
|-----|---------|-----------|--------|
| [2023254](https://bugzilla.mozilla.org/show_bug.cgi?id=2023254) | Fix lifetimes for RemoteMediaDataEncoderChild and RemoteCDMChild | Audio/Video | ASSIGNED (aosmond) |
| [2025302](https://bugzilla.mozilla.org/show_bug.cgi?id=2025302) | HEVC/H.265 in Matroska silently fails when CodecPrivate contains malformed hvcC | Audio/Video | NEW |
| [2023379](https://bugzilla.mozilla.org/show_bug.cgi?id=2023379) | [meta] Media Related Sleep Issues | Audio/Video | NEW |
| [2023367](https://bugzilla.mozilla.org/show_bug.cgi?id=2023367) | Videos not playing | Audio/Video | NEW |
| [2022993](https://bugzilla.mozilla.org/show_bug.cgi?id=2022993) | Crash in futex_wait | Audio/Video: cubeb | ASSIGNED (kinetik) |
| [2023823](https://bugzilla.mozilla.org/show_bug.cgi?id=2023823) | MSE audio track desyncs from video on loop seek via ended event | Audio/Video: Playback | UNCONFIRMED |
| [2024183](https://bugzilla.mozilla.org/show_bug.cgi?id=2024183) | Don't allocate time stretcher on the audio thread | Audio/Video: MSGraph | NEW |
| [2023568](https://bugzilla.mozilla.org/show_bug.cgi?id=2023568) | Use a single rlbox sandbox for all soundtouch instances | Audio/Video: Playback | NEW |
| [2017567](https://bugzilla.mozilla.org/show_bug.cgi?id=2017567) | Handle more TimeUnit overflow cases in MSE | Audio/Video: Playback | NEW (padenot) |
| [2023447](https://bugzilla.mozilla.org/show_bug.cgi?id=2023447) | High power consumption and heat generation when playing YouTube videos | Audio/Video: Playback | UNCONFIRMED |
| [2016587](https://bugzilla.mozilla.org/show_bug.cgi?id=2016587) | Nvidia Tegra Video HW Decoding Regression with Firefox 142+ | Audio/Video: Playback | NEW |
| [2021122](https://bugzilla.mozilla.org/show_bug.cgi?id=2021122) | HEVC video doesn't play in flatpak builds | Audio/Video: Playback | NEW |
| [2016484](https://bugzilla.mozilla.org/show_bug.cgi?id=2016484) | High-bitrate AV1 freezes: DAV1DDecoder busy-waits | Audio/Video: Playback | NEW |
| [2016501](https://bugzilla.mozilla.org/show_bug.cgi?id=2016501) | crash at null in [@ mozilla::EncoderAgent::Dry] | Audio/Video: Web Codecs | NEW (padenot) |
| [2023594](https://bugzilla.mozilla.org/show_bug.cgi?id=2023594) | Applying a rotation to a video causes colors to shift | Audio/Video: Web Codecs | NEW |
| [2021179](https://bugzilla.mozilla.org/show_bug.cgi?id=2021179) | Instagram reels: static sound then mute, entire site lags | Audio/Video: cubeb | NEW |
| [2024598](https://bugzilla.mozilla.org/show_bug.cgi?id=2024598) | Crash in [@ mozilla::AudioCallbackDriver::OutputChannelCount] | Audio/Video: cubeb | NEW |
| [2007762](https://bugzilla.mozilla.org/show_bug.cgi?id=2007762) | Audio and video desync when toggling playback speed on YouTube (PipeWire) | Audio/Video: cubeb | NEW |
| [2020653](https://bugzilla.mozilla.org/show_bug.cgi?id=2020653) | Disconnecting AirPods no longer pauses media on YouTube | Audio/Video: cubeb | UNCONFIRMED |
| [2020823](https://bugzilla.mozilla.org/show_bug.cgi?id=2020823) | h264 video not decoded with hardware in flatpak build | Audio/Video | NEW |
| [2020532](https://bugzilla.mozilla.org/show_bug.cgi?id=2020532) | Strange msgs at FF startup | Audio/Video: cubeb | UNCONFIRMED |
| [2013720](https://bugzilla.mozilla.org/show_bug.cgi?id=2013720) | Screen saver activates when streaming video in Firefox on Linux Mint | Audio/Video: Playback | UNCONFIRMED |
| [2012285](https://bugzilla.mozilla.org/show_bug.cgi?id=2012285) | [NVIDIA] Fails to create headless HW accelerated GL context | Audio/Video: Playback | UNCONFIRMED |
| [2011389](https://bugzilla.mozilla.org/show_bug.cgi?id=2011389) | New stable version 147.0.1 has a huge problem with playing YouTube video | Audio/Video: Playback | UNCONFIRMED |
| [2009171](https://bugzilla.mozilla.org/show_bug.cgi?id=2009171) | Intermittent freeze after Bluetooth disconnect on Windows 11 (fails to rebind audio sink) | Audio/Video: Playback | UNCONFIRMED |
| [2008617](https://bugzilla.mozilla.org/show_bug.cgi?id=2008617) | 4K AV1 Video decode doesn't work on YouTube | Audio/Video: Playback | UNCONFIRMED |
| [2008313](https://bugzilla.mozilla.org/show_bug.cgi?id=2008313) | Audio has stopped working, after update, Linux FF-Only | Audio/Video: Playback | UNCONFIRMED |
| [2018819](https://bugzilla.mozilla.org/show_bug.cgi?id=2018819) | No way to add exceptions to Autoplay default permissions | Audio/Video: Playback | UNCONFIRMED |
| [2023094](https://bugzilla.mozilla.org/show_bug.cgi?id=2023094) | AppLocker Publisher rules don't work when loading DLLs with USER_RESTRICTED token | Audio/Video: GMP | ASSIGNED (bobowen) |
| [1955841](https://bugzilla.mozilla.org/show_bug.cgi?id=1955841) | Video and Audio gets out of sync if 2x is used on YouTube | Audio/Video: Playback | NEW |
| [1956979](https://bugzilla.mozilla.org/show_bug.cgi?id=1956979) | 9s jank trying to run PContent::Msg_CreateAudioIPCConnection while a game is paused | Audio/Video: Playback | ASSIGNED (kinetik) |
| [1991747](https://bugzilla.mozilla.org/show_bug.cgi?id=1991747) | Support MP3 in Matroska | Audio/Video: Playback | NEW |
| [2000420](https://bugzilla.mozilla.org/show_bug.cgi?id=2000420) | playback wants to buffer the whole file if mkv | Audio/Video: Playback | NEW (alwu) |
| [1883738](https://bugzilla.mozilla.org/show_bug.cgi?id=1883738) | Assertion failure: d3d11.IsEnabled() in DeviceManagerDx.cpp | Audio/Video: Playback | REOPENED (alwu) |

**Query B only (pre-window, recently changed)**

| Bug | Summary | Component | Status |
|-----|---------|-----------|--------|
| [1984881](https://bugzilla.mozilla.org/show_bug.cgi?id=1984881) | x.com causes audio interface to open with PipeWire even when nothing is playing | Web Audio | NEW (karlt) |
| [1999639](https://bugzilla.mozilla.org/show_bug.cgi?id=1999639) | Rapidly playing an audio file causes audiodg to use multiple GB of RAM on Windows | Audio/Video: cubeb | NEW |
| [1422891](https://bugzilla.mozilla.org/show_bug.cgi?id=1422891) | [meta] Support mkv\|matroska\|video/x-matroska in Firefox | Audio/Video: Playback | NEW (alwu) |

**S4 — 1 bug**

| Bug | Summary | Component | Status |
|-----|---------|-----------|--------|
| [2021505](https://bugzilla.mozilla.org/show_bug.cgi?id=2021505) | Check bit depth for codec | Audio/Video: Web Codecs | NEW (chunmin) |

---

### Seed Timeline

Creation dates of seed bugs within the window (Dec 25, 2025 – Mar 25, 2026). Eight Query B additions pre-date the window but have recent activity and are noted separately.

```
Dec 2025  [█]                          1 bug
Jan 2026  [███████]                    7 bugs
Feb 2026  [█████]                      5 bugs
Mar 2026  [████████████████████]      20 bugs
─────────────────────────────────────────────────────
          Dec    Jan    Feb    Mar
```

> The March spike is expected given the `changeddate DESC` ordering and the upper boundary of the window. January shows steady discovery. February coverage is lighter (note 5 bugs vs 7 in January).

Pre-window Query B additions: 1422891 (Dec 2017), 1883738 (Mar 2024), 1955841 (Mar 2025), 1956979 (Mar 2025), 1984881 (Aug 2025), 1991747 (Sep 2025), 1999639 (Nov 2025), 2000420 (Nov 2025) — all recently changed, indicating ongoing relevance.

---

## Themes

---

### Theme 1 — Bluetooth Audio Device Issues

**User-facing impact:** Firefox users with Bluetooth headphones and speakers experience a wide range of failures: audio stuttering during playback, desync after YouTube ads, silence after connecting/disconnecting, failure to pause media when buds are removed, jank when switching sources. This affects all major platforms (Windows, macOS, Linux, Android). The issue has been accumulating for years; the meta-bug was created in January 2026 to consolidate the backlog.

**Breadcrumbs (25)**

| Bug ID | Summary | Severity | Status | Last Changed |
|--------|---------|----------|--------|-------------|
| [2011679](https://bugzilla.mozilla.org/show_bug.cgi?id=2011679) | [Meta] Bluetooth device related issues with audio and video | S2 | NEW | 2026-03-20 |
| [2009171](https://bugzilla.mozilla.org/show_bug.cgi?id=2009171) | Intermittent freeze after Bluetooth disconnect on Windows 11 | S3 | UNCONFIRMED | 2026-03-05 |
| [2020653](https://bugzilla.mozilla.org/show_bug.cgi?id=2020653) | Disconnecting AirPods no longer pauses media (YouTube) | S3 | UNCONFIRMED | 2026-03-14 |
| [1987257](https://bugzilla.mozilla.org/show_bug.cgi?id=1987257) | AirPods Pro 2 on macOS 15 — audio desyncs between L/R earbuds | S3 | UNCONFIRMED | 2026-03-14 |
| [1999582](https://bugzilla.mozilla.org/show_bug.cgi?id=1999582) | Short BT audio hiccup when reloading/closing another tab | S3 | UNCONFIRMED | 2026-03-14 |
| [1901224](https://bugzilla.mozilla.org/show_bug.cgi?id=1901224) | Videos pausing with Bose 45 Bluetooth headphones | S3 | NEW | 2026-03-15 |
| [1936430](https://bugzilla.mozilla.org/show_bug.cgi?id=1936430) | Disconnecting BT headphones causes YouTube playback to stall | S3 | NEW | 2026-03-15 |
| [1989476](https://bugzilla.mozilla.org/show_bug.cgi?id=1989476) | Firefox Android does not play over Bluetooth | S3 | UNCONFIRMED | 2026-03-15 |
| [1678846](https://bugzilla.mozilla.org/show_bug.cgi?id=1678846) | No sound after disconnect/reconnect Bluetooth speaker | S3 | NEW (regression) | 2026-03-15 |
| [1957088](https://bugzilla.mozilla.org/show_bug.cgi?id=1957088) | sesame.com — AI voice demo broken with Bluetooth headphones | S3 | NEW (webcompat:site-report) | 2026-02-05 |
| [1824617](https://bugzilla.mozilla.org/show_bug.cgi?id=1824617) | Audio stuttering while using Bluetooth headphones | S3 | UNCONFIRMED | 2026-01-21 |
| [1835986](https://bugzilla.mozilla.org/show_bug.cgi?id=1835986) | Audio and video stutter with Bluetooth output on Android 13 | S3 | NEW | 2026-01-21 |
| [1868267](https://bugzilla.mozilla.org/show_bug.cgi?id=1868267) | Desynched audio channels with Bluetooth AirPods (play/pause clicks) | S3 | UNCONFIRMED | 2026-01-21 |
| [1888896](https://bugzilla.mozilla.org/show_bug.cgi?id=1888896) | A2DP vs HSP/HFP profile switching issue on Windows (padenot) | S3 | NEW | 2026-01-21 |
| [1936931](https://bugzilla.mozilla.org/show_bug.cgi?id=1936931) | Video desyncs with audio after YouTube ads if BT headphones connected | S3 | UNCONFIRMED | 2026-01-21 |
| [1939288](https://bugzilla.mozilla.org/show_bug.cgi?id=1939288) | Videos stutter/pause/buffer when turning off Bluetooth headphones | S3 | UNCONFIRMED | 2026-01-21 |
| [1961555](https://bugzilla.mozilla.org/show_bug.cgi?id=1961555) | Audio stutters on Pixel Buds A-Series during YouTube playlist autoplay (Android) | S3 | UNCONFIRMED | 2026-01-21 |
| [1973353](https://bugzilla.mozilla.org/show_bug.cgi?id=1973353) | Delayed video start/resume by Bluetooth | S3 | UNCONFIRMED | 2026-03-20 |
| [2007835](https://bugzilla.mozilla.org/show_bug.cgi?id=2007835) | Audio stutters with Pixel Buds Pro 2 | S3 | UNCONFIRMED | 2026-01-21 |
| [2008781](https://bugzilla.mozilla.org/show_bug.cgi?id=2008781) | Bluetooth audio stuttering when playing a video | S3 | UNCONFIRMED | 2026-03-04 |
| [2008968](https://bugzilla.mozilla.org/show_bug.cgi?id=2008968) | YouTube stutters at start and on seek with Bluetooth output | S3 | UNCONFIRMED | 2026-01-21 |
| [1706131](https://bugzilla.mozilla.org/show_bug.cgi?id=1706131) | Popping/crackling sounds via Bluetooth in fast-forward | S3 | NEW | 2026-01-21 |
| [1492488](https://bugzilla.mozilla.org/show_bug.cgi?id=1492488) | Can't get audio to work over BT with Bluetooth headset (Windows) | S3 | NEW | 2026-01-21 |
| [1856251](https://bugzilla.mozilla.org/show_bug.cgi?id=1856251) | BT audio goes silent on streaming sites (vidplay, mycloud) after a split-second | S3 | UNCONFIRMED | 2026-01-21 |
| [1861456](https://bugzilla.mozilla.org/show_bug.cgi?id=1861456) | Joining a call with BT headphones causes audio to not work on Pixel 3XL (padenot) | S3 | NEW | 2026-01-21 |

**Timeline:** Individual reports date back to 2018. The meta-bug [2011679](https://bugzilla.mozilla.org/show_bug.cgi?id=2011679) was consolidated by kinetik on 2026-01-21 with 23 deps at creation — suggesting the decision to formally track this as a theme. Two deps are RESOLVED: 1937317 (video stops when headphones removed) was fixed by kinetik in March 2026; 2021805 (wheel-click tweet mutes YouTube) was recently resolved. The foundational fix is the AudioIPC rework ([2024498](https://bugzilla.mozilla.org/show_bug.cgi?id=2024498), ASSIGNED kinetik) which addresses the underlying audio initialization architecture that many of these issues trace back to.

**Stagnation note:** The majority of the 23 meta deps are UNCONFIRMED/NEW and unassigned. Most saw their last non-meta activity prior to January 2026. While the meta itself was recently updated (March 20), individual reports are receiving no direct triage attention.

---

### Theme 2 — AudioIPC / Cubeb Crash & Jank Cluster

**User-facing impact:** Firefox freezes for ~9 seconds when audio tries to initialize while a game is paused in the background (Windows). On Linux/macOS, Firefox can crash with a `futex_wait` panic in the audio system. On mobile, the initialization order of audio IPC causes main-thread blocking. All of these trace to a shared architectural issue in how AudioIPC is initialized — and kinetik is actively working on a fix.

**Breadcrumbs (5)**

| Bug ID | Summary | Severity | Status | Last Changed |
|--------|---------|----------|--------|-------------|
| [2024498](https://bugzilla.mozilla.org/show_bug.cgi?id=2024498) | Rework AudioIPC initialization to avoid blocking parent's main thread | -- | ASSIGNED (kinetik) | 2026-03-23 |
| [2022993](https://bugzilla.mozilla.org/show_bug.cgi?id=2022993) | Crash in [@ syscall \| futex_wait] | S2 | ASSIGNED (kinetik) | 2026-03-22 |
| [2024598](https://bugzilla.mozilla.org/show_bug.cgi?id=2024598) | Crash in [@ mozilla::AudioCallbackDriver::OutputChannelCount] | S3 | NEW | 2026-03-23 |
| [1956979](https://bugzilla.mozilla.org/show_bug.cgi?id=1956979) | 9s jank on PContent::Msg_CreateAudioIPCConnection while game paused | S3 | ASSIGNED (kinetik) | 2026-03-23 |
| [1899317](https://bugzilla.mozilla.org/show_bug.cgi?id=1899317) | Move Cubeb processing to a utility process (Windows) | S3 | ASSIGNED (kinetik) | 2026-03-18 |

**Timeline:** Bug 1899317 (utility process isolation for cubeb, Windows) was opened in May 2024 and has been blocked on the AudioIPC rework ever since. The rework task itself ([2024498](https://bugzilla.mozilla.org/show_bug.cgi?id=2024498)) was filed March 18, 2026 and is actively being worked by kinetik, who is also assigned to the S2 crash [2022993](https://bugzilla.mozilla.org/show_bug.cgi?id=2022993). Resolution of 2024498 will unblock 2022993, 1956979, and 1899317 simultaneously.

**Crash signatures to check in Socorro (enrichment unavailable):**
- [`mozilla::AudioCallbackDriver::OutputChannelCount`](https://crashes.mozilla.org/signatures?q=signature%3A%22mozilla%3A%3AAudioCallbackDriver%3A%3AOutputChannelCount%22)
- [`syscall | std::sys::pal::unix::futex::futex_wait`](https://crashes.mozilla.org/signatures?q=signature%3A%22syscall+%7C+std%3A%3Asys%3A%3Apal%3A%3Aunix%3A%3Afutex%3A%3Afutex_wait%22)

---

### Theme 3 — Android Media Playback / NDK Migration

**User-facing impact:** Firefox for Android is experiencing a topcrash (`topcrash` keyword, S2) affecting Pixel devices on Android 36 in Firefox 148+, traced to a JNI `GetDirectBufferAddress` call failing in `SampleBuffer::WriteToByteBuffer`. Separately, H.264 video playback fails entirely when the "Isolated Content Process" setting is enabled, affecting Samsung Galaxy S24 / Android 16 users on Nightly. Both issues are connected to the ongoing Android Media Codec NDK migration — a massive effort with 70+ tracked sub-bugs.

**Breadcrumbs (5)**

| Bug ID | Summary | Severity | Status | Last Changed |
|--------|---------|----------|--------|-------------|
| [1980764](https://bugzilla.mozilla.org/show_bug.cgi?id=1980764) | [meta] Android Media Codec NDK implementation | -- | NEW (meta, 70+ deps) | 2026-03-13 |
| [2023515](https://bugzilla.mozilla.org/show_bug.cgi?id=2023515) | Crash in [@ JNI CallVoidMethodA / mozilla::jni::Method::Call] (topcrash) | S2 | NEW (jhlin) | 2026-03-21 |
| [2023367](https://bugzilla.mozilla.org/show_bug.cgi?id=2023367) | Videos not playing (H.264 demux fails with Isolated Content Process) | S3 | NEW | 2026-03-21 |
| [2023254](https://bugzilla.mozilla.org/show_bug.cgi?id=2023254) | Fix lifetimes for RemoteMediaDataEncoderChild and RemoteCDMChild | S3 | ASSIGNED (aosmond) | 2026-03-25 |
| [1981478](https://bugzilla.mozilla.org/show_bug.cgi?id=1981478) | Flip prefs to switch to NDK decoding/encoding on Android on Nightly | N/A | NEW (aosmond) | 2026-03-20 |

**Timeline:** The NDK migration meta [1980764](https://bugzilla.mozilla.org/show_bug.cgi?id=1980764) was created August 2025 and represents a deep re-architecture of Android media decoding. The topcrash [2023515](https://bugzilla.mozilla.org/show_bug.cgi?id=2023515) appeared first in Firefox 148 (Android 36 / Pixel devices); jolin@mozilla.com has two patches ready. Bug [2023367](https://bugzilla.mozilla.org/show_bug.cgi?id=2023367) ("Videos not playing") is tied to the Isolated Content Process path interacting poorly with H.264 demuxing — confirmed device-specific (Samsung Galaxy S24 but not Pixel 7). aosmond is actively working on both lifetime fixes and the NDK pref flip.

**Crash signature to check in Socorro:**
- [`mozilla::jni::Method<T>::Call<T>` / `_JNIEnv::CallVoidMethodA`](https://crashes.mozilla.org/signatures?q=signature%3A%22mozilla%3A%3Ajni%3A%3AMethod%3CT%3E%3A%3ACall%3CT%3E%22)

---

### Theme 4 — A/V Sync Regression at Playback Speed Change

**User-facing impact:** On YouTube (and other sites using MSE), repeatedly toggling playback speed (2x) causes audio and video to progressively drift out of sync. Seeking temporarily resets the drift. This is a cross-platform regression (Windows, macOS, Linux, Android) introduced by bug 1752345 that has now been open for over 12 months with no fix landed. Community-submitted duplicate reports continue to arrive.

**Breadcrumbs (5)**

| Bug ID | Summary | Severity | Status | Last Changed |
|--------|---------|----------|--------|-------------|
| [1955841](https://bugzilla.mozilla.org/show_bug.cgi?id=1955841) | Video and Audio gets out of sync if 2x is used on YouTube | S3 | NEW (regression) | 2026-03-23 |
| [2007762](https://bugzilla.mozilla.org/show_bug.cgi?id=2007762) | Audio/video desync toggling playback speed on YouTube (Arch Linux / PipeWire) | S3 | NEW | 2026-03-22 |
| [2023823](https://bugzilla.mozilla.org/show_bug.cgi?id=2023823) | MSE audio track desyncs from video on loop seek via ended event | S3 | UNCONFIRMED | 2026-03-21 |
| [2023568](https://bugzilla.mozilla.org/show_bug.cgi?id=2023568) | Use a single rlbox sandbox for all soundtouch instances | S2 | NEW | 2026-03-20 |
| [2024183](https://bugzilla.mozilla.org/show_bug.cgi?id=2024183) | Don't allocate time stretcher on the audio thread | S3 | NEW | 2026-03-21 |

**Timeline:** [1955841](https://bugzilla.mozilla.org/show_bug.cgi?id=1955841) was filed March 23, 2025 — exactly one year ago — on Nightly 138.0a1. It carries `nightly-community` and `regression` keywords, has 26 comments, and has been confirmed on AMD, Intel, and various platforms. padenot was identified as the regressor author (bug 1752345) and needinfo'd, but noted limited availability. Duplicate bugs confirmed: 1971227, 1979560, 1938766 (4 total reports with near-identical symptom descriptions from unrelated reporters). Bugs 2023568 and 2024183 are refactoring work on the soundtouch/time-stretcher path — these are relevant to the same code area.

**Stagnation note:** [1955841](https://bugzilla.mozilla.org/show_bug.cgi?id=1955841) is an S3 regression open for >12 months. While it received recent comment activity (March 23, 2026), no patch has been proposed and no engineer has been assigned. **This warrants escalation.**

---

### Theme 5 — Hardware Video Decoding Failures (AV1, Flatpak, Tegra)

**User-facing impact:** Several distinct but related hardware decoding failures: (1) high-bitrate AV1 videos on YouTube freeze with a spinning CPU due to a busy-wait bug in `DAV1DDecoder` — a community contributor has provided a patch but no reviewer has been assigned; (2) both H.264 and HEVC hardware decoding fail entirely in Firefox flatpak builds (Steam Deck, Linux); (3) Nvidia Tegra devices regressed in Firefox 142+ with no regressionwindow identified yet.

**Breadcrumbs (6)**

| Bug ID | Summary | Severity | Status | Last Changed |
|--------|---------|----------|--------|-------------|
| [2016484](https://bugzilla.mozilla.org/show_bug.cgi?id=2016484) | High-bitrate AV1 freezes: DAV1DDecoder busy-waits on EAGAIN | S2 | NEW | 2026-03-20 |
| [2021122](https://bugzilla.mozilla.org/show_bug.cgi?id=2021122) | HEVC video doesn't play in flatpak builds | S3 | NEW | 2026-03-21 |
| [2020823](https://bugzilla.mozilla.org/show_bug.cgi?id=2020823) | h264 video not decoded with hardware in flatpak build | S3 | NEW | 2026-03-11 |
| [2016587](https://bugzilla.mozilla.org/show_bug.cgi?id=2016587) | Nvidia Tegra Video HW Decoding Regression with Firefox 142+ | S3 | NEW (regression) | 2026-03-15 |
| [1867638](https://bugzilla.mozilla.org/show_bug.cgi?id=1867638) | [meta] Steam Deck related issues (Arch Linux flatpak) | meta | NEW | 2026-03-04 |
| [2008617](https://bugzilla.mozilla.org/show_bug.cgi?id=2008617) | 4K AV1 Video decode doesn't work on YouTube | S3 | UNCONFIRMED | 2026-03-19 |

**Timeline:** Bug [2016484](https://bugzilla.mozilla.org/show_bug.cgi?id=2016484) (AV1 freeze, S2) was filed February 12, 2026. The root cause is a confirmed busy-wait loop in the dav1d EAGAIN path. A community contributor (`bran.perch-07@icloud.com`) attached two progressively-refined patches; bug 1999830 was marked a duplicate. Despite 14 comments and a working fix, no Mozilla engineer has reviewed the patch as of March 20. The flatpak issues (2020823, 2021122) are tracked under the Steam Deck meta [1867638](https://bugzilla.mozilla.org/show_bug.cgi?id=1867638) — both are unassigned and reflect flatpak sandbox restrictions blocking VA-API/GStreamer access. The Tegra regression [2016587](https://bugzilla.mozilla.org/show_bug.cgi?id=2016587) is flagged `regressionwindow-wanted`, meaning bisection hasn't been done.

**Action item:** [2016484](https://bugzilla.mozilla.org/show_bug.cgi?id=2016484) has a community-submitted patch ready for review. An S2 bug with a working fix and no reviewer is a missed opportunity.

---

### Theme 6 — Media Sleep / Power Management (Screen Inhibitor)

**User-facing impact:** Firefox's media playback fails to properly signal the OS sleep inhibitor in multiple scenarios: the screen saver activates during video playback, the PC doesn't sleep when it should (audio tabs keeping it awake), macOS prevents sleep because Firefox keeps CoreAudio active unnecessarily, and video playback drops after waking from sleep. The inverse problem also exists: video keeps the screen awake even after it ends.

**Breadcrumbs (12)**

| Bug ID | Summary | Severity | Status | Last Changed |
|--------|---------|----------|--------|-------------|
| [2023379](https://bugzilla.mozilla.org/show_bug.cgi?id=2023379) | [meta] Media Related Sleep Issues | S3 | NEW (meta, 16 deps) | 2026-03-23 |
| [2013720](https://bugzilla.mozilla.org/show_bug.cgi?id=2013720) | Screen saver activates when streaming video on Linux Mint | S3 | UNCONFIRMED | 2026-03-16 |
| [1519935](https://bugzilla.mozilla.org/show_bug.cgi?id=1519935) | Windows Sleep mode causes all video to unexpectedly stop after waking | S3 | NEW | 2026-03-15 |
| [1606331](https://bugzilla.mozilla.org/show_bug.cgi?id=1606331) | Netflix video continues after sleep but sound stops | S3 | NEW | 2026-03-15 |
| [1821102](https://bugzilla.mozilla.org/show_bug.cgi?id=1821102) | Firefox keeps coreaudiod active, preventing macOS sleep | S3 | UNCONFIRMED | 2026-03-15 |
| [1851996](https://bugzilla.mozilla.org/show_bug.cgi?id=1851996) | Audio prevents PC from sleep | S3 | UNCONFIRMED | 2026-03-15 |
| [1869101](https://bugzilla.mozilla.org/show_bug.cgi?id=1869101) | After sleep wake, video is very slow and choppy (not Edge) | S3 | UNCONFIRMED | 2026-03-15 |
| [1913428](https://bugzilla.mozilla.org/show_bug.cgi?id=1913428) | End of video in fullscreen doesn't trigger system sleep timer | S3 | UNCONFIRMED | 2026-03-15 |
| [1936430](https://bugzilla.mozilla.org/show_bug.cgi?id=1936430) | BT headphone disconnect causes YouTube playback to stall | S3 | NEW | 2026-03-15 |
| [1961596](https://bugzilla.mozilla.org/show_bug.cgi?id=1961596) | Unmuted video does not play after computer sleep on OSX | S3 | UNCONFIRMED | 2026-03-15 |
| [1977132](https://bugzilla.mozilla.org/show_bug.cgi?id=1977132) | Media playback resumes on Windows lock screen after waking from sleep | S3 | NEW (parity-chrome) | 2026-03-15 |
| [1984927](https://bugzilla.mozilla.org/show_bug.cgi?id=1984927) | Display goes to sleep while watching YouTube videos | S3 | NEW | 2026-03-14 |

**Timeline:** Individual sleep/inhibitor bugs go back to 2019. The meta [2023379](https://bugzilla.mozilla.org/show_bug.cgi?id=2023379) was created March 14, 2026, consolidating 16 long-standing bugs. Bug [2011578](https://bugzilla.mozilla.org/show_bug.cgi?id=2011578) ("Firefox stops audio when monitor sleeps") was recently RESOLVED by kinetik. Otherwise, no deps have an active assignee and most are UNCONFIRMED. The pattern of all 16 deps being touched on March 15 (when the meta was linked) gives a false impression of recent activity — the underlying reports range from 2019 to early 2026.

**Stagnation note:** Most of the 16 meta deps have had no meaningful engineer engagement beyond being linked to the meta. Several (1519935, 1606331, 1821102) have been open for 3–6 years. This is a long-standing, multi-platform category with no current assignee.

---

### Theme 7 — Matroska/MKV Support Gaps

**User-facing impact:** Firefox gained initial Matroska (MKV) support in late 2025. However, significant gaps remain: HEVC/H.265 in MKV silently fails on malformed codec private data, buffering behavior forces the entire file to be downloaded before playback begins, HEVC playback freezes on seek, and several audio codecs (MP3, FLAC, PCM) in MKV containers aren't yet supported.

**Breadcrumbs (8)**

| Bug ID | Summary | Severity | Status | Last Changed |
|--------|---------|----------|--------|-------------|
| [1422891](https://bugzilla.mozilla.org/show_bug.cgi?id=1422891) | [meta] Support mkv\|matroska\|video/x-matroska in Firefox | S3 | NEW (meta, 22 deps, alwu) | 2026-03-23 |
| [2025302](https://bugzilla.mozilla.org/show_bug.cgi?id=2025302) | HEVC/H.265 in Matroska silently fails with malformed hvcC | S3 | NEW | 2026-03-23 |
| [2000420](https://bugzilla.mozilla.org/show_bug.cgi?id=2000420) | Playback wants to buffer the whole file if MKV | S3 | NEW (alwu) | 2026-03-23 |
| [2006226](https://bugzilla.mozilla.org/show_bug.cgi?id=2006226) | HEVC Video in MKV freezes when seeking | S3 | NEW | 2025-12-31 |
| [1988447](https://bugzilla.mozilla.org/show_bug.cgi?id=1988447) | Support Matroska in MSE | -- | NEW (15 comments) | 2025-10-07 |
| [1991747](https://bugzilla.mozilla.org/show_bug.cgi?id=1991747) | Support MP3 in Matroska | S3 | NEW | 2026-03-23 |
| [1991746](https://bugzilla.mozilla.org/show_bug.cgi?id=1991746) | Support FLAC in Matroska | N/A | NEW | 2025-11-15 |
| [1987783](https://bugzilla.mozilla.org/show_bug.cgi?id=1987783) | Proper handle decoder delay for audio codecs in Matroska | -- | NEW (alwu) | 2025-09-16 |

**Timeline:** The Matroska meta [1422891](https://bugzilla.mozilla.org/show_bug.cgi?id=1422891) has been open since December 2017. Major implementation work was completed by alwu in Q3–Q4 2025 (sniffing, basic codec support, telemetry, enabled by default in Nov 2025). Remaining open work includes the buffering regression [2000420](https://bugzilla.mozilla.org/show_bug.cgi?id=2000420), HEVC edge cases, MSE support, and additional codec support. alwu owns the meta and several open deps — this is an active area with a clear owner.

---

### Theme 8 — WebCodecs Regressions

**User-facing impact:** Applying a CSS rotation transform to a `<video>` element causes incorrect color rendering (green/blue tint) — a regression in the WebCodecs pipeline. A separate crash (`EncoderAgent::Dry`) occurs when encoding is attempted in an edge case. A late-beta test regression was also identified affecting 10-bit video rendering.

**Breadcrumbs (4)**

| Bug ID | Summary | Severity | Status | Last Changed |
|--------|---------|----------|--------|-------------|
| [2023594](https://bugzilla.mozilla.org/show_bug.cgi?id=2023594) | Applying a rotation to a video causes colors to shift | S3 | NEW (regression) | 2026-03-20 |
| [2025750](https://bugzilla.mozilla.org/show_bug.cgi?id=2025750) | [Late Beta] Perma reftest image-10bits-rendering-90-video.html fails when Gecko 151 hits beta | S3 | NEW (regression) | 2026-03-24 |
| [2016501](https://bugzilla.mozilla.org/show_bug.cgi?id=2016501) | crash at null in [@ mozilla::EncoderAgent::Dry] | S3 | NEW (crash, testcase, padenot) | 2026-03-10 |
| [2021505](https://bugzilla.mozilla.org/show_bug.cgi?id=2021505) | Check bit depth for codec | S4 | NEW (chunmin) | 2026-03-06 |

**Timeline:** [2023594](https://bugzilla.mozilla.org/show_bug.cgi?id=2023594) was filed March 16, 2026 with 13 comments and a testcase — strong engagement, no patch yet, unassigned. Bug [2025750](https://bugzilla.mozilla.org/show_bug.cgi?id=2025750) was filed March 24 (yesterday) and explicitly connects to the same `image-10bits-rendering-90` test that [2023594](https://bugzilla.mozilla.org/show_bug.cgi?id=2023594) involves — these two are likely related. Together with [2016501](https://bugzilla.mozilla.org/show_bug.cgi?id=2016501) (crash, padenot), this theme appears to represent an emerging quality issue in the WebCodecs video processing path.

**Emerging theme flag:** The co-location of a color-shift regression, a 10-bit rendering test failure, and an encoder null-crash in the WebCodecs area suggests a common underlying issue in color/bit-depth handling after a recent change. Worth connecting these dots before beta.

---

### Theme 9 — Privacy: Audio Device Name PII Leak (Emerging)

**User-facing impact:** The `about:support` page includes audio device names in its output. When users share this information for debugging, they inadvertently expose device names that can contain personally identifiable information (e.g., names like "John's AirPods" or custom speaker labels).

**Breadcrumbs (1 — below threshold but S2 warrants mention)**

| Bug ID | Summary | Severity | Status | Last Changed |
|--------|---------|----------|--------|-------------|
| [2023970](https://bugzilla.mozilla.org/show_bug.cgi?id=2023970) | about:support can leak PII via audio device names | S2 | NEW | 2026-03-24 |

> **Note:** This theme has only 1 breadcrumb and falls below the 3-breadcrumb minimum for inclusion in the ranked summary. However, it carries an **S2 severity** and was filed March 17. Given the privacy impact and the lack of any assignee, it is surfaced here for immediate triage attention.

---

## Closing

### Ranked Signal Summary

| Rank | Theme | Breadcrumbs | Meta-bug | Top Severity | Notes |
|------|-------|-------------|----------|-------------|-------|
| 1 | Bluetooth Audio Device Issues | 25 | [2011679](https://bugzilla.mozilla.org/show_bug.cgi?id=2011679) (23 deps) | S2 | Cross-platform, multi-year backlog, mostly unassigned; AudioIPC rework (2024498) is the key unblocking work |
| 2 | AudioIPC / Cubeb Crash & Jank Cluster | 5 | — | S2 | Active (kinetik), S2 crash blocked on architectural fix; 2024498 is the linchpin |
| 3 | Android Media / NDK Migration | 5 | [1980764](https://bugzilla.mozilla.org/show_bug.cgi?id=1980764) (70+ deps) | S2 | Active (jhlin, aosmond); topcrash with patches ready for review |
| 4 | A/V Sync Regression at Speed Change | 5 | — | S3 | Year-old regression, 4 dupes, cross-platform, no owner — **escalation warranted** |
| 5 | Hardware Video Decoding Failures | 6 | [1867638](https://bugzilla.mozilla.org/show_bug.cgi?id=1867638) | S2 | S2 AV1 bug has community patch with no reviewer; flatpak issues unassigned |
| 6 | Media Sleep / Power Management | 12 | [2023379](https://bugzilla.mozilla.org/show_bug.cgi?id=2023379) (16 deps) | S3 | Multi-year stagnation, all unassigned; meta newly created |
| 7 | Matroska/MKV Support Gaps | 8 | [1422891](https://bugzilla.mozilla.org/show_bug.cgi?id=1422891) (22 deps) | S3 | Active (alwu); significant progress already landed, remaining work clear |
| 8 | WebCodecs Regressions | 4 | — | S3 | Emerging: color-shift + 10-bit test failure may share root cause; needs owner |

---

### Resources Used

| Resource | Detail |
|----------|--------|
| Bugzilla REST API | 7 batch queries, ~120 total bugs fetched |
| Dep crawl depth | 2 (meta deps + shared deps) |
| socorro-cli | Unavailable (TLS error: OSStatus -26276) — crash volume enrichment skipped |
| Crash signatures for manual follow-up | `mozilla::AudioCallbackDriver::OutputChannelCount`, `syscall \| futex_wait`, `mozilla::EncoderAgent::Dry`, `mozilla::jni::Method<T>::Call<T>` |

---

### Suggestions for Skill Improvement

- **Crash enrichment fallback:** When `socorro-cli` fails, attempt a WebFetch to the Socorro REST API (`https://crash-stats.mozilla.org/api/SuperSearch/`) as a fallback path before marking enrichment as skipped.
- **cc_count detection:** The field appears absent from the Bugzilla REST API without authentication. Consider requesting `cc` array length instead, or noting at session start that cc_count scoring will be unavailable.
- **Stagnation age bands:** The current stagnation rule is binary (30/90 days). Adding a "very stagnant" tier (180+ days for S3 regressions) would surface buried long-term issues like 1955841 more clearly.
- **Duplicate detection:** For the A/V sync theme, the 4 duplicate bugs (1955841, 1971227, 1979560, 1938766) were identified through comment analysis. A dedicated duplication signal in Step 4 keyword expansion (searching for `dupe of` relationships) could surface this cluster more reliably.

---

> *"The game is afoot — you have only to follow the chain of clues, and each breadcrumb will lead you, however circuitously, to the truth."*
