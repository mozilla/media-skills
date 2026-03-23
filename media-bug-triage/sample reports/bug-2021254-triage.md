# Bug 2021254 Triage Analysis

**Generated:** 2026-03-21
**Bug URL:** https://bugzilla.mozilla.org/show_bug.cgi?id=2021254

## Bug Information

- **Summary:** Rendering issue on complex transform with box-shadow
- **Reporter:** mynameiskaneel@gmail.com (Guillaume, external)
- **Status:** UNCONFIRMED
- **Product:** Core
- **Component:** Graphics: WebRender
- **Created:** 2026-03-05 (16 days ago)
- **Severity/Priority:** unset / unset
- **Security Sensitive:** No

## Research Summary and Key Findings

The reporter describes a visual artifact where a `box-shadow` is visually cut/clipped when the element has a complex CSS transform combining `skew(20deg) rotate(90deg)`. The effect worsens at larger viewport breakpoints, which the reporter attributes to responsive design using viewport-width (`vw`) units. The issue is that the shadow edge is abruptly cut rather than rendering fully around the transformed element.

The reporter (Guillaume) provided two attachments at filing time:
- `mynameiskaneeldotcom.zip` — likely a test case (website reproduction)
- `mynameiskaneel_bug.json` — described as "my profile" in comment 2, suggesting a Firefox profile or profiler capture

