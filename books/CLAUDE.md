# Books

## Structure

Each book lives in its own directory: `book-01/` through `book-09/`.

### Per-Book Contents
- `CLAUDE.md` — Book-specific context: premise, POV characters, major arcs, time period, key locations, mysteries introduced/resolved
- `outline.md` — Chapter-by-chapter outline with beats, POV assignments, and word count targets
- `chapters/` — One Markdown file per chapter (`ch-01.md`, `ch-02.md`, etc.) with YAML frontmatter
- `notes/` — Working notes:
  - `revision-log.md` — Record of revisions and changes
  - `continuity-notes.md` — New facts, deviations from outline, continuity flags

## Conventions
- Chapter files use zero-padded numbers: `ch-01.md`, not `ch-1.md`
- Every chapter file starts with YAML frontmatter (see root CLAUDE.md for format)
- Chapters are drafted sequentially — don't skip ahead without flagging dependencies
- Cross-book references use the format `book-XX/ch-XX`

## Workflow
1. Review the book's `CLAUDE.md` and `outline.md` before starting any chapter
2. Use `/draft [book] [chapter]` to draft with full context loading
3. Use `/revise [book] [chapter]` to revise with subagent analysis
4. Update `notes/continuity-notes.md` after every drafting session
5. Use `/clear` before switching to a different book
