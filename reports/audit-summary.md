# Continuity Audit Summary — Book 1

**Audit dates**: 2026-03-05
**Commits**: `4a0ed76` (engine upgrade + 22 fixes), `90663bb` (6 remaining fixes), pending (final 10 fixes)
**Checker version**: v2 (presence-map logic + experiential grounding)

---

## Overview

| Metric | Count |
|--------|-------|
| Chapters audited | 24 (ch-01 through ch-24) |
| Errors found | 38 |
| Errors fixed | 38 |
| Errors remaining | 0 |
| Warnings logged | 95+ |
| Warnings recommended for promotion | 13 |
| Reports generated | 24 continuity + 5 regression + 2 character-analyst |
| Files changed | 14 chapter files, 3 bible files, outline, continuity-notes |

---

## All Fixes Applied (by chapter)

### Ch-01 — 6 fixes (commit `4a0ed76`)

| # | Error Type | Fix |
|---|-----------|-----|
| 1 | Unattributed knowledge | Samuel references Harper command before Harper arrives → restructured scene so Harper arrives first |
| 2 | Unattributed knowledge | Clara knows "three weeks" of surveillance → added Samuel dialogue: "I spent three weeks watching that ship" |
| 3 | Unattributed knowledge | Clara knows Samuel tried negotiation → changed to deduction from observed evidence (pistol kicked away) |
| 4 | Unattributed knowledge | Clara "knew the crew by sight" → softened to "likely knew the crew by sight" |
| 5 | Factual precision | "kill twelve people" overcounts Clara's solo kills → changed to "do what she had done" |
| 6 | Weapons logic | "spent Colt" after only two shots → changed to "first Colt" / "the weapon" |

### Ch-02 — 1 fix (commit `4a0ed76`)

| # | Error Type | Fix |
|---|-----------|-----|
| 7 | Physics/setting | East-facing windows with afternoon light → west-facing (2 instances) |

### Ch-03 — 2 fixes (commit `4a0ed76`)

| # | Error Type | Fix |
|---|-----------|-----|
| 8 | Physics/setting | East-facing windows → west-facing (2 instances) |
| 9 | Cross-chapter consistency | "four minutes" (rescue duration) → "three minutes" to match ch-01 |

### Ch-04 — 3 fixes (commit `90663bb`)

| # | Error Type | Fix |
|---|-----------|-----|
| 10 | Unattributed knowledge | Lily knows Samuel's gallery interests without source → "Clara tells me you've been studying our gallery" |
| 11 | Bible/chapter conflict | Discovery story: bible said "drawn by a cello," chapter said "business associate" → bible updated to match chapter |
| 12 | Spatial impossibility | Ocean painting in public AND private gallery same evening → public gallery changed to "harbor at dawn"; private gallery reference changed to "on a previous visit" |

### Ch-06 — 1 fix (commit `4a0ed76`)

| # | Error Type | Fix |
|---|-----------|-----|
| 13 | Cross-chapter consistency | "six men" on the dock → "a dozen men" to match ch-01's body count |

### Ch-10 — 2 fixes (commits `4a0ed76` + `90663bb`)

| # | Error Type | Fix |
|---|-----------|-----|
| 14 | Timeline | "weeks since the river walk" → "days since the river walk" (~7-10 days elapsed) |
| 15 | Timeline | "three days ago" for housekeeper → "a few days ago" (~4 days elapsed) |

### Ch-12 — 1 fix (commit `4a0ed76`)

| # | Error Type | Fix |
|---|-----------|-----|
| 16 | False/shifted memory | Samuel attributes "worth keeping" line to "at the river walk" → "at dinner" (ch-10, not ch-06) |

### Ch-15 — 2 fixes (commit `90663bb`)

| # | Error Type | Fix |
|---|-----------|-----|
| 17 | Count error | "twice before" visiting townhouse → "before — the courtyard, the dining room, Thomas's office" (4+ visits) |
| 18 | Frontmatter error | "enters Thomas's office for the first time" → removed "for the first time" (he was there in ch-09) |

### Ch-16 — 1 fix (commit `90663bb`)

| # | Error Type | Fix |
|---|-----------|-----|
| 19 | POV break | Thomas-alone coda after Clara leaves → "At the doorway she paused and looked back" — Clara observes Thomas through open door, then closes it and leaves |

### Ch-18 — 2 fixes (commit `4a0ed76`)

| # | Error Type | Fix |
|---|-----------|-----|
| 20 | Cross-chapter consistency | Manifest "crew of twelve" → "crew of eight" (matches ch-20, ch-21) |
| 21 | Arithmetic | "feed twenty people" → "feed seventeen people" (8 crew + 1 captain + 8 company) |

### Ch-19 — 1 fix (commit `90663bb`)

| # | Error Type | Fix |
|---|-----------|-----|
| 22 | Timeline tension | "Five years. A fortune spent." → "Five years — the first alone, the last four with Thomas at that desk." Resolves five/four discrepancy |

### Ch-20 — 1 fix (commit `90663bb`)

