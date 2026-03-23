# Bug 2024358 Triage Analysis

**Generated:** 2026-03-21
**Bug URL:** https://bugzilla.mozilla.org/show_bug.cgi?id=2024358

## Bug Information

- **Summary:** firefox browser can not detect org.freedesktop.Platform.codecs-extra causing HEVC software decoding to be unavailable
- **Reporter:** firefoxuserman (striking.stoat.jfzj@hidingmail.com)
- **Status:** UNCONFIRMED
- **Product:** Core
- **Component:** Audio/Video: Playback
- **Created:** 2026-03-18 (3 days ago)
- **Severity/Priority:** -- / -- (unset)
- **Security Sensitive:** No

## Research Summary and Key Findings

The reporter is running Firefox Flatpak (from Flathub) on Fedora Silverblue and observes that HEVC
software decoding is reported as unsupported in about:support, even though
`org.freedesktop.Platform.codecs-extra` is installed (it is part of the default Freedesktop SDK
25.08 runtime). Installing the deprecated `org.freedesktop.Platform.ffmpeg-full` (24.08) resolves
the issue.

The root cause is a Freedesktop SDK runtime transition: `ffmpeg-full` was the traditional Flatpak
codec extension providing a full ffmpeg build with proprietary codecs (including HEVC/H.265). It was
discontinued in SDK 24.08 and replaced by `codecs-extra`. However, `codecs-extra` does not appear
to include HEVC software decoding, and Firefox Flatpak has not been updated to adapt to this
transition.

