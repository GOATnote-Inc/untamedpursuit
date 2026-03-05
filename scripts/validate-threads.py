#!/usr/bin/env python3
"""
Validate thread tracking across chapter frontmatter and open-threads.md.

Checks:
  - Thread coverage matrix: which threads are advanced/introduced in which chapters
  - Orphan threads: threads in frontmatter not found in open-threads.md (and vice versa)
  - Staleness: threads not advanced in N consecutive chapters

Usage:
    python scripts/validate-threads.py          # validate all books with chapters
    python scripts/validate-threads.py 1        # validate book 1 only
    python scripts/validate-threads.py --stale 5  # flag threads stale after 5 chapters (default: 4)
"""

import glob
import os
import re
import sys

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CHAPTERS_GLOB = os.path.join(REPO_ROOT, "books", "book-{book:02d}", "chapters", "ch-*.md")
THREADS_PATH = os.path.join(REPO_ROOT, "bible", "mysteries", "open-threads.md")


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


def normalize_thread_name(raw):
    """Extract the core thread name from a frontmatter thread string.

    Frontmatter entries often look like:
      "Anti-trafficking campaign (Wallace escalates from...)"
    We want: "Anti-trafficking campaign"
    """
    # Take everything before the first parenthetical
    name = re.split(r"\s*\(", raw, maxsplit=1)[0].strip()
    # Also strip trailing punctuation/whitespace
    name = name.rstrip(" —-")
    return name


def parse_open_threads():
    """Parse open-threads.md for thread names and statuses."""
    if not os.path.exists(THREADS_PATH):
        return {}

    with open(THREADS_PATH, "r", encoding="utf-8") as f:
        content = f.read()

    threads = {}
    current_name = None

    for line in content.splitlines():
        heading_m = re.match(r"^### \d+\.\s+(.+?)(?:\s*—\s*.+)?$", line)
        if heading_m:
            current_name = heading_m.group(1).strip()
            threads[current_name] = {"status": "unknown", "line": line}
            continue

        status_m = re.match(r"^\s*-\s+\*\*Status\*\*:\s*(.+)$", line)
        if status_m and current_name:
            raw_status = status_m.group(1).strip()
            if "→" in raw_status:
                raw_status = raw_status.split("→")[-1].strip()
            threads[current_name]["status"] = raw_status
            current_name = None

    return threads


def find_best_match(name, candidates):
    """Find the best matching thread name from candidates using substring matching."""
    name_lower = name.lower()
    for candidate in candidates:
        if candidate.lower() in name_lower or name_lower in candidate.lower():
            return candidate
    # Try word overlap
    name_words = set(name_lower.split())
    best_score = 0
    best_match = None
    for candidate in candidates:
        cand_words = set(candidate.lower().split())
        overlap = len(name_words & cand_words)
        if overlap > best_score and overlap >= 2:
            best_score = overlap
            best_match = candidate
    return best_match


def validate_book(book_num, stale_threshold):
    """Validate threads for a single book."""
    pattern = os.path.join(
        REPO_ROOT, "books", f"book-{book_num:02d}", "chapters", "ch-*.md"
    )
    chapter_files = sorted(glob.glob(pattern))
    if not chapter_files:
        return None

    # Parse all chapters
    chapters = []
    for path in chapter_files:
        fm = parse_frontmatter(path)
        if fm and "chapter" in fm:
            chapters.append(fm)
    chapters.sort(key=lambda c: c["chapter"])

    if not chapters:
        return None

    # Collect all thread names from frontmatter
    fm_threads = {}  # normalized_name -> {introduced: [ch], advanced: [ch]}
    for ch in chapters:
        ch_num = ch["chapter"]
        for raw in ch.get("threads_introduced", []):
            name = normalize_thread_name(raw)
            if name not in fm_threads:
                fm_threads[name] = {"introduced": [], "advanced": []}
            fm_threads[name]["introduced"].append(ch_num)
        for raw in ch.get("threads_advanced", []):
            name = normalize_thread_name(raw)
            if name not in fm_threads:
                fm_threads[name] = {"introduced": [], "advanced": []}
            fm_threads[name]["advanced"].append(ch_num)

    # Parse open-threads.md
    ot_threads = parse_open_threads()

    # Build coverage matrix
    all_ch_nums = [ch["chapter"] for ch in chapters]

    # Match frontmatter threads to open-threads
    matched = {}  # fm_name -> ot_name
    unmatched_fm = []
    for fm_name in fm_threads:
        match = find_best_match(fm_name, ot_threads.keys())
        if match:
            matched[fm_name] = match
        else:
            unmatched_fm.append(fm_name)

    # Find open-threads not referenced in frontmatter
    referenced_ot = set(matched.values())
    unmatched_ot = [
        name
        for name in ot_threads
        if name not in referenced_ot and ot_threads[name]["status"] not in ("resolved", "abandoned")
    ]

    # Staleness check
    stale = []
    for fm_name, data in fm_threads.items():
        all_appearances = sorted(set(data["introduced"] + data["advanced"]))
        if all_appearances:
            last_seen = max(all_appearances)
            max_ch = max(all_ch_nums)
            gap = max_ch - last_seen
            if gap >= stale_threshold:
                stale.append((fm_name, last_seen, gap))

    return {
        "book": book_num,
        "chapters": all_ch_nums,
        "fm_threads": fm_threads,
        "ot_threads": ot_threads,
        "matched": matched,
        "unmatched_fm": unmatched_fm,
        "unmatched_ot": unmatched_ot,
        "stale": stale,
    }


