# Continuity Report: Book 1, Chapter 24

**Checker version**: v2 (with scene-internal knowledge / presence-map logic)
**Date**: 2026-03-05

---

## Presence Map

### Scene 1: Cruces Village (lines 22-64)

| Beat | Characters Present | Entrances / Exits | Information Exchanged |
|------|-------------------|-------------------|----------------------|
| Arrival at Cruces | Samuel, Reyes, Clara, Harper, George, Davis, Marsh, Cole, Jennings, Lily, Ajax | All disembark from bungos | -- |
| Reyes negotiates mules | Reyes, mule trader (visible to Samuel at distance) | -- | Reyes secures twelve mules (reported by Harper) |
| Clara distributes weapons | Clara, Davis, Marsh, Cole, Jennings, Samuel (observing) | Clara moves among company | Rifle to Davis, ammo to Marsh, pistol check for Cole, powder flask for Jennings |
| Clara inspects Samuel | Clara, Samuel | Clara comes to Samuel last | Clara notes pistol, tells him "the trail is mud" |
| Samuel watches Clara depart | Samuel (observing Clara) | -- | Samuel observes Clara's appearance (linen shirt, Colts, sword cane) |
| Harper arrives at Samuel's side | Samuel, Harper | Harper approaches | Harper reports: 12 mules, trail "passable"; reveals Lily shooting since Kingston |
| Harper discusses Lily | Samuel, Harper | -- | Harper taught Lily mornings since Kingston; Samuel reflects on Harper's 4 years with Clara |

### Scene 2: The Mule Trail (lines 66-107)

| Beat | Characters Present | Entrances / Exits | Information Exchanged |
|------|-------------------|-------------------|----------------------|
| Trail begins, column forms | Reyes (front), Clara, Harper, George, Samuel (middle, on mule), Lily (behind, on mule), Ajax, Cole, Jennings, Davis, Marsh (rear) | All on trail, single file | Reyes: "Eighteen miles" |
| Two hours in, Reyes stops | All in column | -- | Reyes and Harper find broken branches, recent fire ash |
| Harper reports to Samuel | Harper, Samuel | Harper walks back along column | Harper: someone passed within the day, several on foot, fire hidden; "A man waiting for something hides his fire" |
| Clara redistributes weapons | Clara (moving along column), all company | -- | Company tightens formation |
| Samuel's pistol reflection | Samuel (interiority) | -- | 13 days of carrying; Harper's maintenance, familiar weight |
| Harper's listening lesson recalled | Samuel (interiority) | -- | Samuel recalls Harper teaching attention on Caroline, Kingston, Chagres |

### Scene 3: Night Camp (lines 108-139)

| Beat | Characters Present | Entrances / Exits | Information Exchanged |
|------|-------------------|-------------------|----------------------|
| Camp at dusk | All company | -- | Reyes: no fire. Dried provisions. |
| Watch positions | Cole, Davis (trail watch), Jennings, Marsh (flanks) | Sentries deployed | -- |
| Samuel sits against tree | Samuel, pistol in lap | -- | Cannot sleep; reflects on jungle sounds vs. ocean |
| Clara sits beside Samuel | Clara joins Samuel | Clara arrives | Shared silence, no speech initially |
| Thomas correspondence codes | Samuel (interiority) | -- | Second checkpoint: Panama City; Thomas's handwriting, cipher, wax |
| "You'll write" exchange | Clara, Samuel | -- | Clara states certainty they'll arrive; Samuel agrees |
| Samuel's love reflection | Samuel (interiority) | -- | What he loves about Clara: her certainty; vulnerability shown once on riverfront walk |
| George and Ajax | George at Clara's feet, Ajax with Lily (elsewhere in dark) | -- | -- |
| Harper at picket line | Harper (audible) | -- | Harper issuing watch instructions |

### Scene 4: Dawn (lines 140-163)

| Beat | Characters Present | Entrances / Exits | Information Exchanged |
|------|-------------------|-------------------|----------------------|
| Dawn, Samuel wakes | Samuel | -- | Slept 1-2 hours |
| Clara checking Colt | Clara (visible to Samuel) | Already standing | Cylinder check: breach, caps, rotation |
| Samuel imitates Clara's routine | Samuel | -- | Checks own pistol same way; absorbed by watching Clara |
| Harper observes Samuel | Harper (10 feet away) | -- | Sees Samuel checking pistol like Clara; says nothing |
| Reyes returns from scouting | Reyes | Emerges from trail ahead | Speaks to Harper; 8 miles to Panama City |
| Harper announces distance | Harper, full company | -- | "Eight miles. Panama City by midday if the trail holds." |
| Company forms, moves out | All | -- | Single file, weapons ready |

