---
name: revise
description: Revise a chapter using all four subagents in parallel
user_invocable: true
arguments:
  - name: book
    description: Book number (1-9)
    required: true
  - name: chapter
    description: Chapter number
    required: true
---

# /revise — Chapter Revision Workflow

Revise chapter ${chapter} of book ${book} using all four analysis subagents.

## Step 1: Read the Chapter

Read `books/book-0${book}/chapters/ch-$(printf '%02d' ${chapter}).md` to understand what needs revision.

## Step 2: Run All Four Subagents in Parallel

Launch all four subagents simultaneously, each analyzing the chapter from their specialty:

1. **continuity-checker** (Opus): Check all facts against the bible
   - Prompt: "Check `books/book-0${book}/chapters/ch-$(printf '%02d' ${chapter}).md` for continuity errors against the series bible. Follow your agent instructions in `.claude/agents/continuity-checker.md`."

2. **historian** (Opus + WebSearch): Fact-check historical claims
   - Prompt: "Check `books/book-0${book}/chapters/ch-$(printf '%02d' ${chapter}).md` for historical accuracy. Follow your agent instructions in `.claude/agents/historian.md`."

3. **style-reviewer** (Sonnet): Check prose style and POV discipline
   - Prompt: "Review the prose style of `books/book-0${book}/chapters/ch-$(printf '%02d' ${chapter}).md`. Follow your agent instructions in `.claude/agents/style-reviewer.md`."

4. **character-analyst** (Opus): Check voice and arc consistency
   - Prompt: "Analyze the characters in `books/book-0${book}/chapters/ch-$(printf '%02d' ${chapter}).md`. Follow your agent instructions in `.claude/agents/character-analyst.md`."

## Step 3: Synthesize Findings

Compile all subagent reports into a unified revision plan:

```markdown
## Revision Plan: Book ${book}, Chapter ${chapter}

### Critical (Must Fix)
<!-- Continuity errors, historical inaccuracies that break immersion -->

### Important (Should Fix)
<!-- POV violations, voice inconsistencies, arc issues -->

### Minor (Consider Fixing)
<!-- Prose polish, pacing tweaks, missed opportunities -->

### New Bible Entries Needed
<!-- Facts from this chapter that should be added to the bible -->
```

Present this plan to the user for approval.

## Step 4: Apply Approved Edits

Once the user approves (or adjusts) the revision plan:

1. Apply edits to the chapter file, working from most critical to least
2. Preserve the author's voice — edits should be invisible
3. Update frontmatter: set status to `revised`, update word_count and summary if changed
4. Update `books/book-0${book}/notes/revision-log.md` with a summary of changes made

## Step 5: Curate Bible

After revision edits are applied, process the chapter's continuity notes into the bible. This closes the feedback loop — facts introduced during drafting are verified during revision and now enter the canonical bible.

1. Read `books/book-0${book}/notes/continuity-notes.md`
2. Find all entries for chapter ${chapter} marked `added to bible? no`
3. For each entry, classify as:
   - **(a) Update Bible Now** — facts that affect future chapters (character traits, relationships, plot details, locations, timeline events, skills, speech patterns)
   - **(b) Skip** — atmospheric/scene-specific detail the bible doesn't need
   - **(c) Needs Author Decision** — conflicts with existing bible content, ambiguous, or has downstream implications
4. For **(a)** entries: update the relevant bible files following bible-maintenance checklists (update both sides of relationships, note source chapter)
5. Mark processed entries: `added to bible? yes` or `added to bible? skip — [reason]`
6. Leave **(c)** entries as `added to bible? no` and flag them in the revision report
7. Present a brief curation summary:
   - **Updated**: N entries → [which bible files]
   - **Skipped**: N entries
   - **Needs Author Decision**: N entries → [what and why]
