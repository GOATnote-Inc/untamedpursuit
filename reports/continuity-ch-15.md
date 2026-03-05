# Continuity Report: Book 1, Chapter 15

**Checker version**: v2 (with scene-internal knowledge / presence-map logic)
**Date**: 2026-03-05

---

## Presence Map

### Scene 1: Samuel's Warehouse — Morning (lines 23-64)

| Beat | Samuel | Callaghan | George | Clara | Brennan (off-page) |
|------|--------|-----------|--------|-------|---------------------|
| Samuel reviews ledger at counting table | PRESENT | nearby (loading floor) | absent | absent | off-page (night watch) |
| Callaghan delivers morning count | PRESENT | PRESENT (enters) | absent | absent | off-page |
| Callaghan reports commission clerk visit | PRESENT | PRESENT | absent | absent | off-page |
| Samuel asks "Brennan — what has he seen?" | PRESENT | PRESENT | absent | absent | off-page (reported through Callaghan) |
| Callaghan departs | PRESENT | EXITS | absent | absent | off-page |

### Scene 2: Samuel's Warehouse — George and Clara arrive (lines 66-101)

| Beat | Samuel | George | Clara | Callaghan | Dockmen |
|------|--------|--------|-------|-----------|---------|
| George enters through loading doors | PRESENT | ENTERS | absent | PRESENT (at river doors) | PRESENT |
| Clara follows | PRESENT | PRESENT | ENTERS | PRESENT | PRESENT |
| Clara reads ledger, identifies lost contracts | PRESENT | PRESENT | PRESENT | nearby | nearby |
| Clara invites Samuel to Thomas's office | PRESENT | PRESENT | PRESENT | nearby | nearby |
| Samuel agrees | PRESENT | PRESENT | PRESENT | nearby | nearby |

### Scene 3: Clara's Townhouse — Thomas's Office (lines 103-208)

