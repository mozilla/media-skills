# Interop 2026 WebRTC — Research Plan

Let's kick off some research on a project my web conferencing team is just kicking off and will be working on for the next year.

## About Interop

The Interop (Web Platform Tests) initiative is a cross-browser collaboration (Mozilla, Google, Apple, Microsoft, etc.) that uses Web Platform Tests (WPT) to measure and drive consistency of web standards implementations across browsers. Overall progress on all tests is tracked by the [Interop 2026 WPT dashboard](https://wpt.fyi/interop-2026).

## About This Project

Improve Firefox scores in specific WebRTC-related web platform tests. The WPT dashboard is configured to track the test failures we will need to address. The WebRTC-specific dashboard pages are:

- [webrtc-encoded-transform](https://wpt.fyi/results/webrtc-encoded-transform?label=master&label=experimental&aligned&view=interop&q=label%3Ainterop-2026-webrtc)
- [webrtc](https://wpt.fyi/results/webrtc?label=master&label=experimental&aligned&view=interop&q=label%3Ainterop-2026-webrtc)
- [webrtc/protocol](https://wpt.fyi/results/webrtc/protocol?label=master&label=experimental&aligned&view=interop&q=label%3Ainterop-2026-webrtc)
- [webrtc/simulcast](https://wpt.fyi/results/webrtc/simulcast?label=master&label=experimental&aligned&view=interop&q=label%3Ainterop-2026-webrtc)

As part of this project, engineering teams at Mozilla, Google, and Apple agreed that the WebRTC tests each browser vendor will work on are tests that **fail in only one of the three main browsers** (Chrome, Firefox, and Safari). For example:

- If a WebRTC test is failing in Firefox but also fails in Chrome or Safari, we would **not** include it in our tracking.
- If a test fails only in Firefox, does not fail in Chrome or Safari, and is tracked by the interop-2026 dashboard, we **would** include it in our planning.
- For this research we will concentrate on the 'label=experimental' wpt dashboard and test runs.

## Bugzilla

The lead developer on this project, Byron Campen, has been filing bugs in Bugzilla for a lot of this test work. We need to collect all the related bugs and organize this work around the individual tests. The starting point is:

**[Bug 2017363 — \[meta\] Interop 2026 WebRTC](https://bugzilla.mozilla.org/show_bug.cgi?id=2017363)**

## Engineering Team

| Engineer | Bugzilla Email | GitHub Account |
|----------|----------------|----------------|
| Byron Campen | docfaraday@gmail.com | https://github.com/docfaraday |
| Michael Froman | mfroman@nostrum.com |
| Daniel Baker | dbaker@mozilla.com |
| Jan-Ivar Bruaroey | jib@mozilla.com | https://github.com/jan-ivar |
| Nico Grunbam | na-g@nostrum.com |
| Andreas Pehrson | apehrson@mozilla.com |

## Triage Spreadsheets

We have a spreadsheet in Google Sheets with our initial project triage notes. The two tabs are available in the working directory as:

- `resources/WebRTC Interop 2026 - Test List.csv` - initial test inventory and notes
- `resources/WebRTC Interop 2026 - Aggregate Bugs.csv` - meta bugs that play into multiple tests.

Notes on these spreadsheets:

- Pay close attention to the **NOTES**, **IMPORTANCE**, and **EXISTING BUG(S)** columns for each test.
- The rows of the main sheet include WPT test scores that may be out of date — the WPT dashboard is the source of truth for current scores.
- Useful for tracking overall progress since the spreadsheets represent our initial understanding of scope.

## Spec Coverage

Much of this work will be associated with WebRTC specification compliance. In the documentation we put together, we should track the areas of the specification that individual tests are associated with.
* [WebRTC Specification](https://w3c.github.io/webrtc-pc/)

## Initial Research Goals

- Create a **Test Inventory** — Itemize the individual web platform tests we will need to improve. With each test entry include:
  - A summary of why the test fails in Firefox based on WPT output
  - Spreadsheet information: Notes, Importance, Bug relationships, Owner if available, Importance / size if known
  - The current Firefox score for the test from wpt.fyi
  - A velocity tracking field - "first seen passing" date
- **Connect development work** — Using spreadsheet and the task related information in Bugzilla, connect development work
   needed to improve test scores with individual tests in our inventory. Sanity check the relationships. Also note assignment
   of work to team members, which provides some input into the development of our roadmap.
- **Search for unknown dependencies** — Using the bugs we already know about, search for additional dependencies in Bugzilla.
- **Define small projects** that encompass accomplishing improving a specific set of test scores. Score these by test score impact.
- **Associate tests with projects** - Keep track of what work will be needed (including the bugs that will need ot be fixed) to address each test.
- **Gap analysis** — Identify gaps between our test lists and Bugzilla.

## Caching

- Don't cache Bugzilla data, always refresh the information we need.
- Cache browser WebRTC scores (total and on a per-test basis) when we retreive them in a local json file. We can use this for
   generating change graphs. Data should have date and time the data was fetched and the each test score for all browsers.
- Load `resources/test-annotations.json` at the start of each run. This file captures non-obvious per-test context that is not
   derivable from WPT scores or Bugzilla: confirmed WPT flaws, invalid tests, deprecated path changes, risky fixes, on-hold
   status, and first-passing dates. Use it to avoid re-investigating known issues. Update it when a run produces new findings
   (e.g. a test changes status, a path changes, a fix lands).

## Report

Report what you have found using the general format below, and save this in the working directory as `report-<YYYY-MM-DD>.md`.

```markdown
**Header** — Time and date, WPT test run time and date and commit, browser versions tested
**Links** - Link to interop 2026 wpt dashboard, link to interop 2026 meta bug

**Project Summary**
   **Score Summary** — Table of passing/total/percentage for Firefox, Chrome, and Safari across all tracked tests
   **Notable Changes** — A per-report "Notable Changes Since Triage Sheet" delta mini-report. Include -
      - A test change summary: points added (new bugs/tests), points removed (fixed), and net change.
      - Tests fully passing our criteria.
      - New bugs filed since the last report.
      - Tracked bugs that have closed since the last report.
      - Anything else notable.
   **Assigned Bugs** - Itemize bugs in Bugzilla that are currently associated with this project and assigned to a member of the team.

**Project Development**
   **Priority Assessment** — Grouped view of the work: high-priority unblocked items, quick wins, items needing investigation, and items on hold
   **Aggregate Bugs** — Bugs that affect multiple test files, with a count of subtests and files impacted per bug.
   **Gap Analysis** — Tests with no bug filed; tests suspected to be WPT test issues rather than Firefox bugs; H264 infrastructure failures that
      are blocking score accuracy.

**Test Inventory** — One entry per test, grouped by directory (`webrtc/`, `webrtc/protocol/`, `webrtc/simulcast/`). Each entry includes:
   - WPT path
   - current scores for all three browsers (green check if Firefox has a perfect score)
   - owner
   - linked bugs (or project(s))
   - spec area
   - notes
   - size/importance

**Experimental Burndown** - Let every sub-test that's failing represent 1 point. Based on the burndown of points thus far, project out
   approximately when we will reach zero.

**Experimental Dependency Graph** — Several projects block each other (e.g., 1765851 → 1765852 → RTCRtpReceiver). A visual or tabular
   dependency map would help sequence work.
```

## Suggest and Exit

Prior to exiting, suggest ways to improve this plan. Specifically -
- ways to improve project tracking over time.
- ways the team can improve the data we have in bugzilla.

---

## Data Access Tips

### wpt.fyi

The WPT dashboard is a client-side rendered JavaScript app — fetching the HTML pages returns only analytics scripts, not test data. Use the API directly instead.

**Correct approach to get live test scores:**

1. Get the latest aligned run IDs and `results_url` values:
   ```
   GET https://wpt.fyi/api/runs?label=experimental&label=master&product=firefox&product=chrome&product=safari&aligned=true&max-count=1
   ```

2. Download the `results_url` files for each browser. Despite the `.json.gz` extension, these files are **plain JSON** (not gzip-compressed) — open them directly without decompression:
   ```
   curl -s -L -o /tmp/firefox_wpt.json /path/from/results_url
   python3 -c "import json; d=json.load(open('/tmp/firefox_wpt.json')); ..."
   ```

3. Filter by path prefix (e.g. `/webrtc/`) and read scores from the `c` field: `[passes, total]`.

**Approaches that don't work:**

- `GET /api/search?q=label:interop-2026-webrtc` — always returns an empty `results` array; only run metadata is included.
- `POST /api/search` with `run_ids` — returns at most 1 result and it is unrelated to the query.
- Fetching `https://wpt.fyi/results/webrtc?...` via WebFetch — the page is JS-rendered; no test data in the HTML.

### Bugzilla

The REST API works reliably. Fetch multiple bugs in a single request to avoid rate limits:

```
GET https://bugzilla.mozilla.org/rest/bug?id=X,Y,Z&include_fields=id,summary,status,resolution,depends_on,blocks
```

The meta bug's `depends_on` field lists all child bug IDs — fetch those first, then batch-query their status.

### GitHub Issues

Two external issue trackers are relevant to this project. Only track issues that are explicitly referenced in our existing
tracking material (spreadsheet, reports, Bugzilla bugs, or test-annotations.json) — do not sweep for new issues.

**WPT test issues** — filed against tests that are broken or invalid:
```
GET https://api.github.com/repos/web-platform-tests/wpt/issues/NNNN
```

**W3C WebRTC spec issues** — spec decisions that may unblock or change Firefox work:
```
GET https://api.github.com/repos/w3c/webrtc-pc/issues/NNNN
```

For each tracked issue, fetch current `state` (open/closed) and note any linked PRs in the closing event.
A newly-closed spec issue may change a test's `on-hold` status in `test-annotations.json`.

### Scripts and temporary data

- Where useful, develop reusable scripts for any WPT related data processing or API calls. Store these in the ./resources/scripts sub folder.
- Store all temporary data and other resources in the ./resources sub directory of this project.
