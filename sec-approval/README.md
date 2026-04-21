## sec-approval

Prepare a Firefox security approval request from a local patch. Runs a
compliance audit against the
[Fixing Security Bugs](https://firefox-source-docs.mozilla.org/bug-mgmt/processes/fixing-security-bugs.html)
guidelines (commit messages, code comments, identifiers, tests, Try push),
then drafts the eight-question
[sec-approval](https://firefox-source-docs.mozilla.org/bug-mgmt/processes/security-approval.html)
questionnaire — optionally posting the comment and setting `sec-approval?`
on the right Phabricator attachment.

### Usage

```
/sec-approval                        # infer bug id from local patch; ask if ambiguous
/sec-approval 1234567                # explicit bug id
/sec-approval 1234567 /tmp/bug-1234567  # pre-fetched bmo-to-md report
```

### Dependencies

1. **[bmo-to-md](https://github.com/padenot/bmo-to-md)** — downloads
   security-restricted bugs as Markdown. The MCP Bugzilla tool cannot read
   `sec-*` bugs, so this CLI is required for any bug fetch step.

   ```bash
   cargo install bmo-to-md
   ```

2. **`bmo-sec-approval` script** — ships with this skill; used for the
   auth check, listing Phabricator attachments on the bug, and posting the
   request. Requires Python 3.8+ (stdlib only, no extra packages).

### Bugzilla API key setup

A Bugzilla API key is needed for two operations:

- Fetching `sec-*` bugs via `bmo-to-md`.
- Listing attachments and posting the sec-approval comment via
  `bmo-sec-approval`.

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
python3 .claude/skills/sec-approval/bmo-sec-approval --check-auth
```

### What the questionnaire covers

The drafted comment follows the exact format Bugzilla auto-generates for
sec-approval requests, answering:

1. Exploit difficulty given the patch.
2. Whether comments, commit messages, or tests paint a bulls-eye.
3. Affected branches (Nightly / Beta / Release / ESR) — reachability is
   checked per branch against pref/flag gates.
4. Regressing bug, if not all branches are affected.
5. Backport availability.
6. Backport risk.
7. Regression risk and testing needs.
8. Landing readiness and Android impact.

### Output

- An on-disk draft at `sec-approval-bug-<bug_id>.md` in the repo root.
- Optionally posts the comment to Bugzilla and sets `sec-approval?` on the
  chosen Phabricator attachment (always previewed via `--dry-run` first).
