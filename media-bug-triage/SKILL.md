---
name: media-bug-triage
description: Firefox bug triage assistant for media, web conferencing, and graphics related issues.
---

# Media Bug Triage Helper

This skill helps triage Mozilla Bugzilla bugs related to media issues in Firefox, but can be applied to other bug types as well.

Typical use:

/media-bug-triage 123456

## Overview

The skill walks through a set of phases during analysis:

1. **Basic Information Gathering** — gather key information from the main bug report and a few related resources, and make quick assessments.
2. **Detailed Information Gathering** — collect comprehensive details: parse the bug, follow links to related bugs, search relevant bugs, and research discovered resources.
3. **Quick Summary and Reporting** — summarize findings and generate a concise triage report.
4. **Developer Tools Investigation** *(Optional)* — investigate the codebase to validate assumptions, identify root causes, and highlight relevant files and tests.

## Run Configuration

Resolve both settings before doing anything else. State the active scope profile when beginning analysis.

**Bug ID** — Extract from user input. Accepted formats:
- Bugzilla ID: `1234567`
- With "Bug" prefix: `Bug 1234567`
- Full URL: `https://bugzilla.mozilla.org/show_bug.cgi?id=1234567`

If no bug ID is provided, prompt the user:
```
Welcome to Firefox Bug Triage Assistant!

Please provide a Bugzilla bug number to analyze (e.g., 1234567) and scope profile (optional, e.g. "graphics", "web-conferencing", "android"). If you don't specify a scope profile, I'll infer it from the bug's component.

Example input: `1234567 scope:graphics`
```

**Scope profile** — If the user specified a topic (e.g. "graphics", "web-conferencing", "android"), use that profile from the Scope Profiles section. If not specified, infer from the triage bug's component after fetching it:
- Audio/Video components → `media`
- WebRTC components → `web-conferencing`
- Graphics components → `graphics`
- GeckoView or Firefox for Android components → `android`
- If the component spans multiple areas, use `media-and-web-conferencing` or ask the user.

**Tips For Agents** - Input may include short suggestions Agents can act on. For example: 
/media-bug-triage 2023481 media [agent tip: triage 2023379 as a part of your analysis.]

**Verbosity** — Be explicit about which workflow step you are in or transitioning to as you execute this skill.

---

## Tools Access

### Bugzilla Access

Use Mozilla's Bugzilla REST API directly through WebFetch. Do not use the moz MCP server for Bugzilla access.

Parse ../shared/Bugzilla.md for details on how to access and use Bugzilla data effectively during this triage process.

#### Bugzilla Access Rules

- Cache fetched bug data in-session to avoid re-fetching the same bug ID within one triage run.
- Restrict bug report searches to bugs newer than 12 months from today to reduce data volume.
- Track bug reports that could not be accessed due to permissions.

#### Bugzilla Use Tracking

Track the following for inclusion in the final report:
- Total number of Bugzilla queries sent
- Total number of bugs processed
- Inaccessible bugs due to permission restrictions

#### Bugzilla Component Restrictions

Limit searches to the components defined by the active scope profile. See the **Scope Profiles** section.

### Firefox Crash Reports

- **socorro-cli** — Query Mozilla's Socorro crash reporting system for crash volume, top crashes, and signature details. Use this during triage to assess crash impact and validate signatures. (https://github.com/yjugl/socorro-cli)
- **crash-analysis** — A skill for deeper standalone crash investigation. Invoke this when a crash signature warrants full analysis beyond what triage requires.

### Firefox Profiler Analysis

