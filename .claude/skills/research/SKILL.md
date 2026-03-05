---
name: research
description: Research a historical topic with sources and documentation
argument-hint: <topic>
---

# /research — Historical Research Workflow

Research "${topic}" for the Untamed Pursuit series.

## Step 1: Check Existing Research

Search the existing research base before going external:

1. Search `research/` for existing coverage of this topic
2. Search `bible/world/` for related world-building entries
3. Check `research/sources.md` for already-documented sources on this topic

If the topic is already well-covered, summarize what we have and ask the user if deeper research is needed.

## Step 2: External Research

Use WebSearch to find reliable information:

1. Search for the topic with academic/scholarly terms
2. Prefer primary historical sources and peer-reviewed scholarship
3. Cross-reference multiple sources for contested claims
4. Note the distinction between established fact, scholarly consensus, and debated interpretation

## Step 3: Document Findings

Write findings to the appropriate location in `research/`:

- **Historical events** → `research/historical-events/[topic].md`
- **Period details** (daily life, culture, technology) → `research/period-details/[topic].md`
- **Fact-checks** (verifying claims in drafts) → `research/fact-checks/[topic].md`

Use this format:

```markdown
# [Topic]

## Summary
[Concise overview of findings]

## Details
[Detailed findings organized by subtopic]

## Sources
1. [Author, Title, Year — specific page/section if available]
2. [URL — accessed date]

## Relevance to Untamed Pursuit
[How this applies to the series — which books, chapters, characters, or scenes]

## Open Questions
[What we still don't know or couldn't verify]
```

## Step 4: Update Master Bibliography

Add all new sources to `research/sources.md` in the appropriate section.

## Step 5: Cross-Reference Bible

If the research reveals information that should update the bible:

1. Identify which bible files would benefit (world-building, timeline, character backgrounds)
2. Present proposed updates to the user
3. On approval, update bible files following bible-maintenance rules

## Step 6: Report

Summarize:
- Key findings
- Sources consulted
- How this affects the series
- Recommended bible updates
- Remaining gaps in knowledge
