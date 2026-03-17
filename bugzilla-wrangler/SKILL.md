---
name: bugzilla-wrangler
description: Support deep dive analysis of Bugzilla reports within specific Products and Components.
---

# Bugzilla Wrangler Skill

## Goal

Discover and surface recurring themes in user-reported Firefox bugs. Connect disparate reports to shared themes, build timelines, assign signal strength, and present actionable findings.

---

## Run Configuration

At invocation, resolve these two settings before doing anything else. State both in the Session Info section of the report.

**Scope profile** — If the user specified a platform or topic (e.g. "android", "web-conferencing", "graphics"), use that profile from the Scope Profiles section below. Otherwise use `media`.

**Seed date window** — If the user specified a date range (e.g. "Q1 2025", "last 90 days", "January through March 2026"), parse it into an explicit `YYYY-MM-DD` lower bound and upper bound and use those in Step 1. Otherwise use the default window:
- Lower bound: `2025-01-01`
- Upper bound: `2025-03-31`

## Scope Profiles

At invocation, check whether the user specified a platform or topic (e.g. "android", "web-conferencing", "graphics"). If so, use the matching profile below. If not, use `media`.

### media
- **Product:** Core
- **Components:** Audio/Video, Audio/Video: cubeb, Audio/Video: GMP, Audio/Video: MediaStreamGraph, Audio/Video: Playback, Audio/Video: Recording, Audio/Video: Web Codecs

### android
- **Product:** Firefox for Android
- **Components:** Media
- **Product:** GeckoView
- **Components:** Media

### web-conferencing
- **Product:** Core
- **Components:** WebRTC, WebRTC: Audio/Video, WebRTC: Networking, DOM: Screen Capture

### media-and-web-conferencing
- **Product:** Core
- **Components:** Audio/Video, Audio/Video: cubeb, Audio/Video: GMP, Audio/Video: MediaStreamGraph, Audio/Video: Playback, Audio/Video: Recording, Audio/Video: Web Codecs, WebRTC, WebRTC: Audio/Video, WebRTC: Networking, DOM: Screen Capture

### graphics
- **Product:** Core
- **Components:** Graphics, Graphics: WebRender, Graphics: CanvasWebGL, Graphics: Layers, Graphics: Text, Canvas: 2D, Layout: Painting, CSS Painting and Compositing

Always exclude bugs belonging to core security groups.

---

## Definitions

**Breadcrumb** — Any resource associated with a theme: a bug report, test case, crash report, etc.

**Signal** — A measure of theme importance based on the number and quality of breadcrumbs. See scoring rules below.

---

## Bugzilla Access Rules

- **Cache first.** Before any API request, derive the cache filename from the active scope: `reports/wrangler_cache_<scope>.json` (e.g. `wrangler_cache_android.json`, `wrangler_cache_media.json`). If that file exists and was written in the current session, load from it. Write to it after every fetch so later steps can reuse the data. Never read or write a different scope's cache file.
- **Batch lookups.** Fetch multiple bugs in one request using `?id=A,B,C` rather than one request per bug.
- **Request only needed fields.** Always include: `id, summary, component, severity, status, creation_time, last_change_time, keywords, depends_on, blocks, cc_count`
- **Fetch `cc_count` separately if missing.** The field can be omitted by the API depending on visibility. If `cc_count` is absent after a batch fetch, retrieve it with a targeted request: `?id=A,B,C&include_fields=id,cc_count`. Always persist `cc_count` in the cache so signal scoring can use it without a second fetch.

---

## Signal Scoring

Apply these rules when ranking themes. Higher-weight factors are listed first.

| Factor | Effect |
|--------|--------|
| Meta/tracking bug exists (`keywords=meta`) | Strong multiplier — use its total dependency count as a proxy for theme breadth |
| Bug status is NEW or ASSIGNED | Counts more than UNCONFIRMED (triage has validated it) |
| `regression` keyword present | Higher priority — represents a user-visible regression from a prior release |
| `stalled` keyword with S1 or S2 severity | Notable: acknowledged but not actively worked |
| High `cc_count` | Proxy for how many users are affected |
| Multiple independent reporters with near-identical summaries | Strong signal that the issue is widespread |
| `last_change_time` older than 30 days with no resolution | Marks a theme as stagnant — call this out in the report |

A theme requires at least 3 breadcrumbs to be included in the report.

---

## Workflow

Before starting, identify the active scope profile. If the user specified a platform (e.g. "android") at invocation, use that profile's Product and Component set for all seed searches and keyword expansion queries. Otherwise use `media`. State the active profile in the Session Info section of the report.

### Step 1 — Fetch Seed Bugs

Retrieve a seed sample of up to 50 bugs using the seed date window resolved in Run Configuration.

Bugzilla REST API parameters for the date window:
- `creation_time=<lower-bound>` — resolved lower bound
- `f1=creation_ts&o1=lessthan&v1=<upper-bound>` — resolved upper bound

Both bounds are required. Additional filters:
- `status=UNCONFIRMED&status=NEW&status=ASSIGNED&status=REOPENED`
- `f2=bug_severity&o2=notequals&v2=--` and `f3=bug_severity&o3=notequals&v3=N/A`
- `f4=keywords&o4=notsubstring&v4=intermittent-testcase` — exclude CI-only intermittent bugs that consume seed slots without representing user-facing issues
- `order=changeddate%20DESC` — surface recently-active bugs first to improve theme freshness

Save results to the cache.

### Step 2 — Identify Initial Themes

