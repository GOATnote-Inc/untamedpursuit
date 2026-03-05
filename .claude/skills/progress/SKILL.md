---
name: progress
description: Regenerate the README progress section from chapter frontmatter
---

# /progress — Update README Progress Section

Scan all chapter files, extract metadata from YAML frontmatter, and regenerate the progress section of README.md between the `<!-- PROGRESS:START -->` and `<!-- PROGRESS:END -->` markers.

## Step 1: Scan Chapters

1. Glob `books/book-*/chapters/ch-*.md` to find all chapter files across all 9 books
2. For each file, read the YAML frontmatter and extract:
   - `book` (number)
   - `chapter` (number)
   - `title` (string)
   - `pov` (string)
   - `status` (draft | revised | final)
   - `word_count` (number)
3. Group chapters by book number

## Step 2: Count Outlined Chapters

For each book that has chapters, read `books/book-XX/outline.md` and count headings matching `## Chapter` to determine how many chapters are outlined.

## Step 3: Generate the Progress Section

Build the replacement content for between the markers:

### Series Table

```markdown
### The Series

| Book | Title | Era | Setting | Status |
|---|---|---|---|---|
```

For each book with drafted chapters, show: `Drafting — X of Y chapters outlined` where X = chapters with files, Y = outlined chapters.

Use this series data:

| Book | Title | Era | Setting |
|---|---|---|---|
| 1 | Fortune's Tide | Era 1 | Philadelphia, ~1846 |
| 2 | *(TBD)* | Era 1 | The Voyage West |
| 3–4 | *(TBD)* | Era 1 | Building the Network |
| 5–9 | *(TBD)* | Era 2 | FIERCE — Eve's Story |

Books without chapter files show `Planned`.

### Chapter Table

For each book with chapters, generate:

```markdown
### Read the Book

The series is free to read. Start here:

**Book X: [Title]** — [`books/book-XX/chapters/`](books/book-XX/chapters/)

| Ch | Title | POV | Words |
|---:|-------|-----|------:|
| 1 | [Chapter Title](books/book-XX/chapters/ch-01.md) | POV Name | X,XXX |
```

Format word counts with commas (e.g., `3,088`).

After each book's table, add a summary line:
```
*Book X: ~TOTAL words drafted* · *Series total: ~GRAND_TOTAL words*
```

Round totals to nearest 10 for the `~` approximation (e.g., 17,257 → 17,260).

## Step 4: Replace in README

1. Read `README.md`
2. Find the `<!-- PROGRESS:START -->` and `<!-- PROGRESS:END -->` markers
3. Replace everything between them (exclusive of markers) with the generated content
4. Write the updated README.md

## Step 5: Report

Print a summary:
- How many books have chapters
- How many total chapters found
- Total word count
- What changed vs. the previous README content (if anything)

**Do NOT commit.** The user decides when to commit.
