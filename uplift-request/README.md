## uplift-request

Prepare a Firefox uplift-approval request for Beta, Release, and/or ESR from
a local patch. Checks whether the patches are already attached to the bug,
runs the sanitization audit once for sec-\* bugs, and drafts the nine-question
[Uplift rules](https://wiki.mozilla.org/Release_Management/Uplift_rules)
form — optionally uploading a raw patch, posting the comment, and setting
`approval-mozilla-{beta,release,esrNN}?` flags in a single API call.

May run standalone (sec-moderate, non-security regressions) or after the
`sec-approval` skill has already filed the approval request.

### Usage

```
/uplift-request                                       # infer bug id from local patch; ask for channels
/uplift-request 1234567 --beta                        # explicit bug id + single channel
/uplift-request 1234567 --beta --release              # multiple channels
/uplift-request 1234567 --esr 140 --esr 115           # multiple ESR lines
/uplift-request 1234567 /tmp/bug-1234567 --beta       # pre-fetched bmo-to-md report
```

### Dependencies

1. **[bmo-to-md](https://github.com/padenot/bmo-to-md)** — downloads
   security-restricted bugs as Markdown. The MCP Bugzilla tool cannot read
   `sec-*` bugs, so this CLI is required when the uplift target is a
   security bug.

   ```bash
   cargo install bmo-to-md
   ```

2. **`bmo-uplift-request` script** — ships with this skill; used for the
   auth check, listing attachments, uploading raw patches, and posting the
   uplift comment with approval flags. Requires Python 3.8+ (stdlib only,
   no extra packages).

3. **[moz-phab](https://moz-conduit.readthedocs.io/en/latest/phabricator-user.html)**
   (optional) — used by the submit step when the patch isn't already on
   Phabricator.

### Bugzilla API key setup

A Bugzilla API key is needed for:

- Fetching `sec-*` bugs via `bmo-to-md`.
- Listing attachments, uploading raw patches, and posting the uplift
  comment via `bmo-uplift-request`.

The config is **shared with the `sec-approval` skill** — if that already
works, this will too, with no extra setup.

Generate a key at
<https://bugzilla.mozilla.org/userprefs.cgi?tab=apikey>, then pick **one**
of the storage options below. The scripts check sources in this order:

| Priority | Source | Notes |
|---|---|---|
| 1 | `BMO_API_KEY` env var | One-off / ephemeral shell |
| 2 | `~/.config/bugzilla/config.toml` | Recommended for daily use |
| 3 | `~/.config/bmo-to-md/config.toml` | Reused if `bmo-to-md` is already configured |

**Option 1 — persistent (recommended):**

```bash
mkdir -p ~/.config/bugzilla
cat > ~/.config/bugzilla/config.toml << 'EOF'
api_key = "YOUR_KEY"
EOF
chmod 600 ~/.config/bugzilla/config.toml
```

**Option 2 — one-off (current shell only):**

```bash
export BMO_API_KEY="YOUR_KEY"
```

Verify the key is wired up without printing it:

```bash
python3 .claude/skills/uplift-request/bmo-uplift-request --check-auth
```

### What the questionnaire covers

The drafted comment follows the exact format release drivers expect,
answering the nine fields from
<https://wiki.mozilla.org/Release_Management/Uplift_rules#Guidelines_on_approval_comments_for_Beta_and_Release>:

1. User impact if declined.
2. Automated test coverage on the target branch.
3. Verified in Nightly.
4. Needs manual QE test.
5. Other uplifts needed.
6. Risk (Low / Medium / High).
7. Why risky / not risky.
8. String changes.
9. Android affected.

For sec-\* bugs, the **User impact if declined** field explicitly names
the sec rating and concrete security consequence — sec-approval has
already gated that content, and release drivers need the severity to
sign off. Other fields stay sanitized (no function names, no line
numbers).

### Output

- An on-disk draft at `uplift-request-bug-<bug_id>.md` in the repo root.
- One block per distinct patch variant (channels that share a patch are
  grouped into one block).
- Optionally uploads a raw patch, posts the comment, and sets
  `approval-mozilla-{beta,release,esrNN}?` flags on the chosen attachment
  in a single atomic API call (always previewed via `--dry-run` first).
