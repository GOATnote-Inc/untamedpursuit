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

TOTAL_BOOKS = 9
ESTIMATED_TOTAL_WORDS = 500_000

STATUS_ORDER = ["Planted", "Developing", "Partially resolved", "Resolved", "Subverted"]

# Series metadata for books without chapters yet
SERIES_INFO = [
    {"books": "1", "title": "Fortune's Tide", "era": "Era 1", "setting": "Philadelphia, ~1846"},
    {"books": "2", "title": "*(TBD)*", "era": "Era 1", "setting": "The Voyage West"},
    {"books": "3\u20134", "title": "*(TBD)*", "era": "Era 1", "setting": "Building the Network"},
    {"books": "5\u20139", "title": "*(TBD)*", "era": "Era 2", "setting": "FIERCE \u2014 Eve's Story"},
]


def replace_between_markers(text, start_marker, end_marker, content):
    """Replace content between start and end markers, preserving the markers."""
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
    """Count chapter headings (## or ###) in a book's outline.md."""
    outline_path = os.path.join(
        REPO_ROOT, "books", f"book-{book_num:02d}", "outline.md"
    )
    if not os.path.exists(outline_path):
        return 0
    with open(outline_path, "r", encoding="utf-8") as f:
        text = f.read()
    return len(re.findall(r"^#{2,3} Chapter", text, re.MULTILINE))


def format_number(n):
    """Format an integer with commas: 3088 -> '3,088'."""
    return f"{n:,}"


def round_to_10(n):
    """Round to nearest 10."""
    return round(n / 10) * 10


def _first_name(pov):
    """Extract first name from a POV string like 'Clara Chen' -> 'Clara'."""
    return pov.split()[0] if pov else pov


def _normalize_status(raw):
    """Collapse 'developing (book 2)' -> 'Developing'."""
    base = re.sub(r'\s*\(.*?\)\s*$', '', raw).strip()
    return base.capitalize()


def _extract_book_ch_refs(text):
    """Extract all (book, chapter) tuples from text containing 'book-NN, ch-NN'."""
    refs = []
    for m in re.finditer(r'book-(\d+),?\s*ch-(\d+)', text, re.IGNORECASE):
        refs.append((int(m.group(1)), int(m.group(2))))
    return refs


def _format_ref(book, ch):
    """Format a (book, chapter) tuple as 'Book 1, Ch 2'."""
    return f"Book {book}, Ch {ch}"


def _planned_books_label(chapters_by_book):
    """Return label like '3-9' for books without chapters yet."""
    active = set(chapters_by_book.keys())
    planned = [b for b in range(1, TOTAL_BOOKS + 1) if b not in active]
    if not planned:
        return None
    if len(planned) == 1:
        return str(planned[0])
    return f"{planned[0]}-{planned[-1]}"


def parse_open_threads():
    """Parse bible/mysteries/open-threads.md for all numbered threads with Status fields.

    Scans the entire file for ### N. headings. Skips entries without a Status
    field (Potential Threads) and explicitly abandoned entries.
    Returns [{"name": str, "status": str, "raw_planted": str, "clues": [(book, ch)]}].
    """
    if not os.path.exists(THREADS_PATH):
        return []

    with open(THREADS_PATH, "r", encoding="utf-8") as f:
        content = f.read()

    threads = []
    # Split into sections by ### N. headings
    sections = re.split(r'(?=^### \d+\.)', content, flags=re.MULTILINE)

    for section in sections:
        heading_m = re.match(r'^### \d+\.\s+(.+?)(?:\s*\u2014\s*.+)?$', section, re.MULTILINE)
        if not heading_m:
            continue

        name = heading_m.group(1).strip()

        # Extract status
        status_m = re.search(r'^\s*-\s+\*\*Status\*\*:\s*(.+)$', section, re.MULTILINE)
        if not status_m:
            continue

        raw_status = status_m.group(1).strip()
        # Handle arrow notation — take final value
        if "\u2192" in raw_status:
            raw_status = raw_status.split("\u2192")[-1].strip()
        elif "->" in raw_status:
            raw_status = raw_status.split("->")[-1].strip()

        # Skip abandoned
        if 'abandoned' in raw_status.lower():
            continue

        # Extract planted line
        planted_m = re.search(r'^\s*-\s+\*\*Planted\*\*:\s*(.+)$', section, re.MULTILINE)
        raw_planted = planted_m.group(1).strip() if planted_m else ""

        # Extract clue references from "Clues given so far" bullets
        clues = []
        clue_section = re.search(
            r'\*\*Clues given so far\*\*:\s*\n((?:\s+-\s+.*\n?)*)', section
        )
        if clue_section:
            for line in clue_section.group(1).splitlines():
                refs = _extract_book_ch_refs(line)
                clues.extend(refs)

        threads.append({
            "name": name,
            "status": raw_status,
            "raw_planted": raw_planted,
            "clues": clues,
        })

    return threads


