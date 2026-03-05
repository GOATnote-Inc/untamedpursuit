# Continuity Report: Book 1, Chapter 3

**Checker version**: v2 (with scene-internal knowledge / presence-map logic)
**Date**: 2026-03-05

---

## Presence Map

### Scene 1: Courtyard Weapons Practice (lines 25-34)

| Beat | Clara | George | Thomas | Samuel |
|------|-------|--------|--------|--------|
| Dawn blade practice | PRESENT | PRESENT (near gate, watching) | absent | absent |
| Colt target practice (clay pots) | PRESENT | PRESENT | absent | absent |
| Sun clears townhouse roof | PRESENT | PRESENT | ARRIVES | absent |

### Scene 2: Thomas Delivers Report (lines 36-83)

| Beat | Clara | George | Thomas | Samuel |
|------|-------|--------|--------|--------|
| Thomas enters through garden gate | PRESENT (cleaning Colt) | PRESENT (tail wag) | PRESENT | absent |
| Thomas delivers Samuel dossier | PRESENT | PRESENT | PRESENT | absent |
| Clara departs to dress for tea | EXITS (toward house) | EXITS (follows Clara) | PRESENT (stays in chair) | absent |

### Scene 3: Tea at Chestnut Street Parlor (lines 87-157)

| Beat | Clara | George | Thomas | Samuel |
|------|-------|--------|--------|--------|
| Clara arrives at 2:45, arranges table | PRESENT | ABSENT (left at townhouse) | absent | absent |
| Samuel arrives at 3:00 | PRESENT | ABSENT | absent | PRESENT |
| Conversation: mutual assessment | PRESENT | ABSENT | absent | PRESENT |
| Samuel reveals Wallace intelligence | PRESENT | ABSENT | absent | PRESENT |
| Clara shares shipping summary | PRESENT | ABSENT | absent | PRESENT |
| Handshake | PRESENT | ABSENT | absent | PRESENT |

### Scene 4: Clara in Carriage (lines 159-173)

| Beat | Clara | George | Thomas | Samuel |
|------|-------|--------|--------|--------|
| Clara walks to carriage, reflects | PRESENT (alone) | absent | absent | absent |

---

## Errors (must fix)

- **[Factual inconsistency / Duration]** ✓ FIXED (2026-03-05): Changed "four minutes" to "three minutes" to match ch-01. — Samuel states the dock rescue took "four minutes" in ch-03, but said "three minutes" in ch-01.
  - **Draft says**: "You destroyed it in four minutes." (ch-03, line 137)
  - **Ch-01 says**: "You found it in three minutes." (ch-01, line 118)
  - **Location**: ch-03, line 137
  - **Note**: Samuel is the speaker in both cases. His own recollection of the same event has changed between chapters. One of these must be corrected for consistency.

- **[Physics / Setting]**: East-facing windows cannot produce warm afternoon light at 3 PM. The sun is in the west during the afternoon; east-facing windows would be in shadow.
  - **Draft says**: "east-facing windows, which filled the room with afternoon light that was warm without being interrogative" (ch-03, line 87); "The afternoon light fell through the east-facing windows" (ch-03, line 119)
  - **Reality**: East-facing windows receive direct sunlight in the morning. For warm 3 PM light, the windows should face west or southwest.
  - **Location**: ch-03, lines 87 and 119; also present in ch-02, lines 94 and 98
  - **Note**: This error is baked into the bible (`bible/world/locations.md` line 28: "East-facing windows, afternoon light") and ch-02. Correcting it requires updating all references. Either change "east-facing" to "west-facing" everywhere, or change the meeting time to morning (which would conflict with the 3 PM appointment).

## Warnings (review needed)

- **[Scene-internal knowledge / Unattributed phrase]**: Clara thinks "He sits at our table" and attributes the phrase to Thomas ("recognized the phrase as Thomas's"), but Thomas never says this phrase on-page in ch-02 or ch-03. His closest statement is: "He is wealthy, strategic, ethical, brave, trains every night, and appreciates art that most people walk past without seeing" (ch-03, line 69).
  - **Location**: ch-03, line 167
  - **Assessment**: The phrase could be read as Clara compressing Thomas's sentiment into a formulation, or as something Thomas said off-page. However, ch-05 later references it as "Thomas's phrase" explicitly (ch-05, line 86). The author may want to have Thomas say this phrase on-page in ch-03 (perhaps in his summary at line 69) to anchor the attribution, or have Clara's interiority frame it more clearly as her paraphrase.

- **[Timeline ambiguity]**: The book-01 timeline describes ch-03 as "Dawn, ~One Day Later" after ch-02, but the chapter text reads as though only one night has passed since the rescue. Samuel says "last night" (lines 105, 137) referring to the dock rescue. Clara references "two hours" of sleep after "the night's violence" (line 29). Thomas "had spent the night" investigating (line 37).
  - **Location**: ch-03, lines 29, 37, 105, 137 vs. `bible/timeline/book-01-timeline.md` line 20
  - **Assessment**: The chapter text reads most naturally as: rescue (night) -> Clara debriefs Thomas (late night, ch-02) -> Clara goes out again -> midnight (end of ch-02) -> Clara sleeps 2 hours -> dawn practice (ch-03) -> tea at 3 PM. In this reading, "last night" works. But the timeline entry "~One Day Later" suggests a full day gap, which would make the rescue "two nights ago." The timeline entry may need updating to match the chapter's internal chronology.

