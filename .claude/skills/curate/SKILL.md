---
name: curate
description: Process continuity notes backlog into the bible
argument-hint: <book>
---

# /curate — Bible Curation Workflow

Process the continuity notes backlog for book ${book} into the canonical bible.

The drafting workflow logs new facts to `books/book-0${book}/notes/continuity-notes.md` but does not update the bible. This skill closes that feedback loop — triaging each unprocessed entry and updating the bible so future chapters draft against complete, current profiles.

## Step 1: Load the Backlog

1. Read `books/book-0${book}/notes/continuity-notes.md`
2. Identify all entries marked `added to bible? no`
3. Count them and report: "Found N unprocessed entries across chapters X–Y."

## Step 2: Triage Each Entry

For every unprocessed entry, classify it into one of three categories:

### (a) Update Bible Now
Facts that affect how future chapters are written:
- Character motivations, personality traits, or backstory
- Relationship shifts or new relationship dynamics
- Plot-critical details (antagonists, alliances, betrayals)
- New character introductions or first appearances
- Physical descriptions that establish recognition cues
- Locations, operational details, or network infrastructure
- Timeline events (dates, sequences, durations)
- Speech patterns, habits, or distinctive behaviors
- Skills, weapons, or capabilities

### (b) Skip — Prose Handles It
Atmospheric detail the prose already conveys and that does not need bible-level tracking:
- One-time sensory details (specific food, weather in a single scene)
- Clothing items that are scene-specific, not character-defining
- Minor action choreography

### (c) Needs Author Decision
Flag for the user when:
- An entry conflicts with existing bible content
- The entry is ambiguous or could be interpreted multiple ways
- The detail could have downstream plot implications the author should weigh
- A character's established traits would change meaningfully

## Step 3: Update the Bible

For each **(a)** entry, update the relevant bible file(s) following the bible-maintenance rule checklists:

### Character Updates
- [ ] Update the character's own profile in `bible/characters/`
- [ ] Update all affected relationship entries (both characters)
- [ ] Update `bible/relationships/relationship-map.md` if relationship dynamics changed
- [ ] Note the source chapter (e.g., "Established in book-01, ch-03")

### Timeline Updates
- [ ] Add events to `bible/timeline/book-0${book}-timeline.md`
- [ ] Check for conflicts with existing timeline entries

### Mystery / Thread Updates
- [ ] Update `bible/mysteries/open-threads.md` if threads were advanced or introduced
- [ ] Note the chapter where advancement occurred

### World-Building Updates
- [ ] Update relevant files in `bible/world/` if locations or infrastructure were established

**Read each bible file before modifying it.** Apply changes carefully — the bible is the source of truth for the entire series.

## Step 4: Mark Entries as Processed

After updating the bible (or classifying as skip), change each processed entry from:
```
added to bible? no
```
to:
```
added to bible? yes
```

For **(b)** skipped entries, change to:
```
added to bible? skip — [brief reason]
```

Leave **(c)** entries as `added to bible? no` until the author decides.

## Step 5: Report

Present a summary to the user:

```markdown
## Curation Report — Book ${book}

### Updated (N entries)
- [bible file]: [what was added] (source: ch-XX)
- ...

### Skipped (N entries)
- [entry summary]: [reason]
- ...

### Needs Author Decision (N entries)
- [entry]: [why it needs a decision]
- ...

### Bible Files Modified
- [list of all files touched]
```

**Do NOT commit.** The user decides when to commit.
