---
name: bugzilla-wrangler
description: Support deep dive analysis of Bugzilla reports within specific Products and Components.
---

# Bugzilla Wrangler Skill

## Goal

Discover and surface recurring themes within bug data in your Products and Components. Connect disparate reports to shared themes, build timelines, assign signal strength, and present actionable findings.

The core logic of weighting is covered in Signal Scoring. You can tweak the ranking system there to alter what you find. Currently we're finding major and minor themes buried in the noise of bugzilla. The tool will surface existing issues, and for more current date ranges, emerging themes that haven't yet been widely recognized.

---

## Run Configuration

At invocation, resolve these two settings before doing anything else. State both in the Session Info section of the report.

**Scope profile** — If the user passed a `custom:` prefix (e.g. `custom:Core::Audio/Video, Firefox for Android::Media`), parse the value as described in the `custom` scope profile below. Otherwise, if the user specified a named platform or topic (e.g. "android", "web-conferencing", "graphics"), use that profile from the Scope Profiles section. If neither, use `media`.

**Seed date window** — If the user specified a date range (e.g. "Q1 2025", "last 90 days", "January through March 2026"), parse it into an explicit `YYYY-MM-DD` lower bound and upper bound and use those in Step 1. Otherwise use a default window from the last three months.

**Seed mode** — Use the hybrid seed strategy in Step 1 by default (recently-created bugs fill up to 75% of seed slots; recently-changed bugs fill the remainder). If the user passed `--no-mixed-seed`, use the creation-time-only strategy instead. State the active seed mode in Session Info.

## Scope Profiles

At invocation, check whether the user specified a platform or topic (e.g. "android", "web-conferencing", "graphics"). If so, use the matching profile below. If not, use `media`.

### media
- **Product:** Core
- **Components:** Audio/Video, Audio/Video: cubeb, Audio/Video: GMP, Audio/Video: MediaStreamGraph, Audio/Video: Playback, Audio/Video: Recording, Audio/Video: Web Codecs, Web Audio

### android
- **Product:** Firefox for Android
- **Components:** Media
- **Product:** GeckoView
- **Components:** Media

### web-conferencing
- **Product:** Core
- **Components:** WebRTC, WebRTC: Audio/Video, WebRTC: Networking, WebRTC: Signaling

### media-and-web-conferencing
- **Product:** Core
- **Components:** Audio/Video, Audio/Video: cubeb, Audio/Video: GMP, Audio/Video: MediaStreamGraph, Audio/Video: Playback, Audio/Video: Recording, Audio/Video: Web Codecs, Web Audio, WebRTC, WebRTC: Audio/Video, WebRTC: Networking, WebRTC: Signaling

### graphics
- **Product:** Core
- **Components:** Graphics, Graphics: WebRender, Graphics: CanvasWebGL, Graphics: Layers, Graphics: Text, Canvas: 2D, Layout: Painting, CSS Painting and Compositing

### webcompat
- **Product:** Web Compatibility
- **Components:**  Site Reports, Knowledge Base

### custom
Defined inline at invocation. The value is a comma-separated list of `Product::Component` pairs. Both `::` and `:` are accepted as the product/component delimiter (e.g. `Core::Audio/Video` or `Core:Audio/Video`). Example invocation:

    /bugzilla-wrangler custom:Core::Audio/Video, Core::WebRTC: Signaling, Firefox for Android::Media

Parsing rules:
- Split the value on `,` to get individual pairs.
- For each pair, split on the first occurrence of `::` or `:` to separate the product (left side) from the component (right side). Strip whitespace from both sides.
- If a pair contains no delimiter, treat the whole string as a component under `Core` and emit a visible warning in Session Info.
- Pairs whose product does not match a known Bugzilla product name should trigger a visible warning in Session Info before proceeding.

The resolved product/component set is used identically to a named scope profile for all subsequent steps. Use `custom` as the scope name in cache filenames and report headers.

---

## Definitions

**Breadcrumb** — Any resource associated with a theme: a bug report, test case, crash report, etc.

