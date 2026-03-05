#!/usr/bin/env python3
"""
Update the README.md progress, metrics, and thread-tracking sections
from chapter YAML frontmatter and project data.

Standalone script (stdlib only — no pip dependencies). Does the same job as
the /progress Claude Code skill, useful as a fallback, pre-commit hook, or
future GitHub Action.

Usage:
    python scripts/update-readme.py          # update in place
    python scripts/update-readme.py --check  # exit 1 if README is out of date
"""

import glob
import os
import re
import sys

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
README_PATH = os.path.join(REPO_ROOT, "README.md")
CHAPTERS_GLOB = os.path.join(REPO_ROOT, "books", "book-*", "chapters", "ch-*.md")
THREADS_PATH = os.path.join(REPO_ROOT, "bible", "mysteries", "open-threads.md")

START_MARKER = "<!-- PROGRESS:START -->"
END_MARKER = "<!-- PROGRESS:END -->"
METRICS_START = "<!-- METRICS:START -->"
METRICS_END = "<!-- METRICS:END -->"
THREADS_START = "<!-- THREADS:START -->"
THREADS_END = "<!-- THREADS:END -->"

# Series metadata for books without chapters yet
SERIES_INFO = [
    {"books": "1", "title": "Fortune's Tide", "era": "Era 1", "setting": "Philadelphia, ~1846"},
    {"books": "2", "title": "*(TBD)*", "era": "Era 1", "setting": "The Voyage West"},
    {"books": "3–4", "title": "*(TBD)*", "era": "Era 1", "setting": "Building the Network"},
    {"books": "5–9", "title": "*(TBD)*", "era": "Era 2", "setting": "FIERCE — Eve's Story"},
]


def replace_between_markers(text, start_marker, end_marker, content):
    """Replace content between start and end markers, preserving the markers.

    Returns text unchanged if markers not found (graceful degradation).
    """
    start_idx = text.find(start_marker)
    end_idx = text.find(end_marker)
    if start_idx == -1 or end_idx == -1:
        return text
    before = text[: start_idx + len(start_marker)]
    after = text[end_idx:]
    return before + content + after


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
        # Simple YAML key: value parsing (handles quoted and unquoted strings, numbers)
        m = re.match(r'^(\w+):\s*"?([^"]*?)"?\s*$', line)
        if m:
            key, val = m.group(1), m.group(2)
            if key in ("book", "chapter", "word_count"):
                try:
                    fm[key] = int(val)
                except ValueError:
                    fm[key] = val
            elif key in ("threads_advanced", "threads_introduced", "continuity_flags"):
                # Handle list parsing
                if val == "[]" or val == "":
                    # Check if next lines are list items
                    items = []
                    if val == "":
                        j = i + 1
                        while j < len(lines) and re.match(r'^\s+-\s+', lines[j]):
                            item_m = re.match(r'^\s+-\s+"?([^"]*?)"?\s*$', lines[j])
                            if item_m:
                                items.append(item_m.group(1))
                            j += 1
                        i = j - 1  # will be incremented below
                    fm[key] = items
                else:
                    fm[key] = []
            else:
                fm[key] = val
        elif re.match(r'^(\w+):\s*$', line):
            # Key with no value — check for list items on subsequent lines
            key_m = re.match(r'^(\w+):\s*$', line)
            key = key_m.group(1)
            if key in ("threads_advanced", "threads_introduced", "continuity_flags"):
                items = []
                j = i + 1
                while j < len(lines) and re.match(r'^\s+-\s+', lines[j]):
                    item_m = re.match(r'^\s+-\s+"?([^"]*?)"?\s*$', lines[j])
                    if item_m:
                        items.append(item_m.group(1))
                    j += 1
                fm[key] = items
                i = j - 1  # will be incremented below
        i += 1
    return fm


def count_outlined_chapters(book_num):
    """Count ## Chapter headings in a book's outline.md."""
    outline_path = os.path.join(
        REPO_ROOT, "books", f"book-{book_num:02d}", "outline.md"
    )
    if not os.path.exists(outline_path):
        return 0
    with open(outline_path, "r", encoding="utf-8") as f:
        text = f.read()
    return len(re.findall(r"^## Chapter", text, re.MULTILINE))


def format_number(n):
    """Format an integer with commas: 3088 -> '3,088'."""
    return f"{n:,}"


def round_to_10(n):
    """Round to nearest 10."""
    return round(n / 10) * 10


