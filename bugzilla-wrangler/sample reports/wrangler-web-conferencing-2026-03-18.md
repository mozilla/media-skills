# WebRTC Wrangler Report

## Session Info

| Field | Value |
|-------|-------|
| **Date Generated** | 2026-03-18 |
| **Scope Profile** | `web-conferencing` — Core: WebRTC, WebRTC: Audio/Video, WebRTC: Networking, WebRTC: Signaling |
| **Seed Timeframe** | 2025-10-01 → 2026-03-18 |
| **Seed Count** | 43 (37 created + 6 changed = 43 unique) |
| **Seed Mode** | mixed-seed (37 created + 6 changed = 43 unique) |
| **Cache Freshness** | Fetched live (user-specified date range, no prior cache) |

---

## Seed Info

### Seed Bugs by Priority

**P1**
- [2001200](https://bugzilla.mozilla.org/show_bug.cgi?id=2001200) — Enable connecting getUserMedia and MediaStreamTrackAudioSourceNode running at different rates *(ASSIGNED: cchang@mozilla.com)*

**P2**
- [2021379](https://bugzilla.mozilla.org/show_bug.cgi?id=2021379) — Crash in [@ AsyncShutdownTimeout | profile-before-change | CamerasParent] (S2)
- [2016455](https://bugzilla.mozilla.org/show_bug.cgi?id=2016455) — Crash in [@ NS_CycleCollectorSuspect3 | nsCycleCollectingAutoRefCnt::decr] (RTCDataChannel::AnnounceClosed) (S2)
- [2010655](https://bugzilla.mozilla.org/show_bug.cgi?id=2010655) — script-metadata-transform.https.html times out on wpt.fyi
- [2010661](https://bugzilla.mozilla.org/show_bug.cgi?id=2010661) — script-change-transform.https.html times out on wpt.fyi
- [2010663](https://bugzilla.mozilla.org/show_bug.cgi?id=2010663) — script-write-twice-transform.https.html times out on wpt.fyi
- [2010667](https://bugzilla.mozilla.org/show_bug.cgi?id=2010667) — RTCRtpScriptTransform-encoded-transform.https.html times out on wpt.fyi
- [2018955](https://bugzilla.mozilla.org/show_bug.cgi?id=2018955) — WebRTC playout may fail silently when default output device operates at 768 kHz on macOS
- [2019255](https://bugzilla.mozilla.org/show_bug.cgi?id=2019255) — WebRTC: TURN with TLS (turns) does not work with an IP with a valid certificate
- [2019330](https://bugzilla.mozilla.org/show_bug.cgi?id=2019330) — Implement RTCIceTransport.component (S2)
- [2019331](https://bugzilla.mozilla.org/show_bug.cgi?id=2019331) — Implement RTCTransportStats.selectedCandidatePairId (S2)
- [2019333](https://bugzilla.mozilla.org/show_bug.cgi?id=2019333) — Implement RTCTransportStats.remote/localCertificateId (S2)
- [2019349](https://bugzilla.mozilla.org/show_bug.cgi?id=2019349) — Implement RTCTransportStats.bytesSent/bytesReceived (S2)
- [2019355](https://bugzilla.mozilla.org/show_bug.cgi?id=2019355) — Implement RTCTransportStats.iceRole (S2)
- [2019356](https://bugzilla.mozilla.org/show_bug.cgi?id=2019356) — Implement RTCTransportStats.dtlsState/dtlsRole (S2)
- [2019359](https://bugzilla.mozilla.org/show_bug.cgi?id=2019359) — Implement RTCRtcpParameters.reducedSize (S2)
- [2019361](https://bugzilla.mozilla.org/show_bug.cgi?id=2019361) — Determine correctness of RTCSctpTransport-events.html (S2)
- [2019370](https://bugzilla.mozilla.org/show_bug.cgi?id=2019370) — Disable setParameters compat mode in wpt (S2)
- [2019375](https://bugzilla.mozilla.org/show_bug.cgi?id=2019375) — Get the real h264 plugin working in wpt.fyi CI tasks (S2, ASSIGNED: apehrson@mozilla.com)
- [2019378](https://bugzilla.mozilla.org/show_bug.cgi?id=2019378) — Determine correctness of RTCSctpTransport-maxChannels.html (S2)
- [2019389](https://bugzilla.mozilla.org/show_bug.cgi?id=2019389) — Implement RTCTransportStats.tlsVersion/dtlsCipher/srtpCipher (S2)
- [2021075](https://bugzilla.mozilla.org/show_bug.cgi?id=2021075) — We should throw when RTCIceServer.credential is empty (S2)
- [2023103](https://bugzilla.mozilla.org/show_bug.cgi?id=2023103) — Crash in [@ abort | BuildFormat] (S3, ASSIGNED: jgrulich@redhat.com)
- [2013936](https://bugzilla.mozilla.org/show_bug.cgi?id=2013936) — SDP with h264 profile_level_id > 5 crashes tab (S3, ASSIGNED: jib@mozilla.com)
- [1571470](https://bugzilla.mozilla.org/show_bug.cgi?id=1571470) — Support webrtc-svc (scalabilityMode) (S3, ASSIGNED: ngrunbaum@me.com) *(changed)*
- [1617686](https://bugzilla.mozilla.org/show_bug.cgi?id=1617686) — Validate ice-ufrag and ice-pwd for invalid characters (S2, ASSIGNED: iamanshulmalik@gmail.com) *(changed)*
- [1529398](https://bugzilla.mozilla.org/show_bug.cgi?id=1529398) — Implement RTCConfiguration.iceCandidatePoolSize (S2, ASSIGNED: mfroman@mozilla.com) *(changed)*

**P3**
- [2023893](https://bugzilla.mozilla.org/show_bug.cgi?id=2023893) — [meta] Interop 2025 Script Transform wpt.fyi timeout issues
- [2005780](https://bugzilla.mozilla.org/show_bug.cgi?id=2005780) — script-transform-generateKeyFrame-simulcast.https.html unreliable on Windows
- [2017189](https://bugzilla.mozilla.org/show_bug.cgi?id=2017189) — AV1 webrtc decoding hangs almost instantly when streaming
- [2022422](https://bugzilla.mozilla.org/show_bug.cgi?id=2022422) — Origin Spoofing in WebRTCParent/Child's unused PeerConnectionBlocker mechanism
- [2016862](https://bugzilla.mozilla.org/show_bug.cgi?id=2016862) — WebRTC: Decoded color_space overwritten with nullopt when RTP metadata absent
- [2004466](https://bugzilla.mozilla.org/show_bug.cgi?id=2004466) — recommended_probe_size > DataSize::Zero() (0 bytes vs. 0 bytes)
- [2020362](https://bugzilla.mozilla.org/show_bug.cgi?id=2020362) — Apparent mishandling of relay-based peer reflexive candidates
- [1994808](https://bugzilla.mozilla.org/show_bug.cgi?id=1994808) — Implement MediaStreamTrack stats
- [1667635](https://bugzilla.mozilla.org/show_bug.cgi?id=1667635) — AbortError Starting video failed returned from getUserMedia until Firefox restarted *(changed)*
- [1776143](https://bugzilla.mozilla.org/show_bug.cgi?id=1776143) — Crash in [@ RtlpWaitOnCriticalSection | ... | sctp_close] *(changed)*
- [2001005](https://bugzilla.mozilla.org/show_bug.cgi?id=2001005) — assertion "auth->password.len" failed

**No Priority (--)**
- [2015946](https://bugzilla.mozilla.org/show_bug.cgi?id=2015946) — Google Meet meetings crash because WebRTC tries to destroy a connected PipeWire stream (S2, ASSIGNED: jgrulich@redhat.com)
- [2021448](https://bugzilla.mozilla.org/show_bug.cgi?id=2021448) — Assertion failure: mDtmfEnabled at AudioConduit.cpp:265 (S3)
- [2021480](https://bugzilla.mozilla.org/show_bug.cgi?id=2021480) — Check failed: streams[i].width > 0 (0 vs. 0) (S3)
- [2021446](https://bugzilla.mozilla.org/show_bug.cgi?id=2021446) — Assertion failure: false at PeerConnectionImpl.cpp:1400 (S3)
- [2000194](https://bugzilla.mozilla.org/show_bug.cgi?id=2000194) — navigator.mediaDevices.enumerateDevices() incorrectly showing macOS Multi-Output Playback Device in list of audio inputs (S4)
- [910249](https://bugzilla.mozilla.org/show_bug.cgi?id=910249) — [meta] Finish implementation of MediaStream.webidl and MediaStreamTrack.webidl *(changed)*

### Seed Creation Timeline

Creation dates of the 37 bugs created within the seed window, by month:

```
Oct 2025  [#                    ]  1 bug
Nov 2025  [###                  ]  3 bugs
Dec 2025  [##                   ]  2 bugs
Jan 2026  [####                 ]  4 bugs
Feb 2026  [##################   ] 18 bugs
Mar 2026  [#########            ]  9 bugs (through Mar 18)
```

**Note:** February's spike is explained by a coordinated wave of Interop 2026 WebRTC sub-bugs filed on Feb 25 (RTCTransportStats series + SctpTransport, RTCIceTransport, etc.). The distribution is otherwise sparse but increasing, suggesting WebRTC attention is growing heading into 2026.

---

## Themes

---

### Theme 1: Interop 2026 WebRTC — API Compliance Gaps

**User-facing impact:** Firefox is missing or incorrectly implementing a significant number of WebRTC standard APIs, causing web conferencing tools, WebRTC test suites, and Interop 2026 benchmarks to fail or report incorrect data. Gaps span transport statistics (RTCTransportStats), RTCP parameters, codec negotiation, ICE credential pool, SVC video, and SctpTransport events.

**Meta bug:** [2017363](https://bugzilla.mozilla.org/show_bug.cgi?id=2017363) — [meta] Interop 2026 WebRTC (40+ open dependencies)
**Parent meta:** [2018559](https://bugzilla.mozilla.org/show_bug.cgi?id=2018559) — [meta] Interop 2026 (cross-product)
**Previous cycle:** [1948300](https://bugzilla.mozilla.org/show_bug.cgi?id=1948300) — [meta] Interop 2025 WebRTC (RESOLVED)
**Supporting meta:** [1805496](https://bugzilla.mozilla.org/show_bug.cgi?id=1805496) — [Meta] WebRTC 1.0+extensions API gap (according to WPT)

| Bug ID | Summary | Severity | Status | Last Changed |
|--------|---------|----------|--------|-------------|
| [2017363](https://bugzilla.mozilla.org/show_bug.cgi?id=2017363) | [meta] Interop 2026 WebRTC | -- | NEW | 2026-02-26 |
| [2019330](https://bugzilla.mozilla.org/show_bug.cgi?id=2019330) | Implement RTCIceTransport.component | S2 | NEW | 2026-03-13 |
| [2019331](https://bugzilla.mozilla.org/show_bug.cgi?id=2019331) | Implement RTCTransportStats.selectedCandidatePairId | S2 | NEW | 2026-03-13 |
| [2019333](https://bugzilla.mozilla.org/show_bug.cgi?id=2019333) | Implement RTCTransportStats.remote/localCertificateId | S2 | NEW | 2026-03-13 |
| [2019349](https://bugzilla.mozilla.org/show_bug.cgi?id=2019349) | Implement RTCTransportStats.bytesSent/bytesReceived | S2 | NEW | 2026-03-13 |
| [2019355](https://bugzilla.mozilla.org/show_bug.cgi?id=2019355) | Implement RTCTransportStats.iceRole | S2 | NEW | 2026-03-13 |
| [2019356](https://bugzilla.mozilla.org/show_bug.cgi?id=2019356) | Implement RTCTransportStats.dtlsState/dtlsRole | S2 | NEW | 2026-03-13 |
| [2019389](https://bugzilla.mozilla.org/show_bug.cgi?id=2019389) | Implement RTCTransportStats.tlsVersion/dtlsCipher/srtpCipher | S2 | NEW | 2026-03-13 |
| [2019359](https://bugzilla.mozilla.org/show_bug.cgi?id=2019359) | Implement RTCRtcpParameters.reducedSize | S2 | NEW | 2026-03-13 |
| [2019370](https://bugzilla.mozilla.org/show_bug.cgi?id=2019370) | Disable setParameters compat mode in wpt | S2 | NEW | 2026-03-07 |
| [2016190](https://bugzilla.mozilla.org/show_bug.cgi?id=2016190) | setCodecPreferences cannot disable red/rtx | S2 | NEW | 2026-02-25 |
| [2019346](https://bugzilla.mozilla.org/show_bug.cgi?id=2019346) | Fix failures in RTCPeerConnection-iceConnectionState.https.html | S2 | NEW | 2026-02-26 |
| [2019353](https://bugzilla.mozilla.org/show_bug.cgi?id=2019353) | Fix bad test cases in RTCPeerConnection-setLocalDescription-answer.html | S2 | NEW | 2026-02-25 |
| [2019365](https://bugzilla.mozilla.org/show_bug.cgi?id=2019365) | Fix failure in RTCDataChannel-GC.html | S2 | NEW | 2026-02-26 |
| [2019381](https://bugzilla.mozilla.org/show_bug.cgi?id=2019381) | Handle reception of early media | S2 | NEW | 2026-02-25 |
| [2019387](https://bugzilla.mozilla.org/show_bug.cgi?id=2019387) | Fix bad setCodecPreferences call in protocol/additional-codecs.html | S2 | NEW | 2026-02-25 |
| [2019461](https://bugzilla.mozilla.org/show_bug.cgi?id=2019461) | Fix or remove protocol/handover-datachannel.html and protocol/handover.html | S2 | NEW | 2026-02-26 |
| [2019469](https://bugzilla.mozilla.org/show_bug.cgi?id=2019469) | protocol/rtp-headerextensions.html failure due to recvonly extmap | S2 | NEW | 2026-02-26 |
| [1529398](https://bugzilla.mozilla.org/show_bug.cgi?id=1529398) | Implement RTCConfiguration.iceCandidatePoolSize | S2 | NEW | 2026-03-13 (ASSIGNED: mfroman@mozilla.com) |
| [1617686](https://bugzilla.mozilla.org/show_bug.cgi?id=1617686) | Validate ice-ufrag and ice-pwd for invalid characters | S2 | ASSIGNED | 2026-03-13 (ASSIGNED: iamanshulmalik@gmail.com) |
| [1805446](https://bugzilla.mozilla.org/show_bug.cgi?id=1805446) | Implement RTCDtlsTransport.getRemoteCertificates() | S2 | NEW | 2026-02-26 |
| [1225723](https://bugzilla.mozilla.org/show_bug.cgi?id=1225723) | Implement RTCTransportStats | S3 | NEW | 2026-02-25 |
| [1994808](https://bugzilla.mozilla.org/show_bug.cgi?id=1994808) | Implement MediaStreamTrack stats | S3 | NEW | 2026-03-02 |
| [2019375](https://bugzilla.mozilla.org/show_bug.cgi?id=2019375) | Get the real h264 plugin working in wpt.fyi CI | S2 | ASSIGNED | 2026-03-10 (ASSIGNED: apehrson@mozilla.com) |

**Timeline:** The Interop 2025 WebRTC meta was resolved (bug 1948300). On Feb 17, 2026, the Interop 2026 meta (2017363) was filed under the cross-product Interop 2026 meta (2018559). On Feb 25 alone, 15+ sub-bugs for RTCTransportStats, RTCRtcpParameters, RTCDtlsTransport, and WPT test fixes were filed. This represents a structured, coordinated effort to close Firefox's WebRTC spec compliance gap before the 2026 Interop evaluation window. Most bugs are unassigned and waiting for engineering bandwidth.

**Stagnation note:** Multiple S2 bugs (2019370, 2016190, 2019353, 2019365) last changed Feb 25–26, now ~21 days without activity. If this persists past Apr 2, these will formally hit the 30-day stagnation threshold.

---

### Theme 2: CamerasParent Shutdown Crash (Rising)

**User-facing impact:** Firefox crashes on shutdown on Windows when a camera was active during the session. This is the highest-volume WebRTC crash in Socorro and is accelerating.

| Bug ID | Summary | Severity | Status | Last Changed | Crash Volume (30d) |
|--------|---------|----------|--------|-------------|-------------------|
| [2021379](https://bugzilla.mozilla.org/show_bug.cgi?id=2021379) | Crash in [@ AsyncShutdownTimeout \| profile-before-change \| CamerasParent] | S2 | NEW | 2026-03-17 | **1,142** (rising) |

**Socorro data:**
- **Signature:** [AsyncShutdownTimeout | profile-before-change | CamerasParent](https://crashes.mozilla.org/signatures?q=signature%3A%22AsyncShutdownTimeout+%7C+profile-before-change+%7C+CamerasParent%22)
- **Volume (30d, since Feb 16):** 1,142 crashes
- **Prior 30d (Jan 16 – Feb 16):** 832 crashes
- **Trend:** RISING (+37%)
- **Top platform:** Windows NT (993 crashes, ~87%)
- **Top Firefox versions:** 148.0 (353), 147.0.4 (225), 148.0.2 (182)
- **Variants:** Includes 2×, 3×, 4× CamerasParent repetitions in the same shutdown sequence

**Timeline:** Bug filed Mar 5, 2026. Not yet assigned. The crash represents Firefox failing to cleanly shut down the camera parent process during profile teardown, a regression that has been steadily worsening into Firefox 148. With >1,000 reports in 30 days and a rising trend, this is the highest-urgency active bug in this scope.

> **Stagnation alert:** This S2 bug has had no owner assigned since filing (Mar 5). Last activity Mar 17 — still within window, but close to crossing the 30-day threshold if unaddressed.

---

### Theme 3: WebRTC SVC (Scalable Video Coding) Support

**User-facing impact:** Firefox does not support `scalabilityMode` in RTCRtpEncodingParameters (SVC/webrtc-svc spec), preventing high-quality adaptive bitrate video in web conferencing apps that use SVC. Competing browsers (Chrome, Safari, Edge) fully support this feature. This is a Interop 2025/2026 capability gap.

| Bug ID | Summary | Severity | Status | Last Changed |
|--------|---------|----------|--------|-------------|
| [1571470](https://bugzilla.mozilla.org/show_bug.cgi?id=1571470) | Support webrtc-svc (scalabilityMode) — *meta* | S3 | ASSIGNED | 2026-03-17 (ASSIGNED: ngrunbaum@me.com) |
| [1991775](https://bugzilla.mozilla.org/show_bug.cgi?id=1991775) | Support VideoConfiguration scalabilityMode and spatialScalability | -- | NEW | 2025-09-30 |
| [2000351](https://bugzilla.mozilla.org/show_bug.cgi?id=2000351) | Support SVC on Android | S3 | NEW | 2025-11-21 |
| [2000407](https://bugzilla.mozilla.org/show_bug.cgi?id=2000407) | Add H265Enabled() to DefaultCodecPrefs | N/A | NEW | 2025-11-23 |
| [2000693](https://bugzilla.mozilla.org/show_bug.cgi?id=2000693) | Add and upstream a constexpr array of all webrtc codecs to libwebrtc | N/A | NEW | 2025-11-18 |
| [2001249](https://bugzilla.mozilla.org/show_bug.cgi?id=2001249) | Clean up lints in json_session_unittests.cpp | S4 | NEW | 2025-11-20 |
| [2001872](https://bugzilla.mozilla.org/show_bug.cgi?id=2001872) | Offer dependency descriptor RTP header by default | N/A | NEW | 2025-12-01 |
| [1947116](https://bugzilla.mozilla.org/show_bug.cgi?id=1947116) | Set all frame metadata in WebrtcMediaDataEncoder | S3 | NEW | 2025-07-10 |

**Timeline:** The meta tracking bug 1571470 has been active since Aug 2019 (52 comments) and is assigned to Nico Grunbaum. Several sub-tasks were recently filed (Nov–Dec 2025) indicating renewed engineering effort. Resolved sub-bugs include RTCRtpEncodingParameters.codec (1894137) and OpenH264 temporal layers (1936052, 1947115), suggesting the work is progressing. The remaining open items cover Android SVC, codec array upstreaming, dependency descriptor headers, and frame metadata.

**parity-chrome / parity-edge / parity-safari:** Many individual items have these keywords on related bugs.

---

### Theme 4: RTCRtpScriptTransform / Encoded Transform WPT Timeouts

**User-facing impact:** Firefox's implementation of RTCRtpScriptTransform (Encoded Transform API) has sporadic timeout failures on wpt.fyi, undermining Interop 2025 scoring. These aren't crash bugs — they're reliability/flakiness issues in the implementation or test runner that cause WPT jobs to timeout.

**Meta bug:** [2023893](https://bugzilla.mozilla.org/show_bug.cgi?id=2023893) — [meta] Interop 2025 Script Transform wpt.fyi timeout issues (filed Mar 17, 2026 — brand new)

| Bug ID | Summary | Severity | Status | Last Changed |
|--------|---------|----------|--------|-------------|
| [2023893](https://bugzilla.mozilla.org/show_bug.cgi?id=2023893) | [meta] Interop 2025 Script Transform wpt.fyi timeout issues | S3 | NEW | 2026-03-17 |
| [2010655](https://bugzilla.mozilla.org/show_bug.cgi?id=2010655) | script-metadata-transform.https.html times out (>60s) on wpt.fyi | S3 | NEW | 2026-03-17 |
| [2010657](https://bugzilla.mozilla.org/show_bug.cgi?id=2010657) | script-transform.https.html times out (>60s) on wpt.fyi | S3 | RESOLVED | 2026-03-17 |
| [2010661](https://bugzilla.mozilla.org/show_bug.cgi?id=2010661) | script-change-transform.https.html times out (>10s) on wpt.fyi | S3 | NEW | 2026-03-17 |
| [2010663](https://bugzilla.mozilla.org/show_bug.cgi?id=2010663) | script-write-twice-transform.https.html times out (>10s) on wpt.fyi | S3 | NEW | 2026-03-17 |
| [2010667](https://bugzilla.mozilla.org/show_bug.cgi?id=2010667) | RTCRtpScriptTransform-encoded-transform.https.html times out (>60s) | S3 | NEW | 2026-03-17 |
| [2005780](https://bugzilla.mozilla.org/show_bug.cgi?id=2005780) | script-transform-generateKeyFrame-simulcast.https.html unreliable on Windows | S3 | NEW | 2026-03-17 |

**Timeline:** Individual timeout bugs started appearing in Dec 2025–Jan 2026 across these test files. The meta bug was created March 17 (yesterday), grouping them for coordinated resolution. One test (2010657) was already resolved with a fix by Byron Campen (bwc). The remaining 5 WPT files still timeout occasionally on wpt.fyi. This pattern suggests the ScriptTransform worker messaging has timing-dependent behavior that needs investigation.

---

### Theme 5: WebRTC Assertion and Fuzzer Failures

**User-facing impact:** Multiple assertion failures in core WebRTC code paths have been discovered via fuzzing, indicating latent correctness issues in audio codec handling, video stream dimensions, and SDP parsing. Users may experience tab crashes or silent data corruption in edge-case RTC scenarios.

**Meta bug:** [1289609](https://bugzilla.mozilla.org/show_bug.cgi?id=1289609) — [meta] Bugs found while Fuzzing with Grizzly (hundreds of deps; all assertion bugs below are tracked here)

| Bug ID | Summary | Severity | Status | Last Changed |
|--------|---------|----------|--------|-------------|
| [2021448](https://bugzilla.mozilla.org/show_bug.cgi?id=2021448) | Assertion failure: mDtmfEnabled at [AudioConduit.cpp:265](https://searchfox.org/mozilla-central/source/dom/media/webrtc/libwebrtcglue/AudioConduit.cpp) | S3 | NEW | 2026-03-14 |
| [2021480](https://bugzilla.mozilla.org/show_bug.cgi?id=2021480) | Check failed: streams[i].width > 0 (0 vs. 0) | S3 | NEW | 2026-03-14 |
| [2021446](https://bugzilla.mozilla.org/show_bug.cgi?id=2021446) | Assertion failure: false at [PeerConnectionImpl.cpp:1400](https://searchfox.org/mozilla-central/source/dom/media/webrtc/jsapi/PeerConnectionImpl.cpp) | S3 | NEW | 2026-03-14 |
| [2004466](https://bugzilla.mozilla.org/show_bug.cgi?id=2004466) | recommended_probe_size > DataSize::Zero() in [pacing_controller.cc:444](https://searchfox.org/mozilla-central/source/third_party/libwebrtc/modules/pacing/pacing_controller.cc) | S3 | NEW | 2026-03-14 |
| [2001005](https://bugzilla.mozilla.org/show_bug.cgi?id=2001005) | assertion "auth->password.len" failed | S3 | NEW | 2026-03-18 |

**Timeline:** All five assertion bugs are tagged `ai-involved` and/or `testcase`, indicating they were discovered through automated fuzzing. Three were filed on the same day (Mar 5, 2026), suggesting a fuzzing campaign targeting WebRTC. Bug 2001005 (assertion in DTLS auth password length check, filed Nov 2025) has the `pernosco` keyword, indicating a developer reproduced it with Pernosco time-travel debugging. None have been assigned yet.

---

### Theme 6: Linux / PipeWire WebRTC Crashes

**User-facing impact:** Firefox on Linux crashes when using Google Meet (and likely other WebRTC apps using PipeWire for screen sharing or camera access). Two distinct crashes are being investigated: one when WebRTC attempts to destroy a still-connected PipeWire stream, and another during video format negotiation (`BuildFormat`).

| Bug ID | Summary | Severity | Status | Last Changed |
|--------|---------|----------|--------|-------------|
| [2015946](https://bugzilla.mozilla.org/show_bug.cgi?id=2015946) | Google Meet meetings crash because WebRTC tries to destroy a connected PipeWire stream | S2 | ASSIGNED | 2026-03-17 (ASSIGNED: jgrulich@redhat.com) |
| [2023103](https://bugzilla.mozilla.org/show_bug.cgi?id=2023103) | Crash in [@ abort \| BuildFormat] | S3 | ASSIGNED | 2026-03-17 (ASSIGNED: jgrulich@redhat.com) |

**Timeline:** Bug 2015946 was filed Feb 10, 2026 by Jan Grulich (Red Hat), who also assigned it to himself — a strong signal of concrete investigation. Eleven comments over ~5 weeks indicate active debugging. The secondary crash (2023103, BuildFormat) appeared Mar 13 and was immediately assigned to the same engineer, suggesting a related PipeWire teardown/initialization issue. Both bugs are being handled by the same Red Hat contributor who has deep expertise in PipeWire + Firefox video stack. Progress is visible but no fix has landed yet.

> **Stagnation note:** Bug 2015946 is S2 and has not received an update in the past 24 hours but is within the 30-day window. Monitor closely.

---

### Theme 7: AV1 / H.264 Video Codec Issues

**User-facing impact:** Users experience WebRTC video streams hanging immediately when AV1 codec is in use (e.g., on platforms like Cloudflare Calls that prefer AV1), or tab crashes when receiving H.264 streams with non-standard profile levels. Color space metadata is also dropped silently, affecting color accuracy for 10-bit video.

| Bug ID | Summary | Severity | Status | Last Changed |
|--------|---------|----------|--------|-------------|
| [2017189](https://bugzilla.mozilla.org/show_bug.cgi?id=2017189) | AV1 webrtc decoding hangs almost instantly when streaming | S3 | NEW | 2026-03-16 |
| [2013936](https://bugzilla.mozilla.org/show_bug.cgi?id=2013936) | SDP with h264 profile_level_id > 5 crashes tab | S3 | ASSIGNED | 2026-02-27 (ASSIGNED: jib@mozilla.com) |
| [2014007](https://bugzilla.mozilla.org/show_bug.cgi?id=2014007) | webrtc/protocol/h264-profile-levels.https.html is timing out on Android | S3 | NEW | 2026-02-05 |
| [2016862](https://bugzilla.mozilla.org/show_bug.cgi?id=2016862) | WebRTC: Decoded color_space overwritten with nullopt when RTP metadata absent | S3 | NEW | 2026-03-15 |
| [2016863](https://bugzilla.mozilla.org/show_bug.cgi?id=2016863) | Add 10-bit AV1 decoding (I010/I410) and color space extraction to vendored dav1d decoder | N/A | UNCONFIRMED | 2026-03-04 |
| [2016864](https://bugzilla.mozilla.org/show_bug.cgi?id=2016864) | Handle 10-bit I010 video frames in MediaPipelineReceiveVideo with color space propagation | N/A | UNCONFIRMED | 2026-03-04 |
| [1610199](https://bugzilla.mozilla.org/show_bug.cgi?id=1610199) | [meta][Linux/EGL] Implement ffmpeg/VAAPI video playback | S3 | NEW | 2026-02-25 (has 2017189 as dep) |

**Timeline:** The AV1 hang (2017189) was filed Feb 16, 2026 with 23 comments — an unusually high engagement rate for an S3 bug — suggesting active user and developer interest. It feeds into the Linux VAAPI meta (1610199) which has 200+ deps. The H264 crash (2013936, assigned to jib) relates to a missing validation on `profile_level_id` values above 5 in SDP, causing the tab to crash and a WPT test to fail on Android (2014007). The color space bugs (2016862–2016864) were filed as a coordinated set and are tagged `good-first-bug`, awaiting contributor pickup.

---

### Theme 8: getUserMedia / Device Enumeration Failures

**User-facing impact:** Camera access fails with an opaque `AbortError` and requires a browser restart to recover. On macOS, loopback/virtual audio devices appear incorrectly in the input device list. These are longstanding issues with significant user impact (1667635 has 34 comments from users across 5+ years).

| Bug ID | Summary | Severity | Status | Last Changed |
|--------|---------|----------|--------|-------------|
| [1667635](https://bugzilla.mozilla.org/show_bug.cgi?id=1667635) | AbortError Starting video failed returned from getUserMedia until Firefox restarted | S3 | UNCONFIRMED | 2026-03-17 |
| [2000194](https://bugzilla.mozilla.org/show_bug.cgi?id=2000194) | enumerateDevices() incorrectly shows macOS Multi-Output Playback Device in audio inputs | S4 | UNCONFIRMED | 2026-03-18 |
| [2018955](https://bugzilla.mozilla.org/show_bug.cgi?id=2018955) | WebRTC playout may fail silently when output device operates at 768 kHz on macOS | S3 | NEW | 2026-03-18 |
| [2001200](https://bugzilla.mozilla.org/show_bug.cgi?id=2001200) | Enable connecting getUserMedia and MediaStreamTrackAudioSourceNode at different rates | S4 | NEW | 2026-03-02 (ASSIGNED: cchang@mozilla.com) |

**Timeline:** Bug 1667635, filed in 2020, remains UNCONFIRMED with 34 comments. It saw a new comment as recently as Mar 17, indicating ongoing user impact. Both 2000194 and 2018955 are macOS-specific edge cases discovered in late 2025 / early 2026. Bug 2001200 (P1 priority despite S4 severity) is actively assigned to C.M. Chang and addresses a WebAudio/WebRTC interaction issue with sample rate mismatches.

> **Stagnation alert:** Bug 1667635 is S3, UNCONFIRMED, and has been open since 2020 with no assignment. While it receives periodic user comments, the engineering status is effectively stalled.

---

### Theme 9: SCTP Crash on Connection Close (Windows)

**User-facing impact:** Firefox crashes on Windows when closing a DataChannel-enabled WebRTC connection, due to a thread-safety issue in the SCTP stack (`sctp_inpcb_free`). This affects real-time data channel applications.

| Bug ID | Summary | Severity | Status | Last Changed | Crash Volume (30d) |
|--------|---------|----------|--------|-------------|-------------------|
| [1776143](https://bugzilla.mozilla.org/show_bug.cgi?id=1776143) | Crash in [@ RtlpWaitOnCriticalSection \| ... \| sctp_inpcb_free \| sctp_close] | S3 | NEW | 2026-03-16 | 365 (falling) |

**Socorro data:**
- **Signature:** [Crash in sctp_inpcb_free / sctp_close](https://crashes.mozilla.org/signatures?q=signature%3A%22sctp_inpcb_free%22)
- **Volume (30d, since Feb 16):** 365 crashes
- **Prior 30d (Jan 16 – Feb 16):** 416 crashes
- **Trend:** FALLING (-12%)

**Timeline:** Bug filed Jun 2022 (44 comments). Originally related to an outdated libusrsctp (its dep 1795697 — a sec-high update — was resolved in Jan 2023). Despite the library update, the crash persists, suggesting the underlying thread-safety issue was not fully resolved. The falling crash trend is encouraging, but 365 monthly crashes still represents meaningful user impact. Byron Campen (bwc) is tracking it.

---

## Emerging Themes

### Emerging: WebRTC Site Compatibility (FaceTime, riverside.fm)

Insufficient breadcrumbs for a full theme, but worth monitoring:

- [1902507](https://bugzilla.mozilla.org/show_bug.cgi?id=1902507) — riverside.fm recommends only Chrome (S2, ASSIGNED: jib@mozilla.com, 28 comments). The site gating is caused by Firefox missing specific WebRTC/stats features tracked in 1994808 (MediaStreamTrack stats).
- [1716090](https://bugzilla.mozilla.org/show_bug.cgi?id=1716090) — [meta] Get FaceTime web working in Firefox (5 open deps, recently changed Mar 2). FaceTime web requires specific ICE/DTLS capabilities still in progress.

These are likely to grow into a full theme once the Interop 2026 API gaps begin closing, as the same missing features drive both issues.

### Emerging: TURN/TLS with IP Address Certificates

- [2019255](https://bugzilla.mozilla.org/show_bug.cgi?id=2019255) — TURN with TLS (turns:) does not work with an IP address + valid certificate (S3, P3, 8 comments, UNCONFIRMED). Enterprise deployments commonly use TURN servers with IP-based TLS certificates. Only 1 breadcrumb in scope, but notable for enterprise web conferencing impact.

---

## Closing

### Ranked Signal Summary

| Rank | Theme | Breadcrumbs | Meta Bug | Top Severity | Notes |
|------|-------|-------------|----------|-------------|-------|
| 1 | Interop 2026 WebRTC API Gaps | 24+ | [2017363](https://bugzilla.mozilla.org/show_bug.cgi?id=2017363) (40+ deps) | S2 | Structured campaign; most bugs unassigned; stagnation risk if Feb 25 bugs stay idle |
| 2 | CamerasParent Shutdown Crash | 1 (crash vol 1,142) | — | S2 | Highest Socorro volume in scope; rising +37%; Windows dominant; unassigned |
| 3 | WebRTC SVC Support | 8+ | [1571470](https://bugzilla.mozilla.org/show_bug.cgi?id=1571470) (assigned) | S3 | Active since 2019; recently reinvigorated; parity gap vs Chrome/Safari/Edge |
| 4 | RTCRtpScriptTransform WPT Timeouts | 6 | [2023893](https://bugzilla.mozilla.org/show_bug.cgi?id=2023893) (new) | S3 | Interop 2025 scoring at risk; meta filed yesterday; 1 of 6 already RESOLVED |
| 5 | WebRTC Assertion / Fuzzer Failures | 5 | [1289609](https://bugzilla.mozilla.org/show_bug.cgi?id=1289609) | S3 | All unassigned; 3 filed same day suggesting fuzzing campaign; `pernosco` tag on one |
| 6 | Linux / PipeWire Crashes | 2 | — | S2 | Both ASSIGNED jgrulich; active investigation; impacts Google Meet on Linux |
| 7 | AV1 / H.264 Codec Issues | 7 | [1610199](https://bugzilla.mozilla.org/show_bug.cgi?id=1610199) | S3 | AV1 hang has 23 comments; H264 assigned to jib; 2 good-first-bugs available |
| 8 | getUserMedia / Device Enumeration | 4 | — | S3 | 1667635 is 5-year-old stalled issue; macOS edge cases newly filed |
| 9 | SCTP Crash on Close (Windows) | 1 (crash vol 365) | — | S3 | Falling trend; 44-comment history; 3-year-old issue; lower urgency |

### Resources Used

| Resource | Details |
|----------|---------|
| Bugzilla REST API | 8 queries (seed A + seed B + 4 dep batches + 2 keyword expansions) |
| Socorro REST API | 6 queries (CamerasParent volume/trend, SCTP volume/trend, RTCDataChannel, platform facets) |
| socorro-cli | 4 attempts — failed with `ParseError(Invalid)` on pipe-delimited signatures; fell back to direct REST API |
| Bug count analyzed | ~75 unique bugs across seed + dep crawl |

### Suggestions for Improving This Skill

1. **socorro-cli pipe-signature fix:** The tool panics on signatures containing `|` characters (e.g., `"A | B | C"`). The skill should document quoting/escaping requirements or fall back to the REST API automatically. Alternatively, a `--signature-contains` mode (substring search) would sidestep the issue entirely.
2. **Duplicate detection across sessions:** A mechanism to compare this run's findings against a prior report (e.g., `wrangler-web-conferencing-*.md`) would allow the skill to flag "new since last run" and "resolved since last run" themes, dramatically increasing its utility for recurring use.
3. **Interop context injection:** When a meta bug for Interop N is detected, automatically surface the wpt.fyi score and trend for the relevant category (e.g., fetch from `wpt.fyi/api/runs?product=firefox`). This would quantify the gap in a way that's immediately actionable.
4. **cc_count retrieval:** The API didn't return `cc_count` in the standard batch response for several bugs. The skill correctly handles this case, but automating a fallback batch fetch for it would ensure signal scoring is more accurate.

---

> *"The art of detection lies not in seeing what is there, but in noticing what has been overlooked — and following the trail before it goes cold."*