- **[Continuity / Reporting deadline]**: In ch-02, Clara gives Thomas two different deadlines for Samuel's dossier. At line 74: "By our weapons practice in the early afternoon." At line 148: "Have that information ready by morning practice." Ch-03 has Thomas arriving in the morning (consistent with the later deadline), but the earlier deadline ("early afternoon") was never corrected or superseded on-page within ch-02.
  - **Location**: ch-02, lines 74 and 148 (upstream issue affecting ch-03 continuity)
  - **Assessment**: Ch-03 follows the later instruction (morning delivery), so ch-03 itself is internally coherent. The inconsistency lives within ch-02.

- **[Historical accuracy]**: Samuel references "geological reports" about California gold in autumn 1846 (line 125). The California Gold Rush began with James Marshall's discovery at Sutter's Mill in January 1848. Pre-1848 knowledge of California gold among the ultra-wealthy is historically plausible (small finds were known earlier), and the text explicitly frames it as insider intelligence ("Most of the country will not hear of this for years"). The bible's `politics.md` dates Gold Rush economics to "1848+."
  - **Location**: ch-03, line 125
  - **Assessment**: The author appears to be using this deliberately as insider intelligence foreshadowing. May warrant a historian subagent review to confirm whether 1846 mineral surveys are defensible.

- **[Scene-internal knowledge]**: Samuel knows detailed information about Clara's operations in lines 109: "Why do you maintain an apparatus capable of mounting a rescue operation within minutes? Why do you fund -- and I believe you fund -- harbor patrols and inspection regimes that the city itself cannot afford?" These are significant intelligence claims beyond what he directly witnessed.
  - **Location**: ch-03, lines 109-111
  - **Assessment**: The chapter explicitly acknowledges this knowledge leap at line 111: "he had arrived with intelligence of his own, or he had spent the night thinking with the same rigor Thomas had spent it investigating. Either answer interested her." Samuel is established as having his own intelligence network (3 weeks of Mercy Jane surveillance, connections to men like Wallace). Clara's harbor patrols and rescue apparatus could be inferred from witnessing Harper's team, the organized response, and the cleanup. This is adequately justified but the author should be aware that Samuel's intelligence-gathering capability is being implied early and should be developed further.

## New Facts Introduced

- **Samuel's age**: Thirty-one years old (first precise age stated; bible says "Circa 1810s (30s)")
- **Samuel's father**: Irish dock worker, "came over during the twenties." Mother's background "less clear, possibly mixed."
- **Samuel's financial philosophy**: Profit-sharing, decision-making authority distributed, reserves to fund a year of losses without touching property
- **Samuel trains nightly with a weapons master**: Confirmed on-page via Thomas's report
- **Samuel frequents a tavern for the music**: Contains hidden art; Samuel noticed the art (on the "art tour")
- **The warehouse sale**: Clara's network sold Samuel a warehouse; "performing well"
- **Wallace named**: Rejected Samuel's partnership offer on western port control; ambition includes war-supply contracts and insider California mineral intelligence; trafficking and port control are "two arms of the same body"
- **Wallace's retaliation**: The Mercy Jane dock attack was Wallace's response to Samuel's refusal
- **Clara owns Chestnut Street parlor**: Through a private holding company; east-facing windows; used for first meetings
- **Clara's shipping holdings**: Prepared a summary representing "perhaps a tenth of her actual position"
- **Clara's courtyard**: Walled space behind her townhouse, packed earth and flagstone, iron chairs, garden gate; used for weapons practice
- **"He sits at our table"**: Phrase attributed to Thomas in Clara's interiority (though not spoken by Thomas on-page)
- **"The honest way isn't usually the easy way"**: Samuel's line; establishes his signature philosophical directness

## Threads Advanced

- **Clara-Samuel courtship (first conversation, mutual assessment)**: The tea scene is the first real conversation between Clara and Samuel. Both demonstrate intelligence, directness, and mutual respect. Clara shares a fraction of her holdings; Samuel shares Wallace intelligence freely. The handshake establishes "the ground where trust could grow." Clara's progressive disarmament continues (dark green silk, no leather coat, sword cane only).
- **Anti-trafficking campaign (Wallace named as escalating threat)**: Samuel connects the Mercy Jane to Wallace's larger port-control and trafficking operation. The Mercy Jane reframed from isolated incident to "symptom" of a systemic disease.
- **Thomas Arlington's jealousy seeds (excluded from tea, delivers intel then watches Clara leave)**: Thomas delivers the dossier in the morning, then Clara goes inside to dress for tea with Samuel. Thomas stays in the courtyard with his portfolio. He is not invited to the tea. The structural exclusion is rendered subtly -- Clara walks away, Thomas keeps working.

## Threads That Could Be Advanced Here

- **Harper's role**: Harper does not appear in ch-03. Given that Clara's daily schedule (established in ch-01, line 152) includes reviewing Thomas's findings "over tea with Harper," his absence from the morning briefing scene is notable. This is not an error -- the schedule was aspirational, and events have overtaken routine -- but the author might consider a brief mention of Harper's whereabouts (e.g., managing the cleanup from the night's dock disturbance at the end of ch-02).
- **George's bond with Samuel**: George is deliberately absent from the tea scene (line 89: "She had left him at the townhouse, and the absence was deliberate. Samuel Taylor had met George in combat. She wanted him to meet her in conversation."). This is well-motivated and sets up future George-Samuel bonding scenes (ch-04 onward, per bible).