---

## Errors (must fix)

### 1. Trail Distance Contradiction: "Eighteen miles" vs. "Twenty miles" ✓ FIXED (2026-03-05): Changed all three "eighteen miles" instances to "twenty miles" in ch-24 body text (lines 68, 134, 162) and YAML frontmatter. Outline also updated.

- **[continuity -- cross-chapter]**: Ch-24 states the mule trail is eighteen miles (line 68: "Eighteen miles"), and Samuel later reflects on "eighteen miles of mud" (line 134). Ch-23 states "Twenty miles of jungle" (ch-23, line 99) in its prose text, and the ch-23 frontmatter also says "twenty miles."
- **Draft says (ch-24)**: "Eighteen miles" (lines 68, 134, 162)
- **Previous chapter says (ch-23)**: "Twenty miles" (line 99, frontmatter thread)
- **Outline says**: The ch-23 outline beat says "eighteen miles," but the ch-23 revision log shows the historian changed "18 to 20 miles" during revision. The ch-24 outline also says "eighteen miles."
- **Location**: Lines 68, 134, 162 of ch-24; line 99 of ch-23
- **Note**: The historian's revision of ch-23 changed 18 to 20 miles (per the continuity notes revision record). Ch-24 was drafted after that revision but uses the pre-revision figure. One or the other must be corrected for consistency.

### 2. "Eighteen miles of mud" Before Completing Eighteen Miles ✓ FIXED (2026-03-05): Changed "eighteen miles of mud" to "twelve miles of mud" (20 total - 8 remaining = 12 walked). Arithmetic now correct.

- **[scene-internal logic]**: At the night camp (line 134), Samuel reflects that he "had walked eighteen miles of mud without complaint." However, at dawn the next morning, Harper announces "Eight miles" to Panama City (line 156). If the trail is eighteen miles total and eight remain, Samuel has only walked approximately ten miles by the time of his nighttime reflection. The "eighteen miles" claim is premature.
- **Draft says**: "how he had walked eighteen miles of mud without complaint" (line 134, during the night camp scene)
- **Fact**: The night camp is made at dusk after the first day's march, with eight miles still remaining. Samuel has walked roughly ten miles, not eighteen.
- **Location**: Line 134

### 3. "Thirteen days of carrying" -- Timeline Arithmetic ✓ FIXED (2026-03-05): Changed "over thirteen days of carrying" to "over a week of carrying" — matches 7-9 day timeline from Kingston (April 17-18) to ch-24 (April 25-26).

- **[continuity -- timeline]**: Ch-24 says Samuel's pistol weight "had become, over thirteen days of carrying, a fact about his body" (line 102). Harper mentioned "requesting permission from Miss Chen to purchase firearms for Mr. Taylor" in Kingston (ch-22, April 17-18). The ch-24 frontmatter places the chapter on April 25-26. From April 18 (the latest he could have received the pistol in Kingston) to April 25 is seven or eight days, not thirteen. Even if the pistol was issued April 12 (the earliest possible -- the day they arrived in Kingston, per ch-22's April 17 timeline, which itself is wrong if he's counting from the actual purchase), thirteen days is difficult to reconcile. The ch-24 continuity notes themselves say the pistol was "issued by Harper in Kingston (ch-22)."
- **Draft says**: "over thirteen days of carrying" (line 102)
- **Timeline says**: Kingston is April 17-18 (ch-22); ch-24 is April 25-26. That is 7-9 days, not 13.
- **Location**: Line 102

---

## Warnings (review needed)

### 1. Harper's Tenure: "Four years" Consistency Check

