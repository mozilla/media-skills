# Bug 2005246 Triage Analysis

**Generated:** 2026-03-18
**Bug URL:** https://bugzilla.mozilla.org/show_bug.cgi?id=2005246

## Bug Information

- **Summary:** We use Mozilla Firefox in our company on an RDS farm where all users connect. The webcam doesn't work with Mozilla Firefox
- **Reporter:** joestyle92@hotmail.fr (external, non-Mozilla)
- **Status:** UNCONFIRMED (open, ~3 months old)
- **Product:** Core
- **Component:** WebRTC: Audio/Video
- **Created:** 2025-12-10
- **Severity/Priority:** -- / --
- **Blocks:** [1708247](https://bugzilla.mozilla.org/show_bug.cgi?id=1708247) ([meta] WebRTC Triage)
- **Pending needinfo:** jib@mozilla.com (since 2025-12-23)
- **Security:** Not security-sensitive (was briefly in `firefox-core-security` group, removed immediately by tschuster@mozilla.com on 2025-12-10 along with product/component reclassification from Firefox::Untriaged to Core::WebRTC: Audio/Video)

## Research Summary and Key Findings

The reporter is an enterprise IT administrator whose company deploys Firefox on an **RDS (Remote Desktop Services) farm**. Users connect via RDP sessions and attempt WebRTC video calls through Zoom and Teams in the browser. Camera fails with `"AbortError: Starting video input failed; DOMException"` — this error is **not from Firefox itself** (as :Gijs correctly identified in comment #5) but from the Zoom/Teams JavaScript SDK wrapping a failed `getUserMedia()` call.

The about:support data (attachment [9532284](https://bugzilla.mozilla.org/attachment.cgi?id=9532284)) is highly informative and confirms the environment:

- **GPU:** RDPUDD Chained DD (VendorID `0x1414` / DeviceID `0xfefe`) — this is the Microsoft RDP virtual display driver, confirming a fully virtualized RDS session with no physical GPU
- **Hardware acceleration:** Inactive; Direct2D disabled, Remote Canvas blocked, HW video zero-copy blocklisted
- **Rendering:** Microsoft Basic Render Driver via ANGLE (software path)
- **Critical error in graphics log:** `"Failed to get D3D11VideoDevice: 0x80004002"` — error `E_NOINTERFACE` means the D3D11 video device interface is unavailable in this virtualized environment
- **OS:** Windows 10 Build 17763 (Server 2019-era), ~3.4 GB RAM
- **Firefox:** 145.0.2 (release), enterprise-managed (multiple locked policies)
- **Enterprise policies active:** Fission locked on, media utility process locked on, DoH disabled, NTLM auth configured

The `D3D11VideoDevice` failure (`0x80004002`) is the most important signal. Firefox's Windows Media Foundation (WMF) camera capture pipeline likely requires D3D11 video device support, which is simply absent in a standard RDS/RDPUDD environment. Chrome works because it uses a different capture stack that does not have this dependency, or falls back more gracefully.

The fact that camera access also fails without hardware video decoding support means the issue is in the **camera capture path** (not just decode/display) — the WMF backend may try to initialize D3D11 video for camera preview processing before the stream is delivered to the web page.

Note that the actual `getUserMedia()` rejection error from Firefox has not yet been provided — the error text "Starting video input failed" is a Zoom/Teams error message wrapping the real DOMException. This is pending on the needinfo for jib@mozilla.com.

## Regression Timeline

No regression indicated. The reporter has not tested older versions — this appears to be a longstanding limitation in RDS/virtualized environments rather than a recent regression. No `mozregression` bisection data available.

## Classification

| Signal | Detected | Evidence |
|--------|----------|----------|
| Clear STR | No | Steps require an enterprise RDS farm with RDP camera redirection — not easily reproducible without that environment |
| Test Case | No | No attached test case |
| Crash Stack | No | Functional failure; no crash |
| Fuzzing | No | Enterprise user report |

## Assessment

- **Suggested Severity:** S3
- **Suggested Priority:** P3

### Assessment Reasoning

Camera capture fails entirely in Firefox when running in a Windows RDS/RDP session — a legitimate and reasonably common enterprise deployment pattern. The workaround is to use Chrome, which the reporter is aware of. This makes it S3 (blocks non-critical functionality with a workaround available in a specific configuration).

The root cause appears to be Firefox's WMF camera backend on Windows attempting to initialize `D3D11VideoDevice` (confirmed failing with `E_NOINTERFACE: 0x80004002`) in an environment where only the RDPUDD virtual display adapter is available. The media utility process (sandboxed, locked on via enterprise policy) interacts with WMF for camera capture, and this pipeline may not degrade gracefully when D3D11Video is unavailable. Chrome likely uses a different capture path or handles the absence of D3D11Video more robustly.

P3 is appropriate given this is a specific enterprise/virtualized use case that affects a real class of users but is not a mainstream deployment. There is no upstream spec issue. The analogous case for cloud PCs on Linux ([1974941](https://bugzilla.mozilla.org/show_bug.cgi?id=1974941)) is already tracked at S3/P3. The key remaining information needed is the actual `getUserMedia` error thrown by Firefox (which should appear in the browser DevTools console when the call fails), which would confirm the exact code path involved.

## Related Bugs

| Bug | Summary | Status | Relation |
|-----|---------|--------|----------|
| [1974941](https://bugzilla.mozilla.org/show_bug.cgi?id=1974941) | Webcam redirection does not work with Windows365 web client in Firefox/Linux | NEW (S3/P3) | Most analogous — cloud/virtual environment camera failure. Linux. Different specific error (OverconstrainedError on frameRate). Partial progress from Bug 1433480. |
| [1991764](https://bugzilla.mozilla.org/show_bug.cgi?id=1991764) | Microsoft Teams does not show video from OBS vcam (virtual camera) | UNCONFIRMED (S3/P3) | Same symptom area (virtual camera + Teams), different mechanism (PipeWire/OBS, Linux, regression Firefox 128→140). |
| [1708247](https://bugzilla.mozilla.org/show_bug.cgi?id=1708247) | [meta] WebRTC Triage | NEW | Meta tracking bug; this bug is in its `depends_on` list. |

No exact duplicate found. Bug 2005246 is the only Windows RDS camera failure report.

## Codebase Investigation

Not performed. Investigation would focus on the Windows WMF camera capture backend, specifically how it handles the absence of `D3D11VideoDevice`. Relevant areas would be in `dom/media/webrtc/` for the WMF-based camera capture on Windows and how the media utility process initializes the video device.

Key files likely involved:
- [dom/media/webrtc/](https://searchfox.org/mozilla-central/source/dom/media/webrtc/) — WebRTC getUserMedia implementation
- Windows WMF camera backend (likely under `dom/media/webrtc/MediaEngineWebRTC*` or Windows-specific capture wrappers)
- Media utility process sandbox configuration (to verify whether it restricts D3D11 access)

## Suggested Investigation Areas

1. **Determine the actual getUserMedia rejection** — the real Firefox error is not yet available. The DevTools console should show the `name` and `message` of the DOMException from the `getUserMedia()` rejection. This is the most important missing piece.
2. **WMF camera backend initialization on Windows without D3D11Video** — check whether the WMF camera capture path calls `QueryInterface` for `ID3D11VideoDevice` and whether that failure is handled gracefully or causes the entire camera capture to abort.
3. **Media utility process and D3D11Video access** — with `media.utility-process.enabled` locked to `true` by enterprise policy, confirm whether the sandboxed utility process has the permissions needed to access camera devices in an RDS session.
4. **Compare with Bug 1974941** — the Windows365/Linux case has seen partial improvement; lessons from that investigation may apply here.
5. **Chrome comparison** — understanding which Chrome camera capture API avoids this D3D11VideoDevice dependency would clarify the right fix direction.

## Suggested Next Steps for jib

The pending needinfo on jib@mozilla.com (added by :Gijs on 2025-12-23) is still open. jib should assess:
- Whether the WMF camera backend can work without D3D11VideoDevice in RDS environments
- Whether there is a known fallback capture path (e.g., DirectShow) that should be tried first in virtualized environments
- What additional information to request from the reporter (primarily the raw getUserMedia error from DevTools)

## Bugzilla Use Tracking

- Total Bugzilla Queries: ~14
- Total Bugs Processed: 6 (2005246, 1708247, 1974941, 1991764, 1933388, plus attachment 9532284)
- Estimated Download Bandwidth Used: ~0.15 MB
- Inaccessible Bugs Due to Permissions: 0
