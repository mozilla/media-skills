## Media Bug Triage

A single-bug triage assistant that researches an open Bugzilla report in depth, finds related bugs and duplicates, cross-references crash data, and produces a structured triage report with a suggested severity/priority assessment and a draft response to the reporter.

Typically executed in a Firefox source directory with various support tools installed (socorro, searchfox).

### What it does

1. **Fetches and parses the bug** — retrieves the full bug report including description, comments, attachments, crash signatures, change history, and dependency fields. Flags security group changes, component reclassifications, and severity/priority assignments from history.

2. **Performs a quick determination** — checks whether the issue is already clearly understood, or likely non-reproducible, and pauses to ask before continuing. This short-circuits unnecessary analysis on clear-cut cases.

3. **Investigates Bugzilla** — derives targeted search terms from the bug's symptoms and component, searches for related bugs in the active scope profile, follows `see_also` / `depends_on` / `blocks` relations up to 3 hops deep, identifies duplicate candidates and bug clusters, and checks for existing meta/tracking bugs or accepted patches.

4. **Enriches with Socorro crash data** — for any crash-keyword bug, looks up the signature to get 30-day volume, affected Firefox versions, top platform, process type, and rising/stable/falling trend.

5. **Investigates the codebase** *(optional)* — uses `searchfox-cli` to locate relevant source files, trace recent changes, and identify existing tests that cover the affected area.

6. **Assesses severity and priority** — produces a suggested S1–S4 severity and P1–P5 priority with written reasoning, classification signals (STR, test case, crash stack, fuzzing), and a "good first bug" assessment where applicable.

7. **Drafts a reporter response** — selects from a library of canned templates (or writes a custom response) covering information requests, status updates, resolutions, and acknowledgements.

8. **Writes a structured report** — saves a Markdown file to `./reports/bug-{BUG_ID}-triage.md` containing all findings, a regression timeline if applicable, codebase investigation notes, and Bugzilla usage statistics.

### Usage

```
/media-bug-triage 1234567
/media-bug-triage Bug 1234567
/media-bug-triage https://bugzilla.mozilla.org/show_bug.cgi?id=1234567
/media-bug-triage 1234567 scope:graphics
/media-bug-triage 1234567 web-conferencing
```

If no bug ID is given, the skill will prompt for one. If no scope is given, it infers the profile from the bug's component.

### Built-in scope profiles

| Profile | Coverage |
|---|---|
| `media` | Core: Audio/Video and sub-components, Web Audio |
| `web-conferencing` | Core: WebRTC and sub-components, DOM: Screen Capture |
| `media-and-web-conferencing` | Combined media + WebRTC components |
| `graphics` | Core: Graphics, Canvas, WebRender, WebGPU, Text, Web Painting |
| `android` | Firefox for Android + GeckoView: Media |

### Output

Reports are saved to `./reports/bug-{BUG_ID}-triage.md`. Each report includes:

- **Bug Information** — summary, reporter, status, product/component, creation date
- **Research Summary** — key findings, related bugs, duplicate candidates
- **Regression Timeline** — when the issue was first observed and what may have caused it (if applicable)
- **Classification** — STR, test case, crash stack, and fuzzing signal table
- **Assessment** — suggested severity and priority with written reasoning
- **Codebase Investigation** — relevant files examined and suggested investigation areas
- **Bugzilla Use Tracking** — query count, bugs processed, inaccessible bugs

### Canned response library

The skill includes ready-to-use response templates for common triage scenarios:

| Category | Templates |
|---|---|
| Information requests | need-str, need-testcase, need-profile, need-crash-report, more-info-needed, need-regression-range, need-system-info |
| Status updates | confirmed, investigating |
| Resolutions | duplicate, wontfix, worksforme, incomplete |
| Acknowledgements | fuzzing-thanks, first-time-contributor, good-report |
| Special cases | security-notice, moved-component, needs-platform-team |