- **[character detail]**: Ch-24 says "Harper had spent four years standing between Clara and what threatened her" (line 62). This is consistent with ch-21 ("where he had stood for four years," line 76), ch-23 ("she had watched Harper for four years," line 95), ch-08 ("four years of mornings," line 31), and ch-13 ("built watch patterns for four years," line 77). However, the timeline places Book 1 opening in ~1846 and the voyage in April 1847. If Harper has served four years, he started circa 1842-1843, when Clara was approximately 12-13 years old (born ~1830s, age 25 at series opening ~1846). Author should verify: did Harper begin serving Clara at age 12-13, or should the tenure be shorter (e.g., "three years" if starting at ~18)?
- **Bible says**: Harper's tenure is not specified with a start date; "four years" is established across multiple chapters.
- **Location**: Line 62

### 2. Lily's Sketchbook "Closed for Once"

- **[minor detail]**: The text says Lily is "standing at the treeline with Ajax, her sketchbook closed for once" (line 54). In ch-23, Lily had her "sketchbook open on her knees, her pencil moving" (ch-23, line 67), and in ch-22 the sketchbook was "closed in her lap" during the pirate hold scene (ch-22, line 40). The "for once" phrasing implies Lily usually has it open, which is consistent with ch-23 and her artist characterization. No error, but "for once" slightly overstates the pattern given that she also had it closed during the hold scene.
- **Location**: Line 54

### 3. Samuel's "Counting table" Reference

- **[POV interiority]**: Samuel reflects on Clara's certainty as "the assessment of a man across a counting table" (line 130). This alludes to their first real meeting at the Chestnut Street parlor (ch-03) or perhaps to Clara visiting his warehouse counting table (ch-06, ch-12, ch-14, ch-15). Both are plausible memories for Samuel. No error, but the phrasing could refer to either -- author should confirm which resonance is intended.
- **Location**: Line 130

### 4. Pipe Tobacco Consistency

- **[character detail -- verified consistent]**: Harper "smelled of sweat and quinine and the pipe tobacco he carried but never smoked" (line 46). This matches ch-20 exactly: "the pipe tobacco he carried but never seemed to smoke" (ch-20, line 129). Consistent. No action needed.

### 5. Jennings's Injury Reference

- **[character detail]**: Jennings is "testing his shoulder -- the pirate's graze still tender beneath the bandage" (line 54). Ch-21 established "Jennings took a graze. Left shoulder" (ch-21, line 152), and ch-22 confirmed "his left shoulder bandaged" (ch-22, line 58). Ch-24 does not specify which shoulder, but says "his shoulder." This is technically consistent but less specific. The injury is approximately 10 days old (April 15-16 to April 25), which is plausible for ongoing tenderness with a bandage. No error.
- **Location**: Line 54

---

## Scene-Internal Knowledge Verification

### Samuel's Knowledge Inventory

