---
name: book-review
description: End-of-book cross-chapter audit before starting the next book
argument-hint: <book>
---

# /book-review — End-of-Book Audit

Run this once when a book is fully drafted, before moving to the next book. Validates cross-chapter consistency that per-chapter `/revise` runs cannot catch.

## Step 1: Run the Book Audit Script

```bash
python3 scripts/book-audit.py ${book} --out
```

This generates `reports/book-${book}-audit.md` covering:
- POV distribution
- Word count distribution and outliers
- Timeline progression and regressions
- Character descriptor tracking across chapters
- Thread progression matrix
- Unresolved continuity flags
- Chapter status summary

## Step 2: Run the Thread Validator

```bash
python3 scripts/validate-threads.py ${book}
```

Review the output for:
- **Orphan threads in open-threads.md**: Series-level threads that should have been advanced in this book but weren't
- **Stale threads**: Threads introduced early in the book that were never picked up again
- **Missing thread entries**: Major threads tracked in frontmatter but not yet added to `bible/mysteries/open-threads.md`

## Step 3: Cross-Chapter Character Consistency

Launch a character-analyst subagent with a cross-book scope:

- Prompt: "Read all ${chapter_count} chapters of book ${book} and check for cross-chapter character consistency. Focus on: (1) voice drift — does each POV character's narration stay consistent from their first chapter to their last? (2) relationship evolution — do character dynamics progress logically? (3) physical continuity — scars, injuries, clothing patterns, recurring descriptors. (4) knowledge consistency — do characters only know what they've been told or witnessed? Follow your agent instructions in `.claude/agents/character-analyst.md`."

## Step 4: Cross-Chapter Historian Review

Launch a historian subagent with a cross-book scope:

- Prompt: "Review all ${chapter_count} chapters of book ${book} for cross-chapter historical consistency. Focus on: (1) timeline plausibility — do travel times, seasonal details, and date references add up? (2) technology consistency — are the same weapons, tools, and materials described consistently? (3) vocabulary consistency — are banned anachronistic terms absent from all chapters? Check against `research/fact-checks/anachronism-rulings.md` for the banned list. Follow your agent instructions in `.claude/agents/historian.md`."

## Step 5: Synthesize and Present

Compile all findings into a single end-of-book review:

```markdown
## Book ${book} — End-of-Book Review

### Cross-Chapter Issues Found
<!-- Issues that span multiple chapters — the kind per-chapter /revise misses -->

### Thread Health
<!-- Threads that need attention before starting the next book -->

### Bible Updates Needed
<!-- Facts from this book that should be canonized before proceeding -->

### Recommended Pre-Book-${next_book} Actions
<!-- Specific tasks to complete before starting the next book -->
```

Present to the user for review. Do not proceed to the next book until this review is addressed.

## Step 6: Update Bible for Book Transition

After the user approves the review:

1. Run `/curate ${book}` to clear any remaining unprocessed bible entries
2. Update `bible/timeline/book-${book}-timeline.md` if any gaps were found
3. Update `bible/mysteries/open-threads.md` with any new threads or status changes
4. Verify all character profiles reflect their end-of-book state