- **profiler-cli** — Fetch and parse Firefox performance profiles from profiler.firefox.com links shared in bug comments. Useful when a reporter attaches a profile to demonstrate a performance regression or hang. (https://github.com/dpalmeiro/profiler-cli)

### Codebase Search

- **searchfox-cli** — Search the Firefox source code by identifier, symbol definition, or path. Use during codebase investigation (Step 6) to locate relevant files, function definitions, and recent changes. Run `searchfox-cli --help` for usage.

---

## Scope Profiles

The active scope profile defines which Bugzilla products and components are searched during the Bugzilla Investigation step. Resolved at invocation — see Run Configuration.

### media
- **Product:** Core
- **Components:** Audio/Video, Audio/Video: cubeb, Audio/Video: GMP, Audio/Video: MediaStreamGraph, Audio/Video: Playback, Audio/Video: Recording, Audio/Video: Web Codecs

### web-conferencing
- **Product:** Core
- **Components:** WebRTC, WebRTC: Audio/Video, WebRTC: Networking, WebRTC: Signaling, DOM: Screen Capture

### media-and-web-conferencing
- **Product:** Core
- **Components:** Audio/Video, Audio/Video: cubeb, Audio/Video: GMP, Audio/Video: MediaStreamGraph, Audio/Video: Playback, Audio/Video: Recording, Audio/Video: Web Codecs, WebRTC, WebRTC: Audio/Video, WebRTC: Networking, WebRTC: Signaling, DOM: Screen Capture

### graphics
- **Product:** Core
- **Components:** Graphics, Graphics: Canvas2D, Graphics: CanvasWebGL, Graphics: Color Management, Graphics: Image Blocking, Graphics: ImageLib, Graphics: Layers, Graphics: Text, Graphics: WebGPU, Graphics: WebRender, Web Painting

### android
- **Product:** Firefox for Android — **Components:** Media
- **Product:** GeckoView — **Components:** Media

---

## Workflow

### Step 1: Resolve Run Configuration

Apply the Run Configuration section: extract the bug ID from user input and resolve the scope profile. If no bug ID was provided, prompt the user as described in Run Configuration. State the active scope profile before proceeding.

### Step 2: Check For Previous Reports

In the ./reports directory, a previous report for this bug may already exist. If you detect one, inform the user and ask if we should continue. If the user prefers not to continue, end the skill.

### Step 3: Fetch Initial Bug Data

Fetch the initial bug report, including:

- The bug summary and bug description (first comment)
- Additional bug comments
- Attachment list and descriptions
- Itemized crash signatures
- Current status, product, component, keywords, whiteboard tags, pending needinfo flags
- Duplicate and See Also related fields (typically lists of additional related bugs)
- Bug dependency related fields
- Change history via `/rest/bug/{id}/history` — fetched in parallel with the above. This records all field changes (who changed what, from what value, to what value, and when). Pay particular attention to:
  - Security group additions or removals (e.g. `firefox-core-security`, `core-security`, `media-core-security`)
  - Product or component reclassifications
  - Flag changes (e.g. `sec-bounty`, `needinfo`)
  - Severity and priority assignments
  - Field changes made by Mozilla employees carry more weight than those made by anonymous or external users.

Print a brief summary of the bug including summary, reporter, reported date (bug age), severity/priority, and note if the bug is security sensitive.

### Step 4: Organize and Analyze Bug Information

#### Check Bug Status

Before proceeding with analysis, check if the bug is closed.

A bug is considered **closed** if its status is one of: `RESOLVED`, `VERIFIED`, `CLOSED`.

If the bug is closed, inform the user and stop:

```
Bug {BUG_ID} is already closed.

Status: {STATUS}
Resolution: {RESOLUTION}
Summary: {SUMMARY}

This bug was resolved as "{RESOLUTION}" and does not require triage analysis.

Would you like to analyze a different bug? Please provide another bug number, or type "exit" to end.
```

If the bug is **open** (status is `NEW`, `UNCONFIRMED`, `ASSIGNED`, `REOPENED`, etc.), proceed with analysis.

#### About:Support Detection

Scan all fetched comments for about:support data using the detection markers defined in the Data Processing Reference. Check both inline comment text and attachment filenames (e.g. `troubleshooting-data.json`, `about-support.txt`).

If about:support data is found, immediately invoke the About:Support Extraction Procedure before continuing. Incorporate the extracted fields — especially crash IDs — into all subsequent analysis steps.

#### Steps to Reproduce (STR)

**Mark as having STR only if:**
- Steps are detailed enough for >70% reproducibility
- Specific conditions, settings, and actions are documented
- A developer could reliably trigger the issue

**Mark as NOT having STR if:**
- Steps are vague ("browse the web", "watch videos")
- Issue is intermittent without clear triggers
- Reporter cannot reliably reproduce
- Steps depend on undocumented environment details

Collect platform specifics and Firefox version information from the bug report and comments, as these are important context for reproducibility.

**Examples:**
- **Good STR:** "1. Open about:config, 2. Set media.hardware-video-decoding.enabled to true, 3. Open youtube.com/watch?v=xyz, 4. Observe crash after 5 seconds"
- **Bad STR:** "Sometimes when watching YouTube videos, the video stops playing"

#### Test Cases

Check for:
- Attached HTML/JS/CSS test files
- Reproduction code in comments
- References to test cases
- Files named: `testcase*`, `repro*`, `poc*`, `reduced*`, `min*`, `minimized*`
- Keywords: `testcase`
- Flags: `in-testsuite+`, `in-qa-testsuite+`

#### Key Contributors

Bugzilla emails to recognize:

- `mozilla.com`, `mozilla.org`, `mozilla.net` — Likely Mozilla employees. Their feedback carries more weight, and seeking their input is straightforward.
- `alice0775@gmail.com` — A prolific external reporter known for accuracy in reporting and testing media-related bugs. Their feedback and confirmation is likely accurate. (A simple cc on bugs is common though and carries little weight.)

#### Crash Stacks

Look for:
- Stack traces with frame addresses (`#0 0x12345...`)
- AddressSanitizer (ASan) output
- UndefinedBehaviorSanitizer (UBSan) output
- ThreadSanitizer (TSan) output
- MemorySanitizer (MSan) output
- `cf_crash_signature` field content

#### Fuzzing Origin

Patterns indicating fuzzing:
- "found while fuzzing"
- fuzzilli, oss-fuzz, fuzzfetch, grizzly references
- Fuzzer tool mentions

#### Regression Timeline

If the reporter mentions this issue is a **regression**, track the reporting timeline of when the issue was first observed and any information about what may have caused the regression. This information is often found in the initial bug report but may also appear in follow-up comments.

- The reporter may provide a regressing bug ID, or information about which Firefox version or approximately when the issue started.
- They may have run Mozilla's regression finder `mozregression` and are sharing results.
- Other users may add additional timeline information.

Tracking the reporting timeline helps validate assumptions, visualize when a regression occurred, or identify the range of changes that may have caused it.

When investigating regressions, we may need to ask for:
- Whether the issue occurred in previous versions
- Suggest mozregression for bisection
- If a regression range is provided, examine changesets in the codebase
- Related commits via git log/blame
- Clear steps to reproduce
- Firefox version and OS
- Firefox profile with logs (link to about:logging)
- Crash report IDs (link to about:crashes)
- Minimal test case

If the bug report lacks critical information:
- Identify exactly what's missing
- Select an appropriate canned response or draft a custom request
- Be specific about what you need (not just "more info")
- Explain why this information helps

#### Crash Volume

If the bug is associated with crash signature(s), check Socorro for crash volume data for each signature. Attempt to incorporate crash volume changes into the analysis timeline and use this information to validate assumptions or provide additional context about impact.

#### Media Feature Notes

**Auto-play** (terms: auto play, autoplay, play blocking, video blocking):
- There are subtle differences between Firefox's auto-play behavior and that of Chrome and Safari. (https://wiki.mozilla.org/Media/block-autoplay)
- Users often confuse a different behavior as a bug vs. a feature.
- If the issue appears to be auto-play related, assess whether it is a valid bug or a misunderstanding of how Firefox works.

#### Good First Bug Assessment

As you triage, assess bugs for "good first bug" qualities and note this in your summaries. You may come across existing good first bugs tagged with the `good-first-bug` keyword.

Good First Bug qualities:
- A specific, well-understood, well-defined, and easily reproducible issue
- A simple bug where you have already generated proposed source changes to fix it
- Does not represent a major flaw users would commonly experience (P3/S3 or lower)
- An AI agent could confidently fix it with a simple patch unlikely to cause regressions

### Step 5: Quick Determination

#### Confidence Check

Based on the information gathered, evaluate these two questions:

**1. Is the issue clearly understood and the resolution evident?**
> "Do we have enough information to confidently describe the issue and propose a clear solution?"

- **Yes** — Summarize findings and pause. Ask the user if they would like to continue with further analysis.
- **No** — Continue to the next question.

**2. Is the issue likely non-reproducible?**
> "Is there insufficient, inconsistent, or contradictory information that makes reproduction unlikely without further input from the reporter?"

- **Yes** — Summarize findings and pause. Ask the user if they would like to continue, or prefer to request more information from the reporter.
- **No** — Continue to the Bugzilla Investigation step.

### Step 6: Bugzilla Investigation

**Goal:** Broaden our view beyond the single bug report by searching for similar reports, following
bug relationships, and building a picture of the issue landscape. The output is a structured set of
related bugs organized by relevance — including duplicate candidates, related meta bugs, and any
patterns suggesting a common root cause.

#### Phase A: Derive Search Terms

From the bug summary, symptoms, and component, extract 5–10 targeted search terms. Prefer:
- Specific error messages, API names, or symptom phrases from the bug description
- Technical terms that distinguish this issue from general noise
- Component-specific terms likely to appear in similar reports

Avoid generic terms ("crash", "broken", "doesn't work") that will produce noisy, unrelated results.

#### Phase B: Keyword Search

Search Bugzilla using the derived terms. Apply the component restrictions from the Tools Access
section and limit results to bugs from the past 12 months unless the issue appears older.

Also seed the search with any bugs already in the triage bug's `see_also`, `depends_on`, and
`blocks` fields — these are highest-confidence related bugs and should be retrieved first.

For each result, fetch a **lightweight summary** sufficient to assess relevance:
- Summary, status/resolution, component, severity, priority, platform
- First comment (truncated to ~500 characters)
- Whether it has a `duplicate_of` or non-empty `see_also` field

#### Phase C: Relevance Assessment

For each result from Phase B, make a quick relevance judgment:
- **High relevance** — symptoms, platform, component, and/or error message closely match the
  triage bug. Fetch the full bug (comments, attachments, history).
- **Possible relevance** — partial match with some overlapping signals but not conclusive. Note
  it, but do not fetch full data unless a pattern emerges across multiple partial matches.
- **Not relevant** — dismiss.

Be selective. Fetch full data only for bugs that clearly warrant it — the goal is signal, not coverage.

#### Phase D: Follow Bug Relations

For high-relevance bugs, follow their `see_also`, `duplicate_of`, `depends_on`, and `blocks`
relations to discover additional related bugs.

**Relation reach limit:** Do not follow relations more than **3 hops** from the original triage
bug. This prevents runaway traversal on densely connected bug clusters.

#### Phase E: Analysis

With the gathered data, perform the following analysis:

**Duplicate identification** — Identify bugs that appear to describe the same issue. Note the
oldest open report (typically the canonical one to keep when marking duplicates).

**Clustering** — If there are multiple related bugs, group them by apparent root cause or symptom.
For each cluster, assess:
- Does this cluster point to a single underlying cause, or are these likely distinct issues?
- Is there an existing meta bug tracking this area?
- Does any bug in the cluster have an accepted fix or patch that may also resolve the triage bug?

**Dependency mapping** — Note any `depends_on` / `blocks` relationships that affect
prioritization — e.g., if the triage bug blocks a high-priority issue.

**Root cause signals** — Across all gathered bugs, note any recurring patterns (same code path,
same preferences, same platform or hardware combination) that may point toward a common root cause.

Present a summary of findings (2–3 sentences) to the user, including key related bugs.

Prompt for next steps:
1. Copy the summary to the clipboard.
2. Triage a new bug (expected input: `2, bug identifier`).
3. Continue analysis.
4. Generate the final, detailed triage report.
5. Exit skill.

- If option 1: copy to clipboard and re-prompt.
- If option 3: move on to Codebase Investigation.
- If option 4: move on to Generate Analysis Report.

### Step 7: Codebase Investigation

If the triage bug likely reports a valid issue in Firefox and we have a good understanding of it, investigate the codebase to understand where the issue might originate.

- **Identify relevant files** using the component and keywords
- **Search for related code** using `searchfox-cli` or grep tools
- **Read relevant source files** to understand the affected area
- **Look for recent changes** that might relate to the issue
- **Check for existing tests** that cover the functionality

This investigation helps:
- Confirm the bug's validity
- Understand the scope of impact
- Identify potential root causes
- Suggest specific code areas to investigate
- Determine if a fix might be straightforward

### Step 8: Suggest Requesting Feedback?

At this point, you should have a good understanding of the issue, its symptoms, and possible causes. Determine if we need to ask the reporter or others for additional information to confirm our understanding. This is particularly important if there are information gaps preventing a confident assessment, or if there are multiple possible causes that need to be narrowed down. Requesting more information is often more economical than having developers analyze an issue with incomplete information.

> Do not delay triage if the perceived issue represents an S1 or S2 severity. We can still ask for information, but should not block the triage process.

#### Feedback Request Drafting

Draft an appropriate response using either:
1. A canned response template (see Canned Response Reference below)
2. A custom response for unique situations

Response guidelines:
- Be professional, helpful, and welcoming.
- Thank reporters (especially new contributors).
- Be specific about what information is needed.
- Provide clear next steps.
- Keep responses concise and actionable.

### Step 9: Generate Analysis Report

Generate a detailed triage report and summary in markdown format. See the **Analysis Report Format** section for structure details.

Always write the report to a `./reports` sub-directory with the filename `bug-{BUG_ID}-triage.md`. If the file already exists, create a new file with a numeric suffix (e.g., `bug-{BUG_ID}-triage-2.md`).

Prompt for next steps:
1. Copy the detailed report to the clipboard.
2. Copy the shorter summary to the clipboard.
3. Ask a question (format: `3, question text`).
4. Triage another bug.
5. Exit skill.

- If option 1 or 2: copy to clipboard and re-prompt.
- If option 3: prompt for a question about the bug or analysis, provide an answer, then return to this prompt.
- If option 4: prompt for a new bug identifier and restart the triage process.

### Step 10: End of Analysis

When analysis is complete and a report is generated, end the skill. Before ending, update the `FUNCTIONALITY.md` file with any new information or insights gained that may be useful for future analyses. Also suggest any improvements to this skill that would make future analyses more effective or efficient.

---

## Canned Response Reference

Use these templates as starting points, customizing for each bug. Full templates are in the `CANNED_RESPONSES.md` supplement file.

### Information Requests

| ID | Use When | Template Summary |
|----|----------|------------------|
| `need-str` | STR missing/unclear | Request specific reproduction steps |
| `need-testcase` | Need minimal test | Request reduced HTML/JS/CSS example |
| `need-profile` | Need logs | Request Firefox profile via about:logging |
| `need-crash-report` | Crash without report | Request bp-* IDs from about:crashes |
| `more-info-needed` | General info gap | Request version, OS, extensions, regression info |
| `need-regression-range` | Possible regression | Suggest mozregression bisection |
| `need-system-info` | Need hardware/system details | Request about:support info |

### Status Updates

| ID | Use When | Template Summary |
|----|----------|------------------|
| `confirmed` | Reproduced issue | Confirm with environment details |
| `investigating` | Looking into it | Acknowledge and request patience |

### Resolutions

| ID | Use When | Template Summary |
|----|----------|------------------|
| `duplicate` | Same as another bug | Link to duplicate, explain |
| `wontfix` | Won't be fixed | Explain reasoning |
| `worksforme` | Can't reproduce | Share test environment, request more info |
| `incomplete` | No response to needinfo | Close with invitation to refile |

### Acknowledgements

| ID | Use When | Template Summary |
|----|----------|------------------|
| `fuzzing-thanks` | Fuzzer-found bug | Thank for fuzzing contribution |
| `first-time-contributor` | New reporter | Welcome message |
| `good-report` | Quality report | Thank for clear details |

### Special Cases

| ID | Use When | Template Summary |
|----|----------|------------------|
| `security-notice` | Security implications | Restrict visibility, link to bounty program |
| `moved-component` | Wrong component | Explain the move |
| `needs-platform-team` | Platform-specific | Add platform specialists |

---

## Analysis Report Format

Suggested structure for the triage report. Adjust as needed based on available information.

**Safety rules:**
- When referencing bugs with security ratings, highlight them appropriately and avoid including summary text. Instead, link to the bug and let the reader explore the details.

**Format Notes**
- Use 'linkable' format for all bug IDs, for example - [1234567](https://bugzilla.mozilla.org/show_bug.cgi?id=1234567)
- Use searchfox links for code references, for example - [MediaDecoderStateMachine.cpp](https://searchfox.org/mozilla-central/source/dom/media/MediaDecoderStateMachine.cpp)
- When referencing crash signatures, link to Socorro search results for that signature, for example - [Crash Signature](https://crashes.mozilla.org/signatures?q=signature%3A%22%3Csignature%3E%22)

```markdown
# Bug {BUG_ID} Triage Analysis

**Generated:** {CURRENT_DATE}
**Bug URL:** https://bugzilla.mozilla.org/show_bug.cgi?id={BUG_ID}

## Bug Information

- **Summary:** {SUMMARY}
- **Reporter:** {REPORTER}
- **Status:** {STATUS}
- **Product:** {PRODUCT}
- **Component:** {COMPONENT}
- **Created:** {CREATION_TIME}

## Research Summary and Key Findings

Detail the issue, symptoms, and any relevant information gathered from the bug report, related bugs,
and codebase investigation. Summarize key findings. Identify other Bugzilla reports that are related
or possible duplicates. Note that codebase inspection results, if completed, are detailed separately below.

## Regression Timeline

If applicable, summarize any information about when this issue was first observed and what may have
caused the regression. This information is often found in the initial bug report or in follow-up comments.

## Classification

| Signal | Detected | Evidence |
|--------|----------|----------|
| Clear STR | Yes/No | [brief evidence] |
| Test Case | Yes/No | [brief evidence] |
| Crash Stack | Yes/No | [brief evidence] |
| Fuzzing | Yes/No | [brief evidence] |

## Assessment

- **Suggested Severity:** S1/S2/S3/S4/N/A/--
- **Suggested Priority:** P1/P2/P3/P5/--

### Assessment Reasoning

[2-3 paragraphs maximum.]

## Codebase Investigation

Detail any codebase investigation performed, including relevant files examined and specific areas
worth investigating further based on your research.

## Suggested Investigation Areas

[Specific code areas developers should look at.]

## Bugzilla Use Tracking

- Total Bugzilla Queries: {TOTAL_QUERIES}
- Total Bugs Processed: {TOTAL_BUGS}
- Estimated Download Bandwidth Used: {BANDWIDTH} MB
- Inaccessible Bugs Due to Permissions: {INACCESSIBLE_BUGS}
```