Read the seed bugs and group them by shared symptoms, components, keywords, or user-facing impact. Name each candidate theme descriptively (e.g., "Bluetooth audio stutter", "WebRender visual glitches").

### Step 3 — Dependency Crawl + Socorro Crash Enrichment

For each seed bug, collect `depends_on` and `blocks` IDs. Batch-fetch them in a single request. Repeat up to **depth 5**. Do not restrict your search to specific bugzilla products and components. Search any Product or Component when crawling for breadcrumbs.

Prioritize bugs with `keywords=meta` — these tracking bugs directly amplify signal. Note the total dependency count of any meta-bug you find.

When crawling deps of a meta-bug that has more than 50 dependencies, do not fetch all of them. Instead, filter to the most recent by sorting: use `order=changeddate%20DESC&limit=20` to fetch only the 20 most recently changed deps. This avoids context overload from omnibus tracking bugs (e.g. site-scout meta).

**Alongside the dep crawl**, for any seed bug or dep bug (at any crawl depth) that carries the `crash` keyword, cross-reference with Socorro to quantify user impact. Use `socorro-cli` to look up each crash signature:

```
socorro-cli search --signature "TrackBuffersManager::RemoveFrames"
socorro-cli search --signature "CAudioClient::GetCurrentPadding"
```

**Android/Fenix scope:** Java and Kotlin stack traces use a different product namespace in Socorro and return 0 results when searched without a product filter. For the `android` scope profile, always pass `--product Fenix` and use `--facet signature` to discover relevant crash signatures rather than guessing Java class names directly:

```
socorro-cli search --product Fenix --facet signature --num-facets 20
socorro-cli search --product Fenix --facet signature --query "media" --num-facets 20
```

Pick the most relevant signatures from the facet output, then drill into each with a standard `--signature` search to get volume and trend data.

For each crash bug, note:
- **Volume:** number of crash reports in the past 30 days
- **Top platform:** which OS accounts for the most reports
- **Trend:** rising, stable, or falling — use `--date` to compare two windows (e.g. `--date ">=2026-02-13"` vs `--date ">=2026-01-14"`) to determine direction

Attach these metrics to the bug record so signal scoring in Step 5 can use them immediately. A crash with >1 000 reports in 30 days should elevate the theme's rank regardless of other signals. Add a `Crash Volume (30d)` column to affected themes' breadcrumb tables in the report.

If `socorro-cli` is unavailable, note that enrichment was skipped and recommend it as a follow-up action in the closing section.

### Step 4 — Keyword Expansion

For each developing theme, run 1–2 targeted searches against the same component set to find bugs not connected via the dependency graph. Examples:

- A rendering glitch theme → search `keywords=regression` in `Graphics: WebRender`
- An audio theme → search for `bluetooth` or `audio sink` in `Audio/Video`
- A site-specific theme (e.g. Twitch, YouTube) → search the site name as a text term in the full component set, not just via the dependency graph; meta-bugs for popular sites may be recent and not yet widely linked
- Any audio/video theme → always run a `keywords=webcompat:site-report` search across the Audio/Video component set; site-report bugs (e.g. a specific site's audio broken) rarely appear in dep graphs but carry strong user-impact signal and are frequently filed independently by webcompat triage

Add any relevant results to the theme's breadcrumb list.

### Step 5 — Score and Rank

Apply the signal scoring rules to each theme. Rank themes by total signal. Discard any theme with fewer than 3 breadcrumbs. Independently, choose a few themes to highlight which might represent emerging issues, even if the initial signal for the theme is weaker.

### Step 6 — Report

Present findings in this structure:

**Session Info:**
- Date of report generation
- Scope profile
- Seed timeframe
- Seed count
- Cache freshness

**Seed Info:**
- A tight itemized list of the initial set of seed bugs (ID and summary), organized by
  priority. If ASSIGNED include the assignee in the list entry.
- A breakdown of the creation dates of the seed bugs, showing how many were created in
  each month of the seed date window. Some sort of horizontal visual timeline showing where the bugs
  fall would be helpful. This helps validate that the seed is representative of the entire window.

**Per theme:**
- Plain-language description of the user-facing impact
- Breadcrumb table: `Bug ID | Summary | Severity | Status | Last Changed`
- Timeline narrative: when reports began, whether a meta-bug formed, current assignee/triage state
- Stagnation callout if any S1/S2 bug has had no activity in the past 30 days, or if any S3 regression bug has had no activity in the past 90 days

**Closing:**
- Ranked signal summary table across all themes (columns: Rank, Theme, Breadcrumb count, Meta-bug, Top severity, Notes)
- Resources used (queries, tools, tokens) during this run
- Suggestions for improving this skill
- A whimsical quote that is family-friendly and loosely related to the theme of discovery, investigation, or problem-solving.

**Format Notes**
- Use 'linkable' format for all bug IDs, for example - [1234567](https://bugzilla.mozilla.org/show_bug.cgi?id=1234567)
- Use searchfox links for code references, for example - [MediaDecoderStateMachine.cpp](https://searchfox.org/mozilla-central/source/dom/media/MediaDecoderStateMachine.cpp)
- When referencing crash signatures, link to Socorro search results for that signature, for example - [Crash Signature](https://crashes.mozilla.org/signatures?q=signature%3A%22%3Csignature%3E%22)

Offer to save the research report under "./reports". The filename format should be `wrangler-<scope>-<DATE>.md`. If the file already exists, we should not overwrite it, but instead create a new file with a suffix, like `wrangler-<scope>-<DATE>-2.md`, and so on.
