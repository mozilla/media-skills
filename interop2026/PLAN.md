# Interop 2026 WebRTC — Research Plan

Let's kick off some research on a project my web conferencing team is just kicking off and will be working on for the next year.

## About Interop

The Interop (Web Platform Tests) initiative is a cross-browser collaboration (Mozilla, Google, Apple, Microsoft, etc.) that uses Web Platform Tests (WPT) to measure and drive consistency of web standards implementations across browsers. Overall progress on all tests is tracked by the [Interop 2026 WPT dashboard](https://wpt.fyi/interop-2026).

## About This Project

Improve Firefox scores in specific WebRTC-related web platform tests. The WPT dashboard is configured to track the test failures we will need to address. The WebRTC-specific dashboard pages are:

- [webrtc](https://wpt.fyi/results/webrtc?label=master&label=experimental&aligned&view=interop&q=label%3Ainterop-2026-webrtc)
- [webrtc/protocol](https://wpt.fyi/results/webrtc/protocol?label=master&label=experimental&aligned&view=interop&q=label%3Ainterop-2026-webrtc)
- [webrtc/simulcast](https://wpt.fyi/results/webrtc/simulcast?label=master&label=experimental&aligned&view=interop&q=label%3Ainterop-2026-webrtc)
- [webrtc-encoded-transform](https://wpt.fyi/results/webrtc-encoded-transform?label=master&label=experimental&aligned&view=interop&q=label%3Ainterop-2026-webrtc)

As part of this project, engineering teams at Mozilla, Google, and Apple agreed that the WebRTC tests each browser vendor will work on are tests that **fail in only one of the three main browsers** (Chrome, Firefox, and Safari). 

Terminology:
- A wpt subtest is a single, individual wpt platform test contained in a wpt test file. For our score tracking, these are the individual 'tests' we will be tracking.
- A wpt test, typically an html file that has a path associated with it, contains a set of related wpt subtests. For example - 'webrtc/protocol/additional-codecs.html'. 
- A group of tests make up a test suite. For example there is a webrtc protocol suite in 'webrtc/protocol' and a css viewport suite in 'css/css-viewport'.
- Sets of test suites make up each of the interop test **focus areas**.
- The tests we will track for this project are contained in the **WebRTC Focus Area**.

Identifying tests we will track:
- If a wpt subtest is reliably failing in Firefox and also reliably fails in Chrome or Safari, we should **not** include it in our tracking.
- If a wpt subtest is reliably failing in Firefox, but does not reliably fail in Chrome or Safari, and is tracked by an interop-2026 WebRTC focus area, we **should** include it in our tracking.
- Note, 'reliably' implies the test exibits the behavior over multiple subsequent test runs.
- For this research we will concentrate on the 'label=experimental' wpt dashboard scores and test runs.

Be careful about differentiating between 'subtests' and 'tests'. In documentation the term 'test' can be used to describe subtests or test files. For scoring in our work here, we are tracking succeeding and failing subtests scores, categroized by tests (the test filename) and test suites (webrtc, protocol, simulcast, encoded-transform). 

## Bugzilla

The lead developer on this project, Byron Campen, has been filing bugs in Bugzilla for a lot of this test work. We need to collect all the related bugs and organize this work around the individual tests. The starting point is:

**[Bug 2017363 — \[meta\] Interop 2026 WebRTC](https://bugzilla.mozilla.org/show_bug.cgi?id=2017363)**

## Engineering Team

| Engineer | Bugzilla Email | GitHub Account |
|----------|----------------|----------------|
| Daniel Baker | dbaker@mozilla.com |
| Jan-Ivar Bruaroey | jib@mozilla.com | https://github.com/jan-ivar |
| Byron Campen | docfaraday@gmail.com | https://github.com/docfaraday |
| Michael Froman | mfroman@nostrum.com |
| Nico Grunbam | na-g@nostrum.com |
| Andreas Pehrson | apehrson@mozilla.com |

## Triage Spreadsheets

We have a spreadsheet in Google Sheets with our initial project triage notes. The two tabs are available in the working directory as:

- `resources/WebRTC Interop 2026 - Test List.csv` - initial test inventory and notes
- `resources/WebRTC Interop 2026 - Aggregate Bugs.csv` - meta bugs that play into multiple tests.

Notes on these spreadsheets:

- The **FILE** column contains the wpt test name (filename).
- The tests itemized here are all tracked by the WebRTC interop 2026 focus area.
- Pay close attention to the **NOTES**, **IMPORTANCE**, and **EXISTING BUG(S)** columns for each test.
- The rows of the main sheet include WPT test scores that may be out of date — the WPT dashboard is the source of truth for current scores.
- Useful for tracking overall progress since these spreadsheets **represent our initial understanding of project scope**.

## Spec Coverage

Much of this work will be associated with WebRTC specification compliance. In the documentation we put together, we should track the areas of the specification that individual tests are associated with.
* [WebRTC Specification](https://w3c.github.io/webrtc-pc/)

## Research Goals

- Create a **Test Inventory** — Itemize the individual web platform tests we will need to improve. With each test entry include:
  - A summary of why the test fails in Firefox based on WPT output
  - Spreadsheet information: Notes, Importance, Bug relationships, Owner if available, Importance / size if known
  - The current Firefox score for the test from wpt.fyi
  - A velocity tracking field - "first seen passing" date
- **Connect development work** — Using spreadsheet and the task related information in Bugzilla, connect development work needed to improve test scores with individual tests in our inventory. Sanity check the relationships. Also note assignment of work to team members, which provides some input into the development of our roadmap.
- **Search for unknown dependencies** — Using the bugs we already know about, search for additional dependencies in Bugzilla.
  - **Comment scan** — Run `resources/scripts/scan_bug_comments.py` to scan Bugzilla comments on all tracked bugs for new w3c spec links and WPT repo links not yet recorded in `test-annotations.json`. For each find:
    - If clearly connected to a tracked test → add to `_github_issues` and the relevant test annotation.
    - If connection is uncertain → add to `_gap_analysis.comment_scan` in `test-annotations.json` for future investigation.
- **Define small projects** that encompass accomplishing improving a specific set of test scores. Score these by test score impact.
- **Associate tests with projects** - Keep track of what work will be needed (including the bugs that will need ot be fixed) to address each test.
- **Experimental Dependency Graph** — Several projects block each other (e.g., 1765851 → 1765852 → RTCRtpReceiver). Develop a project dependency map to help sequence work.
- **Gap analysis** - Identify unknown gaps between our test lists and Bugzilla or Github. Check for tracked tests with multi-browser failures in the latest test score data. (Sometimes tests fail intermittently.) We should call these out as something to keep track of.

## Caching

- Don't cache Bugzilla data, always refresh the information we need.
- Cache browser WebRTC scores (total and on a per-test basis) when we retreive them in a local json file. We can use this for generating change graphs. Data should have date and time the data was fetched and the each test score for all browsers.
- Load `resources/test-annotations.json` at the start of each run. This file captures non-obvious per-test context that is not derivable from WPT scores or Bugzilla: confirmed WPT flaws, invalid tests, deprecated path changes, risky fixes, on-hold status, and first-passing dates. Use it to avoid re-investigating known issues. Update it when a run produces new findings.
   (e.g. a test changes status, a path changes, a fix lands).

## Report

Save output in the working directory as `report-<YYYY-MM-DD>.md`, following the structure in [`report-template.md`](report-template.md). Fill in all placeholder values; remove any sections that have no content for the current run.

**Format Notes**
- Use 'linkable' format for all bug IDs, for example - [1234567](https://bugzilla.mozilla.org/show_bug.cgi?id=1234567)

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

To discover new GitHub issues not yet recorded, run the comment scan script:
```
python3 resources/scripts/scan_bug_comments.py
```
This scans all Bugzilla comments on tracked bugs and reports w3c and WPT GitHub links not in `test-annotations.json`.

### Scripts and temporary data

- Where useful, develop reusable scripts for any WPT related data processing or API calls. Store these in the ./resources/scripts sub folder.
- Store all temporary data and other resources in the ./resources sub directory of this project.