| # | Error Type | Fix |
|---|-----------|-----|
| 23 | Unattributed knowledge | Samuel knows "six days in a hold" with no source → added Harper dialogue: "Six days in that hold, Mr. Taylor." Grounds ch-22 echo. |

### Ch-21–24 — 1 systemic fix (commit `4a0ed76`)

| # | Error Type | Fix |
|---|-----------|-----|
| 24 | Name collision | Harper's man "Marsh" collides with Wallace's accountant "Edward Marsh" → renamed to "Ward" across ch-21, ch-22, ch-23, ch-24, outline, continuity-notes, anchor file |

### Ch-22 — 1 fix (commit `4a0ed76`)

| # | Error Type | Fix |
|---|-----------|-----|
| 25 | False memory | Samuel recalls Clara "knelt beside the children" (never happened in ch-01) → "looked at the children pressed against George" |

### Ch-23 — 1 fix (commit `4a0ed76`)

| # | Error Type | Fix |
|---|-----------|-----|
| 26 | Spatial impossibility | Harper speaks to Jennings across separate bungos → changed to Davis (who is in Harper's bungo) |

### Ch-24 — 2 fixes (commit `4a0ed76`)

| # | Error Type | Fix |
|---|-----------|-----|
| 27 | Cross-chapter consistency | "Eighteen miles" trail distance → "Twenty miles" (3 instances + YAML frontmatter, matching ch-23 historian revision) |
| 28 | Arithmetic | "eighteen miles of mud" at night camp (only ~12 miles walked) → "twelve miles of mud" |

### Ch-02 — 3 additional fixes (final batch)

| # | Error Type | Fix |
|---|-----------|-----|
| 29 | Timeline contradiction | "Past midnight" → "Nearly midnight" (line 24) — resolves conflict with midnight clock strike at line 158 |
| 30 | Timeline (bible) | "The Following Morning" → "Same Night" in `bible/timeline/book-01-timeline.md` |
| 31 | Internal inconsistency | "By our weapons practice in the early afternoon" → "By morning practice" (line 74) — matches line 148 |

### Ch-05 — 1 additional fix (final batch)

| # | Error Type | Fix |
|---|-----------|-----|
| 32 | Unattributed knowledge | "I haven't heard you sing like that in a while" → "Harper tells me you sang like you used to" (line 76) — Thomas wasn't at the performance |

### Ch-07 — 1 additional fix (final batch)

| # | Error Type | Fix |
|---|-----------|-----|
| 33 | Unattributed knowledge | "its dining room that seated forty" → "its private dining room" (line 26) — capacity number not in bible |

### Ch-08 — 2 additional fixes (final batch)

| # | Error Type | Fix |
|---|-----------|-----|
| 34 | Arithmetic | "three of his men" → "four of his men" (line 79) — matches line 115 and established 4-man team |
| 35 | Unattributed knowledge | "more than a ten-item plan" → "a proper plan" (line 233) — Samuel never saw the plan |

### Ch-20 — 1 additional fix (final batch)

| # | Error Type | Fix |
|---|-----------|-----|
| 36 | Arithmetic | "fifteen souls" → "seventeen souls" (line 61) — correct headcount: 1+8+1+4+1+1+1=17 |

### Ch-23 — 1 additional fix (final batch)

| # | Error Type | Fix |
|---|-----------|-----|
| 37 | False memory | "first seen across a counting table" → "first seen on a dock in the gaslight" (line 87) — Clara first saw Samuel at the Mercy Jane rescue |

### Ch-24 — 1 additional fix (final batch)

| # | Error Type | Fix |
|---|-----------|-----|
| 38 | Timeline arithmetic | "over thirteen days of carrying" → "over a week of carrying" (line 102) — pistol issued April 17-18, ch-24 is April 25-26 = 7-9 days |

### Supporting file changes

| File | Changes |
|------|---------|
| `bible/world/locations.md` | East-facing → west-facing (Chestnut Street parlor) |
| `bible/characters/samuel-taylor.md` | Golden Compass discovery: "drawn by a cello" → "through a business associate" (Background + Continuity Notes) |
| `books/book-01/outline.md` | East-facing → west-facing; Marsh → Ward (6 refs); Brennan → Tierney (ship crew, 4 refs); eighteen → twenty miles (3 refs); ocean painting → harbor at dawn |
| `books/book-01/notes/continuity-notes.md` | East-facing → west-facing; Tierney → Brennan (warehouse watchman, line 875); Marsh → Ward (6 refs); eighteen → twenty miles |
| `books/book-01/notes/ch-24-anchor.md` | Marsh → Ward; eighteen → twenty miles |

### Engine upgrades

| File | Change |
|------|--------|
| `.claude/agents/continuity-checker.md` | Added presence-map logic (Process step 4) + scene-internal knowledge check |
| `.claude/agents/character-analyst.md` | Added experiential grounding check (Process step 5) + report format + flag type |

---

## Previously Unfixed Errors — Now Fixed (10)

All 10 remaining errors were fixed and regression-checked. Details:

| # | Ch | Error | Fix Applied |
|---|-----|-------|-------------|
| 29 | 02 | "Past midnight" contradicts midnight clock strike | "Nearly midnight" (line 24) |
| 30 | 02 | Timeline entry said "The Following Morning" | "Same Night" in `bible/timeline/book-01-timeline.md` |
| 31 | 02 | Dossier deadlines: "early afternoon" vs. "morning practice" | "By morning practice" (line 74) |
| 32 | 05 | Thomas assesses singing without attending performance | "Harper tells me you sang like you used to" (line 76) |
| 33 | 07 | "dining room that seated forty" — unattributed fact | "its private dining room" (line 26) |
| 34 | 08 | Harper arrives with "three" men, approach says "four" | "four of his men" (line 79) |
| 35 | 08 | Samuel references "ten-item plan" never disclosed to him | "a proper plan" (line 233) |
| 36 | 20 | "fifteen souls" headcount — should be 17 | "seventeen souls" (line 61) |
| 37 | 23 | "first seen across a counting table" — false memory | "first seen on a dock in the gaslight" (line 87) |
| 38 | 24 | "thirteen days of carrying" — should be ~7-9 days | "over a week of carrying" (line 102) |

---

## Warnings Recommended for Promotion to Errors (13)

These warnings involve characters possessing knowledge, memories, or emotional reactions with no on-page source — the exact class of error the upgraded presence-map and experiential-grounding engines were designed to catch.

| Ch | Warning | Issue | Recommended Fix |
|----|---------|-------|-----------------|
| 3 | W1 | Clara attributes "He sits at our table" to Thomas — Thomas never says this on-page | Have Thomas say it on-page, or frame as Clara's paraphrase |
| 5 | W2 | Clara says Samuel recognized the Rembrandt "on his first visit" — never stated to her | Source to off-page dinner ("Samuel mentioned...") or remove specificity |
| 5 | W3 | Clara knows Samuel's exact visit count and timeline ("three months... four times") | Same as above |
| 6 | W1 | Clara describes Samuel weeping "in a room full of strangers" — she was on stage | Change to inference from his wet face backstage, or attribute to Harper |
| 7 | W1 | Samuel remembers "the gesture she had used at the riverfront" — but in ch-06 it was Samuel who inclined his head, not Clara | Fix the attribution or add Clara's reciprocal gesture in ch-06 |
| 9 | W1 | Clara tells Samuel that Harper saw his workers arriving — Harper never says this on-page | Add to Harper's dialogue in the preceding scene |
| 13 | W1 | Clara names Callaghan and Brennan to Harper without on-page acquisition | Add a brief attribution ("Samuel's man Callaghan") |
| 13 | W2 | Clara states inspection order not established on-page | Add a line establishing the sequence was discussed |
| 14 | W1 | Clara's interiority says Samuel "watching ships built and broken" — his father loaded ships, not built them | Change "built and broken" to "loaded and launched" or similar |
| 16 | W3 | Thomas references mineral reports from ch-03 tea where he was not present | Attribute to Clara relaying, or Thomas's independent network |
| 19 | W3 | Clara references "Samuel's father's drawer" — detail from Samuel's private interiority never shared | Soften to what Clara could observe, or add a scene where Samuel shares this |
| 19 | W5 | Clara characterizes "the city he had closed behind him" — projects into Samuel's psychology | Reframe as external observation |
| 22 | W1 | Samuel identifies "George's weight" from below decks, in a passage about inability to identify sounds | Phrase as inference: "What must have been George's weight" |

---

## Error Taxonomy (all 38 errors found)

| Category | Count | Examples |
|----------|-------|---------|
| Unattributed knowledge | 10 | Clara's "three weeks," Lily's gallery knowledge, Samuel's "six days" |
| False/shifted memory | 4 | Counting table first-meeting, children kneeling, river walk quote |
| Arithmetic/count errors | 8 | Crew 12→8, trail 18→20, visit count, provisions, pistol days |
| Timeline contradictions | 4 | Weeks→days, midnight contradiction, deadline shift, three days ago |
| Cross-chapter consistency | 4 | Four/three minutes, six/dozen men, east/west-facing, five/four years |
| Spatial impossibility | 3 | Harper/Jennings across bungos, ocean painting in two galleries |
| POV break | 1 | Thomas-alone coda |
| Bible/draft conflict | 2 | Golden Compass discovery story, frontmatter "first time" |
| Name collision | 1 | Marsh (2 characters) |
| Weapons/combat logic | 1 | "Spent Colt" |

---

## Engine Upgrade Impact

The v2 presence-map logic was responsible for detecting **15 of 38 errors** (39%) — issues that the v1 checker (bible-only cross-reference) would have missed because they involve intra-scene temporal tracking, character positioning, and knowledge acquisition chains.

The experiential-grounding addition to the character-analyst caught the remaining false-memory and emotional-reaction issues that the continuity-checker's factual lens does not cover.

---

*Generated 2026-03-05. Updated same day: all 38 errors fixed and regression-checked. Next action: evaluate the 13 warnings recommended for promotion.*
