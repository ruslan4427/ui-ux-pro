# ui-ux-pro

A Claude Code skill for UI/UX work. Two jobs:

1. **Keep a project's own design system consistent** — extract tokens that already exist, work inside them, don't invent new palettes for projects that have one.
2. **Bring in current design thinking without breaking that system** — curated palette, typography, and trend references + opt-in style directions (minimalist, brutalist, Lusion-style).

MIT licensed. No telemetry. No network calls. Runs locally.

## Install

Drop it into Claude Code's skills directory:

```bash
git clone https://github.com/ruslan4427/ui-ux-pro.git ~/.claude/skills/ui-ux-pro
```

Claude Code auto-loads any skill under `~/.claude/skills/` with a `SKILL.md`. No config.

The two helper scripts need Python 3:

```bash
python3 ~/.claude/skills/ui-ux-pro/scripts/check_contrast.py "#111" "#F5F4EF"
python3 ~/.claude/skills/ui-ux-pro/scripts/extract_tokens.py /path/to/your/project
```

## What it does

**Section 1 — Tokens first.** Before Claude suggests any color, font, or spacing value, it runs `extract_tokens.py` against the project. The script looks for:

- a `CLAUDE.md`/`AGENTS.md` design-system block
- a Tailwind v4 `@theme` block in CSS
- `:root { --token: value }` custom properties
- a `tailwind.config.{js,ts,mjs}`

If the project already has a system, Claude works inside it. If not, Claude pulls from `references/palettes.md` and `references/typography.md`.

**Section 2 — Accessibility.** Every text/background pair gets checked through `check_contrast.py`. Pass/fail at WCAG AA and AAA for normal and large text, before anything is called done.

**Section 3 — Visual verification.** After a UI change, Claude opens the dev server in a browser (via the built-in Browser pane or Claude in Chrome) and compares against the extracted tokens — not just the diff.

**Section 4 — Current design thinking.** `references/trends.md` and `references/palettes.md` are refreshed on a schedule (see [CHANGELOG.md](CHANGELOG.md) for the last refresh date). Used for new projects, and to flag what reads as dated on existing ones.

**Section 5 — Style selection (opt-in).** If you ask for a specific taste direction ("minimalist", "brutalist", "Lusion feel"), Claude loads the matching file from `references/styles/` and follows its typography, palette, layout, motion, and forbidden lists. Two rules still apply:

- Tokens come first — a style pick doesn't override an existing design system.
- Contrast still gets verified — a style file's palette is a starting point, not a guarantee for a specific pair.

## Scripts

### `scripts/extract_tokens.py <path>`

Prints what it found. Example output for a Tailwind v4 + CLAUDE.md project:

```
Found: CLAUDE.md design system block (23 lines)
Found: @theme inline (12 tokens)
  --color-ink: #111
  --color-paper: #F5F4EF
  --radius-card: 16px
  ...
```

### `scripts/check_contrast.py <fg> <bg>`

```
$ python3 check_contrast.py "#111" "#F5F4EF"
Contrast ratio: 18.47:1
Normal text:  AA PASS  AAA PASS
Large text:   AA PASS  AAA PASS
```

## References

- `references/palettes.md` — curated palettes grouped by vibe.
- `references/typography.md` — pairings (display + body) with licensing notes.
- `references/trends.md` — current design directions, refreshed periodically.
- `references/accessibility-checklist.md` — touch targets, focus states, aria attrs.
- `references/styles/` — style-specific overrides (minimalist, brutalist, lusion).

## When NOT to use

Backend/API design, CLI/terminal styling, pure code refactors, config-only edits, architecture diagrams, test debugging — even when those queries mention "design", "dashboard", or color words.

## Shipped by

[`claude-shiploop`](https://github.com/ruslan4427/claude-shiploop) — the discipline that produced this. See the case study at [hrekov.dev/work/claude-shiploop](https://hrekov.dev/work/claude-shiploop).

## License

MIT — see [LICENSE](LICENSE).
