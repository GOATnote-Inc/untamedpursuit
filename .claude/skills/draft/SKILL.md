---
name: draft
description: Draft a chapter with full bible context loaded
user_invocable: true
arguments:
  - name: book
    description: Book number (1-9)
    required: true
  - name: chapter
    description: Chapter number
    required: true
---

# /draft — Chapter Drafting Workflow

Draft chapter ${chapter} of book ${book} with full series context.

## Step 1: Load Context

Read all of the following files to establish context before writing:

1. `books/book-0${book}/outline.md` — Find the outline entry for chapter ${chapter}
2. `books/book-0${book}/CLAUDE.md` — Book-specific premise, POVs, arcs
3. `bible/characters/` — Read the POV character's profile, then profiles of all characters appearing in this chapter (per outline)
4. `bible/timeline/book-0${book}-timeline.md` — Timeline context for this chapter's events
5. `bible/relationships/relationship-map.md` — Dynamics between characters in this chapter
6. `bible/mysteries/open-threads.md` — Threads that could be advanced
7. `books/book-0${book}/notes/continuity-notes.md` — Any flags from previous chapters

If this is not chapter 1, also read the previous chapter:
8. `books/book-0${book}/chapters/ch-$(printf '%02d' $((${chapter} - 1))).md`

## Step 2: Confirm Plan

Before writing, summarize:
- **POV character**: [name and current emotional state]
- **Scene(s)**: [what happens in this chapter per the outline]
- **Location & time**: [where and when]
- **Characters present**: [who appears]
- **Threads to advance**: [which open threads this chapter touches]
- **Key beats**: [the outline's required story beats]

Ask the user to confirm or adjust before proceeding.

## Step 2.5: Write Compaction Anchor

Before beginning the draft, write a compaction anchor file to protect context if compaction occurs mid-chapter:

**File**: `books/book-0${book}/notes/ch-$(printf '%02d' ${chapter})-anchor.md`

Include:
- **Chapter**: Book ${book}, Chapter ${chapter}
- **POV**: The POV character and their current emotional state
- **Outline beats**: The key beats from the outline for this chapter
- **Bible facts loaded**: The most important character, relationship, and world facts consulted for this chapter
- **Previous chapter landing**: How the previous chapter ended (emotional state, last scene, unresolved tension)
- **Threads active**: Which open threads this chapter advances
- **Continuity flags**: Any flags from previous chapters that apply here

If compaction occurs mid-draft, reload this file first to recover full drafting context.

## Step 3: Draft

Write the chapter following these rules:
- Use the chapter template from `.claude/skills/draft/templates/chapter-template.md`
- Fill in YAML frontmatter completely
- Third-person limited, past tense, from the designated POV character
- Follow the outline beats but allow organic discovery
- Use each character's documented speech patterns
- Mark any concerns with `<!-- FLAG: ... -->` comments
- Aspire to prose vitality: curiosity, wit, surprising imagery, varied rhythm (see `.claude/rules/prose-craft.md`)
- Target the word count suggested in the outline, or 3,000-5,000 words if unspecified

## Step 4: Post-Draft Bookkeeping

After completing the draft:

1. **Update frontmatter**: Set word_count, summary, threads_advanced, threads_introduced, and any continuity_flags
2. **Log new facts**: If the chapter introduced any new facts not in the bible (character details, place descriptions, timeline events), log them in `books/book-0${book}/notes/continuity-notes.md`
3. **Log deviations**: If the chapter deviated from the outline, note how and why in `books/book-0${book}/notes/continuity-notes.md`
4. **Report**: Summarize what was written, any flags raised, and threads advanced

## Step 5: Remind About Progress

After completing bookkeeping, note: "README progress section may be out of date. Run `/progress` to update before pushing."
