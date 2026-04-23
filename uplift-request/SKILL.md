---
name: uplift-request
description: Help prepare a Firefox uplift approval request (Beta, Release, and/or ESR) by checking whether patches are already on the bug, auditing sanitization once for sec-* bugs, and drafting the approval comment per https://wiki.mozilla.org/Release_Management/Uplift_rules. Use after a fix is ready and needs to ride into a stabilization branch. May or may not follow sec-approval (sec-moderate typically skips sec-approval but may still need uplift).
argument-hint: "[bug-id] [path-to-bug-report] [--beta] [--release] [--esr NN]"
allowed-tools:
  - Bash(git:*)
  - Bash(jj:*)
  - Bash(searchfox-cli:*)
  - Bash(bmo-to-md:*)
  - Bash(moz-phab:*)
  - Bash(python3:*)
  - Read
  - Grep
  - Glob
  - AskUserQuestion
  - WebFetch
  - Write
---

# Uplift Request Skill

Drafts a Bugzilla uplift-approval comment for Firefox Beta, Release, and/or
ESR, following the
[Uplift rules](https://wiki.mozilla.org/Release_Management/Uplift_rules).

> Dependencies and Bugzilla API key setup live in
> [`README.md`](./README.md). Point the user there if `bmo-to-md` or
> `bmo-uplift-request --check-auth` fails.

This skill may run standalone (e.g. sec-moderate, non-security regressions) or
after `sec-approval` has already been filed. The sanitization audit for
sec-\* bugs runs exactly **once**, early in the flow, and all later steps
trust that result.

The Bugzilla API key config is shared with the `sec-approval` skill — if
that works, this will too. Never read or print the key; use
`python3 .claude/skills/uplift-request/bmo-uplift-request --check-auth`
to test availability.

**Arguments:** $0

Parse:

- The first all-digit token with **6 or more digits** and not immediately
  following `--esr` is the **bug ID**. The 6-digit floor avoids collision
  with ESR version numbers (`--esr 140`), which are 2–3 digits.
- Any token containing `/` is the **bug report path** (a folder of markdown
  written by `bmo-to-md`).
- `--beta`, `--release`, and `--esr NN` select target channels; multiple are
  allowed. If none are supplied, ask after Step 1.

All arguments are optional.

---

## Step 1 — Gather context

### Retrieve the bug

- **sec-\* or otherwise restricted**: `mcp__moz__get_bugzilla_bug` will fail.
  Use the same priority order as `sec-approval`:
  1. If the user supplied a bug-report path, read `summary.md` / `bug-<id>.md`
     from that folder.
  2. Otherwise run `bmo-to-md -o /tmp/bug-<id> -a <bug_id>` (requires a
     Bugzilla API key — check with the `--check-auth` command above).
  3. Otherwise ask the user.
- **public bugs**: prefer `mcp__moz__get_bugzilla_bug`.

Collect: component, keywords, severity, `sec-*` level (if any), existing
`status-firefoxNN` / `tracking-firefoxNN` flags, regressor bug if known, and
any prior uplift comments.

### Inspect local commits

```bash
# Detect VCS
jj --version 2>/dev/null && echo "jj" || echo "git"
```

**git:**

```bash
git log --oneline origin/main..HEAD
git log origin/main..HEAD --format=%B
git diff --stat origin/main..HEAD   # overview first — the full diff can
                                    # be large; read hunks selectively
git diff origin/main..HEAD -- <file>  # for each file of interest
```

**jj:**

```bash
jj log -T builtin_log_detailed -r 'trunk()..@'
jj diff --stat -r 'trunk()..@'      # overview first
jj diff -r 'trunk()..@' <file>      # for each file of interest
```

Record: commit messages, every `Differential Revision: .../D<N>` trailer, and
the full diff.

### Current release context

```
WebFetch: https://whattrainisitnow.com/calendar/
```

Extract current Nightly, Beta, Release, and live ESR versions. Also read the
local tree version if available: `cat config/milestone.txt`.

---

## Step 2 — Determine target channel(s)

If the user did not pass `--beta` / `--release` / `--esr NN`, ask with a
single `AskUserQuestion` (multiSelect) using concrete versions from the
calendar (e.g. "Beta 149", "ESR 140", "ESR 128"). Only offer ESR versions
that are currently supported.

A single block may cover several channels when they share the same patch.
See Step 6 for the block-grouping rule (one block per distinct patch
variant, not per channel).

---

## Step 3 — Check whether patches are on the bug

Goal: know which of the four scenarios below we're in, so Step 4 can audit
exactly once.

1. **List attachments** (the script never prints the API key):

   ```bash
   python3 .claude/skills/uplift-request/bmo-uplift-request <bug_id> --list
   ```

   This prints each active Phabricator and raw-patch (`text/plain`)
   attachment with its ID, Phabricator revision (if any), summary, and
   current flags.

2. **Match** each local commit against the attachments:

   - **Strong — Phabricator**: `Differential Revision: .../D<N>` trailer
     matches an attachment whose summary or (decoded) data contains `D<N>`.
   - **Strong — raw patch**: fetch the `text/plain` attachment content and
     compare the first few `diff --git` hunk headers against the local diff.
     Matching file paths + identical hunk headers is a strong match;
     identical bodies is conclusive.
   - **Weak**: title/summary overlap only — treat as "possible", confirm with
     the user before trusting.

3. **Record the scenario** (sec-\* cases only — non-sec bugs skip Step 4):

   - **A.** No matching attachments. Local has the patches.
     → User hasn't submitted. Audit local commits.
   - **B.** Same as A, but the user only wants the form drafted (no
     submission). → Audit local commits.
   - **C.** Attachments match local. → Audit local commits (same content).
   - **D.** Attachments exist but diverge from local, or there are no local
     commits.
     → Audit what we can fetch: raw-patch attachment content and/or local
     commits if present. For Phabricator attachments with no local match we
     cannot pull the diff without Phab auth — flag that to the user and ask
     them to confirm the attached patches were sanitized.

Present the outcome as a short table before branching.

---

## Step 4 — Sanitization audit (sec-\* only, runs once)

Skip this entire step for non-sec bugs.

Run **Phase 1 — Compliance Audit** from the `sec-approval` skill
(commit messages, inline comments, identifiers, tests, Try server,
obfuscation). Do not duplicate the audit text here — follow the checks in
`.claude/skills/sec-approval/SKILL.md` Phase 1 and present the same
PASS/FAIL table.

**Inputs, per scenario from Step 3:**

| Scenario | What to audit                                                                        |
| -------- | ------------------------------------------------------------------------------------ |
| A, B     | Local commits (and diffs).                                                           |
| C        | Local commits (same content as the attachments).                                     |
| D        | Local commits if any; raw-patch attachment content; for Phabricator-only, ask user.  |

**Outcome:**

- **All PASS** → set an internal flag `sanitization_ok = true`. Steps 5 and 6
  proceed without re-auditing.
- **Any FAIL** → block. Present the specific violations with suggested fixes
  and ask the user to resolve them. After fixes, re-run this step. If
  attachments on the bug already contain unsanitized content (scenario C/D
  where the audit fails), remind the user they must update both local **and**
  re-submit the sanitized version (Step 5) before continuing.

No downstream step runs the audit again.

---

## Step 5 — Submit path (only if patches aren't on the bug, or need re-submission)

Triggers:

- Scenario A: user asks Claude to submit.
- Scenario D after a re-sanitization.

Two submit paths. Prefer **5a (moz-phab uplift)** unless the user has a
concrete reason to fall back to raw-patch attachments. Either path is
user-visible and hard-to-reverse — always confirm before running.

Scenario B (user submits themselves later) — skip this step; just tell
the user which commands to run when they are ready.

### 5a — moz-phab uplift (preferred)

The moz-phab uplift flow creates a new Phabricator revision per target
train, and a bot automatically adds Release Managers as reviewers when
the lando uplift form is completed. Wiki:
<https://wiki.mozilla.org/Release_Management/Requesting_an_Uplift#Requesting_Uplift_using_moz-phab>

On path 5a the Step 7 answer file is **not** posted as a BMO comment —
instead the user pastes its contents into the lando uplift form (URL
printed at the end of each `moz-phab uplift` run). Skip Step 8 in that
case.

**Preflight (once per run):**

1. `moz-phab uplift --list-trains` confirms train names (they begin
   with `firefox-` and do not always match the branch name; e.g.
   `firefox-esr140`, `firefox-esr115`, `firefox-beta`,
   `firefox-release`).
2. **Check whether each target branch already has the fix.** A Nightly
   library uprev (libaom/libvpx/dav1d/etc.) often carries the upstream
   fix across merge day — e.g. once Beta rotates forward, Beta may
   already contain the patched file. Confirm before committing any
   uplift work:
   ```bash
   git fetch upstream <target-branch>
   # File check: does the target version still have the pre-fix marker?
   git show upstream/<target-branch>:path/to/file \
       | grep -c '<pre-fix-token>'
   # History check: does the uprev bug already live on the branch?
   git log --oneline upstream/<target-branch> -- path/to/file | head
   ```
   If the fix is already present, skip that channel entirely and tell
   the user — the corresponding `approval-mozilla-*?` flag on any
   pre-existing raw-patch attachment is now moot.

**Per-channel flow:** for each channel that still needs the patch,

1. Ensure the worktree is on `mozilla-firefox/firefox` and the target
   tip is fetched (`upstream/beta`, `upstream/release`,
   `upstream/esrNN`).
2. Stash irrelevant working-tree modifications so only the uplift diff
   is present:
   ```bash
   git stash push -m "uplift-tmp" -- <paths-to-stash>
   ```
3. Create a local branch off the target tip and commit the uplift
   patch. Cherry-pick when the same diff applies verbatim; otherwise
   `git apply` the prepared `.patch` file:
   ```bash
   git checkout -b bug-<bug_id>-<channel> upstream/<target-branch>
   git cherry-pick <uplift-commit>
   # OR
   git apply /path/to/bug<bug_id>-uplift-<channel>.patch
   git add <paths> && git commit -m "<sanitized subject>"
   ```
4. **Sanitized commit subject for sec-\* bugs.** The subject
   propagates into the Phabricator revision title, bot notifications,
   and CI logs — keep it maximally generic. Good: `Bug <id> -
   Cherry-pick <library> fix`, `Bug <id> - Backport <library> patch`.
   Avoid words that hint at the bug class: *thread-safety, race,
   bounds, overflow, use-after-free, free, UAF, heap*, or specific
   symbol/file names (`grain_synthesis.c`, `add_film_grain_run`,
   etc.). Strip the commit body entirely.
5. **Before the first `moz-phab uplift` of the run, ask the user**
   whether they want WIP (Changes Planned) or not-WIP (Needs Review).
   Reuse the answer for every subsequent channel in the same run.
   - **WIP (default, safer)**: moz-phab submits as "Changes Planned".
     Release Managers are **not** notified until the user completes
     the lando uplift form (or flips WIP off explicitly). Use this
     when the user still wants to eyeball the Phabricator revision
     before it goes live.
   - **Not-WIP**: pass `--no-wip` on the moz-phab command. The
     revision is created in "Needs Review" immediately.
6. Run `moz-phab uplift --train <train> <base-rev> <tip-rev>`,
   appending `--no-wip` if the user asked for not-WIP:
   ```bash
   moz-phab uplift --train firefox-esr140 upstream/esr140 HEAD
   # or:
   moz-phab uplift --train firefox-esr140 --no-wip upstream/esr140 HEAD
   ```
   `--yes` skips interactive confirmation; `--no-rebase` is useful
   when the patch has already been adapted for the target branch.
7. **If the revision was submitted WIP and the user later wants to
   flip it to Needs Review**, the local commit must first carry a
   `Differential Revision: https://phabricator.services.mozilla.com/D<id>`
   trailer so moz-phab knows which revision to update. The initial
   `moz-phab uplift` run does **not** add that trailer to the local
   commit. If you rerun `moz-phab uplift ... --no-wip` without first
   amending the commit to add the trailer, moz-phab will create a
   **new** revision instead of updating the existing one. Fix:
   ```bash
   git commit --amend -m "$(git log -1 --format=%s)

   Differential Revision: https://phabricator.services.mozilla.com/D<id>"
   moz-phab uplift --train <train> --no-wip --no-rebase --yes \
       upstream/<target-branch> HEAD
   # If a duplicate got created first, abandon it:
   moz-phab abandon D<duplicate-id> --yes
   ```
8. Open the lando URL printed at the end of the run
   (`https://lando.moz.tools/uplift/request/?revisions=<rev-id>`) and
   paste the Step 7 answer file into the nine-question uplift form —
   completing the form is what actually sends the request to Release
   Managers. Do this whether the revision was submitted WIP or
   not-WIP; the lando form is a separate step from the moz-phab
   submission.

**Reusing one worktree for several channels.** Fine — just create a
fresh `bug-<bug_id>-<channel>` branch off each target tip. Cherry-pick
from the first channel's branch. Between channels, the stash and any
untracked files ride along.

**Sec-\* bug visibility.** `moz-phab uplift` inherits the bug's
Phabricator security group — revisions created from a
media-core-security (or similar) bug are "secure" and visible only to
that group, matching the existing Phabricator attachments. Verify
this on the first revision you create before proceeding to the rest.

### 5b — Raw patch + BMO approval flags (fallback)

Use when moz-phab uplift isn't applicable — e.g. the bug predates
moz-phab uplift support, or the patch only exists as a text file and
the user doesn't want to turn it into a Phabricator revision. Upload
via the helper script; it can set approval flags and post the Step 7
comment in the same API call.

```bash
git format-patch -1 HEAD -o /tmp
python3 .claude/skills/uplift-request/bmo-uplift-request \
    <bug_id> --attach /tmp/0001-*.patch --dry-run
# If the dry-run looks right, re-run without --dry-run.
```

The summary defaults to the patch Subject (with `[PATCH n/m]`
stripped); pass `--summary` to override. When re-submitting a
sanitized version after Step 4 flagged the existing attachment
(scenario D), pass `--obsolete <old_attachment_id>` (repeatable) so
the stale patch is marked obsolete atomically with the upload. Combine
`--attach` with `--beta` / `--release` / `--esr NN` (and an optional
positional comment file) to upload the patch, post the uplift form,
and set approval flags in a single API call.

After submission, re-list attachments to record the new IDs for
Step 8.

---

## Step 6 — Draft the uplift questionnaire

The form, per
<https://wiki.mozilla.org/Release_Management/Uplift_rules#Guidelines_on_approval_comments_for_Beta_and_Release>,
has nine fields (same set for Beta, Release, ESR):

1. **User impact if declined** — user-facing consequence, not repro steps.
   - For sec-\* bugs: **state the security impact explicitly**. Lead with
     `sec-<rating> <class>` (e.g. "sec-high heap memory disclosure",
     "sec-moderate UAF") and describe the concrete observable consequence
     (what web content or an attacker can see/do). Do **not** sanitize this
     field down to generic "returns incorrect data" — approvers are release
     drivers who need to understand the severity they're signing off on, and
     sec-approval has already gated this content.
2. **Is this code covered by automated tests?** — Yes / No / Unknown. Answer
   based on what is **currently landed on the target branch**, not on what the
   uplift bundle will add once approved. If the test is attached/queued but
   not yet in-tree on that branch, answer **No** and note "New test attached;
   will land with the uplift." If the test is landed on trunk but the uplift
   crosses into a release branch where it isn't yet backported, the answer for
   that branch is still **No**. Only answer **Yes** when coverage already
   exists on the target branch at the time of the approval request.
3. **Has the fix been verified in Nightly?** — Yes / No (ask the user).
4. **Needs manual test from QE?** — Yes / No; if Yes, provide/reference repro.
5. **List of other uplifts needed** — dependent patches not on the target
   branch.
6. **Risk to taking this patch** — Low / Medium / High.
7. **Why is the change risky/not risky?** — concrete justification tied to
   diff size, scope, test coverage, behaviour changes.
8. **String changes made/needed** — "none" or describe. String changes need
   l10n driver approval.
9. **Is Android affected?** — Yes / No / Unknown based on whether touched code
   is shared with GeckoView.

Use the bug, the diff, and the `status-firefoxNN` flags to fill every field.
Keep answers tight and factual — one sentence where possible.

**For sec-\* bugs** (already sanitized by Step 4): keep the same caution in
the *text* of the risk/why-risky and test-coverage fields — no function
names, no line numbers, no code snippets in those. The **User impact if
declined** field is the explicit exception: it must name the sec rating and
concrete security consequence so approvers can judge severity. Keep it
factual and short, but do not under-sell it.

**Group uplift blocks by patch identity, not by channel.** Produce one
block per **distinct patch variant**, listing every channel that shares it:

- Same patch applies cleanly to Beta, Release, and ESR 140, but ESR 115 needs
  a rebase → **2 blocks**: one headed
  `### Uplift Request — Firefox Beta 150 / Release 149 / ESR 140`, another
  headed `### Uplift Request — Firefox ESR 115`.
- Same patch applies cleanly to every requested channel → **1 block** headed
  with all the channels it covers.
- Every channel needs a different patch → one block per channel.

Default to "one block covering all requested channels" when the patch is
small/structural and likely to cherry-pick cleanly. If backport conflicts
surface later, split the block then. Rationale: each block maps to one
attachment submission + approval-flag batch on Bugzilla — one block per
patch is the natural grouping, and duplicating identical answer text across
per-channel blocks is noise.

---

## Step 7 — Write the markdown file

Write to the repository root as `uplift-request-bug-<bug_id>.md` (or
`uplift-request.md` if no bug ID). Use compact markdown — no blank lines
between bullets, one answer per line:

```text
### Uplift Request — Firefox <channels this patch covers>
* **User impact if declined**: <answer>
* **Is this code covered by automated tests?**: <Yes/No/Unknown>
* **Has the fix been verified in Nightly?**: <Yes/No>
* **Needs manual test from QE?**: <Yes/No — steps or reference>
* **List of other uplifts needed**: <answer or "None">
* **Risk to taking this patch**: <Low/Medium/High>
* **Why is the change risky/not risky?**: <answer>
* **String changes made/needed**: <none or description>
* **Is Android affected?**: <Yes/No/Unknown>

*Drafted with the assistance of Claude Code — reviewed and approved by the patch author.*
```

The heading lists every channel the block's patch applies to — e.g.
`### Uplift Request — Firefox Beta 150 / Release 149 / ESR 140 / ESR 115`
for a clean-everywhere patch, or a single-channel heading for a
rebased variant. When the request covers multiple distinct patches,
concatenate one block per patch separated by a single blank line. Use the
`Write` tool, then tell the user the file path.

**Once the answer file exists, remind the user what to do with it:**

- If path 5a (moz-phab uplift) is in use — or will be in use — tell
  the user to paste the relevant block from this file into the lando
  uplift form at the URL `moz-phab uplift` prints
  (`https://lando.moz.tools/uplift/request/?revisions=<rev-id>`) for
  each revision. Mention it explicitly, per channel — this is the
  step that replaces a Bugzilla comment in the moz-phab flow and it
  is easy to forget.
- If path 5b (raw-patch + BMO flags) is in use, Step 8 posts the
  file contents as a Bugzilla comment automatically; no manual
  paste needed.

---

## Step 8 — Post to Bugzilla (only for path 5b; skip for path 5a)

Ask the user whether to post. Always dry-run first.

1. **Check API key** — never read or print it:

   ```bash
   python3 .claude/skills/uplift-request/bmo-uplift-request --check-auth
   ```

   On failure, offer the user the two options already documented in
   `sec-approval` (persistent in `~/.config/bugzilla/config.toml`, or
   one-time `$BMO_API_KEY`) and stop. The same config is used for both
   skills, so if `sec-approval` already works, this will too.

2. **Resolve attachment(s)**: uplift flags go on Phabricator attachments (one
   flag per target branch, often one attachment per backport patch). Use the
   `--list` output and the local commits' `D<N>` trailers to pick defaults.
   Ask the user to confirm. If none match (e.g. raw-patch-only), ask for the
   attachment ID.

3. **Dry-run per block.** Each block from Step 6 corresponds to one
   attachment and the channels that block covers — pass every channel flag
   for that block in a single invocation:

   ```bash
   python3 .claude/skills/uplift-request/bmo-uplift-request \
       <bug_id> uplift-request-bug-<bug_id>.md \
       --attachment <id> --beta --release --esr 140 --esr 115 --dry-run
   ```

   Flags supported: `--beta`, `--release`, `--esr NN` (combine all the
   channels that share the block's patch). Show the dry-run output and
   confirm.

4. **Post** — re-run without `--dry-run`. When the request has multiple
   blocks (distinct patch variants on different attachments), invoke the
   script once per block with that block's attachment and channel flags.

5. Report the Bugzilla URL printed by the script.

---

## Tips

- Uplift flags:
  - `approval-mozilla-beta?`
  - `approval-mozilla-release?`
  - `approval-mozilla-esr{NN}?` (version-specific, e.g. `approval-mozilla-esr140?`)
- Beta cut-offs, ESR dot-releases, and merge-day dates come from
  <https://whattrainisitnow.com/calendar/> — don't guess.
- String changes need l10n driver approval separate from release drivers.
- ESR uplift is *additional* to sec-approval when both apply.
- If `bmo-to-md` isn't installed, point the user to `cargo install bmo-to-md`
  (<https://github.com/padenot/bmo-to-md>).
