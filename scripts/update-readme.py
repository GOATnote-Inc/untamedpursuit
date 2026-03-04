#!/usr/bin/env python3
"""
Update the README.md progress section from chapter YAML frontmatter.

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

START_MARKER = "<!-- PROGRESS:START -->"
END_MARKER = "<!-- PROGRESS:END -->"

# Series metadata for books without chapters yet
SERIES_INFO = [
    {"books": "1", "title": "Fortune's Tide", "era": "Era 1", "setting": "Philadelphia, ~1846"},
    {"books": "2", "title": "*(TBD)*", "era": "Era 1", "setting": "The Voyage West"},
    {"books": "3–4", "title": "*(TBD)*", "era": "Era 1", "setting": "Building the Network"},
    {"books": "5–9", "title": "*(TBD)*", "era": "Era 2", "setting": "FIERCE — Eve's Story"},
]


def parse_frontmatter(filepath):
    """Extract YAML frontmatter fields from a chapter file."""
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()

    match = re.match(r"^---\n(.*?\n)---", content, re.DOTALL)
    if not match:
        return None

    fm = {}
    for line in match.group(1).splitlines():
        # Simple YAML key: value parsing (handles quoted and unquoted strings, numbers)
        m = re.match(r'^(\w+):\s*"?([^"]*?)"?\s*$', line)
        if m:
            key, val = m.group(1), m.group(2)
            if key in ("book", "chapter", "word_count"):
                try:
                    fm[key] = int(val)
                except ValueError:
                    fm[key] = val
            else:
                fm[key] = val
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

    # Generate progress content
    new_content = generate_progress(chapters_by_book)

    # Read README
    with open(README_PATH, "r", encoding="utf-8") as f:
        readme = f.read()

    # Find markers
    start_idx = readme.find(START_MARKER)
    end_idx = readme.find(END_MARKER)
    if start_idx == -1 or end_idx == -1:
        print("ERROR: Progress markers not found in README.md", file=sys.stderr)
        print(f"  Looking for: {START_MARKER}", file=sys.stderr)
        print(f"  And: {END_MARKER}", file=sys.stderr)
        sys.exit(1)

    # Build new README
    before = readme[: start_idx + len(START_MARKER)]
    after = readme[end_idx:]
    new_readme = before + new_content + after

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