**Signal** — A measure of theme importance based on the number and quality of breadcrumbs. See scoring rules below.

---

## Bugzilla Access Rules

- **Cache policy.** Derive the cache filename from the active scope: `reports/wrangler_cache_<scope>.json` (e.g. `wrangler_cache_android.json`, `wrangler_cache_media.json`, `wrangler_cache_custom.json`). Never read or write a different scope's cache file.
  - **Default date window (no user-specified range):** Always skip the cache on read — fetch fresh data from Bugzilla regardless of whether a cache file exists. Write the fresh results to the cache after every fetch so later steps within the same session can reuse the data.
  - **User-specified date range:** Cache first. If the cache file exists and was written in the current session, load from it. Write to it after every fetch so later steps can reuse the data.
- **Batch lookups.** Fetch multiple bugs in one request using `?id=A,B,C` rather than one request per bug.
- **Request only needed fields.** Always include: `id, summary, component, severity, status, creation_time, last_change_time, keywords, depends_on, blocks, cc_count`
- **Fetch `cc_count` separately if missing.** The field can be omitted by the API depending on visibility. If `cc_count` is absent after a batch fetch, retrieve it with a targeted request: `?id=A,B,C&include_fields=id,cc_count`. Always persist `cc_count` in the cache so signal scoring can use it without a second fetch.
- Always exclude bugs belonging to core security groups.

## Bug Filtering Rules

- Filter intermittent test bugs (bugs with the keyword intermittent-failure) out of the seed lists.
- Changes to bugs by release-mgmt-account-bot@mozilla.tld should be treated as questionably accurate.

---

## Signal Scoring

Apply these rules when ranking themes. Higher-weight factors are listed first.

| Factor | Effect |
|--------|--------|
| Bug severity is S1 or S2 | Validated internally as a major issue. |
| Bug priority is P1 or P2 | Validated internally as a priority to fix. |
| Crash volume and trend | >1 000 reports in 30 days is a strong signal; a rising trend (comparing two 30-day windows via Socorro) elevates the theme regardless of other factors |
| `regression` keyword present | Higher priority — represents a user-visible regression from a prior release |
| Bug status is NEW or ASSIGNED | Counts more than UNCONFIRMED (triage has validated it) |
| `cc_count` ≥ 10: moderate boost; `cc_count` ≥ 25: strong boost | Proxy for how many users are tracking the issue |
| `comment_count` ≥ 15: moderate boost; `comment_count` ≥ 40: strong boost | Proxy for community demand and sustained engagement around the issue. Add `comment_count` to `include_fields`. |
| Non-Mozilla commenter activity | A thread dominated by non-mozilla.com accounts signals direct end-user impact rather than internal triage noise; weight proportionally to the number of distinct non-Mozilla participants |
| High duplicate count or independent reporters with near-identical summaries | Both indicate broad user impact; weight more heavily when duplicates originate from unrelated reporters rather than a single coordinated source (e.g. a forum post) |
| `last_change_time` older than 30 days with no resolution | *Negative factor*: marks a theme as stagnant — call this out in the report rather than using it as a positive signal |
| `stalled` keyword with S1 or S2 severity | Notable: acknowledged this needs to be fixed but there are no engineers available |
| Meta/tracking bug exists (`keywords=meta`) | Strong multiplier — use its total dependency count as a proxy for theme breadth |

A theme requires at least 3 breadcrumbs to be included in the report.

---

## Bug Severity Definitions
| Severity | Meaning |
|----------|---------|
| **S1**   | Catastrophic: Blocks development/testing, affects 25%+ users, data loss, no workaround |
| **S2**   | Serious: Major functionality impaired, high impact, no satisfactory workaround |
| **S3**   | Normal: Blocks non-critical functionality, workarounds in Firefox exist |
| **S4**   | Small/Trivial: Minor significance, cosmetic, low user impact |
| **N/A**  | Not Applicable: Task or Enhancement type bugs |
| **--**   | Unknown: Not enough information, might be a meta bug, new untriaged, older or abandoned. Investigate. |