def print_report(result, stale_threshold):
    """Print the validation report for a single book."""
    book = result["book"]
    chapters = result["chapters"]
    fm_threads = result["fm_threads"]
    matched = result["matched"]
    unmatched_fm = result["unmatched_fm"]
    unmatched_ot = result["unmatched_ot"]
    stale = result["stale"]

    print(f"\n{'='*60}")
    print(f"Thread Validation — Book {book}")
    print(f"{'='*60}")
    print(f"Chapters: {min(chapters)}–{max(chapters)} ({len(chapters)} total)")
    print(f"Threads in frontmatter: {len(fm_threads)}")
    print(f"Threads in open-threads.md: {len(result['ot_threads'])}")
    print(f"Matched: {len(matched)}")
    print()

    # Coverage matrix
    print("THREAD COVERAGE MATRIX")
    print("-" * 60)
    for fm_name in sorted(fm_threads.keys()):
        data = fm_threads[fm_name]
        ot_name = matched.get(fm_name, "")
        status = ""
        if ot_name and ot_name in result["ot_threads"]:
            status = f" [{result['ot_threads'][ot_name]['status']}]"

        intro_chs = ", ".join(str(c) for c in data["introduced"])
        adv_chs = ", ".join(str(c) for c in data["advanced"])

        display_name = fm_name[:45]
        print(f"  {display_name}{status}")
        if intro_chs:
            print(f"    Introduced: ch-{intro_chs}")
        if adv_chs:
            print(f"    Advanced:   ch-{adv_chs}")
        print()

    # Orphans
    if unmatched_fm:
        print("ORPHAN THREADS (in frontmatter, not in open-threads.md)")
        print("-" * 60)
        for name in sorted(unmatched_fm):
            print(f"  - {name}")
        print()

    if unmatched_ot:
        print("ORPHAN THREADS (in open-threads.md, not in frontmatter)")
        print("-" * 60)
        for name in sorted(unmatched_ot):
            status = result["ot_threads"][name]["status"]
            print(f"  - {name} [{status}]")
        print()

    # Staleness
    if stale:
        print(f"STALE THREADS (not seen in {stale_threshold}+ chapters)")
        print("-" * 60)
        for name, last_seen, gap in sorted(stale, key=lambda x: -x[2]):
            print(f"  - {name}: last seen ch-{last_seen} ({gap} chapters ago)")
        print()

    # Summary
    issues = len(unmatched_fm) + len(unmatched_ot) + len(stale)
    if issues == 0:
        print("No issues found.")
    else:
        print(f"TOTAL ISSUES: {issues}")
        if unmatched_fm:
            print(f"  {len(unmatched_fm)} orphan thread(s) in frontmatter")
        if unmatched_ot:
            print(f"  {len(unmatched_ot)} orphan thread(s) in open-threads.md")
        if stale:
            print(f"  {len(stale)} stale thread(s)")


def main():
    args = sys.argv[1:]
    stale_threshold = 4
    book_filter = None

    i = 0
    while i < len(args):
        if args[i] == "--stale" and i + 1 < len(args):
            stale_threshold = int(args[i + 1])
            i += 2
        elif args[i].isdigit():
            book_filter = int(args[i])
            i += 1
        else:
            i += 1

    if book_filter:
        books = [book_filter]
    else:
        # Find all books with chapters
        all_patterns = sorted(
            glob.glob(os.path.join(REPO_ROOT, "books", "book-*", "chapters", "ch-*.md"))
        )
        books = sorted(
            set(
                int(re.search(r"book-(\d+)", p).group(1))
                for p in all_patterns
                if re.search(r"book-(\d+)", p)
            )
        )

    if not books:
        print("No books with chapters found.")
        sys.exit(1)

    for book_num in books:
        result = validate_book(book_num, stale_threshold)
        if result:
            print_report(result, stale_threshold)


if __name__ == "__main__":
    main()
