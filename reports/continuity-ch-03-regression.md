# Regression Report: Book 1, Chapter 3

**Type**: Regression check (post-modification)
**Date**: 2026-03-05
**Trigger**: "east-facing windows" changed to "west-facing windows" in ch-03; "four minutes" flagged but not yet fixed

---

## 1. Window Direction Change: CLEAN

The "east-facing" to "west-facing" correction has been applied consistently across all active files. No remaining "east-facing" references exist in any chapter, bible entry, outline, or continuity note.

| File | Status |
|------|--------|
| `books/book-01/chapters/ch-03.md` line 87 | "west-facing windows" -- correct |
| `books/book-01/chapters/ch-03.md` line 119 | "west-facing windows" -- correct |
| `books/book-01/chapters/ch-02.md` line 94 | "west-facing windows" -- correct |
| `books/book-01/chapters/ch-02.md` line 98 | "West-facing windows" -- correct |
| `bible/world/locations.md` line 28 | "West-facing windows, afternoon light" -- correct |
| `books/book-01/outline.md` line 116 | "west-facing windows" -- correct |
| `books/book-01/notes/continuity-notes.md` line 26 | "west-facing windows" -- correct |

**Stale references in old reports** (not errors -- these describe the state before the fix):
- `reports/continuity-ch-03.md` lines 53-57, 91 -- references "east-facing" as part of the original error description
- `reports/continuity-ch-02.md` line 80 -- references "east-facing" in the original new-facts log

These are historical report artifacts, not live contradictions. No action needed unless the author prefers to annotate them as superseded.

## 2. "Four Minutes" Duration: STILL PRESENT (unfixed)

Confirmed: the inconsistency remains in the draft.

- **ch-01, line 118**: Samuel says "You found it in three minutes."
- **ch-03, line 137**: Samuel says "You destroyed it in four minutes."

Samuel is the speaker in both cases, recalling the same event. Ch-01 takes precedence as the earlier chapter. Line 137 of ch-03 should be changed from "four minutes" to "three minutes."

## 3. New Contradictions Introduced by the Window Fix: NONE

The west-facing change introduces no new contradictions. West-facing windows producing warm afternoon light at a 3 PM meeting is physically correct (the sun is in the west/southwest during afternoon hours in autumn at Philadelphia's latitude). All references -- ch-02, ch-03, the bible, the outline, and the continuity notes -- are now aligned.

---

## Summary

| Check | Result |
|-------|--------|
| No remaining "east-facing" in active files | PASS |
| "Four minutes" still present in ch-03 line 137 | CONFIRMED (awaiting fix) |
| No new contradictions from the window fix | PASS |

**Open action item**: Change "four minutes" to "three minutes" on ch-03, line 137.
