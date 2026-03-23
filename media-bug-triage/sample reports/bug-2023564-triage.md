# Bug 2023564 Triage Analysis

**Generated:** 2026-03-19
**Bug URL:** https://bugzilla.mozilla.org/show_bug.cgi?id=2023564

## Bug Information

- **Summary:** memory leak when viewing cctv
- **Reporter:** kristian.kd.dunn@gmail.com (external)
- **Status:** UNCONFIRMED
- **Product:** Core
- **Component:** WebRTC: Audio/Video *(moved from Firefox::Untriaged by Bugbug bot)*
- **Severity:** --
- **Priority:** --
- **Created:** 2026-03-16 (3 days old)
- **Assigned To:** nobody@mozilla.org
- **Pending Flags:** `needinfo?(jmathies@mozilla.com)` — set by apehrson@mozilla.com on 2026-03-19 to identify the right person to investigate

## Research Summary and Key Findings

The reporter observes a progressive memory leak after approximately 15 minutes of viewing a CCTV camera stream via [ispyconnect](https://www.ispyconnect.com/) on Windows 11 with Firefox 148.0.2. The system eventually crashes and terminates all browsers using the GPU for video decoding (including Brave), indicating a system-wide GPU memory exhaustion rather than a Firefox-isolated leak. Hardware: Ryzen 9 7900 X3D, 64GB RAM, RTX 3060, latest drivers. The issue occurs on both low-resolution and 4K streams.

A notable behavioral clue: memory drops when the user navigates back to the video tab. This suggests the memory accumulation may be tied to background-tab handling — either WASM worker allocations or frame buffers accumulating while the tab is backgrounded, rather than a classic unrecoverable leak.

**Component routing concern:** Bugbug auto-classified this to WebRTC: Audio/Video. However, comment 6 from ngrunbaum@me.com (not a Mozilla employee) points out that the stream likely uses WebSockets, not WebRTC, and that a worker running WASM performs frame decoding. jmathies (Mozilla, WebRTC) confirmed no media activity was visible in the profile, suggesting the component assignment is incorrect. The pending needinfo on jmathies from apehrson is asking who should own this.

A Firefox profiler profile was shared by the reporter: https://share.firefox.dev/4shMngE. jmathies noted only a modest memory increase over the recording duration with no clear media pipeline activity.

**Related bugs:**
- [1992567](https://bugzilla.mozilla.org/show_bug.cgi?id=1992567) — Memory leak while screen sharing (RESOLVED FIXED, WebRTC: Audio/Video, S3/P2). Different mechanism (screen sharing vs. video stream via WASM); not a duplicate but same component context.
- [1992558](https://bugzilla.mozilla.org/show_bug.cgi?id=1992558) — Wasm64 high memory usage / memory leak on Windows preventing Emscripten suite completion (ASSIGNED, S3/P1). Targets Wasm64 specifically; too narrow to be the same issue but worth monitoring if WASM is confirmed as the root cause here.

## Regression Timeline

Not reported as a regression. No version bisection data available.

## Classification

| Signal | Detected | Evidence |
|--------|----------|----------|
| Clear STR | No | Steps require specific CCTV hardware + ispyconnect software; timing is ~15 min and non-deterministic |
| Test Case | No | No attached test case |
| Crash Stack | No | No crash IDs or stack traces; reporter describes browser termination |
| Fuzzing | No | — |

## Assessment

- **Suggested Severity:** S3
- **Suggested Priority:** --

### Assessment Reasoning

The bug causes a browser crash and system-level GPU memory exhaustion, but it requires a specific and uncommon reproduction environment (Annke CCTV + ispyconnect + Windows 11) and approximately 15 minutes to manifest. These factors place it at S3 rather than S2. The impact extends beyond Firefox (Brave also crashes), which points to a system-level GPU memory issue rather than a Firefox-specific regression.

The root mechanism is not yet established. jmathies was unable to identify media pipeline activity in the profile, and an external commenter suggests WebSocket + WASM worker for decoding. If confirmed, the bug should be re-routed away from WebRTC: Audio/Video — likely to DOM: Workers, JavaScript: WebAssembly, or Graphics, depending on where the actual allocation pressure originates.

Priority is left unset pending correct component routing and further investigation. No regression range, no crash IDs, and no test case are available to accelerate triage.

## Codebase Investigation

Not performed. The component assignment is in question, and performing meaningful codebase investigation would require first identifying the actual mechanism (WebRTC vs. WASM workers vs. GPU memory). Investigation should follow once jmathies responds to the pending needinfo and the correct component is established.

## Suggested Investigation Areas

Once the mechanism is confirmed:
- If WASM worker: [js/src/wasm/](https://searchfox.org/mozilla-central/source/js/src/wasm/) for memory handling and ArrayBuffer lifetime; [dom/workers/](https://searchfox.org/mozilla-central/source/dom/workers/) for worker lifetime and cleanup.
- If GPU/graphics memory: [gfx/](https://searchfox.org/mozilla-central/source/gfx/) particularly texture/surface pooling in WebRender.
- The background-tab memory drop behavior may be worth investigating via [dom/base/](https://searchfox.org/mozilla-central/source/dom/base/) tab backgrounding logic or [dom/media/](https://searchfox.org/mozilla-central/source/dom/media/) for any media suspension handling.
- The profiler profile at https://share.firefox.dev/4shMngE should be analyzed more carefully for worker/WASM activity, focusing on memory allocations in the worker thread rather than the media pipeline.

## Suggested Next Steps

1. **Await jmathies needinfo response** to get correct component routing.
2. **Re-route component** once the mechanism is identified (WASM/Workers/Graphics rather than WebRTC: Audio/Video).
3. **Request more info from reporter:** Specifically ask for about:support data to capture GPU driver details and any non-default prefs; ask whether the issue is reproducible with hardware video decoding disabled (`about:config` → `media.hardware-video-decoding.enabled = false`), which would help isolate GPU vs. software path.
4. **Attempt profile re-analysis** with focus on WASM/worker threads, not media pipeline.

## Bugzilla Use Tracking

- Total Bugzilla Queries: 9
- Total Bugs Processed: 4 (2023564, 1992567, 1992558, 1961915)
- Estimated Download Bandwidth Used: ~0.1 MB
- Inaccessible Bugs Due to Permissions: 0