The Firefox Flatpak build is already configured to use `FREEDESKTOP_VERSION = "25.08"` (see
[flatpak.py](https://searchfox.org/mozilla-central/source/python/mozbuild/mozbuild/repackaging/flatpak.py#25))
and pulls from the `org.mozilla.firefox.BaseApp` channel pinned to 25.08. The codec detection logic
is not in Firefox's media code but in the Flatpak runtime/BaseApp environment.

**Related bugs:**
- [2021122](https://bugzilla.mozilla.org/show_bug.cgi?id=2021122) — "HEVC video doesn't play in
  flatpak builds" (NEW, S3/P3) — Filed 2026-03-04 by Jeff Muizelaar [:jrmuizel]
  (jmuizelaar@mozilla.com). Attributes the same root cause: ffmpeg in the Flatpak environment
  lacking HEVC decode support. References our bug via `see_also`. **High likelihood of being
  the canonical tracking bug for this issue.**
- [2020823](https://bugzilla.mozilla.org/show_bug.cgi?id=2020823) — "h264 video not decoded with
  hardware in flatpak build" (NEW, S3/P3) — Filed same day by Jeff Muizelaar. Related ffmpeg
  decode issue in the Flatpak environment for H264. Both bugs block meta
  [1867638](https://bugzilla.mozilla.org/show_bug.cgi?id=1867638) (Steam Deck issues).
- [1940880](https://bugzilla.mozilla.org/show_bug.cgi?id=1940880) — "Firefox flatpak need version
  23.06 ffmpeg-full as a dependency" (NEW, S3) — Earlier report of ffmpeg version compatibility
  in Flatpak. A patch was posted to pin ffmpeg to 23.04 to avoid 24.08 issues.
- [1867638](https://bugzilla.mozilla.org/show_bug.cgi?id=1867638) — "[meta] Steam Deck related
  issues (Arch Linux flatpak distribution)" — Meta bug tracking a cluster of Flatpak/SteamOS
  codec and playback issues.

**Bug 2024358 is likely a duplicate or related sub-report of bug 2021122**, which was filed two
weeks earlier by a Mozilla employee and tracks the same underlying issue. However, 2024358 adds
useful context about the specific package transition (`ffmpeg-full` → `codecs-extra`) and confirms
HEVC software decoding as the affected capability.

## Classification

| Signal | Detected | Evidence |
|--------|----------|----------|
| Clear STR | Yes | Steps are specific: Fedora Silverblue + Firefox Flatpak + check about:support |
| Test Case | No | No attached test file |
| Crash Stack | No | Not a crash |
| Fuzzing | No | User-reported |

**Platform:** Linux x86_64, Fedora Silverblue, Firefox 148.0 (Flatpak from Flathub)

## Regression Timeline

Not explicitly a regression, but represents a breakage introduced by the Freedesktop SDK 25.08
transition that removed `ffmpeg-full` and replaced it with `codecs-extra`. The reporter notes
`ffmpeg-full` was discontinued since SDK 24.08.

## Assessment

- **Suggested Severity:** S3
- **Suggested Priority:** P3

### Assessment Reasoning

This is a platform-specific codec support issue affecting Firefox Flatpak users on Linux systems
using the Freedesktop SDK 25.08 runtime. HEVC software decoding is unavailable because
`codecs-extra` (the SDK 25.08 codec extension) does not provide HEVC support in the way that the
deprecated `ffmpeg-full` extension did. This affects a meaningful subset of Flatpak users on modern
Linux distributions (those on Freedesktop SDK 25.08 without `ffmpeg-full` installed).

The severity is S3 (significant but not data-loss or security critical): a specific codec (HEVC)
fails to software-decode in a specific Firefox distribution channel (Flatpak). Hardware HEVC
decoding reportedly still works, and the issue can be worked around by installing the deprecated
`ffmpeg-full` extension. Other major functionality is unaffected.

The fix is likely in the Firefox Flatpak BaseApp configuration or the `org.mozilla.firefox.BaseApp`
repository (maintained outside the Firefox source tree). This may require either updating the
Flatpak manifest to explicitly depend on `codecs-extra` for codec passthrough, or coordinating with
Freedesktop SDK maintainers to ensure HEVC support is available via `codecs-extra`. Given bug
2021122 is already being tracked by a Mozilla employee, this bug should be marked as a duplicate or
linked as a see_also.

## Codebase Investigation

The relevant Firefox code is at
[python/mozbuild/mozbuild/repackaging/flatpak.py](https://searchfox.org/mozilla-central/source/python/mozbuild/mozbuild/repackaging/flatpak.py):
- Line 25: `FREEDESKTOP_VERSION = "25.08"` — confirms Firefox Flatpak targets SDK 25.08
- The build pulls `org.mozilla.firefox.BaseApp` at channel `25.08` from Flathub
- Codec detection is not in Firefox's media code (`dom/media`) — it's entirely in the Flatpak runtime/BaseApp layer

No codec detection logic specific to `ffmpeg-full` or `codecs-extra` was found in the Firefox
source. The issue is upstream of Firefox's own code, in how the Flatpak runtime exposes codec
libraries to the sandboxed application.

## Suggested Investigation Areas

1. **org.mozilla.firefox.BaseApp** — Check whether the BaseApp's Flatpak manifest for the 25.08
   channel correctly declares `codecs-extra` as a codec extension and whether ffmpeg is built with
   HEVC support in that context.
2. **Bug 2021122** — Jeff Muizelaar's bug is the canonical tracking bug. Consider marking 2024358
   as a duplicate of 2021122 or adding it to `see_also`.
3. **`codecs-extra` package contents** — Verify whether `org.freedesktop.Platform.codecs-extra`
   (25.08) actually includes HEVC/H.265 support in its ffmpeg build, or whether this codec is
   intentionally excluded due to patent concerns.
4. **Bug 1940880 patch** — Review the patch posted by aosmond@mozilla.com that pins ffmpeg to
   23.04 to understand how the BaseApp manages codec version dependencies.

## Bugzilla Use Tracking

- Total Bugzilla Queries: 10
- Total Bugs Processed: 6 (2024358, 2021122, 2020823, 1940880, 1867638, search results)
- Estimated Download Bandwidth Used: ~0.2 MB
- Inaccessible Bugs Due to Permissions: 0
