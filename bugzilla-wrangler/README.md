## Bugzilla Wrangler

A research skill that surfaces recurring themes and emerging issues buried in Mozilla's Bugzilla database. Given a product/component scope and a date window, it fetches seed bugs, crawls dependency graphs, cross-references crash data from Socorro, and produces a ranked signal report — all saved to `./reports/`.

Typically executed in a Firefox source directory with various support tools installed (socorro, searchfox).

### What it does

1. **Seeds from Bugzilla** — fetches up to 50 open bugs (unconfirmed, new, assigned, or reopened) from the specified scope and date window, using a hybrid strategy that mixes recently-created and recently-changed bugs for better coverage.

2. **Identifies themes** — groups seed bugs by shared symptoms, keywords, affected components, and user-facing impact. Each theme gets a plain-language name (e.g. "Bluetooth audio stutter", "WebRender visual glitch").

3. **Crawls dependency graphs** — follows `depends_on` / `blocks` links up to 5 levels deep across *all* products and components to gather breadcrumbs and find meta/tracking bugs. Meta-bug dependency counts are used as a proxy for theme breadth.

4. **Enriches with Socorro crash data** — for any bug carrying the `crash` keyword, looks up the crash signature to get 30-day volume, affected Firefox versions, top platform, process type, and a rising/stable/falling trend.

5. **Scores and ranks themes** — applies a weighted signal model that factors in duplicate counts, cc_count (when available), comment activity, bug severity/priority, crash volume, regression keywords, and non-Mozilla commenter participation. Themes with fewer than 3 breadcrumbs are discarded.

6. **Writes a structured report** — saves a Markdown file to `./reports/wrangler-<scope>-<DATE>.md` with session info, a seed timeline, per-theme breadcrumb tables and narratives, stagnation callouts for S1/S2 bugs with no recent activity, and a ranked summary table.

### Usage

```
/bugzilla-wrangler
/bugzilla-wrangler media last three months
/bugzilla-wrangler web-conferencing date range:10-01-2025 to 03-18-2026
/bugzilla-wrangler android
/bugzilla-wrangler graphics --no-mixed-seed
/bugzilla-wrangler custom:Core::Audio/Video, Core::WebRTC: Signaling, Firefox for Android::Media
```

If no scope or date range is given, defaults to the `media` profile for the past three months.

### Built-in scope profiles

| Profile | Coverage |
|---|---|
| `media` | Core: Audio/Video and sub-components, Web Audio |
| `web-conferencing` | Core: WebRTC and sub-components |
| `android` | Firefox for Android + GeckoView: Media |
| `media-and-web-conferencing` | Combined media + WebRTC components |
| `graphics` | Core: Graphics, WebRender, Canvas, Layout: Painting, CSS Compositing |
| `webcompat` | Web Compatibility: Site Reports, Knowledge Base |
| `custom:` | Any comma-separated `Product::Component` list you specify inline |

### Flags

- `--no-mixed-seed` — use creation-time-only seeding instead of the default hybrid strategy (recently-created + recently-changed).

### Output

Reports are written to `./reports/wrangler-<scope>-<DATE>.md`. Each report includes:

- **Session Info** — scope, date window, seed count, seed mode, cache freshness
- **Seed Info** — itemized seed bug list and a visual distribution timeline
- **Per-theme sections** — user-facing description, breadcrumb table, timeline narrative, stagnation callouts
- **Closing summary** — ranked signal table, resources used, and suggestions for improving the skill
