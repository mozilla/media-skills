# Bugzilla Wrangler Report — Graphics
**Generated:** 2026-03-18

---

## Session Info

| Field | Value |
|-------|-------|
| Scope | `graphics` (Core: Graphics, Graphics: WebRender, Graphics: CanvasWebGL, Graphics: Layers, Graphics: Text, Canvas: 2D, Layout: Painting, CSS Painting and Compositing) |
| Seed timeframe | 2025-12-18 → 2026-03-18 (default 3-month window) |
| Seed count | 50 |
| Seed mode | mixed-seed (37 created + 13 changed = 50 unique) |
| Cache freshness | Live fetch (default window — cache skipped on read, written after fetch) |

---

## Seed Info

### Seed Bugs (by priority, then severity)

| Bug ID | Summary | Component | Sev | Status |
|--------|---------|-----------|-----|--------|
| [2020096](https://bugzilla.mozilla.org/show_bug.cgi?id=2020096) | Large SVG consumes all system resources | Graphics | S2 | NEW |
| [2020195](https://bugzilla.mozilla.org/show_bug.cgi?id=2020195) | Canvas displays screen content from other applications | Graphics: CanvasWebGL | S2 | UNCONFIRMED |
| [2019679](https://bugzilla.mozilla.org/show_bug.cgi?id=2019679) | WebRender GPU texture corruption triggered by CSS animation | Graphics: WebRender | S2 | UNCONFIRMED |
| [2013967](https://bugzilla.mozilla.org/show_bug.cgi?id=2013967) | 3D transforms don't display correctly with opacity and rotation | Graphics: WebRender | S2 | ASSIGNED |
| [2020844](https://bugzilla.mozilla.org/show_bug.cgi?id=2020844) | Large parts of UI glitch with Layer Compositor on macOS | Graphics: WebRender | S2 | UNCONFIRMED |
| [2021972](https://bugzilla.mozilla.org/show_bug.cgi?id=2021972) | Hit MOZ_CRASH(ElementAt) in WebRender | Graphics: WebRender | S3 | NEW |
| [2020923](https://bugzilla.mozilla.org/show_bug.cgi?id=2020923) | Remove remaining usage of non-quad gradients | Graphics: WebRender | S3 | NEW |
| [2020981](https://bugzilla.mozilla.org/show_bug.cgi?id=2020981) | 39.23 - 4.23% bing-search FirstVisualChange regression | Graphics: WebRender | S3 | NEW |
| [2023886](https://bugzilla.mozilla.org/show_bug.cgi?id=2023886) | Port normal borders from brush to quads | Graphics: WebRender | S3 | NEW |
| [2023466](https://bugzilla.mozilla.org/show_bug.cgi?id=2023466) | Pop out window is faded, or has greyish cast | Graphics: WebRender | S3 | UNCONFIRMED |
| [2020420](https://bugzilla.mozilla.org/show_bug.cgi?id=2020420) | Fullscreen mode goes black in YouTube with hardware acceleration | Graphics | S3 | UNCONFIRMED |
| [2016655](https://bugzilla.mozilla.org/show_bug.cgi?id=2016655) | Mixed rendering of background-attachment: fixed and backdrop-filter broken | Graphics: WebRender | S3 | NEW |
| [2022521](https://bugzilla.mozilla.org/show_bug.cgi?id=2022521) | backdrop-filter renders incorrectly on modal overlays and sidebars | Graphics: WebRender | S3 | UNCONFIRMED |
| [2020192](https://bugzilla.mozilla.org/show_bug.cgi?id=2020192) | Frame rate is limited to the monitor with lowest FPS | Graphics: WebRender | S3 | UNCONFIRMED |
| [2021699](https://bugzilla.mozilla.org/show_bug.cgi?id=2021699) | Stack exhaustion in FreeType load_truetype_glyph() | Graphics: Text | S3 | NEW |
| [2016821](https://bugzilla.mozilla.org/show_bug.cgi?id=2016821) | Blurry text, which becomes sharp when selecting | Graphics: Text | S3 | NEW |
| [2019903](https://bugzilla.mozilla.org/show_bug.cgi?id=2019903) | Shutdown hang from LoadCmapsRunnable during shutdown phases | Graphics: Text | S3 | NEW |
| [2019786](https://bugzilla.mozilla.org/show_bug.cgi?id=2019786) | wrench-deps jobs permafailing on ESR115 | Graphics: WebRender | S4 | NEW |
| [2019155](https://bugzilla.mozilla.org/show_bug.cgi?id=2019155) | Valid WebGL2 shaders get link error on Windows only | Graphics: WebRender | S3 | UNCONFIRMED |
| [2008381](https://bugzilla.mozilla.org/show_bug.cgi?id=2008381) | Hit MOZ_CRASH(explicit panic) at render_task.rs | Graphics: WebRender | S3 | NEW |
| [2013674](https://bugzilla.mozilla.org/show_bug.cgi?id=2013674) | Memory leak | Graphics | S3 | UNCONFIRMED |
| [2018607](https://bugzilla.mozilla.org/show_bug.cgi?id=2018607) | SVG backdrop-filter won't apply feTurbulence/feDisplacementMap | Graphics | S3 | UNCONFIRMED |
| [2011453](https://bugzilla.mozilla.org/show_bug.cgi?id=2011453) | Visible round border between picked color and dark background | Graphics: WebRender | S3 | NEW |
| [2018463](https://bugzilla.mozilla.org/show_bug.cgi?id=2018463) | Firefox Nightly Linux font rendering is blurry | Graphics | S3 | UNCONFIRMED |
| [2018404](https://bugzilla.mozilla.org/show_bug.cgi?id=2018404) | webgl: report INVALID_ENUM instead of INVALID_VALUE | Graphics: CanvasWebGL | S3 | UNCONFIRMED |
| [2017580](https://bugzilla.mozilla.org/show_bug.cgi?id=2017580) | GPU process memory growth when Foundry Virtual Tabletop is launched | Graphics | S3 | UNCONFIRMED |
| [2015602](https://bugzilla.mozilla.org/show_bug.cgi?id=2015602) | Significant performance issue with complex SVG | Graphics | S3 | UNCONFIRMED |
| [2015471](https://bugzilla.mozilla.org/show_bug.cgi?id=2015471) | Crash in [@ memcpy \| FT_Stream_ReadAt] | Graphics: Text | S3 | NEW |
| [2017679](https://bugzilla.mozilla.org/show_bug.cgi?id=2017679) | calc() in SVG rect x/y attributes renders incorrectly | Graphics: WebRender | S3 | UNCONFIRMED |
| [2016487](https://bugzilla.mozilla.org/show_bug.cgi?id=2016487) | Hit MOZ_CRASH at gpu_buffer.rs:446 | Graphics: WebRender | S3 | NEW |
| [2015955](https://bugzilla.mozilla.org/show_bug.cgi?id=2015955) | Large event jank from synchronous decoding of images | Graphics: CanvasWebGL | S3 | NEW |
| [2015437](https://bugzilla.mozilla.org/show_bug.cgi?id=2015437) | Crash in [@ dri2_allocate_textures] on mesa 25.0.7.0 | Graphics | S3 | NEW |
| [2008637](https://bugzilla.mozilla.org/show_bug.cgi?id=2008637) | Integer overflow in ShmSegmentsReader can lead to crash | Graphics: WebRender | S3 | UNCONFIRMED |
| [2010645](https://bugzilla.mozilla.org/show_bug.cgi?id=2010645) | WebGL Google map turns black after zooming | Graphics: CanvasWebGL | S3 | UNCONFIRMED |
| [2012337](https://bugzilla.mozilla.org/show_bug.cgi?id=2012337) | Severe scrolling lag on Rockstar Games GTA VI website | Graphics: WebRender | S3 | NEW |
| [2013247](https://bugzilla.mozilla.org/show_bug.cgi?id=2013247) | Crash in TileCacheInstance::setup_compositor_surfaces_impl | Graphics: WebRender | S3 | NEW |
| [2014745](https://bugzilla.mozilla.org/show_bug.cgi?id=2014745) | WEBRENDER_SCISSORED_CACHE_CLEARS is disabled | Graphics | S4 | UNCONFIRMED |
| **From Query B (recently changed, unique):** | | | | |
| [1965442](https://bugzilla.mozilla.org/show_bug.cgi?id=1965442) | Freezing on text input or pausing/playing a video | Graphics: WebRender | S3 | UNCONFIRMED |
| [1887835](https://bugzilla.mozilla.org/show_bug.cgi?id=1887835) | [meta] [project] Quad shaders | Graphics: WebRender | S3 | NEW |
| [1769944](https://bugzilla.mozilla.org/show_bug.cgi?id=1769944) | Credit Card backdrop-filter animation uses 2x more GPU than Chrome | Graphics: WebRender | S3 | UNCONFIRMED |
| [1988728](https://bugzilla.mozilla.org/show_bug.cgi?id=1988728) | backdrop-filter: blur is laggy when GPU acceleration isn't available | Graphics: WebRender | S3 | UNCONFIRMED |
| [1799334](https://bugzilla.mozilla.org/show_bug.cgi?id=1799334) | backdrop-filter doesn't blur remote `<browser>` element | Graphics: WebRender | S3 | UNCONFIRMED |
| [2002404](https://bugzilla.mozilla.org/show_bug.cgi?id=2002404) | Selecting hamburger menu can activate video playback | Graphics: WebRender | S3 | UNCONFIRMED |
| [1582153](https://bugzilla.mozilla.org/show_bug.cgi?id=1582153) | [meta] [project] Improve blob rendering performance | Graphics: WebRender | S2 | NEW |
| [1997150](https://bugzilla.mozilla.org/show_bug.cgi?id=1997150) | Image upsampling is not gamma-correct | Graphics | S3 | NEW |
| [1806281](https://bugzilla.mozilla.org/show_bug.cgi?id=1806281) | An image on a Codepen demo is blurry (perspective ChooseScale) | Graphics: WebRender | S3 | ASSIGNED |
| [1985706](https://bugzilla.mozilla.org/show_bug.cgi?id=1985706) | Full-page screenshots from extensions show a 1px dark line | Graphics | S3 | NEW |
| [1996466](https://bugzilla.mozilla.org/show_bug.cgi?id=1996466) | Firefox freezes or temporarily crashes when opening website from history | Graphics | S3 | UNCONFIRMED |
| [2005440](https://bugzilla.mozilla.org/show_bug.cgi?id=2005440) | [Regression] Emojis fail to render on macOS (aarch64) in Lockdown mode | Graphics | S3 | ASSIGNED |
| [1726232](https://bugzilla.mozilla.org/show_bug.cgi?id=1726232) | [css-borders-4] Add CSS corner-shape support | Graphics: WebRender | S3 | NEW |

### Seed Distribution by Creation Month

```
Pre-2026   [████████████░░] 13 bugs  (changed recently, created earlier)
Jan 2026   [███████░░░░░░░]  7 bugs
Feb 2026   [███████████████████░░░░░░░░] 19 bugs
Mar 2026   [████████████░░░░░] 11 bugs
           ├──────────────────────────────────┤
           Dec 2025      Jan       Feb       Mar 2026
```

---

## Theme 1: WebRender GPU Process Topcrash — `copy_into_staging_buffer`

**User-facing impact:** Firefox crashes silently in the GPU process on Windows. Users on Nightly (Firefox 150) experience sudden browser crashes with no warning, particularly during rendering operations. **29,263 crashes** in the last 30 days — up from just 35 in the prior 30-day window. This represents an **836x increase** and is the single most urgent issue in this report.

> **STAGNATION ALERT:** Bug [2021367](https://bugzilla.mozilla.org/show_bug.cgi?id=2021367) filed 2026-03-05 with `topcrash` keyword, currently unassigned with severity `--`. Given 29,263 crash reports, this warrants immediate S1/P1 triage.

### Breadcrumbs

| Bug ID | Summary | Severity | Status | Last Changed |
|--------|---------|----------|--------|--------------|
| [2021367](https://bugzilla.mozilla.org/show_bug.cgi?id=2021367) | Crash in [@ webrender::renderer::upload::copy_into_staging_buffer] | -- | NEW | 2026-03-18 |

### Crash Volume

| Metric | Value |
|--------|-------|
| Crash volume (last 30d) | **29,263** |
| Crash volume (prior 30d, Jan 17–Feb 17) | 35 |
| Trend | **Rising (836x spike)** |
| Top platform | Windows NT (100%) |
| Process type | GPU (100%) |
| Affected versions | Firefox 150.0a1 (nightly, 99.9%), 149.0a1 (nightly), 147.x (release, marginal) |

### Timeline Narrative

This crash was quiet until early March 2026, when volume exploded. Bug [2021367](https://bugzilla.mozilla.org/show_bug.cgi?id=2021367) was filed on 2026-03-05 and tagged `topcrash` by triage, blocking the Graphics Triage Tracker ([1632611](https://bugzilla.mozilla.org/show_bug.cgi?id=1632611)). As of this report it remains **unassigned with no severity set**. The crash is exclusively in the GPU process on Windows, pointing to a Windows-specific WebRender upload path regression introduced in the Firefox 150 nightly development cycle.

**Socorro link:** [webrender::renderer::upload::copy_into_staging_buffer](https://crashes.mozilla.org/signatures?q=signature%3A%22webrender%3A%3Arenderer%3A%3Aupload%3A%3Acopy_into_staging_buffer%22)

---

## Theme 2: backdrop-filter Correctness and Performance

**User-facing impact:** The CSS `backdrop-filter` property is broken in a wide variety of scenarios — blur effects don't apply in tables or sticky elements, incorrect rendering on modal overlays, excessive GPU usage, and missing blur on remote browser elements. This affects popular real-world sites and browser chrome UI alike.

### Breadcrumbs

| Bug ID | Summary | Severity | Status | Last Changed |
|--------|---------|----------|--------|--------------|
| [1888025](https://bugzilla.mozilla.org/show_bug.cgi?id=1888025) | [meta] Fix correctness issues with backdrop-filter | S3 | NEW | 2026-03-12 |
| [1888024](https://bugzilla.mozilla.org/show_bug.cgi?id=1888024) | [meta] Fix performance issues with backdrop-filter | **S2** | NEW | 2025-12-05 |
| [2022521](https://bugzilla.mozilla.org/show_bug.cgi?id=2022521) | backdrop-filter renders incorrectly on modal overlays and sidebars | S3 | UNCONFIRMED | 2026-03-12 |
| [2016655](https://bugzilla.mozilla.org/show_bug.cgi?id=2016655) | Mixed rendering of background-attachment: fixed and backdrop-filter broken | S3 | NEW | 2026-03-13 |
| [1799334](https://bugzilla.mozilla.org/show_bug.cgi?id=1799334) | backdrop-filter doesn't blur remote `<browser>` element | S3 | UNCONFIRMED | 2026-03-17 |
| [1988728](https://bugzilla.mozilla.org/show_bug.cgi?id=1988728) | backdrop-filter: blur is laggy when GPU acceleration isn't available | S3 | UNCONFIRMED | 2026-03-17 |
| [1769944](https://bugzilla.mozilla.org/show_bug.cgi?id=1769944) | backdrop-filter animation uses 2x more GPU than Chrome | S3 | UNCONFIRMED | 2026-03-17 |
| [1909463](https://bugzilla.mozilla.org/show_bug.cgi?id=1909463) | backdrop-filter doesn't work with position sticky in complex pages | S3 | UNCONFIRMED | 2025-06-19 |
| [1905015](https://bugzilla.mozilla.org/show_bug.cgi?id=1905015) | backdrop-filter: blur doesn't apply in some usages of `thead` elements | S3 | NEW | 2024-07-29 |
| [1915010](https://bugzilla.mozilla.org/show_bug.cgi?id=1915010) | backdrop-filter: saturate causes text not to render | S3 | NEW | 2024-10-23 |
| [1955851](https://bugzilla.mozilla.org/show_bug.cgi?id=1955851) | mask-image doesn't work with child elements that use backdrop-filter blur | S3 | UNCONFIRMED | 2025-03-26 |
| [1991304](https://bugzilla.mozilla.org/show_bug.cgi?id=1991304) | Regression rendering bug when backdrop-filter is combined with other effects | S3 | NEW | 2025-11-18 |
| [2018607](https://bugzilla.mozilla.org/show_bug.cgi?id=2018607) | SVG backdrop-filter won't apply feTurbulence/feDisplacementMap | S3 | UNCONFIRMED | 2026-02-24 |

### Timeline Narrative

Two meta bugs were created in March 2024 — [1888024](https://bugzilla.mozilla.org/show_bug.cgi?id=1888024) for performance (S2, 9 deps) and [1888025](https://bugzilla.mozilla.org/show_bug.cgi?id=1888025) for correctness (S3, **51 deps**) — representing coordinated awareness of the problem. However, neither meta bug has a clear owner or active assignee as of this report. The correctness meta was last touched 2026-03-12 (when 2022521 was filed and linked). Correctness issues span at least 7 distinct failure modes across table elements, sticky positioning, opacity interactions, saturate filters, and remote browser elements. The performance meta (S2) hasn't had activity since December 2025.

> **STAGNATION ALERT:** [1888024](https://bugzilla.mozilla.org/show_bug.cgi?id=1888024) is S2 with no activity since 2025-12-05 — over 90 days stagnant.

---

## Theme 3: SVG Rendering Regressions and Performance

**User-facing impact:** SVG content misbehaves across multiple dimensions: large SVGs consume all system resources, recent regressions break `feOffset` shadows and `fill` attribute updates, `calc()` in geometry attributes renders wrong, and blob rendering performance has long-standing meta-tracked issues.

### Breadcrumbs

| Bug ID | Summary | Severity | Status | Last Changed |
|--------|---------|----------|--------|--------------|
| [1582153](https://bugzilla.mozilla.org/show_bug.cgi?id=1582153) | [meta] Improve blob rendering performance | **S2** | NEW | 2026-03-17 |
| [2020096](https://bugzilla.mozilla.org/show_bug.cgi?id=2020096) | Large SVG consumes all system resources | **S2** | NEW | 2026-03-17 |
| [2023989](https://bugzilla.mozilla.org/show_bug.cgi?id=2023989) | SVG feOffset shadow-effect positioned incorrectly and invalidated wrong | -- | NEW | 2026-03-18 |
| [2022954](https://bugzilla.mozilla.org/show_bug.cgi?id=2022954) | Changing SVG path fill attribute breaks display of another path | -- | NEW | 2026-03-14 |
| [2017679](https://bugzilla.mozilla.org/show_bug.cgi?id=2017679) | calc() in SVG rect x/y attributes renders incorrectly | S3 | UNCONFIRMED | 2026-02-19 |
| [2018607](https://bugzilla.mozilla.org/show_bug.cgi?id=2018607) | SVG backdrop-filter won't apply feTurbulence/feDisplacementMap | S3 | UNCONFIRMED | 2026-02-24 |
| [2015602](https://bugzilla.mozilla.org/show_bug.cgi?id=2015602) | Significant performance issue with complex SVG | S3 | UNCONFIRMED | 2026-02-20 |
| [1975517](https://bugzilla.mozilla.org/show_bug.cgi?id=1975517) | Apple TV trailer videos only use magenta and white colors in SW-WR | -- | NEW | 2026-03-13 |

### Timeline Narrative

The blob rendering meta bug [1582153](https://bugzilla.mozilla.org/show_bug.cgi?id=1582153) has accumulated over 100 dependencies since 2019 and remains S2/P3 with no clear completion horizon. More urgently, two fresh regressions landed in March 2026: [2023989](https://bugzilla.mozilla.org/show_bug.cgi?id=2023989) (feOffset wrong position, filed 2026-03-17, unassigned) and [2022954](https://bugzilla.mozilla.org/show_bug.cgi?id=2022954) (fill attribute breaks sibling paths, filed 2026-03-12 with `nightly-community` keyword). Both lack severity assignment. Bug [2020096](https://bugzilla.mozilla.org/show_bug.cgi?id=2020096) (large SVG resource exhaustion) is S2/P2 and was filed February 28 — still no assignee. The Apple TV color corruption ([1975517](https://bugzilla.mozilla.org/show_bug.cgi?id=1975517)) affects the Software WebRender fallback path and has been open since July 2025.

---

## Theme 4: WebRender Visual Regressions — 3D, Compositing, Forced Colors

**User-facing impact:** Several S2 regressions affect how content is composited: 3D transforms with opacity render incorrectly, large portions of the macOS UI glitch when the Layer Compositor is used, and — critically — Find in Page is completely invisible to users in Forced Colors (high-contrast) mode, breaking accessibility.

### Breadcrumbs

| Bug ID | Summary | Severity | Status | Last Changed |
|--------|---------|----------|--------|--------------|
| [1975275](https://bugzilla.mozilla.org/show_bug.cgi?id=1975275) | Find in page is invisible in forced colors mode | **S2** | NEW | 2026-02-26 |
| [2013967](https://bugzilla.mozilla.org/show_bug.cgi?id=2013967) | 3D transforms don't display correctly with opacity and rotation | **S2** | ASSIGNED | 2026-03-10 |
| [2019679](https://bugzilla.mozilla.org/show_bug.cgi?id=2019679) | WebRender GPU texture corruption triggered by CSS animation | **S2** | UNCONFIRMED | 2026-03-12 |
| [2020844](https://bugzilla.mozilla.org/show_bug.cgi?id=2020844) | Large parts of UI glitch with Layer Compositor on macOS | **S2** | UNCONFIRMED | 2026-03-09 |
| [1744455](https://bugzilla.mozilla.org/show_bug.cgi?id=1744455) | Window preview in alt+tab glitchy at 60Hz with Intel+Nvidia | S3 | NEW | 2026-03-15 |

### Timeline Narrative

Bug [1975275](https://bugzilla.mozilla.org/show_bug.cgi?id=1975275) is an accessibility regression (keywords: `access, regression, stalled`) filed July 2025 — **over 8 months ago** — where the Find in Page bar is completely invisible to users in Forced Colors mode. It is unassigned with no activity since February 2026. This directly harms users with visual impairments who rely on high-contrast mode.

Bug [2013967](https://bugzilla.mozilla.org/show_bug.cgi?id=2013967) (3D transforms + opacity) is assigned but `stalled`, last touched March 2026. The macOS compositor glitch [2020844](https://bugzilla.mozilla.org/show_bug.cgi?id=2020844) is S2 UNCONFIRMED, depends on the GPU memory leak meta [2017820].

> **STAGNATION ALERT:** [1975275](https://bugzilla.mozilla.org/show_bug.cgi?id=1975275) is S2 (accessibility regression) with the `stalled` keyword and no assignee. The `stalled` + S2 combination means this is acknowledged as important but blocked. **Needs immediate attention.**

> **STAGNATION ALERT:** [2013967](https://bugzilla.mozilla.org/show_bug.cgi?id=2013967) is S2 + `stalled` despite being ASSIGNED. Assignee needs to be checked for progress or reassigned.

---

## Theme 5: WebGL Compatibility and Security Issues

**User-facing impact:** A canvas security bug allows the WebGL canvas to accidentally display screen content from other desktop applications — a potential privacy/security vector. Separately, Google Maps turns black after zooming in WebGL, `blitFramebuffer` fails on Windows, and some WebGL2 shaders fail to link on Windows only.

### Breadcrumbs

| Bug ID | Summary | Severity | Status | Last Changed |
|--------|---------|----------|--------|--------------|
| [2020195](https://bugzilla.mozilla.org/show_bug.cgi?id=2020195) | Canvas displays screen content from other applications | **S2** | UNCONFIRMED | 2026-03-15 |
| [1866762](https://bugzilla.mozilla.org/show_bug.cgi?id=1866762) | WebGL blitFramebuffer doesn't work on Windows with RGB8 format | S3 | NEW | 2026-02-16 |
| [2010645](https://bugzilla.mozilla.org/show_bug.cgi?id=2010645) | WebGL Google map turns black after zooming | S3 | UNCONFIRMED | 2026-02-16 |
| [2019155](https://bugzilla.mozilla.org/show_bug.cgi?id=2019155) | Valid WebGL2 shaders get link error on Windows only | S3 | UNCONFIRMED | 2026-02-27 |
| [2018404](https://bugzilla.mozilla.org/show_bug.cgi?id=2018404) | webgl: report INVALID_ENUM instead of INVALID_VALUE | S3 | UNCONFIRMED | 2026-02-23 |
| [1986389](https://bugzilla.mozilla.org/show_bug.cgi?id=1986389) | gsmarena.com — 3D image not displayed | S4 | NEW | 2026-03-09 |

### Timeline Narrative

Bug [2020195](https://bugzilla.mozilla.org/show_bug.cgi?id=2020195) is the most concerning: filed March 1, 2026, it has keywords `reporter-external, sec-vector` and is currently UNCONFIRMED (S2/P2). If confirmed, this is a privacy regression — GPU texture memory from other processes leaking into the canvas context. It is linked to the Graphics Triage Tracker. The WebGL regression [1866762](https://bugzilla.mozilla.org/show_bug.cgi?id=1866762) (blitFramebuffer on Windows/RGB8) has 18 comments but no assignee after being open since November 2023.

---

## Theme 6: GPU Memory Leaks

**User-facing impact:** Firefox's GPU process leaks memory over time, leading to system slowdowns and eventual crashes. This affects users who run WebGL-heavy applications (e.g., Foundry Virtual Tabletop) and has also been linked to long-running tab use.

### Breadcrumbs

| Bug ID | Summary | Severity | Status | Last Changed |
|--------|---------|----------|--------|--------------|
| [1902566](https://bugzilla.mozilla.org/show_bug.cgi?id=1902566) | [meta] Graphics memory leaks (system and/or GPU) | S3 | NEW | 2026-02-18 |
| [1965442](https://bugzilla.mozilla.org/show_bug.cgi?id=1965442) | Freezing on text input or pausing/playing a video | S3 | UNCONFIRMED | 2026-03-17 |
| [2017580](https://bugzilla.mozilla.org/show_bug.cgi?id=2017580) | GPU process memory growth when Foundry Virtual Tabletop is launched | S3 | UNCONFIRMED | 2026-02-20 |
| [2013674](https://bugzilla.mozilla.org/show_bug.cgi?id=2013674) | Memory leak (10 comments) | S3 | UNCONFIRMED | 2026-02-25 |
| [1996466](https://bugzilla.mozilla.org/show_bug.cgi?id=1996466) | Firefox freezes or temporarily crashes when opening website from history | S3 | UNCONFIRMED | 2026-03-16 |

### Timeline Narrative

Meta bug [1902566](https://bugzilla.mozilla.org/show_bug.cgi?id=1902566) (created June 2024, P2, 18 deps) tracks a known category of GPU memory leak bugs. Bug [1965442](https://bugzilla.mozilla.org/show_bug.cgi?id=1965442) has been accumulating reports since May 2025 (18 comments), blocking both the Graphics Triage Tracker and the GPU memory meta. [2017580](https://bugzilla.mozilla.org/show_bug.cgi?id=2017580) implicates Foundry Virtual Tabletop, suggesting a WebGL-specific memory leak path.

---

## Theme 7: Text and Font Rendering Issues

**User-facing impact:** Text appears blurry in certain states, emoji fail to render on locked-down macOS builds, Linux Nightly shows systematic font blurriness, and two FreeType-related crashes affect text rendering stability.

### Breadcrumbs

| Bug ID | Summary | Severity | Status | Last Changed |
|--------|---------|----------|--------|--------------|
| [2005440](https://bugzilla.mozilla.org/show_bug.cgi?id=2005440) | [Regression] Emojis fail to render on macOS aarch64 in Lockdown mode | S3 | ASSIGNED | 2026-03-16 |
| [2016821](https://bugzilla.mozilla.org/show_bug.cgi?id=2016821) | Blurry text, which becomes sharp when selecting | S3 | NEW | 2026-03-10 |
| [2018463](https://bugzilla.mozilla.org/show_bug.cgi?id=2018463) | Firefox Nightly Linux font rendering is blurry | S3 | UNCONFIRMED | 2026-02-23 |
| [2021699](https://bugzilla.mozilla.org/show_bug.cgi?id=2021699) | Stack exhaustion in FreeType load_truetype_glyph() | S3 | NEW | 2026-03-12 |
| [2015471](https://bugzilla.mozilla.org/show_bug.cgi?id=2015471) | Crash in [@ memcpy \| FT_Stream_ReadAt] | S3 | NEW | 2026-02-20 |
| [2019903](https://bugzilla.mozilla.org/show_bug.cgi?id=2019903) | Shutdown hang from LoadCmapsRunnable | S3 | NEW | 2026-03-08 |

### Timeline Narrative

The emoji regression [2005440](https://bugzilla.mozilla.org/show_bug.cgi?id=2005440) (27 comments, P3) has been ASSIGNED since December 2025 and is still open — it specifically affects macOS aarch64 in Lockdown Mode, a security-sensitive context. Blurry text reports ([2016821](https://bugzilla.mozilla.org/show_bug.cgi?id=2016821), [2018463](https://bugzilla.mozilla.org/show_bug.cgi?id=2018463)) may share a root cause around text selection triggering re-render with correct hinting. The two FreeType crashes are unconfirmed and untriaged.

---

## Emerging Theme: Intel Arc A770 Persistent Tab Crash

**User-facing impact:** Intel Arc A770 GPU users experience tab crashes without crash reports being generated, making the issue hard to diagnose remotely. 67 comments over 2+ years suggests significant community impact.

### Breadcrumbs

| Bug ID | Summary | Severity | Status | Last Changed |
|--------|---------|----------|--------|--------------|
| [1835275](https://bugzilla.mozilla.org/show_bug.cgi?id=1835275) | [Intel Arc A770] rendertexturehost tab crash without crash report | S3 | REOPENED | 2026-02-16 |

**Assignee:** sotaro.ikeda.g@gmail.com

The bug has been REOPENED, indicating a prior fix regressed. With 67 comments and Intel Arc being a common modern GPU, the real-world impact is likely broader than the bug count implies. Note: crashes without reports are systematically undercounted in Socorro.

---

## Signal Summary Table

| Rank | Theme | Breadcrumbs | Meta Bug | Top Severity | Notes |
|------|-------|-------------|----------|-------------|-------|
| 1 | WebRender Topcrash (copy_into_staging_buffer) | 1 | — | `--` (should be S1) | **29,263 crashes**, 836x spike, Windows GPU process, nightly 150.0a1, **unassigned** |
| 2 | backdrop-filter Correctness & Performance | 13 | [1888025](https://bugzilla.mozilla.org/show_bug.cgi?id=1888025) (51 deps), [1888024](https://bugzilla.mozilla.org/show_bug.cgi?id=1888024) (9 deps) | S2 | Long-standing, S2 perf meta stagnant >90d |
| 3 | SVG Rendering & Performance | 8 | [1582153](https://bugzilla.mozilla.org/show_bug.cgi?id=1582153) (100+ deps) | S2 | 2 fresh regressions in March 2026; S2 resource exhaustion untriaged |
| 4 | WebRender Visual Regressions (3D, Compositing, Forced Colors) | 5 | — | S2 | S2 accessibility regression stalled 8+ months |
| 5 | WebGL Compatibility & Security | 6 | — | S2 | Potential privacy bug (canvas shows other apps' content) |
| 6 | GPU Memory Leaks | 5 | [1902566](https://bugzilla.mozilla.org/show_bug.cgi?id=1902566) (18 deps) | S3 | P2 meta; ongoing freeze/crash reports |
| 7 | Text & Font Rendering | 6 | — | S3 | Emoji regression assigned but stalled; FreeType crashes untriaged |
| 8 | Intel Arc A770 Tab Crash | 1 | — | S3 | 67 comments, REOPENED, assigned to sotaro.ikeda.g |

---

## Resources Used

- **Bugzilla REST API:** Query A (creation-time seed, 38 bugs), Query B (changed-time seed, 25 bugs), dependency batch fetches, keyword expansion (regression, webcompat:site-report)
- **Socorro:** `socorro-cli search` for `webrender::renderer::upload::copy_into_staging_buffer` (volume, platform, process type, trend comparison)
- **Meta bugs discovered:** 1887835 (quad shaders, 37 deps), 1582153 (blob perf, 100+ deps), 1888024 (backdrop-filter perf, 9 deps), 1888025 (backdrop-filter correctness, 51 deps), 1632611 (triage tracker), 1902566 (memory leaks, 18 deps)
- **Depth-5 dep crawl** performed; meta bugs with >50 deps limited to 20 most recently changed

## Suggestions for Improving This Skill

- **Socorro signature format sensitivity:** The tool returned 0 results for partial-match signatures (e.g. `load_truetype_glyph`) but 29,263 for exact Rust path signatures. A fallback `--facet signature` search with a keyword could auto-discover the right signature from a bug's crash keyword.
- **cc_count enrichment:** The batch API omitted `cc_count` for all bugs — a secondary targeted fetch for cc_count would improve signal scoring accuracy.
- **Assigned bug staleness:** When a bug is ASSIGNED + stalled, a diff of last-comment-author vs. assignee would help identify stuck handoffs vs. active owners.

---

> *"The detective's art is not to find the obvious clue, but to notice the 836 copies of it."*