[alice0775@gmail.com](https://bugzilla.mozilla.org/user_profile?login=alice0775%40gmail.com) (a prolific and accurate external reporter known for media/graphics bug accuracy) added herself to CC within 30 minutes of filing, suggesting she spotted the issue independently or confirmed she could reproduce it. She has not commented.

The component was automatically moved from Firefox::Untriaged to Core::Graphics: WebRender by the release-mgmt bot on 2026-03-19.

### Codebase Context

In `CreateWebRenderCommands` for `nsDisplayBoxShadowOuter` ([nsDisplayList.cpp:4519](https://searchfox.org/mozilla-central/source/layout/painting/nsDisplayList.cpp#4519)), the clip rect passed to WebRender for the shadow primitive is derived from `GetBoundsInternal()`, which calls [`nsLayoutUtils::GetBoxShadowRectForFrame`](https://searchfox.org/mozilla-central/source/layout/base/nsLayoutUtils.cpp#8099). This function computes the shadow's bounding rectangle in the frame's **local coordinate space**, accounting for shadow offset, spread, and blur radius — but without knowledge of the applied CSS transform.

When a complex 2D transform like `skew(20deg) rotate(90deg)` is applied, the visual extent of the shadow in screen space diverges significantly from the layout-space bounds. WebRender applies the transform via its spatial tree, but if the clip rect is too small relative to the actual screen-space extent of the shadow, it can appear cut. The "larger breakpoints" symptom is consistent with this: as the element grows wider via `vw` units, the skew and rotation produce a proportionally larger discrepancy between the layout-space clip and the screen-space extent of the shadow.

### Related Bugs

- **[1973159](https://bugzilla.mozilla.org/show_bug.cgi?id=1973159)** (S3, NEW) — "Transformed child in a transformed element has incorrect overflow box" — alice0775 identified a regression window for this. It directly addresses WebRender producing incorrect overflow/clip boxes for elements under complex transforms. Possibly the same root cause.
- **[1986109](https://bugzilla.mozilla.org/show_bug.cgi?id=1986109)** (S3, NEW) — "Graphical glitches when 'overflow: clip' is toggled with rotate/scale transform" — similar category: transforms + clipping/overflow in WebRender.
- **[2018240](https://bugzilla.mozilla.org/show_bug.cgi?id=2018240)** (N/A, P3, REOPENED) — "Implement box-shadow primitives on top of the quad infrastructure" — Nicolas Silva (nical) is actively reworking box-shadow rendering in WebRender. First comment: "Today WR contains a first attempt at supporting box-shadow which is disabled. I want to follow a different approach." This ongoing refactor may resolve or relate to the current bug.

## Regression Timeline

Not reported as a regression. No mozregression data provided. No information on which Firefox version introduced the issue.

## Classification

| Signal | Detected | Evidence |
|--------|----------|----------|
| Clear STR | Partial | Description references skew+rotate+box-shadow; test case zip attached but no in-comment steps |
| Test Case | Likely | zip attachment `mynameiskaneeldotcom.zip` provided at filing |
| Crash Stack | No | Not a crash |
| Fuzzing | No | External user report |

## Assessment

- **Suggested Severity:** S3
- **Suggested Priority:** --

### Assessment Reasoning

This is a visual rendering defect affecting a specific combination of CSS features (complex 2D transforms + `box-shadow`). There is no data loss, no crash, and no security concern. The affected scenario — `skew + rotate + box-shadow + vw sizing` — is relatively niche, but the reporter has provided a test case and the prolific reporter alice0775 was quick to CC herself, suggesting the issue is real and reproducible.

The severity is S3 because this represents incorrect rendering behavior of a CSS standard feature that a developer has specifically relied on. The impact is visual only and limited to this specific transform combination.

The issue fits a known pattern in WebRender where clip bounds for primitives are computed in layout space without full accounting for how complex transforms change the screen-space extent of those bounds. Bug [1973159](https://bugzilla.mozilla.org/show_bug.cgi?id=1973159) tracks a closely related issue. The active box-shadow refactor in bug [2018240](https://bugzilla.mozilla.org/show_bug.cgi?id=2018240) by nical may be relevant context.

More information is needed from the reporter (OS, regression range, cross-browser comparison) before a developer can confidently investigate.

## Codebase Investigation

### Relevant Files Examined

- [layout/painting/nsDisplayList.cpp](https://searchfox.org/mozilla-central/source/layout/painting/nsDisplayList.cpp) — `nsDisplayBoxShadowOuter::CreateWebRenderCommands` (line 4519): pushes box-shadow to WebRender; derives `clipRect` from `GetBounds()`.
- [layout/base/nsLayoutUtils.cpp](https://searchfox.org/mozilla-central/source/layout/base/nsLayoutUtils.cpp) — `GetBoxShadowRectForFrame` (line 8099): computes shadow bounding rect in frame-local space (offset + spread + blur, no transform knowledge).
- [gfx/wr/webrender/src/box_shadow.rs](https://searchfox.org/mozilla-central/source/gfx/wr/webrender/src/box_shadow.rs) — `add_box_shadow` (line 175): WebRender side; uses `prim_info.clip_rect` as the clip for the shadow primitive.
- [gfx/wr/webrender/src/pattern/mod.rs](https://searchfox.org/mozilla-central/source/gfx/wr/webrender/src/pattern/mod.rs) — new pattern-based box-shadow module, part of bug 2018240 refactor work.

### Findings

The layout-space clip rect for the box-shadow is computed without awareness of the applied CSS transform. For a simple translate this is fine; for `skew + rotate`, the screen-space extent of the shadow can significantly exceed the layout-space bounds used as the clip. This is the likely cause of the visible cut.

The "larger breakpoints" symptom is explained by: as the element width grows (via `vw` units), the skew produces a proportionally taller visual footprint in screen space, while the layout-space clip remains based on the original rectangular bounds.

### Suggested Investigation Areas

1. **`nsDisplayBoxShadowOuter::GetBoundsInternal`** — Check if bounds computed here adequately account for the transform when used as a WR clip rect.
2. **Bug 1973159** — Investigate whether the incorrect overflow box for transformed elements is the same root cause.
3. **`GetBoxShadowRectForFrame`** — Verify whether the function's output needs to be inflated to account for complex transforms before being used as a clip rect in WR.
4. **Bug 2018240** — Nicolas Silva's box-shadow refactor may already address this or provide a better foundation to fix it.

## Suggested Response to Reporter

```
Thank you for the detailed report and for attaching a test case!

To help us investigate this further, could you please provide:

1. **Operating system and version** (e.g., Windows 11, macOS 15, Ubuntu 24.04)
2. **Does this issue occur in other browsers?** (e.g., Chrome, Safari) — this helps us determine if it's Firefox-specific behavior or a cross-browser rendering difference.
3. **Is this a regression?** Did it work correctly in an older version of Firefox? If so, approximately when did it stop working? You can use [mozregression](https://mozilla.github.io/mozregression/) to bisect the range.
4. **Steps to reproduce** — could you share a minimal HTML/CSS snippet that demonstrates the issue? (The attached zip is helpful, but a self-contained snippet makes it easier for us to test quickly.)

Thank you again for the clear description and test case!
```

## Bugzilla Use Tracking

- Total Bugzilla Queries: 11
- Total Bugs Processed: 14
- Estimated Download Bandwidth Used: ~0.2 MB
- Inaccessible Bugs Due to Permissions: 0