def parse_open_threads():
    """Parse bible/mysteries/open-threads.md for active thread statuses.

    Returns [{"name": str, "status": str}].
    Only parses the ## Active Threads section (stops at ## Potential Threads).
    Handles arrow notation (developing → resolved → take final value).
    """
    if not os.path.exists(THREADS_PATH):
        return []

    with open(THREADS_PATH, "r", encoding="utf-8") as f:
        content = f.read()

    # Extract only the Active Threads section
    active_match = re.search(
        r"^## Active Threads\s*\n(.*?)(?=^## (?!Active)|\Z)",
        content,
        re.MULTILINE | re.DOTALL,
    )
    if not active_match:
        return []

    active_section = active_match.group(1)
    threads = []
    current_name = None

    for line in active_section.splitlines():
        # Match ### N. Thread Name or ### N. Thread Name — Subtitle
        heading_m = re.match(r"^### \d+\.\s+(.+?)(?:\s*—\s*.+)?$", line)
        if heading_m:
            current_name = heading_m.group(1).strip()
            continue

        # Match - **Status**: value
        status_m = re.match(r"^\s*-\s+\*\*Status\*\*:\s*(.+)$", line)
        if status_m and current_name:
            raw_status = status_m.group(1).strip()
            # Handle arrow notation — take final value
            if "→" in raw_status:
                raw_status = raw_status.split("→")[-1].strip()
            elif "->" in raw_status:
                raw_status = raw_status.split("->")[-1].strip()
            threads.append({"name": current_name, "status": raw_status})
            current_name = None

    return threads


def generate_metrics(chapters_by_book):
    """Generate metrics section with Mermaid pie charts and summary table."""
    all_chapters = [
        ch for chs in chapters_by_book.values() for ch in chs
    ]
    if not all_chapters:
        return ""

    lines = []
    lines.append("")
    lines.append("### Project Metrics")
    lines.append("")

    # --- Status pie chart ---
    status_counts = {}
    for ch in all_chapters:
        s = ch.get("status", "draft")
        status_counts[s] = status_counts.get(s, 0) + 1

    lines.append("**Chapter Status**")
    lines.append("")
    lines.append("```mermaid")
    lines.append("pie title Chapter Status")
    for status, count in sorted(status_counts.items()):
        if count > 0:
            lines.append(f'    "{status.capitalize()}" : {count}')
    lines.append("```")
    lines.append("")

    # --- POV pie chart ---
    pov_counts = {}
    for ch in all_chapters:
        pov = ch.get("pov", "Unknown")
        pov_counts[pov] = pov_counts.get(pov, 0) + 1

    lines.append("**POV Distribution**")
    lines.append("")
    lines.append("```mermaid")
    lines.append("pie title POV Distribution")
    for pov, count in sorted(pov_counts.items()):
        if count > 0:
            lines.append(f'    "{pov}" : {count}')
    lines.append("```")
    lines.append("")

    # --- Summary table ---
    total_chapters = len(all_chapters)
    total_words = sum(ch.get("word_count", 0) for ch in all_chapters)
    avg_words = total_words // total_chapters if total_chapters else 0
    books_count = len(chapters_by_book)

    lines.append("| Metric | Value |")
    lines.append("|--------|------:|")
    lines.append(f"| Books in progress | {books_count} |")
    lines.append(f"| Chapters drafted | {total_chapters} |")
    lines.append(f"| Total words | {format_number(total_words)} |")
    lines.append(f"| Average words/chapter | {format_number(avg_words)} |")

    for status, count in sorted(status_counts.items()):
        pct = round(100 * count / total_chapters)
        lines.append(f"| {status.capitalize()} | {count} ({pct}%) |")

    lines.append("")
    return "\n".join(lines)


def generate_threads():
    """Generate threads section with Mermaid pie chart and summary table."""
    threads = parse_open_threads()
    if not threads:
        return ""

    lines = []
    lines.append("")
    lines.append("### Thread Tracker")
    lines.append("")

    # --- Status pie chart ---
    status_counts = {}
    for t in threads:
        s = t["status"]
        status_counts[s] = status_counts.get(s, 0) + 1

    lines.append("```mermaid")
    lines.append("pie title Active Thread Status")
    for status, count in sorted(status_counts.items()):
        if count > 0:
            lines.append(f'    "{status.capitalize()}" : {count}')
    lines.append("```")
    lines.append("")

    # --- Summary table ---
    lines.append("| Status | Count | Threads |")
    lines.append("|--------|------:|---------|")
    status_groups = {}
    for t in threads:
        status_groups.setdefault(t["status"], []).append(t["name"])
    for status, names in sorted(status_groups.items()):
        truncated = [n[:40] + "..." if len(n) > 40 else n for n in names]
        lines.append(f"| {status.capitalize()} | {len(names)} | {', '.join(truncated)} |")

    lines.append("")
    return "\n".join(lines)


