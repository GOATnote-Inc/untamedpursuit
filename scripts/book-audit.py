#!/usr/bin/env python3
"""
Cross-chapter audit for a single book.

Validates consistency across all chapters in a book:
  - Character description consistency (repeated descriptors tracked)
  - Timeline sanity (date ordering, gap detection)
  - Thread progression matrix (which threads span which chapters)
  - POV balance (distribution across characters)
  - Word count distribution

Usage:
    python3 scripts/book-audit.py 1          # audit book 1
    python3 scripts/book-audit.py 1 --out    # write to reports/book-01-audit.md
"""

import glob
import os
import re
import sys
from collections import Counter, defaultdict

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def parse_frontmatter(filepath):
    """Extract YAML frontmatter fields from a chapter file."""
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()

    match = re.match(r"^---\n(.*?\n)---", content, re.DOTALL)
    if not match:
        return None

    fm = {}
    lines = match.group(1).splitlines()
    i = 0
    while i < len(lines):
        line = lines[i]
        m = re.match(r'^(\w+):\s*"?([^"]*?)"?\s*$', line)
        if m:
            key, val = m.group(1), m.group(2)
            if key in ("book", "chapter", "word_count"):
                try:
                    fm[key] = int(val)
                except ValueError:
                    fm[key] = val
            elif key in ("threads_advanced", "threads_introduced", "continuity_flags"):
                if val == "[]" or val == "":
                    items = []
                    if val == "":
                        j = i + 1
                        while j < len(lines) and re.match(r"^\s+-\s+", lines[j]):
                            item_m = re.match(r'^\s+-\s+"?([^"]*?)"?\s*$', lines[j])
                            if item_m:
                                items.append(item_m.group(1))
                            j += 1
                        i = j - 1
                    fm[key] = items
                else:
                    fm[key] = []
            else:
                fm[key] = val
        elif re.match(r"^(\w+):\s*$", line):
            key_m = re.match(r"^(\w+):\s*$", line)
            key = key_m.group(1)
            if key in ("threads_advanced", "threads_introduced", "continuity_flags"):
                items = []
                j = i + 1
                while j < len(lines) and re.match(r"^\s+-\s+", lines[j]):
                    item_m = re.match(r'^\s+-\s+"?([^"]*?)"?\s*$', lines[j])
                    if item_m:
                        items.append(item_m.group(1))
                    j += 1
                fm[key] = items
                i = j - 1
        i += 1
    return fm


def read_chapter_text(filepath):
    """Read chapter text (everything after frontmatter)."""
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()
    match = re.match(r"^---\n.*?\n---\n*", content, re.DOTALL)
    if match:
        return content[match.end():]
    return content


def normalize_thread_name(raw):
    """Extract core thread name before parenthetical."""
    name = re.split(r"\s*\(", raw, maxsplit=1)[0].strip()
    return name.rstrip(" —-")


# Known character descriptors to track across chapters
CHARACTER_PATTERNS = {
    "Clara": [
        (r"leather coat", "leather coat"),
        (r"sword cane", "sword cane"),
        (r"dark green silk", "dark green silk"),
        (r"holster", "holsters"),
        (r"Colt", "Colts"),
        (r"midnight blue", "midnight blue gown"),
    ],
    "Thomas": [
        (r"silver at (?:his )?temples", "silver at temples"),
        (r"mahogany desk", "mahogany desk"),
        (r"ink on (?:both )?(?:his )?hands", "ink on hands"),
        (r"boyish grin", "boyish grin"),
        (r"grandfather clock", "grandfather clock"),
    ],
    "Samuel": [
        (r"walnut desk", "walnut desk"),
        (r"Front Street", "Front Street warehouse"),
        (r"counting table", "counting table"),
    ],
    "George": [
        (r"140.pound|hundred.and.forty", "140 pounds"),
        (r"muzzle", "muzzle (George)"),
        (r"hand signal|open palm", "hand signals"),
    ],
    "Harper": [
        (r"Miss Chen", "Miss Chen (Harper)"),
        (r"weathered", "weathered (Harper)"),
        (r"pipe tobacco", "pipe tobacco"),
    ],
}

# Timeline parsing patterns
TIMELINE_ORDER = [
    "Autumn 1846",
    "Late Autumn 1846",
    "January 1847",
    "Late March 1847",
    "April 3, 1847",
    "April 3-7, 1847",
    "April 15-16, 1847",
    "April 17-18, 1847",
    "April 22-24, 1847",
    "April 25-26, 1847",
]