def generate_metrics(chapters_by_book):
    """Generate Series Dashboard with text progress bar and per-book table."""
    all_chapters = [ch for chs in chapters_by_book.values() for ch in chs]
    if not all_chapters:
        return ""

    total_chapters = len(all_chapters)
    total_words = sum(ch.get("word_count", 0) for ch in all_chapters)
    avg_words = total_words // total_chapters if total_chapters else 0
    books_in_progress = len(chapters_by_book)
    pct = round(100 * total_words / ESTIMATED_TOTAL_WORDS)

    lines = []
    lines.append("")
    lines.append("### Series Dashboard")
    lines.append("")

    # Summary line
    lines.append(
        f"**{TOTAL_BOOKS} books planned** \u00b7 "
        f"**{books_in_progress} in progress** \u00b7 "
        f"**~{format_number(round_to_10(total_words))} of "
        f"~{format_number(ESTIMATED_TOTAL_WORDS)} estimated words**"
    )
    lines.append("")

    # Text progress bar
    bar_width = 40
    filled = round(bar_width * pct / 100)
    bar = "\u2588" * filled + "\u2591" * (bar_width - filled)
    lines.append("```")
    lines.append("Series Progress")
    lines.append(f"[{bar}] {pct}%")
    lines.append("```")
    lines.append("")

    # Per-book table
    book_nums = sorted(chapters_by_book.keys())
    planned_label = _planned_books_label(chapters_by_book)

    # Header row
    header = "| |"
    separator = "|---|"
    for bn in book_nums:
        header += f" Book {bn} |"
        separator += "---|"
    if planned_label:
        header += f" Books {planned_label} |"
        separator += "---|"

    lines.append(header)
    lines.append(separator)

    # Chapters row
    ch_row = "| **Chapters** |"
    for bn in book_nums:
        ch_count = len(chapters_by_book[bn])
        outlined = count_outlined_chapters(bn)
        if outlined > 0:
            ch_row += f" {ch_count} of {outlined} outlined |"
        else:
            ch_row += f" {ch_count} |"
    if planned_label:
        ch_row += " -- |"
    lines.append(ch_row)

    # Words row
    w_row = "| **Words** |"
    for bn in book_nums:
        book_words = sum(ch.get("word_count", 0) for ch in chapters_by_book[bn])
        w_row += f" {format_number(round_to_10(book_words))} |"
    if planned_label:
        w_row += " -- |"
    lines.append(w_row)

    # POV row
    pov_row = "| **POV** |"
    for bn in book_nums:
        pov_counts = {}
        for ch in chapters_by_book[bn]:
            pov = ch.get("pov", "Unknown")
            first = _first_name(pov)
            pov_counts[first] = pov_counts.get(first, 0) + 1
        pov_parts = [
            f"{name} ({count})"
            for name, count in sorted(pov_counts.items(), key=lambda x: -x[1])
        ]
        pov_row += f" {' \u00b7 '.join(pov_parts)} |"
    if planned_label:
        pov_row += " -- |"
    lines.append(pov_row)

    lines.append("")

    # Footer
    lines.append(
        f"*{total_chapters} chapters \u00b7 "
        f"{format_number(total_words)} words \u00b7 "
        f"{format_number(avg_words)} avg words/chapter*"
    )
    lines.append("")

    return "\n".join(lines)