---

## Bug Priority Definitions
| Priority | Meaning |
|----------|---------|
| **P1**   | Fix in current release cycle (critical) |
| **P2**   | Fix in next release cycle or following |
| **P3**   | Backlog (lower priority, address when resources allow) |
| **P4**   | Won't fix, but accept patches (nice-to-have) |
| **P5**   | Won't fix, but accept patches (nice-to-have) |
| **--**   | Unknown: Not enough information, might be a meta bug, new untriaged, older or abandoned. Investigate. |

---

## Workflow

Before starting, identify the active scope profile. If the user specified a platform (e.g. "android") at invocation, use that profile's Product and Component set for all seed searches and keyword expansion queries. Otherwise use `media`. State the active profile in the Session Info section of the report.

### Step 1 — Fetch Seed Bugs

Retrieve a seed sample of up to 50 bugs using the seed date window resolved in Run Configuration.

The common filter parameters below apply to all queries in this step:
- `status=UNCONFIRMED&status=NEW&status=ASSIGNED&status=REOPENED`
- `f2=bug_severity&o2=notequals&v2=--` and `f3=bug_severity&o3=notequals&v3=N/A`
- `f4=keywords&o4=notsubstring&v4=intermittent-testcase` — exclude CI-only intermittent bugs
- `order=changeddate%20DESC`

**Default seed mode** (no `--no-mixed-seed` flag):

Run two queries in parallel:

*Query A — recently created (up to 38 bugs):*
- `creation_time=<lower-bound>`
- `f1=creation_ts&o1=lessthan&v1=<upper-bound>`
- `limit=38`

*Query B — recently changed (up to 25 candidates):*
- `f1=delta_ts&o1=greaterthan&v1=<lower-bound>`
- `f2=delta_ts&o2=lessthan&v2=<upper-bound>`
- `limit=25`

Merge the two result sets: start with all bugs from Query A, then append bugs from Query B whose IDs are not already present, until the combined list reaches 50. Discard any remainder from Query B. Record the final composition as `<A-count> created + <B-unique-count> changed = <total> unique` for the Session Info section.

**Creation-time-only mode** (`--no-mixed-seed` flag):

Fetch up to 50 bugs created within the seed date window:
- `creation_time=<lower-bound>`
- `f1=creation_ts&o1=lessthan&v1=<upper-bound>`
- `limit=50`

Save results to the cache.

**Low seed count check:** After saving, count the results. If fewer than 10 bugs were returned, emit a visible inline warning before proceeding — for example:

> **Warning: Low seed count** — only N bugs returned for the `<scope>` profile over `<window>`. Results may not be representative. Consider widening the date window or relaxing filters.

Continue with the analysis regardless, but carry the low-seed flag into the report.

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
- **Affected Firefox versions:** which version of Firefox experience the crash. 
- **Top platform:** which OS accounts for the most reports
- **Process type:** process type(s) that experience the crash.
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

Present a short summary of the themes you've found. Save the full research report under "./reports". The filename format should be `wrangler-<scope>-<DATE>.md`. If the file already exists, we should not overwrite it, but instead create a new file with a suffix, like `wrangler-<scope>-<DATE>-2.md`, and so on.

**Session Info:**
- Date of report generation
- Scope profile
- Seed timeframe
- Seed count — if fewer than 10, render as **"N (low)"** and include a callout box immediately below Session Info explaining the limitation and suggesting remedies (e.g. widen the date window, relax the severity filter)
- Seed mode — `mixed-seed (<A> created + <B> changed = <total> unique)` or `creation-time-only (--no-mixed-seed)`
- Cache freshness — note whether data was fetched live (default window) or loaded from session cache (user-specified range)

**Seed Info:**
- A tight itemized list of the initial set of seed bugs (ID and summary), organized by
  priority.
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
- In tables that itemize bugs, if the bug is ASSIGNED include the assignee information. 
