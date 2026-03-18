# Bugzilla Wrangler Report: WebRTC / Web Conferencing
**Generated:** 2026-03-18

---

## Session Info

| Field | Value |
|---|---|
| **Scope profile** | `web-conferencing` — Core: WebRTC, WebRTC: Audio/Video, WebRTC: Networking, WebRTC: Signaling |
| **Seed timeframe** | 2025-12-18 to 2026-03-18 (last 3 months) |
| **Seed count** | 45 unique |
| **Seed mode** | mixed-seed (38 created + 7 changed = 45 unique) |
| **Cache freshness** | Fresh — fetched this session (2026-03-18) |

---

## Seed Info

### Seed Bug List (by priority)

**P1**
- [2014357](https://bugzilla.mozilla.org/show_bug.cgi?id=2014357) — Enable two byte RTP header extension ids (S2, NEW)

**P2**
- [2021379](https://bugzilla.mozilla.org/show_bug.cgi?id=2021379) — Crash in CamerasParent async shutdown (S2, NEW)
- [2016455](https://bugzilla.mozilla.org/show_bug.cgi?id=2016455) — Crash in RTCDataChannel::AnnounceClosed cycle collector (S2, NEW)
- [2015946](https://bugzilla.mozilla.org/show_bug.cgi?id=2015946) — Google Meet crash: WebRTC destroys connected PipeWire stream (S2, ASSIGNED)
- [2023103](https://bugzilla.mozilla.org/show_bug.cgi?id=2023103) — Crash in abort|BuildFormat (S3, ASSIGNED)
- [2018955](https://bugzilla.mozilla.org/show_bug.cgi?id=2018955) — WebRTC playout fails silently at 768 kHz on macOS (S3, NEW)
- [2019330](https://bugzilla.mozilla.org/show_bug.cgi?id=2019330) — Implement RTCIceTransport.component (S2, NEW)
- [2019331](https://bugzilla.mozilla.org/show_bug.cgi?id=2019331) — Implement RTCTransportStats.selectedCandidatePairId (S2, NEW)
- [2019333](https://bugzilla.mozilla.org/show_bug.cgi?id=2019333) — Implement RTCTransportStats.remote/localCertificateId (S2, NEW)
- [2019349](https://bugzilla.mozilla.org/show_bug.cgi?id=2019349) — Implement RTCTransportStats.bytesSent/bytesReceived (S2, NEW)
- [2019355](https://bugzilla.mozilla.org/show_bug.cgi?id=2019355) — Implement RTCTransportStats.iceRole (S2, NEW)
- [2019356](https://bugzilla.mozilla.org/show_bug.cgi?id=2019356) — Implement RTCTransportStats.dtlsState/dtlsRole (S2, NEW)
- [2019359](https://bugzilla.mozilla.org/show_bug.cgi?id=2019359) — Implement RTCRtcpParameters.reducedSize (S2, NEW)
- [2019389](https://bugzilla.mozilla.org/show_bug.cgi?id=2019389) — Implement RTCTransportStats.tlsVersion/dtlsCipher/srtpCipher (S2, NEW)
- [2019375](https://bugzilla.mozilla.org/show_bug.cgi?id=2019375) — Get real h264 plugin working in wpt.fyi CI (S2, ASSIGNED)
- [2021075](https://bugzilla.mozilla.org/show_bug.cgi?id=2021075) — Throw when RTCIceServer.credential is empty (S2, NEW)
- [2019378](https://bugzilla.mozilla.org/show_bug.cgi?id=2019378) — Determine correctness of RTCSctpTransport-maxChannels.html (S2, NEW)
- [2019361](https://bugzilla.mozilla.org/show_bug.cgi?id=2019361) — Determine correctness of RTCSctpTransport-events.html (S2, NEW)
- [2019346](https://bugzilla.mozilla.org/show_bug.cgi?id=2019346) — Fix RTCPeerConnection-iceConnectionState.https.html failures (S2, NEW)
- [2019370](https://bugzilla.mozilla.org/show_bug.cgi?id=2019370) — Disable setParameters compat mode in wpt (S2, NEW)
- [2019365](https://bugzilla.mozilla.org/show_bug.cgi?id=2019365) — Fix RTCDataChannel-GC.html failure (S2, NEW)
- [2019461](https://bugzilla.mozilla.org/show_bug.cgi?id=2019461) — Fix protocol/handover-datachannel.html (S2, NEW)
- [2019469](https://bugzilla.mozilla.org/show_bug.cgi?id=2019469) — protocol/rtp-headerextensions.html recvonly extmap failure (S2, NEW)
- [2019332](https://bugzilla.mozilla.org/show_bug.cgi?id=2019332) — Implement RTCIceTransport.getSelectedCandidatePair() (S2, NEW)
- [1617686](https://bugzilla.mozilla.org/show_bug.cgi?id=1617686) — Validate ice-ufrag and ice-pwd for invalid characters (S2, ASSIGNED)
- [2013936](https://bugzilla.mozilla.org/show_bug.cgi?id=2013936) — SDP with h264 profile_level_id > 5 crashes tab (S3, ASSIGNED)
- [2010655](https://bugzilla.mozilla.org/show_bug.cgi?id=2010655) — script-metadata-transform.https.html times out on wpt.fyi (S3, NEW)
- [1571470](https://bugzilla.mozilla.org/show_bug.cgi?id=1571470) — Support webrtc-svc (scalabilityMode) (S3, ASSIGNED)

**P3**
- [2023893](https://bugzilla.mozilla.org/show_bug.cgi?id=2023893) — [meta] Interop 2025 Script Transform wpt.fyi timeouts (S3, NEW)
- [2017189](https://bugzilla.mozilla.org/show_bug.cgi?id=2017189) — AV1 WebRTC decoding hangs instantly when streaming (S3, NEW)
- [2022422](https://bugzilla.mozilla.org/show_bug.cgi?id=2022422) — Origin spoofing in unused PeerConnectionBlocker mechanism (S3, NEW)
- [2016862](https://bugzilla.mozilla.org/show_bug.cgi?id=2016862) — WebRTC: Decoded color_space overwritten with nullopt (S3, NEW)
- [2019255](https://bugzilla.mozilla.org/show_bug.cgi?id=2019255) — TURN with TLS doesn't work with IP + valid certificate (S3, UNCONFIRMED)
- [2020362](https://bugzilla.mozilla.org/show_bug.cgi?id=2020362) — Mishandling of relay-based peer reflexive candidates (S3, NEW)
- [2004466](https://bugzilla.mozilla.org/show_bug.cgi?id=2004466) — recommended_probe_size assertion in pacing_controller.cc (S3, NEW)
- [2010661](https://bugzilla.mozilla.org/show_bug.cgi?id=2010661) — script-change-transform.https.html times out (S3, NEW)
- [2010663](https://bugzilla.mozilla.org/show_bug.cgi?id=2010663) — script-write-twice-transform.https.html times out (S3, NEW)
- [2010667](https://bugzilla.mozilla.org/show_bug.cgi?id=2010667) — RTCRtpScriptTransform-encoded-transform.https.html times out (S3, NEW)
- [2005780](https://bugzilla.mozilla.org/show_bug.cgi?id=2005780) — script-transform-generateKeyFrame-simulcast.https.html unreliable on Windows (S3, NEW)
- [1667635](https://bugzilla.mozilla.org/show_bug.cgi?id=1667635) — AbortError from getUserMedia until Firefox restarted (S3, UNCONFIRMED, old)

**Other (P--, recently changed)**
- [2021448](https://bugzilla.mozilla.org/show_bug.cgi?id=2021448) — Assertion: mDtmfEnabled at AudioConduit.cpp:265 (S3, NEW)
- [2021480](https://bugzilla.mozilla.org/show_bug.cgi?id=2021480) — Check failed: streams[i].width > 0 (S3, NEW)
- [2021446](https://bugzilla.mozilla.org/show_bug.cgi?id=2021446) — Assertion failure at PeerConnectionImpl.cpp:1400 (S3, NEW)
- [910249](https://bugzilla.mozilla.org/show_bug.cgi?id=910249) — [meta] Finish implementation of MediaStream.webidl (S3, NEW, old)
- [1776143](https://bugzilla.mozilla.org/show_bug.cgi?id=1776143) — Crash in SCTP sctp_inpcb_free | sctp_close (S3, NEW)

### Seed Timeline

Seed date window: Dec 18, 2025 – Mar 18, 2026

```
Dec 2025  |  Jan 2026  |     Feb 2026     |     Mar 2026
----------+------------+------------------+------------------
 **         ****        *************************   *********
  2          4                25                      9+5(old)
```

> Note: The Feb 2026 spike (25 of 38 created bugs) reflects a coordinated burst of
> Interop 2026 WebRTC wpt.fyi filing activity around Feb 25. This is an artifact
> of planned triage, not a real crisis spike. The 5 "old" bugs in the seed came from
> the recently-changed query (1667635, 910249, 1571470, 1776143, 1617686).

---

## Theme 1: RTCDataChannel Lifecycle Crash — Use-After-Free (S2, >1000 crashes/30d)

**User-facing impact:** Firefox tab crashes silently during or after video/audio calls that use WebRTC data channels. The crash occurs in the content process when `RTCDataChannel::AnnounceClosed` is called during cycle collection of a reference-counted object, indicating a use-after-free or teardown ordering bug. With 1,296 reports in the past 30 days — and rising — this is the highest-volume crash in the WebRTC components.

### Breadcrumbs

| Bug ID | Summary | Severity | Status | Last Changed |
|--------|---------|----------|--------|--------------|
| [2016455](https://bugzilla.mozilla.org/show_bug.cgi?id=2016455) | Crash in NS_CycleCollectorSuspect3 / nsCycleCollectingAutoRefCnt::decr (RTCDataChannel::AnnounceClosed) | S2 | NEW | 2026-03-17 |

**Crash Volume (30d):** [1,296 reports](https://crashes.mozilla.org/signatures?q=signature%3A%22NS_CycleCollectorSuspect3%20%7C%20nsCycleCollectingAutoRefCnt%3A%3Adecr%22)
- Prior 30d: 1,001 — **Trend: rising (+29%)**
- Top platform: Windows NT (74%), Mac OS X (16%), Linux (10%)
- Process type: content (99%), parent (1%)

### Timeline

Filed 2026-02-12. Only one comment. No assignee. The crash predates the Interop 2026 work burst — it wasn't triaged as part of any meta effort. The signature `NS_CycleCollectorSuspect3` is broad (a cycle collector instrumentation hook) but the notes in the bug specifically identify `RTCDataChannel::AnnounceClosed` as the call site, narrowing the likely cause to an RTCDataChannel object being suspect-scanned after it has already been partially torn down.

### Stagnation

> **Stagnation Alert:** This S2 crash has **no assignee and minimal triage activity** since filing, despite exceeding the 1,000-crash/30d threshold. The rising trend adds urgency. This should be escalated.

---

## Theme 2: CamerasParent Async Shutdown Hang Crash (S2, 663 crashes/30d, Rising)

**User-facing impact:** Firefox crashes during shutdown (when a tab using the camera or a WebRTC call is closed) because the CamerasParent component does not shut down within the async shutdown timeout. Affects users who use getUserMedia for camera access — video calls, virtual backgrounds, browser-based camera tools. The crash is widespread across Windows and Linux.

### Breadcrumbs

| Bug ID | Summary | Severity | Status | Last Changed |
|--------|---------|----------|--------|--------------|
| [2021379](https://bugzilla.mozilla.org/show_bug.cgi?id=2021379) | Crash in AsyncShutdownTimeout / profile-before-change / CamerasParent | S2 | NEW | 2026-03-17 |
| [1951799](https://bugzilla.mozilla.org/show_bug.cgi?id=1951799) | Intermittent assertion failure: !singleton().mCameras at CamerasChild.h:84 | S3 | NEW | 2025-07-22 |

**Crash Volume (30d):** [663 reports](https://crashes.mozilla.org/signatures?q=signature%3A%22AsyncShutdownTimeout%20%7C%20profile-before-change%20%7C%20CamerasParent%22)
- Prior 30d: 518 — **Trend: rising (+28%)**
- Top platform: Windows NT (86%), Linux (10%), Mac OS X (3%)
- Process type: parent (95%), main (5%)

### Timeline

Bug 2021379 filed 2026-03-05, P2, no assignee. The intermittent assertion in 1951799 (filed March 2025) is likely related — both involve the `CamerasChild`/`CamerasParent` IPC pair being torn down in a race condition. The rising trend across two consecutive 30-day windows suggests this is not a one-off but a structural issue in camera IPC teardown.

---

## Theme 3: abort|BuildFormat Linux Crash — Explosive Growth (S3, 198/30d, +421%)

**User-facing impact:** Firefox crashes on Linux while negotiating media format parameters during a WebRTC session. The `abort | BuildFormat` signature indicates a hard abort inside codec format construction. All 198 crashes in the past 30 days are exclusively on **Linux**, and the trend is a dramatic 5x increase compared to the prior window (38 reports). This is a strong emerging signal.

### Breadcrumbs

| Bug ID | Summary | Severity | Status | Last Changed |
|--------|---------|----------|--------|--------------|
| [2023103](https://bugzilla.mozilla.org/show_bug.cgi?id=2023103) | Crash in abort \| BuildFormat | S3 | ASSIGNED | 2026-03-17 |

**Crash Volume (30d):** [198 reports](https://crashes.mozilla.org/signatures?q=signature%3A%22abort%20%7C%20BuildFormat%22)
- Prior 30d: 38 — **Trend: strongly rising (+421%)**
- Platform: **Linux only** (100%)
- Process type: parent (100%)

### Timeline

Filed 2026-03-13, assigned. The Linux-only and parent-process nature points to a Linux-specific code path in WebRTC audio/video codec negotiation. The explosive trend starting in this window is notable — this may be tied to a recent libwebrtc vendored update or a Linux kernel/driver interaction. Actively assigned.

---

## Theme 4: Google Meet / PipeWire Stream Crash (S2, Active)

**User-facing impact:** Google Meet (and potentially other WebRTC video conferencing services) crashes Firefox on Linux systems using PipeWire. The WebRTC stack attempts to destroy a PipeWire stream that is still connected, causing an invalid state crash. This affects the broad and growing base of Linux desktop users running modern distributions with PipeWire as the audio/video subsystem (Fedora, Ubuntu 22.04+, Arch, etc.).

### Breadcrumbs

| Bug ID | Summary | Severity | Status | Last Changed |
|--------|---------|----------|--------|--------------|
| [2015946](https://bugzilla.mozilla.org/show_bug.cgi?id=2015946) | Google Meet crashes — WebRTC tries to destroy connected PipeWire stream | S2 | ASSIGNED | 2026-03-17 |

### Timeline

Filed 2026-02-10. Actively assigned with 11 comments. No crash keyword, so no Socorro cross-reference is available, but the user-reported failure mode is clear: Google Meet calls crash the tab on PipeWire systems. PipeWire has been the default on major distros since 2022+. This is actively being worked.

---

## Theme 5: Interop 2026 WebRTC — WPT Compliance Gaps (Major Theme)

**User-facing impact:** Firefox's WebRTC implementation is missing or has broken implementations of key APIs required for Interop 2026: `RTCTransportStats`, `RTCIceTransport`, RTP header extensions, DTLS/RTCP parameters, H.264 codec support in CI, and various test suite failures in wpt.fyi. These gaps cause Firefox to score lower on the Interop benchmark, and some gaps (e.g., missing stats fields, broken ICE state reporting) affect real-world application compatibility.

### Breadcrumbs

| Bug ID | Summary | Severity | Status | Last Changed |
|--------|---------|----------|--------|--------------|
| [2017363](https://bugzilla.mozilla.org/show_bug.cgi?id=2017363) | [meta] Interop 2026 WebRTC (41 deps) | -- | NEW | 2026-02-26 |
| [2014357](https://bugzilla.mozilla.org/show_bug.cgi?id=2014357) | Enable two byte RTP header extension ids | S2 | NEW | 2026-02-26 |
| [2019375](https://bugzilla.mozilla.org/show_bug.cgi?id=2019375) | Get real h264 plugin working in wpt.fyi CI | S2 | ASSIGNED | 2026-03-10 |
| [2019330](https://bugzilla.mozilla.org/show_bug.cgi?id=2019330) | Implement RTCIceTransport.component | S2 | NEW | 2026-03-13 |
| [2019331](https://bugzilla.mozilla.org/show_bug.cgi?id=2019331) | Implement RTCTransportStats.selectedCandidatePairId | S2 | NEW | 2026-03-13 |
| [2019333](https://bugzilla.mozilla.org/show_bug.cgi?id=2019333) | Implement RTCTransportStats.remote/localCertificateId | S2 | NEW | 2026-03-13 |
| [2019349](https://bugzilla.mozilla.org/show_bug.cgi?id=2019349) | Implement RTCTransportStats.bytesSent/bytesReceived | S2 | NEW | 2026-03-13 |
| [2019355](https://bugzilla.mozilla.org/show_bug.cgi?id=2019355) | Implement RTCTransportStats.iceRole | S2 | NEW | 2026-03-13 |
| [2019356](https://bugzilla.mozilla.org/show_bug.cgi?id=2019356) | Implement RTCTransportStats.dtlsState/dtlsRole | S2 | NEW | 2026-03-13 |
| [2019359](https://bugzilla.mozilla.org/show_bug.cgi?id=2019359) | Implement RTCRtcpParameters.reducedSize | S2 | NEW | 2026-03-13 |
| [2019389](https://bugzilla.mozilla.org/show_bug.cgi?id=2019389) | Implement RTCTransportStats.tlsVersion/dtlsCipher/srtpCipher | S2 | NEW | 2026-03-13 |
| [2019332](https://bugzilla.mozilla.org/show_bug.cgi?id=2019332) | Implement RTCIceTransport.getSelectedCandidatePair() | S2 | NEW | 2026-02-26 |
| [2019346](https://bugzilla.mozilla.org/show_bug.cgi?id=2019346) | Fix RTCPeerConnection-iceConnectionState failures | S2 | NEW | 2026-02-26 |
| [2019361](https://bugzilla.mozilla.org/show_bug.cgi?id=2019361) | Determine correctness of RTCSctpTransport-events.html | S2 | NEW | 2026-03-03 |
| [2019365](https://bugzilla.mozilla.org/show_bug.cgi?id=2019365) | Fix failure in RTCDataChannel-GC.html | S2 | NEW | 2026-02-26 |
| [2019370](https://bugzilla.mozilla.org/show_bug.cgi?id=2019370) | Disable setParameters compat mode in wpt | S2 | NEW | 2026-02-26 |
| [2019378](https://bugzilla.mozilla.org/show_bug.cgi?id=2019378) | Determine correctness of RTCSctpTransport-maxChannels | S2 | NEW | 2026-03-03 |
| [2019461](https://bugzilla.mozilla.org/show_bug.cgi?id=2019461) | Fix protocol/handover-datachannel.html | S2 | NEW | 2026-02-26 |
| [2019469](https://bugzilla.mozilla.org/show_bug.cgi?id=2019469) | rtp-headerextensions.html recvonly extmap failure | S2 | NEW | 2026-02-26 |
| [2021075](https://bugzilla.mozilla.org/show_bug.cgi?id=2021075) | Throw when RTCIceServer.credential is empty | S2 | NEW | 2026-03-04 |
| [1617686](https://bugzilla.mozilla.org/show_bug.cgi?id=1617686) | Validate ice-ufrag and ice-pwd for invalid characters | S2 | ASSIGNED | 2026-03-13 |
| [1225723](https://bugzilla.mozilla.org/show_bug.cgi?id=1225723) | [parent] Implement RTCTransportStats | S3 | NEW | 2026-02-25 |
| [1307994](https://bugzilla.mozilla.org/show_bug.cgi?id=1307994) | [parent] Implement RTCIceTransport interface | S3 | NEW | 2026-02-25 |

### Timeline

The Interop 2026 meta bug [2017363](https://bugzilla.mozilla.org/show_bug.cgi?id=2017363) was filed 2026-02-17. A large batch of ~20 sub-tasks was filed on 2026-02-25 in a single coordinated effort, covering two main areas: (1) **RTCTransportStats** — roughly 8 missing fields in the `RTCTransportStats` dictionary, parent-tracked in [1225723](https://bugzilla.mozilla.org/show_bug.cgi?id=1225723) (open since 2015); and (2) **RTCIceTransport** — 2 missing methods/events, parent-tracked in [1307994](https://bugzilla.mozilla.org/show_bug.cgi?id=1307994) (open since 2016). Most sub-tasks are P2 NEW with no assignees, suggesting they were triaged but not yet claimed.

The P1 standout is [2014357](https://bugzilla.mozilla.org/show_bug.cgi?id=2014357) (two-byte RTP header extension ids), which would unblock a broad class of interoperability issues with simulcast and other advanced codec configurations.

> **Note:** 39 of the 41 meta deps have `last_change_time` within the last 3 weeks, meaning this is an **active triage push**, not stagnant backlog.

---

## Theme 6: RTCRtpScriptTransform / EncodedTransform WPT Timeouts (Interop 2025)

**User-facing impact:** Web applications using the WebRTC Encoded Transform API (`RTCRtpScriptTransform`) may behave incorrectly or time out under load. Tests for this API consistently time out on wpt.fyi, particularly the `RTCRtpScriptTransform-encoded-transform.https.html` and `script-metadata-transform.https.html` tests. This indicates a performance or correctness issue in Firefox's implementation that may affect real-world use of the API (e.g., end-to-end encryption in video calls).

### Breadcrumbs

| Bug ID | Summary | Severity | Status | Last Changed |
|--------|---------|----------|--------|--------------|
| [2023893](https://bugzilla.mozilla.org/show_bug.cgi?id=2023893) | [meta] Interop 2025 Script Transform wpt.fyi timeout issues | S3 | NEW | 2026-03-17 |
| [2010655](https://bugzilla.mozilla.org/show_bug.cgi?id=2010655) | script-metadata-transform.https.html times out (>60s) on wpt.fyi | S3 | NEW | 2026-03-17 |
| [2010661](https://bugzilla.mozilla.org/show_bug.cgi?id=2010661) | script-change-transform.https.html times out (>10s) | S3 | NEW | 2026-03-17 |
| [2010663](https://bugzilla.mozilla.org/show_bug.cgi?id=2010663) | script-write-twice-transform.https.html times out (>10s) | S3 | NEW | 2026-03-17 |
| [2010667](https://bugzilla.mozilla.org/show_bug.cgi?id=2010667) | RTCRtpScriptTransform-encoded-transform.https.html times out (>60s) | S3 | NEW | 2026-03-17 |
| [2005780](https://bugzilla.mozilla.org/show_bug.cgi?id=2005780) | script-transform-generateKeyFrame-simulcast.https.html unreliable on Windows | S3 | NEW | 2026-03-17 |

### Timeline

The individual timeout bugs were filed in January 2026 (2010655–2010667), with an additional simulcast reliability bug from December 2025 (2005780). The organizing meta bug 2023893 was created 2026-03-17 to consolidate them. All are P2 with no assignees. The meta has 6 deps (including one not yet fetched: 2010657). This is part of the broader Interop 2025 script transform work.

---

## Theme 7: WebRTC-SVC / Scalable Video Coding Implementation

**User-facing impact:** Firefox does not yet fully support `RTCRtpEncodingParameters.scalabilityMode` — the standard API for scalable video coding used by Google Meet, Zoom, and other platforms for adaptive streaming quality. This means Firefox users may fall back to lower-quality video streams or fail to participate in SVC-capable sessions, causing degraded call quality compared to other browsers.

### Breadcrumbs

| Bug ID | Summary | Severity | Status | Last Changed |
|--------|---------|----------|--------|--------------|
| [1571470](https://bugzilla.mozilla.org/show_bug.cgi?id=1571470) | Support webrtc-svc (scalabilityMode) | S3 | ASSIGNED | 2026-03-17 |
| [1947116](https://bugzilla.mozilla.org/show_bug.cgi?id=1947116) | Set all frame metadata in WebrtcMediaDataEncoder | S3 | NEW | 2025-07-10 |
| [1991775](https://bugzilla.mozilla.org/show_bug.cgi?id=1991775) | Support VideoConfiguration scalabilityMode and spatialScalability | -- | NEW | 2025-09-30 |

### Timeline

Bug 1571470 was opened in August 2019 and now has 52 comments — a long-running, high-engagement implementation effort. It is currently ASSIGNED. Three of its five dependencies are resolved; the two remaining are 1947116 (WebrtcMediaDataEncoder metadata) and 1991775 (VideoConfiguration API). It blocks 6 bugs (1805496, 2000351, 2000407, 2000693, 2001249, 2001872), meaning SVC completion has downstream consequences for codec simulcast work.

---

## Theme 8: Audio Input Failures — getUserMedia, macOS Devices, Regression Cluster

**User-facing impact:** Firefox users on macOS and some Linux configurations encounter audio input failures in web conferencing applications. Reported patterns include: (1) camera input failing with AbortError until full browser restart; (2) silent audio playout failure when the system audio device operates at unusual sample rates (768 kHz, a value used by some macOS virtual audio devices); (3) audio channel reordering in Microsoft Teams; (4) complete audio input failure after headset interrupts on macOS 15.5 (Discord regression); (5) simultaneous getUserMedia requests hanging indefinitely. This cluster collectively represents a multi-vector reliability problem for audio I/O in web conferencing.

### Breadcrumbs

| Bug ID | Summary | Severity | Status | Last Changed |
|--------|---------|----------|--------|--------------|
| [2023388](https://bugzilla.mozilla.org/show_bug.cgi?id=2023388) | Cubeb Pain Points (S2 meta, tracks audio I/O issues) | S2 | NEW | 2026-03-15 |
| [2018955](https://bugzilla.mozilla.org/show_bug.cgi?id=2018955) | WebRTC playout fails silently when default device at 768 kHz (macOS) | S3 | NEW | 2026-03-16 |
| [1667635](https://bugzilla.mozilla.org/show_bug.cgi?id=1667635) | AbortError from getUserMedia until Firefox restarted | S3 | UNCONFIRMED | 2026-03-17 |
| [1978259](https://bugzilla.mozilla.org/show_bug.cgi?id=1978259) | Audio channels shift in Microsoft Teams | S3 | UNCONFIRMED | 2026-01-20 |
| [1970645](https://bugzilla.mozilla.org/show_bug.cgi?id=1970645) | [macOS 15.5] Headset interrupts on Discord causes audio input failure | S3 | NEW | 2025-08-05 |
| [1960901](https://bugzilla.mozilla.org/show_bug.cgi?id=1960901) | Simultaneous getUserMedia requests hang infinitely | S3 | NEW | 2025-06-20 |

### Timeline

A new S2 meta bug [2023388](https://bugzilla.mozilla.org/show_bug.cgi?id=2023388) — "Cubeb Pain Points" — was created 2026-03-15 and already has 2018955 as a dependency. This signals intentional consolidation of audio device issues. The AbortError bug (1667635) is UNCONFIRMED and 5 years old but received activity as recently as 2026-03-17, suggesting users are still hitting it.

### Stagnation

> **Stagnation Alert — S3 Regressions:**
> - [1960901](https://bugzilla.mozilla.org/show_bug.cgi?id=1960901) (simultaneous getUserMedia hang, S3, P2, regression) — last changed **2025-06-20**, over **9 months stagnant**
> - [1970645](https://bugzilla.mozilla.org/show_bug.cgi?id=1970645) (macOS 15.5 Discord headset, S3, regression) — last changed **2025-08-05**, over **7 months stagnant**
>
> Both are S3 regressions with no activity in 90+ days. Per scoring policy, these are flagged as stagnant.

---

## Theme 9: AV1 / High-Bit-Depth Video Quality in WebRTC

**User-facing impact:** AV1-encoded WebRTC video streams hang almost immediately when decoding. Additionally, 10-bit AV1 video (I010/I410 formats) and proper color space metadata are not supported in Firefox's WebRTC receive path, causing visual quality degradation or incorrect color rendering on high-fidelity streams. As AV1 adoption grows (used in Google Meet, Teams, Discord), these issues affect a growing share of users.

### Breadcrumbs

| Bug ID | Summary | Severity | Status | Last Changed |
|--------|---------|----------|--------|--------------|
| [2017189](https://bugzilla.mozilla.org/show_bug.cgi?id=2017189) | AV1 WebRTC decoding hangs almost instantly when streaming | S3 | NEW | 2026-03-16 |
| [2016862](https://bugzilla.mozilla.org/show_bug.cgi?id=2016862) | WebRTC: Decoded color_space overwritten with nullopt when RTP metadata absent | S3 | NEW | 2026-03-15 |
| [2016863](https://bugzilla.mozilla.org/show_bug.cgi?id=2016863) | WebRTC: Add 10-bit AV1 decoding (I010/I410) to vendored dav1d decoder | N/A | UNCONFIRMED | 2026-03-04 |
| [2016864](https://bugzilla.mozilla.org/show_bug.cgi?id=2016864) | WebRTC: Handle 10-bit I010 video frames in MediaPipelineReceiveVideo | N/A | UNCONFIRMED | 2026-03-04 |

### Timeline

All four bugs filed in February 2026 as a coordinated cluster. Bug 2017189 (the hang) has 23 comments — highest engagement of the group — and is blocked by the VAAPI meta ([1610199](https://bugzilla.mozilla.org/show_bug.cgi?id=1610199)). Bugs 2016863 and 2016864 are UNCONFIRMED (no triage) despite being directly related to the confirmed 2016862. Bug 2016862 carries `good-first-bug` — the color space fix is likely achievable without deep WebRTC expertise.

---

## Theme 10: WebRTC Assertion / Fuzzing Failures (Fuzzer-Reported API Edge Cases)

**User-facing impact:** Several WebRTC API edge cases trigger hard assertions or CHECK failures that abort the browser process. These were discovered via automated fuzzing (AI-assisted or Grizzly). While the reproduction cases are synthetic, the underlying state machines being violated (DTMF track not enabled, zero-width stream dimensions, invalid PeerConnectionImpl state) can theoretically be reached by adversarial or malformed web content.

### Breadcrumbs

| Bug ID | Summary | Severity | Status | Last Changed |
|--------|---------|----------|--------|--------------|
| [2021448](https://bugzilla.mozilla.org/show_bug.cgi?id=2021448) | Assertion: mDtmfEnabled at AudioConduit.cpp:265 | S3 | NEW | 2026-03-14 |
| [2021480](https://bugzilla.mozilla.org/show_bug.cgi?id=2021480) | Check failed: streams[i].width > 0 | S3 | NEW | 2026-03-14 |
| [2021446](https://bugzilla.mozilla.org/show_bug.cgi?id=2021446) | Assertion failure at PeerConnectionImpl.cpp:1400 | S3 | NEW | 2026-03-14 |
| [2004466](https://bugzilla.mozilla.org/show_bug.cgi?id=2004466) | recommended_probe_size assertion in pacing_controller.cc:444 | S3 | NEW | 2026-03-14 |

### Timeline

Bugs 2021446, 2021448, and 2021480 were all filed 2026-03-05 — same day, AI-involved fuzzing. All block the Grizzly fuzzing meta ([1289609](https://bugzilla.mozilla.org/show_bug.cgi?id=1289609)). Bug 2004466 is older (Dec 2025) and is a standalone assertion. None are assigned.

---

## Emerging Themes to Watch

### E1: abort|BuildFormat Linux Crash — Already at Theme 3
The +421% crash trend in a single month on Linux is the strongest emerging signal in this report. Actively assigned but the root cause is unknown. Watch for further escalation.

### E2: Cubeb Pain Points Meta (S2, Just Created)
[2023388](https://bugzilla.mozilla.org/show_bug.cgi?id=2023388) was created 2026-03-15 as a deliberate aggregation point for audio device issues. With S2 severity and a fresh creation, this signals intent to prioritize audio I/O reliability. More bugs will likely be added as dependents.

### E3: FaceTime Web Compatibility
[1716090](https://bugzilla.mozilla.org/show_bug.cgi?id=1716090) — [meta] Get FaceTime web working in Firefox — is a `webcompat:site-report` + `webcompat:needs-diagnosis` meta with 5 open deps and a last-changed of 2026-03-02. FaceTime Web is a high-profile site; this meta has never received enough triage attention to acquire severity or priority.

---

## Closing: Ranked Signal Summary

| Rank | Theme | Breadcrumbs | Meta Bug | Top Severity | Notes |
|------|-------|-------------|----------|--------------|-------|
| 1 | RTCDataChannel Lifecycle Crash | 1+ (crash vol >1000/30d) | — | S2 | 1,296 crashes/30d rising; no assignee; urgent |
| 2 | Interop 2026 WPT Compliance | 23 | [2017363](https://bugzilla.mozilla.org/show_bug.cgi?id=2017363) (41 deps) | S2 | Active triage push; many P2 unassigned items |
| 3 | CamerasParent Shutdown Crash | 2 | — | S2 | 663/30d rising; P2 with no assignee |
| 4 | abort\|BuildFormat Linux Crash | 1 | — | S3 | +421% trend; Linux only; ASSIGNED |
| 5 | Google Meet PipeWire Crash | 1 | — | S2 | ASSIGNED; Linux PipeWire; 11 comments |
| 6 | Audio Input Failures Cluster | 6 | [2023388](https://bugzilla.mozilla.org/show_bug.cgi?id=2023388) (S2) | S2 | macOS + getUserMedia + Teams/Discord regressions; 2 stagnant bugs |
| 7 | RTCRtpScriptTransform WPT Timeouts | 6 | [2023893](https://bugzilla.mozilla.org/show_bug.cgi?id=2023893) | S3 | Interop 2025 work; P2; no assignees |
| 8 | WebRTC-SVC (scalabilityMode) | 3 | — | S3 | ASSIGNED P2; 52 comments; major feature gap |
| 9 | AV1/10-bit Video Quality | 4 | — | S3 | Decoding hang + color space issues; good-first-bug available |
| 10 | WebRTC Assertion/Fuzzing | 4 | [1289609](https://bugzilla.mozilla.org/show_bug.cgi?id=1289609) | S3 | Fuzzer-found edge cases; no assignees |

---

## Resources Used

| Resource | Detail |
|----------|--------|
| Bugzilla REST API | 8 batch fetches; ~120 bugs retrieved |
| Socorro | 4 signatures searched; 30d + trend windows |
| Dep crawl depth | 2 levels (meta deps + selected sub-deps) |
| Keyword expansion | `keywords=regression`, `keywords=webcompat:site-report` in scope |
| Cache | Written fresh to `reports/wrangler_cache_web-conferencing.json` |

---

## Suggestions for Improving This Skill

- **Assignee field in breadcrumb tables:** The current `include_fields` list omits `assigned_to` from Bugzilla API calls. Adding it would allow the report to directly name engineers on ASSIGNED bugs without a second fetch.
- **Crash signature linking from bug text:** For bugs tagged `crash` without a Socorro signature in the summary, the skill currently can't auto-link. A heuristic to extract the signature from the first comment would improve crash enrichment coverage (e.g., bug 2015946 has no crash tag but is clearly a crash).
- **Stagnation threshold tuning:** The current 30-day S1/S2 threshold and 90-day S3 regression threshold are useful but could be supplemented with a "filed >60d, never assigned" rule for S2 bugs (bug 2016455 would have caught this).

---

*"The game is afoot — not to solve every mystery at once, but to know which door to knock on first."*

---

*Save this report? Suggested filename: `wrangler-web-conferencing-2026-03-18.md` — already saved.*