| Fact Samuel states or knows | Source | Verified? |
|----------------------------|--------|-----------|
| Harper spent four years with Clara | Established across multiple chapters; plausible shared knowledge | Yes |
| Lily has been shooting since Kingston | Harper tells him directly in this scene (line 60) | Yes |
| Clara showed him vulnerability once on a riverfront walk | He was present at ch-06 riverfront walk (his experience, Clara's POV) | Yes |
| Thomas's correspondence codes, handwriting, cipher, wax | Established in ch-22 (line 166), ch-23; Samuel carries these | Yes |
| Clara survived pirates | Samuel was aboard the Caroline during ch-21 pirate fight | Yes |
| Clara crossed the Atlantic | Samuel was aboard the Caroline for the crossing | Yes |
| Clara navigated a river through jungle | Samuel was on the Chagres (ch-23, bungo 2) | Yes |
| Harper taught him to listen (Caroline, Kingston, Chagres) | Established across ch-20, ch-22, ch-23 | Yes |
| Clara's routine weapon check every morning since the Caroline | Samuel has been aboard since ch-19; plausible repeated observation | Yes |
| Clara's assessment of a man across a counting table | Samuel present at ch-03 tea and Clara's warehouse visits | Yes |
| The pistol was issued by Harper in Kingston | Stated in ch-24 narrative (line 34); Harper requested permission in ch-22 | Yes (though see timeline error above) |
| Second checkpoint is Panama City (Thomas's system) | Samuel carries the codes; plausible he was briefed | Yes |

### POV Discipline

- POV is Samuel Taylor throughout. No breaks detected.
- All observations are limited to what Samuel can see, hear, or plausibly infer.
- Interiority is consistently Samuel's: his merchant-body protests, his reflections on Clara, his awareness of Harper.
- One minor note: Samuel knows Clara "had crossed the Atlantic, survived pirates, navigated a river" (line 130) -- this is phrased as his observation of her journey, not as secret knowledge. Verified.

### Character Presence Tracking

- The company is fully accounted for: Reyes, Clara, Harper, George, Samuel, Lily, Ajax, Davis, Marsh, Cole, Jennings.
- No dead or absent characters appear unexpectedly.
- Tierney (mentioned in ch-21, ch-23) is absent -- he stayed with the Caroline in Kingston (per the ch-23 revision notes). His absence is unremarked, which is consistent.
- The bungo boatmen are not mentioned at Cruces -- they presumably returned with the bungos. This is implicit and reasonable.

---

## New Facts Introduced

- **Cruces village**: Dozen structures of lashed wood and thatched palm above a gravel bank; mule corrals of stripped poles; smell of dung and cook smoke. (Not previously described.)
- **Clara's canvas satchel**: Carried from Kingston, containing weapons for distribution.
- **Samuel's pistol specifics**: .36 caliber Colt Paterson, issued by Harper in Kingston, cleaned and loaded by Harper. Walnut grip.
- **Twelve mules**: Secured by Reyes at Cruces for the overland trail.
- **Camino de Cruces details**: Road of Crosses, Spanish colonial, three centuries old. Dressed stone blocks erupting through mud. Built for Peruvian gold/silver transport.
- **Trail threat signs**: Broken branches at man-height, recent fire ash concealed at trail's margin. Someone passed within the day, several on foot.
- **Harper's assessment of threat**: "A man waiting for something hides his fire" -- distinguishes bandits from organized ambush.
- **Night camp location**: Hollow where trail widened and a stream crossed. No fire (Reyes specific). Dried provisions.
- **Samuel's weapon ritual**: Unconsciously imitates Clara's cylinder-check routine. Harper observes and says nothing.
- **Lily continues shooting practice**: Since Kingston, mornings, at her request. Harper taught her.
- **Eight miles remaining at dawn**: Reyes scouts, reports eight miles to Panama City; midday arrival if trail holds.

---

## Threads Advanced

- **Clara-Samuel courtship**: Night camp proximity without performance -- Clara sits beside him, not touching. Samuel identifies what he loves: her certainty. He walks because she walks. Deepening emotional bond expressed through restraint.
- **Harper's arc before death**: Peak competence on the trail. Reads signs with Reyes, teaches Lily, organizes the column, issues watch instructions. "The last morning of the man who stood between other people and what threatened them." Harper observes Samuel's transformation (imitating Clara's weapon check) and says nothing -- the compliment he would never deliver.
- **Thomas Arlington's jealousy seeds**: Correspondence codes in Samuel's pocket. Thomas's handwriting, cipher, wax. The second checkpoint is Panama City. Samuel will write to "the people who had left him behind." Thomas's infrastructure sustains them but his person is absent.
- **Samuel's transformation**: The pistol shifts from instrument to extension. At dawn, he checks it the way Clara checks hers -- unconscious imitation, identity change in progress.

---

## Threads That Could Be Advanced Here

- **Wallace/antagonist thread**: The trail threat (concealed fire, organized human presence) could be connected to Wallace's network, paralleling the "not random" pirate attack in ch-21. Currently left ambiguous -- opportunity for explicit or implicit connection.
- **Clara's disarmament pattern**: Clara is in her "jungle register" (linen, shoulder rig, sword cane) with no coat. The chapter could note this is the most stripped-down Samuel has ever seen her outside of training -- continuing the armor-as-emotional-register thread.
- **Thomas's one-man-who-didn't-fire thread**: Ch-21 planted Tierney (Thomas's recommendation) not firing during the pirate attack. His absence from the company could be noted by Samuel or Harper as relevant to the trail threat.

---

## Summary of Required Fixes

| # | Type | Description | Location |
|---|------|-------------|----------|
| 1 | Cross-chapter contradiction | Trail distance: "eighteen miles" (ch-24) vs. "twenty miles" (ch-23 revised prose) | Lines 68, 134, 162 |
| 2 | Scene-internal logic | Samuel reflects on "eighteen miles of mud" at the night camp, but eight miles remain | Line 134 |
| 3 | Timeline arithmetic | "Thirteen days of carrying" the pistol, but Kingston to Cruces is 7-9 days | Line 102 |
