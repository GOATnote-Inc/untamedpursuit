#!/usr/bin/env python3
"""
Compile individual chapter files into a single readable markdown file per book.

Output: books/book-NN/book.md — a reading-format file with linked TOC,
chapter prose, and generation timestamp. Never edited directly; rebuilt
from chapter sources on demand.

Usage:
    python3 scripts/compile-book.py 1          # compile book 1
    python3 scripts/compile-book.py 1 2        # compile books 1 and 2
    python3 scripts/compile-book.py --all      # compile all books with chapters
"""

import glob
import os
import re
import sys
from datetime import date

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

BOOK_TITLES = {
    1: "Fortune's Tide",
    2: "The Golden Shore",
}


def parse_frontmatter(filepath):
    """Extract YAML frontmatter fields from a chapter file."""
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()

    match = re.match(r"^---\n(.*?\n)---", content, re.DOTALL)
    if not match:
        return None

    fm = {}
    for line in match.group(1).splitlines():
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


def read_chapter_text(filepath):
    """Read chapter text (everything after frontmatter)."""
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()
    match = re.match(r"^---\n.*?\n---\n*", content, re.DOTALL)
    if match:
        return content[match.end():]
    return content


def get_book_title(book_num):
    """Get the book title, falling back to CLAUDE.md heading then 'Book N'."""
    if book_num in BOOK_TITLES:
        return BOOK_TITLES[book_num]
    claude_path = os.path.join(
        REPO_ROOT, "books", f"book-{book_num:02d}", "CLAUDE.md"
    )
    if os.path.exists(claude_path):
        with open(claude_path, "r", encoding="utf-8") as f:
            first_line = f.readline().strip()
        m = re.match(r"^#\s+Book\s+\d+\s*[—–-]\s*(.+)$", first_line)
        if m:
            return m.group(1).strip()
    return f"Book {book_num}"


def make_anchor(text):
    """Generate GitHub-compatible anchor from heading text."""
    text = text.lower()
    text = re.sub(r"[^a-z0-9\s-]", "", text)
    text = re.sub(r"\s+", "-", text.strip())
    return text


def compile_book(book_num):
    """Compile all chapters of a book into books/book-NN/book.md."""
    pattern = os.path.join(
        REPO_ROOT, "books", f"book-{book_num:02d}", "chapters", "ch-*.md"
    )
    chapter_files = sorted(glob.glob(pattern))

    if not chapter_files:
        print(f"No chapters found for book {book_num}.")
        return False

    chapters = []
    for path in chapter_files:
        fm = parse_frontmatter(path)
        if fm and "chapter" in fm:
            text = read_chapter_text(path)
            chapters.append({"fm": fm, "text": text})
    chapters.sort(key=lambda c: c["fm"]["chapter"])

    if not chapters:
        print(f"No valid chapters found for book {book_num}.")
        return False

    title = get_book_title(book_num)
    total_words = sum(c["fm"].get("word_count", 0) for c in chapters)
    ch_count = len(chapters)

    lines = []

    # Book heading
    lines.append(f"# {title}")
    lines.append("")
    lines.append(f"**Untamed Pursuit** \u2014 Book {book_num}")
    lines.append("")
    lines.append(f"*{ch_count} chapters \u00b7 ~{total_words:,} words*")
    lines.append("")
    lines.append("---")
    lines.append("")

    # Table of contents
    lines.append("## Contents")
    lines.append("")
    for c in chapters:
        ch_num = c["fm"]["chapter"]
        ch_title = c["fm"].get("title", f"Chapter {ch_num}")
        anchor = make_anchor(f"Chapter {ch_num}: {ch_title}")
        lines.append(f"{ch_num}. [{ch_title}](#{anchor})")
    lines.append("")
    lines.append("---")

    # Chapter content
    for c in chapters:
        text = c["text"]
        # Source chapters use # (own document); compiled uses ## (book is the document)
        text = re.sub(r"^# Chapter", "## Chapter", text, count=1)
        lines.append("")
        lines.append(text.rstrip())
        lines.append("")
        lines.append("---")

    # Footer
    lines.append("")
    lines.append(f"*Compiled from chapter sources on {date.today().isoformat()}*")
    lines.append("")

    out_path = os.path.join(REPO_ROOT, "books", f"book-{book_num:02d}", "book.md")
    with open(out_path, "w", encoding="utf-8") as f:
        f.write("\n".join(lines))

    print(f"Book {book_num}: {ch_count} chapters, ~{total_words:,} words \u2192 {out_path}")
    return True


def find_books_with_chapters():
    """Find all book numbers that have chapter files."""
    pattern = os.path.join(REPO_ROOT, "books", "book-*", "chapters", "ch-*.md")
    book_nums = set()
    for path in glob.glob(pattern):
        m = re.search(r"book-(\d+)", path)
        if m:
            book_nums.add(int(m.group(1)))
    return sorted(book_nums)


def main():
    if len(sys.argv) < 2:
        print("Usage: python3 scripts/compile-book.py <book_num> [book_num ...] | --all")
        sys.exit(1)

    if "--all" in sys.argv:
        book_nums = find_books_with_chapters()
        if not book_nums:
            print("No books with chapters found.")
            sys.exit(1)
    else:
        book_nums = []
        for arg in sys.argv[1:]:
            if arg.isdigit():
                book_nums.append(int(arg))
            else:
                print(f"Invalid argument: {arg}")
                sys.exit(1)

    success = 0
    for bn in book_nums:
        if compile_book(bn):
            success += 1

    if success == 0:
        sys.exit(1)


if __name__ == "__main__":
    main()
