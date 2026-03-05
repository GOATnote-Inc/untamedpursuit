# Regression Report: Ch-02 Window Orientation Change

**Date**: 2026-03-05
**Change**: "east-facing windows" changed to "west-facing windows" in ch-02 (two occurrences)
**Original error flagged in**: `reports/continuity-ch-03.md`, Error #2

---

## 1. Consistency Within Ch-02

**PASS.** No remaining "east-facing" references in ch-02.

- Line 94: "the way afternoon light fell through the **west-facing** windows of the Chestnut Street parlor" -- updated.
- Line 98: "**West-facing** windows. You want the afternoon light." -- updated.
- Grep for `east-facing` in ch-02 returns zero matches.
- The "east wall" reference at line 50 ("Clara moved from the window to the maps on the east wall") is unrelated -- it describes a wall inside Thomas's ground-floor office, not the Chestnut Street parlor. No change needed.

## 2. Cross-Reference: No New Contradictions

All other sources are consistent with "west-facing":

| Source | Text | Status |
|--------|------|--------|
| `bible/world/locations.md` line 28 | "West-facing windows, afternoon light" | CONSISTENT |
| `books/book-01/chapters/ch-03.md` line 87 | "west-facing windows" | CONSISTENT |
| `books/book-01/chapters/ch-03.md` line 119 | "The afternoon light fell through the west-facing windows" | CONSISTENT |
| `books/book-01/outline.md` line 116 | "west-facing windows" | CONSISTENT |
| `books/book-01/notes/continuity-notes.md` line 26 | "west-facing windows, afternoon light" | CONSISTENT |

The physics now hold: west-facing windows receive direct afternoon sunlight, consistent with the 3 PM tea scene in ch-03.

## 3. No Other Issues Introduced

The change is purely directional vocabulary in Clara's interiority (line 94) and Thomas's dialogue (line 98). No surrounding prose, scene logic, or character knowledge was altered. The existing ch-02 errors (midnight timeline contradiction, shifting dossier deadline) remain as previously reported and are unaffected by this change.

## 4. Stale References in Old Reports

Two prior continuity reports still contain "east-facing" references that are now outdated. These are historical reports, not source-of-truth documents, so they do not create contradictions -- but for completeness:

- `reports/continuity-ch-02.md` line 80: "east-facing windows, afternoon light" in New Facts Introduced
- `reports/continuity-ch-03.md` lines 53-57: Error #2 flagging the east-facing physics problem (now resolved)
- `reports/continuity-ch-03.md` line 91: "east-facing windows" in New Facts Introduced

These reports reflect the state of the drafts at the time they were written. No action required unless the author wishes to update them for clarity.

---

**Verdict**: The east-to-west change is complete and consistent across all source files. No new contradictions introduced. The original physics error (flagged in the ch-03 continuity report) is resolved.