def generate_progress(chapters_by_book):
    """Generate the markdown content between progress markers."""
    lines = []

    # --- Series table ---
    lines.append("")
    lines.append("### The Series")
    lines.append("")
    lines.append("| Book | Title | Era | Setting | Status |")
    lines.append("|---|---|---|---|---|")

    for info in SERIES_INFO:
        book_label = info["books"]
        # Determine if this row covers a single book with chapters
        if book_label.isdigit():
            book_num = int(book_label)
            if book_num in chapters_by_book:
                ch_count = len(chapters_by_book[book_num])
                outlined = count_outlined_chapters(book_num)
                status = f"Drafting — {ch_count} of {outlined} chapters outlined"
            else:
                status = "Planned"
        else:
            status = "Planned"
        lines.append(
            f"| {book_label} | {info['title']} | {info['era']} | {info['setting']} | {status} |"
        )

    # --- Chapter tables ---
    grand_total = 0
    books_with_chapters = sorted(chapters_by_book.keys())

    if books_with_chapters:
        lines.append("")
        lines.append("### Read the Book")
        lines.append("")
        lines.append("The series is free to read. Start here:")

    for book_num in books_with_chapters:
        chapters = sorted(chapters_by_book[book_num], key=lambda c: c["chapter"])

        # Find book title from series info
        book_title = "*(TBD)*"
        for info in SERIES_INFO:
            if info["books"] == str(book_num):
                book_title = info["title"]
                break

        book_dir = f"books/book-{book_num:02d}/chapters/"

        lines.append("")
        lines.append(
            f"**Book {book_num}: {book_title}** — [`{book_dir}`]({book_dir})"
        )
        lines.append("")
        lines.append("| Ch | Title | POV | Words |")
        lines.append("|---:|-------|-----|------:|")

        book_total = 0
        for ch in chapters:
            ch_num = ch["chapter"]
            title = ch.get("title", f"Chapter {ch_num}")
            pov = ch.get("pov", "—")
            wc = ch.get("word_count", 0)
            book_total += wc
            ch_file = f"books/book-{book_num:02d}/chapters/ch-{ch_num:02d}.md"
            lines.append(
                f"| {ch_num} | [{title}]({ch_file}) | {pov} | {format_number(wc)} |"
            )

        grand_total += book_total
        book_approx = format_number(round_to_10(book_total))
        grand_approx = format_number(round_to_10(grand_total))
        lines.append("")
        lines.append(
            f"*Book {book_num}: ~{book_approx} words drafted* · *Series total: ~{grand_approx} words*"
        )

    lines.append("")
    return "\n".join(lines)


def main():
    check_mode = "--check" in sys.argv

    # Scan chapters
    chapter_files = sorted(glob.glob(CHAPTERS_GLOB))
    chapters_by_book = {}
    for path in chapter_files:
        fm = parse_frontmatter(path)
        if fm and "book" in fm and "chapter" in fm:
            chapters_by_book.setdefault(fm["book"], []).append(fm)

    # Generate all sections
    progress_content = generate_progress(chapters_by_book)
    metrics_content = generate_metrics(chapters_by_book)
    threads_content = generate_threads()

    # Read README
    with open(README_PATH, "r", encoding="utf-8") as f:
        readme = f.read()

    # Replace all marker sections
    new_readme = replace_between_markers(readme, START_MARKER, END_MARKER, progress_content)
    new_readme = replace_between_markers(new_readme, METRICS_START, METRICS_END, metrics_content)
    new_readme = replace_between_markers(new_readme, THREADS_START, THREADS_END, threads_content)

    if check_mode:
        if new_readme != readme:
            print("README.md is out of date. Run: python scripts/update-readme.py")
            sys.exit(1)
        else:
            print("README.md is up to date.")
            sys.exit(0)

    if new_readme == readme:
        print("README.md is already up to date. No changes made.")
    else:
        with open(README_PATH, "w", encoding="utf-8") as f:
            f.write(new_readme)
        print("README.md updated.")

    # Summary
    total_chapters = sum(len(chs) for chs in chapters_by_book.values())
    total_words = sum(
        ch.get("word_count", 0)
        for chs in chapters_by_book.values()
        for ch in chs
    )
    print(f"  Books with chapters: {len(chapters_by_book)}")
    print(f"  Total chapters: {total_chapters}")
    print(f"  Total words: {format_number(total_words)}")


if __name__ == "__main__":
    main()
