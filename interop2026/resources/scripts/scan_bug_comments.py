#!/usr/bin/env python3
"""
Scan Bugzilla comments for tracked bugs and surface external links not yet
recorded in test-annotations.json.

Scans for:
  - GitHub w3c links     (github.com/w3c/...)
  - GitHub WPT links     (github.com/web-platform-tests/wpt/...)

Outputs a diff: items found in comments that are NOT already known in
test-annotations.json (_github_issues + spec_issue/wpt_issue fields).

Usage:
    python3 scan_bug_comments.py [--annotations PATH] [--delay SECONDS]

Requirements: Python 3.8+, no third-party deps
"""

import argparse
import json
import re
import ssl
import sys
import time
import urllib.request
from collections import defaultdict
from pathlib import Path

ANNOTATIONS_DEFAULT = Path(__file__).parent.parent / "test-annotations.json"

BUGZILLA_COMMENT_URL = "https://bugzilla.mozilla.org/rest/bug/{id}/comment"

# Patterns to scan for in comment text
RE_W3C = re.compile(
    r"https?://github\.com/(w3c/[^\s\)\]\">]+)", re.IGNORECASE
)
RE_WPT = re.compile(
    r"https?://github\.com/(web-platform-tests/wpt[^\s\)\]\">]*)", re.IGNORECASE
)


def load_annotations(path: Path) -> dict:
    with open(path) as f:
        return json.load(f)


def extract_known_github(annotations: dict) -> set:
    """Return set of known github paths, e.g. 'w3c/webrtc-pc/issues/2899'."""
    known_github = set()

    for key, val in annotations.items():
        if key.startswith("_"):
            continue
        for field in ("spec_issue", "wpt_issue"):
            url = val.get(field, "")
            if url:
                m = re.search(r"github\.com/(.+)", url)
                if m:
                    known_github.add(m.group(1).rstrip("/"))

    for repo, issues in annotations.get("_github_issues", {}).items():
        for issue_num in issues:
            known_github.add(f"{repo}/issues/{issue_num}")

    # also pull from _gap_analysis if present
    for item in annotations.get("_gap_analysis", {}).get("comment_scan", []):
        url = item.get("url", "")
        if url:
            m = re.search(r"github\.com/(.+)", url)
            if m:
                known_github.add(m.group(1).rstrip("/").split("#")[0])

    return known_github


def all_tracked_bugs(annotations: dict) -> set:
    bugs = set()
    for key, val in annotations.items():
        if key.startswith("_"):
            continue
        for bug_id in val.get("bugs", []):
            bugs.add(int(bug_id))
    return bugs


def _ssl_context():
    """Return an SSL context, trying system certs then certifi then unverified."""
    try:
        ctx = ssl.create_default_context()
        # macOS: try loading the system keychain certs via certifi if available
        try:
            import certifi
            ctx = ssl.create_default_context(cafile=certifi.where())
        except ImportError:
            pass
        return ctx
    except Exception:
        return ssl._create_unverified_context()


_CTX = _ssl_context()


def fetch_comments(bug_id: int) -> list[dict]:
    url = BUGZILLA_COMMENT_URL.format(id=bug_id)
    try:
        with urllib.request.urlopen(url, timeout=30, context=_CTX) as resp:
            data = json.loads(resp.read().decode())
        return data.get("bugs", {}).get(str(bug_id), {}).get("comments", [])
    except Exception as e:
        print(f"  WARNING: could not fetch bug {bug_id}: {e}", file=sys.stderr)
        return []


def normalise_github_path(raw: str) -> str:
    """Strip trailing punctuation, markdown closers, and fragment anchors."""
    raw = raw.rstrip(".,;:!?)")
    raw = re.sub(r"[)\]]+$", "", raw)
    # strip fragment (e.g. #issuecomment-123) — kept for display but stripped
    # for deduplication purposes separately
    return raw


def base_github_path(path: str) -> str:
    """Return path without fragment anchor, for known-link comparison."""
    return path.split("#")[0]


def scan_text(text: str) -> dict:
    """Return dict of {w3c: [...], wpt: [...]} found in text."""
    results = {"w3c": [], "wpt": []}

    for m in RE_W3C.finditer(text):
        path = normalise_github_path(m.group(1))
        # exclude WPT repo (handled separately)
        if not path.startswith("web-platform-tests"):
            results["w3c"].append(path)

    for m in RE_WPT.finditer(text):
        path = normalise_github_path(m.group(1))
        results["wpt"].append(path)

    return results