| Beat | Samuel | Thomas | Clara | George | Housekeeper |
|------|--------|--------|-------|--------|-------------|
| Samuel arrives at townhouse, 2:00 | PRESENT | inside (office) | absent (upstairs) | absent | ENTERS (answers door) |
| Housekeeper leads to office | PRESENT | PRESENT (behind desk) | absent | absent | EXITS |
| Thomas greets Samuel, handshake | PRESENT | PRESENT | absent | absent | absent |
| Thomas and Samuel discuss Wallace, commission clerk | PRESENT | PRESENT | absent | absent | absent |
| Clara enters the room | PRESENT | PRESENT | ENTERS | ENTERS (behind Clara) | absent |
| Thomas presents fleet design (six ships) | PRESENT | PRESENT | PRESENT | PRESENT (by fireplace) | absent |
| Samuel proposes berth calculations | PRESENT | PRESENT | PRESENT | PRESENT | absent |
| Thomas presents Wallace intelligence (Hale's report) | PRESENT | PRESENT | PRESENT | PRESENT | absent |
| Samuel proposes shore trade strategy | PRESENT | PRESENT | PRESENT | PRESENT | absent |
| Thomas's pen pauses — watches Clara watching Samuel | PRESENT | PRESENT | PRESENT | PRESENT | absent |

### Scene 4: Clara's Townhouse — Thomas departs (lines 200-208)

| Beat | Samuel | Thomas | Clara | George |
|------|--------|--------|-------|--------|
| Thomas gathers folios, departs upstairs | PRESENT | EXITS | PRESENT (at window) | PRESENT (by hearth) |
| Clara and Samuel alone in office | PRESENT | absent (upstairs) | PRESENT | PRESENT |
| Clara reveals Osprey's failed predecessors | PRESENT | absent | PRESENT | PRESENT |
| Samuel: "I choose the cargo" | PRESENT | absent | PRESENT | PRESENT |

### Scene 5: Waterfront / Warehouse — Evening (lines 242-249)

| Beat | Samuel | Others |
|------|--------|--------|
| Samuel walks south along waterfront | PRESENT | absent |
| Returns to warehouse, opens fresh ledger page | PRESENT | absent |

---

## Errors (must fix)

### 1. **[Visit count]**: Samuel claims he has been to Clara's townhouse "twice before" — actual count is at least four

- **Draft says** (line 104): "He had been to the townhouse twice before — the courtyard for weapons practice, the dining room for dinner"
- **Chapters say**: Samuel visited the townhouse in ch-07 (weapons practice in courtyard), ch-08 (came through the courtyard door for the Boundary fight muster, later washed hands at courtyard pump), ch-09 (entered the townhouse, met Thomas in the hallway, gathered in Thomas's office for the first three-way planning session, then walked through the courtyard), and ch-10 (dinner in the dining room). That is four visits, not two.
- **Impact**: Samuel's interiority only recalls two visits, omitting the Boundary fight muster (ch-08) and the post-fight planning session (ch-09). This is a factual error in the POV character's memory.
- **Location**: Line 104

### 2. **[Scene-internal knowledge / frontmatter]**: Frontmatter summary claims Samuel "enters Thomas's office for the first time" — he was already in that office in ch-09

- **Draft frontmatter says** (line 10 summary): "Clara brings Samuel into Thomas's office for the first time to see the new fleet design"
- **Ch-09 says** (line 146): "They gathered around Thomas's desk — the three of them, for the first time, in the room where Clara's strategy had always been a conversation between two."
- **Impact**: The ch-09 text explicitly places Samuel in Thomas's office. The ch-15 frontmatter's "first time" claim is false. The body text of ch-15 does not explicitly repeat this "first time" claim (the body text focuses on what Clara is offering strategically, not on whether Samuel has physically been in the room before), so the error is confined to the frontmatter summary. However, the frontmatter should be corrected.
- **Location**: YAML frontmatter, summary field

---

## Warnings (review needed)

### 1. **[Timeline gap]**: Ambiguous time passage between ch-14 and ch-15

- Ch-14 ends with the Osprey inspection just completed and Wallace expected to have the report "by the end of the week." Ch-15 opens with Samuel noting "the erosion had begun in the week since the inspections" (line 28), and Thomas later says Wallace "received the inspection report four days ago" (line 160). This implies roughly a week has passed between ch-14 and ch-15. The timeline is internally consistent within ch-15, but the gap between chapters is not explicitly marked. The author may want to confirm this aligns with the intended pacing.

### 2. **[Knowledge attribution]**: Callaghan reports Brennan's intelligence, but the attribution chain is slightly loose

- At line 56, Samuel asks "Brennan. What has he seen?" Callaghan then reports watchers near the coal depot — "Two men. Wharf side, near the coal depot. Three days running." The information is attributed to Brennan by implication (Samuel's question), but Callaghan delivers it without explicitly saying "Brennan saw" or "Brennan reports." This is a natural conversational pattern and not an error, but the watcher intelligence crosses from one off-page character (Brennan) through another on-page character (Callaghan) to Samuel. The chain is plausible but slightly compressed. Author's call on whether to tighten the attribution.

### 3. **[Disarmament pattern]**: Clara's clothing/armament in ch-15 may need thread-tracking

- Clara wears "the leather coat open at the throat, the sword cane resting against her shoulder rather than planting with each step" (line 72). Later, in Thomas's office, she wears "dark green silk — no coat, no visible weapons" (line 132). This continues the disarmament pattern tracked in open-threads.md (Thread 11). The coat-open-at-throat and cane-on-shoulder at the warehouse is a new register — partially armed but at ease. The dark green silk in the office echoes her ch-03 dress for the first tea and her ch-06 dress under the leather coat. Author should confirm this is intentional tracking of the pattern.

### 4. **[Thomas's description]**: "Silver threading the temples" vs. established "silver at the temples"

- Ch-15 (line 112) uses "silver threading the temples." All previous chapters use "silver at the temples" or "silver at his temples." The variant is not contradictory but introduces a slightly different phrasing. Minor — likely not worth changing, but flagged for consistency-conscious prose.

### 5. **[Cathay's provisions at Samuel's warehouse]**: Implied logistical partnership

- Callaghan reports "The Cathay's provisions are staged for loading" (line 40). The Cathay is Clara's ship. This implies Samuel's warehouse is now providing provisions or staging for Clara's fleet — a logistical relationship not explicitly established on-page before ch-15. It is a natural consequence of the developing partnership, but the author may want to note that this represents an operational integration that happened between chapters.

---

## Scene-Internal Knowledge Verification

### Samuel's interiority — knowledge trace

| Information in Samuel's thoughts | Source (on-page or backstory) | Status |
|---|---|---|
| Two contracts lost — cotton broker, provisions firm | His own ledger (line 26) | VALID — direct observation |
| Erosion began "in the week since the inspections" | Samuel's ledger tracking + ch-14 events | VALID — he was present for the inspection arc |
| Third floor holds "sixty-three passages' worth of evidence" | Learned from Clara in ch-12 (line 126) | VALID |
| "The night of the cargo move" | He was present — ch-13 | VALID |
| Commission clerk visited yesterday asking about third floor | Callaghan tells him on-page (line 44) | VALID |
| Watchers near coal depot, wrong shoes | Callaghan tells him on-page (line 58) | VALID — via Brennan through Callaghan |
| Cotton broker shipped through warehouse for three years | Samuel's own business knowledge | VALID — plausible backstory |
| Clara "looked like a woman who had slept" — assessment | Samuel's direct observation (line 72) | VALID |
| George's position "he had not taken before" at Samuel's feet | Samuel's direct observation (line 88) | VALID — established that George has been near Samuel in previous scenes but this position is new |
| The Osprey's compartments, previous failed designs | Clara tells him on-page in this chapter (lines 218-219) | VALID |
| "His father loaded ships for other men his entire life" | Samuel's established backstory (ch-03, ch-06, ch-12) | VALID |
| Thomas: "Hale's notation: structural features of undetermined purpose" | Thomas states on-page (line 160) | VALID — Thomas's intelligence; Samuel was not present for the inspection itself (that was Clara and Thomas in ch-14), but Thomas tells him here |
| Germantown timber firm worth eight hundred dollars a season | Samuel's own business knowledge (line 174) | VALID — plausible commercial knowledge |

### Thomas's knowledge trace

| Information Thomas states | Source | Status |
|---|---|---|
| Wallace received inspection report four days ago | "Confirmed through my source at the commission" (line 160) | VALID — Thomas's established intelligence network |
| Hale's notation language | Thomas was present aboard the Osprey during inspection (ch-14) | VALID |
| Three shipping partners approached by Wallace's combination | Thomas's intelligence work (lines 168-169) | VALID — consistent with his role |
| Germantown timber firm is the one considering | Thomas's intelligence (line 172) | VALID |

### Clara's knowledge trace

| Information Clara states/knows | Source | Status |
|---|---|---|
| "Four years. The Osprey was the third design." | Her own backstory — she built the ships | VALID — new fact introduced |
| "The first two failed — compartments too small, the air too poor" | Her own experience | VALID — new fact introduced |

---

## New Facts Introduced

- **Osprey's failed predecessors**: Clara reveals the Osprey was the third design; the first two failed due to compartments that were too small and poor air circulation. Four years of building ships for rescue work. (line 218)
- **The fleet system**: Thomas's new design — six rotating commercial vessels with temporary timber frames instead of permanent concealed compartments. Route rotation, ownership dispersed through agents and trustees. (lines 140-142)
- **Wallace's commercial squeeze**: Contracts pulled through intermediaries offering favorable terms; three of Clara's shipping partners approached; economic warfare to defund rescue work. (lines 164-176)
- **Shore trade counter-strategy**: Samuel proposes Chesapeake provisions trade and Eastern Shore routes to replace lost contracts — firms beyond Wallace's social reach. (lines 188-193)
- **Samuel's dock section committed to fleet operations**: The fleet will move through Samuel's dock section. (line 227)
- **"I choose the cargo"**: Samuel's commitment, explicitly framed against his father's legacy. (line 237)
- **Commission clerk Wilkins**: Harbor commission, Office of the Inspector General — visited Samuel's warehouse asking about the third floor. (line 52)
- **Watchers near the coal depot**: Two men, three days running, wrong shoes — surveillance on Samuel's warehouse. (lines 58-59)
- **Germantown timber firm considering Wallace's offer**: Worth $800/season to Samuel. (lines 172-174)

---

## Threads Advanced

- **Anti-trafficking campaign**: Wallace escalates from legal maneuver (inspection) to economic warfare (pulling contracts, approaching Clara's partners, probing the warehouse). The Osprey is replaced by a six-vessel rotating fleet — Thomas's design with Samuel's dock operations and Clara's funding. The shift from single-ship concealment to pattern-based concealment is a fundamental strategic evolution.
- **Thomas Arlington's jealousy seeds**: Samuel enters Thomas's working territory. Thomas is generous and brilliant at the desk — presents the fleet design, offers useful intelligence, watches Clara watch Samuel. The pen pauses (line 198). Thomas takes "the quick inventory of a man who catalogued everything in a room before leaving it" (line 202). Clara is shown Thomas's work and says nothing. Thomas's departure leaves Clara and Samuel alone in his space — the displacement is physical and territorial.
- **Clara-Samuel courtship**: Clara brings Samuel into the strategic inner sanctum. The shared planning session (berth calculations, shore trade) cements their operational partnership. Clara's private disclosure about the Osprey's predecessors (the first time she has spoken about the failed designs) deepens the intimacy. "I choose the cargo" is Samuel's most definitive commitment — framed through his father's legacy, it binds his identity to Clara's work.

---

## Threads That Could Be Advanced Here

- **Clara's progressive disarmament pattern (Thread 11)**: The chapter already tracks this (leather coat open at warehouse, dark green silk in office), but the thread is not advanced with narrative commentary the way earlier chapters handled it. Samuel notices the coat but does not compare it to her previous armament states the way earlier Samuel-POV chapters did. This may be intentional (the pattern is now familiar enough to operate without commentary) or a missed opportunity.
- **Clara's father wound (Thread 12)**: Samuel's closing words — "My father loaded ships for other men his entire life. He never chose the cargo" — directly echo the father-wound theme. Clara's silence in response resonates with her own father's legacy ("A Chen does not fail"). The parallel between the two fathers is present but not surfaced in Samuel's interiority. This could be a deliberate withholding or an opportunity for deeper connection.
