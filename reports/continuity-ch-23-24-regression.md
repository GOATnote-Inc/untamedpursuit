# Regression Report: Chapters 23 and 24 (Marsh-to-Ward Rename + Trail Distance Change)

**Date**: 2026-03-05
**Scope**: Verify rename of "Marsh" to "Ward" in ch-23 and ch-24; verify trail distance change from eighteen to twenty miles; check arithmetic consistency.

---

## 1. Marsh-to-Ward Rename

### Ch-23: PASS
- Zero instances of "Marsh" remain.
- "Ward" appears twice:
  - Line 47 (bungo roster): "Clara, Harper, George, Davis, and Ward in the first."
  - Line 81 (watch rotation): "Davis and Ward took the first watch."
- Both usages are correct in context.

### Ch-24: PASS
- Zero instances of "Marsh" remain.
- "Ward" appears four times:
  - Line 32: "Ammunition for Ward."
  - Line 54: "Davis and Ward loading gear onto the first mules."
  - Line 76: "Davis and Ward at the rear."
  - Line 112: "Jennings and Ward at the flanks."
- All usages are correct in context.

### Other chapters: NO CONFLICT
- "Marsh" still appears in ch-09 and ch-11, but these all refer to **Edward Marsh**, Wallace's accountant -- a different character entirely. No rename needed there.
- Ch-21 and ch-22 already use "Ward" for the company member (confirmed: no "Marsh" in either file). The rename is consistent across the Kingston-through-Isthmus arc (ch-21 through ch-24).

---

## 2. Trail Distance: Twenty Miles

### Ch-23 frontmatter (line 19): "twenty miles" -- PASS
- Reads: "The mule trail ahead (Cruces, twenty miles, the dangers with shape and the ones without)"

### Ch-23 body (line 99): "Twenty miles" -- PASS
- Reads: "Twenty miles of jungle that Reyes described with a specificity Harper recognized"

### Ch-24 body (line 70): "Twenty miles" -- PASS (two instances on same line)
- Reads: "Twenty miles. Reyes said it as a fact..." and "Twenty miles of jungle that had eaten a road and was still hungry."

### Cross-reference: Ch-23 and Ch-24 agree on twenty miles. CONSISTENT.

---

## 3. Night Camp Distance: Twelve Miles Walked

### Ch-24 body (line 134): "twelve miles" -- PASS
- Reads: "how he had walked twelve miles of mud without complaint"
- Context: night camp reflection. Samuel has walked 12 of the 20 total miles on day 1.

---

## 4. Day 2 Remaining Distance: Eight Miles

### Ch-24 body (line 156): "Eight miles" -- PASS
- Reads: "'Eight miles,' Harper said to the company."
- Arithmetic check: 20 total - 12 walked on day 1 = 8 remaining. **Correct.**

### Ch-24 body (line 162): "Eight miles" repeated three times -- PASS
- Reads: "Eight miles to Panama City. Eight miles to the Pacific. Eight miles of jungle..."
- Consistent with line 156.

---

## 5. Residual Inconsistencies Introduced

### ERROR: Ch-24 frontmatter summary still says "eighteen-mile"

- **Location**: Line 10 (YAML summary field)
- **Draft says**: "The company reaches Cruces and begins the eighteen-mile mule trail toward Panama City."
- **Should say**: "...the twenty-mile mule trail..."
- **Severity**: Must fix. The frontmatter summary was not updated when the body text was changed.

### WARNING: Outline and anchor note still say "eighteen miles"

The following upstream documents were not updated and now conflict with the chapter text:

| File | Line | Current Text |
|------|------|-------------|
| `outline.md` | 1184 | "Cruces, the mule trail, eighteen miles" |
| `outline.md` | 1197 | "Cruces, eighteen miles, dangers with shape and without" |
| `outline.md` | 1236 | "Eighteen miles. Mules in single file." |
| `notes/ch-24-anchor.md` | 14 | "Eighteen miles. Mules single file." |

These are planning documents, not prose, so the priority is lower -- but they will cause confusion in future continuity checks if left as-is.

### CONFIRMED CONSISTENT: continuity-notes.md already updated
- `notes/continuity-notes.md` line 1564 says "twenty miles" (ch-23 entry).
- `notes/continuity-notes.md` line 1596 says "twenty miles" (ch-24 entry).
- These match the revised chapter text. No fix needed.

---

## Summary

| Check | Result |
|-------|--------|
| All "Marsh" removed from ch-23 | PASS |
| All "Marsh" removed from ch-24 | PASS |
| No collateral damage to Edward Marsh (ch-09) | PASS |
| "Ward" consistent across ch-21 through ch-24 | PASS |
| Ch-23 says "twenty miles" (frontmatter + body) | PASS |
| Ch-24 says "Twenty miles" at trail start (line 70) | PASS |
| Ch-24 says "twelve miles" at night camp (line 134) | PASS |
| Ch-24 says "Eight miles" on day 2 (line 156) | PASS |
| Arithmetic: 20 - 12 = 8 | PASS |
| Ch-24 frontmatter summary: still says "eighteen-mile" | **FAIL** |
| Outline + anchor note: still say "eighteen miles" | **WARNING** |

**Action required**: Update ch-24 frontmatter summary (line 10) from "eighteen-mile" to "twenty-mile." Consider updating outline.md lines 1184, 1197, 1236, and ch-24-anchor.md line 14 to match.