def generate_threads():
    """Generate Narrative Debt section with summary and thread table."""
    threads = parse_open_threads()
    if not threads:
        return ""

    # Count by normalized status
    status_counts = {}
    for t in threads:
        norm = _normalize_status(t["status"])
        status_counts[norm] = status_counts.get(norm, 0) + 1

    lines = []
    lines.append("")
    lines.append("### Narrative Debt")
    lines.append("")

    # Summary line — ordered by lifecycle stage
    total = len(threads)
    ordered_statuses = sorted(
        status_counts.keys(),
        key=lambda s: STATUS_ORDER.index(s) if s in STATUS_ORDER else 99,
    )
    status_parts = [f"**{status_counts[s]} {s.lower()}**" for s in ordered_statuses]
    lines.append(f"**{total} threads tracked** \u00b7 {' \u00b7 '.join(status_parts)}")
    lines.append("")

    # Thread table
    lines.append("| Thread | Status | Planted | Latest |")
    lines.append("|--------|--------|---------|--------|")

    resolved_count = 0

    for t in threads:
        name = t["name"]
        norm_status = _normalize_status(t["status"])

        if "resolved" in norm_status.lower():
            resolved_count += 1

        # Extract planted reference
        planted_refs = _extract_book_ch_refs(t["raw_planted"])
        if planted_refs:
            planted_str = _format_ref(*planted_refs[0])
        elif t["clues"]:
            planted_str = _format_ref(*t["clues"][0])
        else:
            raw = t["raw_planted"]
            planted_str = (raw[:37] + "...") if len(raw) > 40 else raw if raw else "--"

        # Extract latest reference
        if t["clues"]:
            latest_str = _format_ref(*t["clues"][-1])
        else:
            latest_str = "--"

        lines.append(f"| {name} | {norm_status} | {planted_str} | {latest_str} |")

    lines.append("")

    # Plant-to-resolution ratio
    open_count = total - resolved_count
    lines.append(f"*Plant-to-resolution ratio: {open_count}:{resolved_count}*")
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
                chs = chapters_by_book[book_num]
                ch_count = len(chs)
                outlined = count_outlined_chapters(book_num)
                # Check if all chapters are revised or final
                all_done = all(
                    ch.get("status", "").strip('"') in ("revised", "final")
                    for ch in chs
                )
                if all_done:
                    status = f"Revised \u2014 {ch_count} chapters"
                elif outlined > 0:
                    status = f"Drafting \u2014 {ch_count} of {outlined} chapters"
                else:
                    status = f"Drafting \u2014 {ch_count} chapters"
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
            f"**Book {book_num}: {book_title}** \u2014 [`{book_dir}`]({book_dir})"
        )
        lines.append("")
        book_md_path = os.path.join(
            REPO_ROOT, "books", f"book-{book_num:02d}", "book.md"
        )
        if os.path.exists(book_md_path):
            book_words = sum(ch.get("word_count", 0) for ch in chapters)
            lines.append(
                f"> [Read the full book](books/book-{book_num:02d}/book.md) "
                f"\u00b7 {len(chapters)} chapters "
                f"\u00b7 ~{format_number(round_to_10(book_words))} words"
            )
            lines.append("")
        lines.append("| Ch | Title | POV | Words |")
        lines.append("|---:|-------|-----|------:|")

        book_total = 0
        for ch in chapters:
            ch_num = ch["chapter"]
            title = ch.get("title", f"Chapter {ch_num}")
            pov = ch.get("pov", "\u2014")
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
            f"*Book {book_num}: ~{book_approx} words drafted* \u00b7 *Series total: ~{grand_approx} words*"
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