def classify_github(path: str) -> str:
    """Return a short human-readable label for a github path."""
    if "/issues/" in path:
        return "issue"
    if "/pull/" in path:
        return "PR"
    if "/commit/" in path:
        return "commit"
    return "link"


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--annotations",
        default=str(ANNOTATIONS_DEFAULT),
        help="Path to test-annotations.json",
    )
    parser.add_argument(
        "--delay",
        type=float,
        default=0.5,
        help="Seconds to wait between Bugzilla API calls (default: 0.5)",
    )
    parser.add_argument(
        "--include-known",
        action="store_true",
        help="Also show already-known links (for verification)",
    )
    args = parser.parse_args()

    annotations_path = Path(args.annotations)
    print(f"Loading annotations from {annotations_path}", file=sys.stderr)
    annotations = load_annotations(annotations_path)

    known_github = extract_known_github(annotations)
    tracked_bugs = all_tracked_bugs(annotations)

    print(
        f"Tracking {len(tracked_bugs)} bugs, "
        f"{len(known_github)} known GitHub links",
        file=sys.stderr,
    )
    print(f"Scanning comments for {len(tracked_bugs)} bugs...\n", file=sys.stderr)

    # Maps bug_id → {w3c: set, wpt: set, bugs: set}
    found: dict[int, dict] = {}

    for i, bug_id in enumerate(sorted(tracked_bugs), 1):
        print(f"  [{i}/{len(tracked_bugs)}] bug {bug_id}...", file=sys.stderr, end=" ")
        comments = fetch_comments(bug_id)
        print(f"{len(comments)} comments", file=sys.stderr)

        agg = {"w3c": set(), "wpt": set()}
        for comment in comments:
            text = comment.get("text", "")
            hits = scan_text(text)
            agg["w3c"].update(hits["w3c"])
            agg["wpt"].update(hits["wpt"])

        found[bug_id] = agg

        if i < len(tracked_bugs):
            time.sleep(args.delay)

    # ── Build the diff report ──────────────────────────────────────────────

    # Collect new GitHub links: path → set of bug IDs that mention it
    new_w3c: dict[str, set] = defaultdict(set)
    new_wpt: dict[str, set] = defaultdict(set)
    already_w3c: dict[str, set] = defaultdict(set)
    already_wpt: dict[str, set] = defaultdict(set)

    for bug_id, agg in found.items():
        for path in agg["w3c"]:
            base = base_github_path(path)
            is_known = any(
                base == k or base.startswith(k + "/") or k.startswith(base + "/")
                for k in known_github
            )
            if is_known:
                already_w3c[path].add(bug_id)
            else:
                new_w3c[path].add(bug_id)

        for path in agg["wpt"]:
            base = base_github_path(path)
            is_known = any(
                base == k or base.startswith(k + "/") or k.startswith(base + "/")
                for k in known_github
            )
            if is_known:
                already_wpt[path].add(bug_id)
            else:
                new_wpt[path].add(bug_id)

    # ── Print results ──────────────────────────────────────────────────────

    def gh_url(path):
        return f"https://github.com/{path}"

    def source_list(bug_set):
        return ", ".join(f"bug {b}" for b in sorted(bug_set))

    any_new = new_w3c or new_wpt

    print("=" * 72)
    print("SCAN RESULTS — Bugzilla comment scan for Interop 2026 WebRTC")
    print("=" * 72)

    # ── New w3c links ──────────────────────────────────────────────────────
    print(f"\n── NEW w3c GitHub links ({len(new_w3c)}) ──")
    if new_w3c:
        for path in sorted(new_w3c):
            sources = source_list(new_w3c[path])
            kind = classify_github(path)
            print(f"  [{kind}] {gh_url(path)}")
            print(f"          mentioned in: {sources}")
    else:
        print("  (none)")

    # ── New WPT links ──────────────────────────────────────────────────────
    print(f"\n── NEW web-platform-tests/wpt links ({len(new_wpt)}) ──")
    if new_wpt:
        for path in sorted(new_wpt):
            sources = source_list(new_wpt[path])
            kind = classify_github(path)
            print(f"  [{kind}] {gh_url(path)}")
            print(f"          mentioned in: {sources}")
    else:
        print("  (none)")

    # ── Already-known links (optional) ────────────────────────────────────
    if args.include_known:
        print(f"\n── Already-known w3c links ({len(already_w3c)}) ──")
        for path in sorted(already_w3c):
            print(f"  {gh_url(path)}  ← {source_list(already_w3c[path])}")

        print(f"\n── Already-known WPT links ({len(already_wpt)}) ──")
        for path in sorted(already_wpt):
            print(f"  {gh_url(path)}  ← {source_list(already_wpt[path])}")

    print()
    if any_new:
        total_new = len(new_w3c) + len(new_wpt)
        print(f"SUMMARY: {total_new} new items found across all categories.")
    else:
        print("SUMMARY: No new items found — annotations are up to date.")


if __name__ == "__main__":
    main()