def audit_book(book_num):
    """Run all audit checks for a single book."""
    pattern = os.path.join(
        REPO_ROOT, "books", f"book-{book_num:02d}", "chapters", "ch-*.md"
    )
    chapter_files = sorted(glob.glob(pattern))
    if not chapter_files:
        return None

    chapters = []
    for path in chapter_files:
        fm = parse_frontmatter(path)
        if fm and "chapter" in fm:
            fm["_path"] = path
            fm["_text"] = read_chapter_text(path)
            chapters.append(fm)
    chapters.sort(key=lambda c: c["chapter"])

    if not chapters:
        return None

    report = []
    report.append(f"# Book {book_num} — Cross-Chapter Audit")
    report.append("")
    report.append(f"Chapters: {len(chapters)} (ch-{chapters[0]['chapter']:02d} through ch-{chapters[-1]['chapter']:02d})")
    total_words = sum(ch.get("word_count", 0) for ch in chapters)
    report.append(f"Total words: {total_words:,}")
    report.append("")

    # --- 1. POV Balance ---
    report.append("## POV Distribution")
    report.append("")
    pov_counts = Counter(ch.get("pov", "Unknown") for ch in chapters)
    report.append("| POV Character | Chapters | % |")
    report.append("|---------------|----------|---|")
    for pov, count in pov_counts.most_common():
        pct = round(100 * count / len(chapters))
        ch_nums = [str(ch["chapter"]) for ch in chapters if ch.get("pov") == pov]
        report.append(f"| {pov} | {', '.join(ch_nums)} ({count}) | {pct}% |")
    report.append("")

    # --- 2. Word Count Distribution ---
    report.append("## Word Count Distribution")
    report.append("")
    word_counts = [ch.get("word_count", 0) for ch in chapters]
    avg_wc = sum(word_counts) // len(word_counts) if word_counts else 0
    min_wc = min(word_counts) if word_counts else 0
    max_wc = max(word_counts) if word_counts else 0
    report.append(f"- Average: {avg_wc:,} words")
    report.append(f"- Range: {min_wc:,} – {max_wc:,}")
    report.append("")
    # Flag outliers (>1.5x or <0.5x average)
    outliers = []
    for ch in chapters:
        wc = ch.get("word_count", 0)
        if avg_wc > 0 and (wc > avg_wc * 1.5 or wc < avg_wc * 0.5):
            outliers.append((ch["chapter"], wc, "long" if wc > avg_wc else "short"))
    if outliers:
        report.append("**Outliers:**")
        for ch_num, wc, direction in outliers:
            report.append(f"- ch-{ch_num:02d}: {wc:,} words ({direction})")
        report.append("")

    # --- 3. Timeline Sanity ---
    report.append("## Timeline Progression")
    report.append("")
    report.append("| Chapter | Timeline | Location |")
    report.append("|---------|----------|----------|")
    prev_timeline = None
    timeline_issues = []
    for ch in chapters:
        timeline = ch.get("timeline", "—")
        location = ch.get("location", "—")
        marker = ""
        # Check for timeline regression
        if prev_timeline and timeline:
            prev_norm = prev_timeline.replace("\u2013", "-").strip()
            curr_norm = timeline.replace("\u2013", "-").strip()
            # Simple check: if both are in our known order, verify sequence
            prev_idx = next(
                (i for i, t in enumerate(TIMELINE_ORDER) if prev_norm in t or t in prev_norm),
                -1,
            )
            curr_idx = next(
                (i for i, t in enumerate(TIMELINE_ORDER) if curr_norm in t or t in curr_norm),
                -1,
            )
            if prev_idx >= 0 and curr_idx >= 0 and curr_idx < prev_idx:
                marker = " **REGRESSION**"
                timeline_issues.append(
                    f"ch-{ch['chapter']}: '{timeline}' follows '{prev_timeline}'"
                )
        report.append(f"| {ch['chapter']} | {timeline}{marker} | {location[:50]} |")
        prev_timeline = timeline
    report.append("")
    if timeline_issues:
        report.append("**Timeline issues:**")
        for issue in timeline_issues:
            report.append(f"- {issue}")
        report.append("")

    # --- 4. Status Summary ---
    report.append("## Chapter Status")
    report.append("")
    status_counts = Counter(ch.get("status", "unknown") for ch in chapters)
    for status, count in status_counts.most_common():
        ch_nums = [str(ch["chapter"]) for ch in chapters if ch.get("status") == status]
        report.append(f"- **{status}**: {', '.join(ch_nums)} ({count})")
    report.append("")

    # --- 5. Character Description Consistency ---
    report.append("## Character Descriptor Tracking")
    report.append("")
    report.append("Tracks recurring descriptors across chapters to catch drift or contradiction.")
    report.append("")
    for char_name, patterns in CHARACTER_PATTERNS.items():
        char_hits = []
        for regex, label in patterns:
            hit_chapters = []
            for ch in chapters:
                if re.search(regex, ch["_text"], re.IGNORECASE):
                    hit_chapters.append(ch["chapter"])
            if hit_chapters:
                char_hits.append((label, hit_chapters))
        if char_hits:
            report.append(f"### {char_name}")
            report.append("")
            report.append("| Descriptor | Chapters |")
            report.append("|------------|----------|")
            for label, ch_nums in char_hits:
                report.append(f"| {label} | {', '.join(str(c) for c in ch_nums)} |")
            report.append("")

    # --- 6. Thread Progression Matrix ---
    report.append("## Thread Progression")
    report.append("")
    report.append("Major threads (appearing in 3+ chapters):")
    report.append("")
    thread_data = defaultdict(lambda: {"introduced": [], "advanced": []})
    for ch in chapters:
        ch_num = ch["chapter"]
        for raw in ch.get("threads_introduced", []):
            name = normalize_thread_name(raw)
            thread_data[name]["introduced"].append(ch_num)
        for raw in ch.get("threads_advanced", []):
            name = normalize_thread_name(raw)
            thread_data[name]["advanced"].append(ch_num)

    # Filter to threads appearing in 3+ chapters
    major_threads = {
        name: data
        for name, data in thread_data.items()
        if len(data["introduced"]) + len(data["advanced"]) >= 3
    }
    if major_threads:
        report.append("| Thread | Introduced | Advanced | Span |")
        report.append("|--------|-----------|----------|------|")
        for name in sorted(major_threads.keys()):
            data = major_threads[name]
            intro = ", ".join(str(c) for c in data["introduced"]) or "—"
            adv = ", ".join(str(c) for c in data["advanced"]) or "—"
            all_chs = sorted(set(data["introduced"] + data["advanced"]))
            span = f"ch-{min(all_chs)}–{max(all_chs)}" if all_chs else "—"
            display = name[:50]
            report.append(f"| {display} | {intro} | {adv} | {span} |")
        report.append("")

    # --- 7. Continuity Flags ---
    report.append("## Unresolved Continuity Flags")
    report.append("")
    flags_found = False
    for ch in chapters:
        flags = ch.get("continuity_flags", [])
        if flags:
            flags_found = True
            for flag in flags:
                report.append(f"- ch-{ch['chapter']}: {flag}")
    if not flags_found:
        report.append("No unresolved continuity flags in frontmatter.")
    report.append("")

    # --- Summary ---
    issue_count = len(timeline_issues) + len(outliers)
    unresolved_flags = sum(len(ch.get("continuity_flags", [])) for ch in chapters)
    draft_count = status_counts.get("draft", 0)

    report.append("## Summary")
    report.append("")
    report.append(f"- Chapters: {len(chapters)}")
    report.append(f"- Total words: {total_words:,}")
    report.append(f"- POV characters: {len(pov_counts)}")
    report.append(f"- Major threads (3+ chapters): {len(major_threads)}")
    report.append(f"- Timeline issues: {len(timeline_issues)}")
    report.append(f"- Word count outliers: {len(outliers)}")
    report.append(f"- Unresolved continuity flags: {unresolved_flags}")
    report.append(f"- Chapters still in draft: {draft_count}")
    report.append("")

    return "\n".join(report)


def main():
    args = sys.argv[1:]
    if not args or not args[0].isdigit():
        print("Usage: python3 scripts/book-audit.py <book_number> [--out]")
        sys.exit(1)

    book_num = int(args[0])
    write_file = "--out" in args

    report = audit_book(book_num)
    if report is None:
        print(f"No chapters found for book {book_num}.")
        sys.exit(1)

    if write_file:
        out_path = os.path.join(REPO_ROOT, "reports", f"book-{book_num:02d}-audit.md")
        with open(out_path, "w", encoding="utf-8") as f:
            f.write(report)
        print(f"Audit written to {out_path}")
    else:
        print(report)


if __name__ == "__main__":
    main()
