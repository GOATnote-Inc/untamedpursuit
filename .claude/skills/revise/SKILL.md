---
name: revise
description: Revise a chapter using all five subagents in parallel
argument-hint: <book> <chapter>
---

# /revise — Chapter Revision Workflow

Revise chapter ${chapter} of book ${book} using all five analysis subagents.

## Step 1: Read the Chapter

Read `books/book-0${book}/chapters/ch-$(printf '%02d' ${chapter}).md` to understand what needs revision.

## Step 2: Run All Five Subagents in Parallel

Launch all five subagents simultaneously, each analyzing the chapter from their specialty:

1. **continuity-checker** (Opus): Check all facts against the bible
   - Prompt: "Check `books/book-0${book}/chapters/ch-$(printf '%02d' ${chapter}).md` for continuity errors against the series bible. Follow your agent instructions in `.claude/agents/continuity-checker.md`."

2. **historian** (Opus + WebSearch): Fact-check historical claims
   - Prompt: "Check `books/book-0${book}/chapters/ch-$(printf '%02d' ${chapter}).md` for historical accuracy. Follow your agent instructions in `.claude/agents/historian.md`."

3. **style-reviewer** (Sonnet): Check prose style and POV discipline
   - Prompt: "Review the prose style of `books/book-0${book}/chapters/ch-$(printf '%02d' ${chapter}).md`. Follow your agent instructions in `.claude/agents/style-reviewer.md`."

4. **character-analyst** (Opus): Check voice and arc consistency
   - Prompt: "Analyze the characters in `books/book-0${book}/chapters/ch-$(printf '%02d' ${chapter}).md`. Follow your agent instructions in `.claude/agents/character-analyst.md`."

5. **prose-brilliance** (Opus): Pressure-test for character honesty and narrative aliveness
   - Prompt: "Pressure-test `books/book-0${book}/chapters/ch-$(printf '%02d' ${chapter}).md` for character honesty, competence traps, admiration problems, and voice independence. Follow your agent instructions in `.claude/agents/prose-brilliance.md`."

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

## Step 3.5: Archive Subagent Reports

Save each subagent's report to `reports/` when it contains substantive findings. This makes all five agents' work independently retrievable.

- **continuity-checker**: Save to `reports/continuity-ch-${chapter}.md` (already standard)
- **historian**: Save to `reports/historian-ch-${chapter}.md` if errors, anachronisms, or period-detail opportunities were found
- **style-reviewer**: Save to `reports/style-ch-${chapter}.md` if POV breaks, pattern violations, or quantitative threshold breaches were found
- **character-analyst**: Save to `reports/character-analyst-ch-${chapter}.md` (already standard for significant findings)
- **prose-brilliance**: Save to `reports/prose-brilliance-ch-${chapter}.md` (already standard)

Clean passes (no findings) do not need separate reports — note "clean pass" in continuity-notes only.

## Step 4: Apply Approved Edits

Once the user approves (or adjusts) the revision plan:

1. Apply edits to the chapter file, working from most critical to least
2. Preserve the author's voice — edits should be invisible
3. Update frontmatter: set status to `revised`, update word_count and summary if changed
4. Update `books/book-0${book}/notes/revision-log.md` with an entry in this exact format:

```markdown
### Chapter ${chapter} — [YYYY-MM-DD]
- **Subagent findings**: [1-sentence summary per agent that found issues]
- **Changes made**: [bulleted list of edits applied, grouped by type]
- **Bible updates**: [bible files modified, or "None"]
- **Word count**: [before] → [after] ([+/-] net)
```

This step is mandatory — do not skip it even if changes were minor.

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
