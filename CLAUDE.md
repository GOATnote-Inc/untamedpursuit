# Untamed Pursuit — Series Bible & Style Guide

## Series Identity

**Untamed Pursuit** is a 9-book continuous historical fiction series with shared characters, a sequential timeline, and an interconnected world. Every book is a chapter in one larger story.

## Prose Style

- **POV**: Third-person limited. One POV character per chapter. Never break POV.
- **Tense**: Past tense. No present-tense narration except in direct thought.
- **Voice**: Literary but propulsive. Vivid sensory detail, precise period language, emotional interiority — but always in service of forward motion. No purple prose.
- **Dialogue**: Period-appropriate but readable. Characters have distinct speech patterns documented in their bible profiles. Use dialogue tags sparingly — "said" is default. Action beats over adverbs.
- **Pacing**: Scenes earn their length. Cut anything that doesn't advance plot, reveal character, or build world.

## The Bible Is Canon

The `bible/` directory is the single source of truth for all facts about this series:
- Characters, relationships, timeline, world-building, themes, and mysteries
- When drafting, **always consult the bible** before introducing facts about characters, places, or events
- If a chapter introduces new facts, **log them** in the book's `notes/continuity-notes.md`
- If a draft contradicts the bible, the **bible wins** — flag the discrepancy, don't silently resolve it

## Cross-Book Continuity

- Earlier books take precedence over later books in all factual disputes
- Characters age, learn, and change — but their core traits are consistent unless an arc explicitly transforms them
- Track every promise made to the reader (foreshadowing, mysteries, character goals) in `bible/mysteries/open-threads.md`
- Never introduce a character, place, or event that contradicts established canon without flagging it

## Chapter Frontmatter Format

Every chapter file (`books/book-XX/chapters/ch-XX.md`) begins with YAML frontmatter:

```yaml
---
book: 1
chapter: 3
title: "Chapter Title"
pov: "Character Name"
timeline: "Month Year"
location: "Place Name"
status: draft | revised | final
word_count: 0
summary: "One-sentence summary of the chapter's action."
threads_advanced: []
threads_introduced: []
continuity_flags: []
---
```

## Compaction Instructions

When running `/compact`, **always preserve**:
1. The current scene's state (where we are in the chapter, what just happened)
2. The POV character and their emotional/psychological state in this moment
3. Active plot threads being advanced in this chapter
4. Any continuity flags or unresolved questions raised during drafting
5. The chapter's frontmatter (book, chapter, POV, timeline, location, status)
6. Any pending revision notes or subagent feedback not yet addressed

## Work Modes

- **Drafting**: Creative, expansive. Follow the outline but allow organic discovery.
- **Editing**: Critical, precise. Minimal intervention. Every change must improve.
- **Research**: Academic rigor. Sources required. Primary over secondary.
- **Bible maintenance**: High caution. Read before modifying. Update both sides of relationships.

Use `/clear` when switching between work modes or between books.
