# Workflow Conventions

## Git Rules

- Commit after completing a discrete unit of work (a chapter draft, a bible update, a research session)
- Commit messages follow: `[area] action description` — e.g., `[book-01] draft ch-03`, `[bible] add character profile: elena`, `[research] roman road networks`
- Never commit mid-sentence or mid-scene
- Use branches for experimental plot directions: `experiment/book-03-alt-ending`
- A **pre-commit hook** automatically updates the README progress section on every commit via `scripts/update-readme.py`. No manual step needed — just commit normally and the README stays current. To reinstall: `cp scripts/hooks/pre-commit .git/hooks/pre-commit`

## Subagent Usage

Use subagents to keep analysis work out of the main context window:

- **continuity-checker**: Run after drafting any chapter. Catches bible contradictions.
- **historian**: Run when a chapter references specific historical events, dates, or period details.
- **style-reviewer**: Run during revision. Catches POV breaks, tense slips, dialogue tag issues.
- **character-analyst**: Run when a character's behavior feels off or when introducing a character in a new book.

Always run subagents via the `/revise` skill to get parallel analysis.

## Context Management

- **`/clear`** between books and between work modes (drafting vs. research vs. bible maintenance)
- **`/compact`** mid-chapter — the root CLAUDE.md has instructions for what to preserve
- **Write state to files** — never rely on context alone. Chapters, notes, and research go on disk.
- **Worktrees** for parallel work streams:
  - `main` branch: bible, series-arc, finalized content
  - Drafting worktree: active chapter work
  - Research worktree: historical research sessions

## File Conventions

- All prose in Markdown (`.md`)
- One file per chapter: `ch-01.md`, `ch-02.md`, etc.
- One file per character: `bible/characters/firstname-lastname.md`
- Filenames are lowercase, hyphen-separated
- YAML frontmatter on all chapter files and character profiles
