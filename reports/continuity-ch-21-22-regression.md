## Regression Report: Book 1, Chapters 21-22 — Marsh-to-Ward Rename

**Date**: 2026-03-05
**Scope**: Verify all instances of Harper's man "Marsh" renamed to "Ward" in ch-21 and ch-22; confirm no residual references, no new contradictions.

---

### 1. Rename Verification: ch-21

| Line | Context | Status |
|------|---------|--------|
| 76 | "Davis and Ward at the starboard rail" | PASS — was "Marsh" |
| 126 | "Davis and Ward finding their marks" | PASS — was "Marsh" |
| 130 | Harper's dialogue: "Ward — the line at the bow." | PASS — was "Marsh" |

**Residual "Marsh" in ch-21**: None. Grep confirms zero matches.

### 2. Rename Verification: ch-22

| Line | Context | Status |
|------|---------|--------|
| 58 | "Davis and Ward went ashore with a list." | PASS — was "Marsh" |

**Residual "Marsh" in ch-22**: None. Grep confirms zero matches.

### 3. Downstream Chapters

Chapters 23 and 24 also use "Ward" throughout (no "Marsh" found). The continuity notes (`books/book-01/notes/continuity-notes.md`) and the ch-24 anchor file (`notes/ch-24-anchor.md`) already reflect the "Ward" name. These were updated as part of the same rename pass.

### 4. Naturalness in Context

The quartet reads as: **Davis, Ward, Cole, Jennings**. All monosyllabic surnames, period-appropriate, phonetically distinct from one another and from the main cast. Harper's dialogue on line 130 -- "Davis -- the helmsman. Ward -- the line at the bow." -- reads cleanly; the crisp, one-syllable name fits Harper's clipped command style.

### 5. New Name Collision Check

- **"Ward" in the bible**: No matches. No existing character named Ward in any profile, relationship map, or world-building file.
- **"Ward" in all chapters (book-01)**: Appears only in ch-21 through ch-24, always referring to Harper's man. No collision.

### 6. Edward Marsh (Wallace's Accountant) -- Unaffected

Edward Marsh remains in ch-09 (lines 62, 66, 70, 76, 146, 154, 174) and ch-11 (line 77) as Wallace's captured accountant. These references are correct and untouched. The rename resolves the name collision flagged in the original ch-21 and ch-22 continuity reports.

### 7. No New Contradictions

- Harper's four men are consistently Davis, Ward, Cole, Jennings across ch-21, ch-22, ch-23, ch-24, the outline (ch-23/ch-24/ch-26/ch-28/ch-30 beats), continuity notes, and the ch-24 anchor file.
- No character knowledge, positioning, or relationship logic was altered -- only the surname was swapped.

---

### Stale References (Not Errors -- Previous Reports)

The following **old continuity reports** still reference "Marsh" as Harper's man. These are historical analysis documents, not chapter text, so they do not affect the narrative. Noted for awareness:

| File | Description |
|------|-------------|
| `reports/continuity-ch-21.md` | Original report that flagged the name collision; references "Davis, Marsh, Cole, Jennings" |
| `reports/continuity-ch-22.md` | Same; includes the Marsh/Edward Marsh collision warning |
| `reports/continuity-ch-23.md` | Presence maps list "Marsh" in bungo assignments |
| `reports/continuity-ch-24.md` | Presence maps list "Marsh" in trail formation and watch positions |

Additionally, the **outline** at line 1727 (ch-30, beat 5 -- "The Resolve") still reads "Davis, Marsh, George" instead of "Davis, Ward, George." This should be updated.

---

### Verdict

**PASS.** The Marsh-to-Ward rename is complete and consistent across all four chapter files (ch-21 through ch-24) and supporting notes. The original name collision with Edward Marsh is resolved. One stale reference remains in the outline (ch-30 beat 5) that should be corrected.
