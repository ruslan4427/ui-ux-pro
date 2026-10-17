---
name: ui-ux-pro
description: UI/UX design skill. Use whenever the user wants to design, build, refine, polish, or redo any interface or visual UI work — even one-liners like a single WCAG contrast check or picking one color. Covers pages, screens, components, layouts, hero sections, forms, dashboards, checkout flows, settings, landing pages, empty/loading states, modals. Triggers include picking color palettes, font pairings, or typography; fixing spacing/padding/visual hierarchy or a "cramped/off/generic" feel; cleaning up inconsistent tokens or shades; choosing UI patterns (skeletons, cards, empty states); making something feel more distinctive, on-brand, or warmer; mobile/responsive polish; accessibility, contrast, focus states, keyboard nav. Always starts from the project's own existing design tokens instead of inventing new ones. Applies to both new projects (needs vibe/palette/fonts) and existing ones (needs consistency). Do NOT use for backend/API/database design, CLI/terminal styling, code refactors, config-only edits (e.g. adding a color to tailwind.config with no design decision), architecture diagrams, or debugging test failures — even when those queries mention design/dashboard/color words.
---

# ui-ux-pro

Two jobs: keep a project's own design system consistent, and bring in current
design thinking without breaking that system.

If the user asks for a specific taste direction ("minimalist", "brutalist",
"editorial", etc.), see section 5 — load the matching file from
`references/styles/` first, since it deliberately overrides some of the
defaults in the sections below.

## 1. Always start from the project's own tokens

Before suggesting any color, font, or spacing value, run:

```bash
python3 scripts/extract_tokens.py <path-to-project>
```

It looks for design tokens already in use — a `CLAUDE.md`/`AGENTS.md` design
system section, a Tailwind `@theme` block, `:root` CSS custom properties, or a
`tailwind.config.*`. If the project has an existing system, work inside it.
Never invent a new palette for a project that already has one — extend it.

If the project has no tokens yet (new project), that's the signal to pull from
`references/palettes.md` and `references/typography.md` instead.

## 2. Check accessibility before calling anything done

Run every text/background color pair through:

```bash
python3 scripts/check_contrast.py <fg-hex> <bg-hex>
```

It reports the WCAG contrast ratio and pass/fail at AA and AAA, for normal and
large text. Cross-check against `references/accessibility-checklist.md`
(touch targets, focus states, aria attributes) before marking UI work done.

## 3. Verify visually, not just in code

After implementing a UI change, use the browser tools already available in
this session (the built-in Browser pane, or Claude in Chrome if the user asks
for it) to open the running dev server and look at the actual result — don't
just trust the diff. Take a screenshot, compare against the tokens extracted
in step 1, and check at both mobile and desktop widths.

## 4. Pull in current design thinking

`references/trends.md` and `references/palettes.md` are refreshed on a
schedule (see `CHANGELOG.md` for the last refresh date). Use them for:

- **New projects** — pick a direction from `trends.md`, a palette from
  `palettes.md` that passes contrast, a pairing from `typography.md`.
- **Existing projects** — compare the project's current patterns against
  `trends.md` and flag what reads as dated, but only change what the user
  asked to update. Don't do a wholesale redesign uninvited.

If `CHANGELOG.md`'s last refresh is more than ~2 months old, say so before
relying on `trends.md` — it may be stale.

## 5. Style selection (opt-in)

The default direction from sections 1–4 aims for a broadly good, safe SaaS
result. If the user signals a specific taste direction, that's an intentional
override — read the matching file from `references/styles/` and follow *its*
typography, palette, layout, motion, and forbidden lists in preference to
the general defaults.

Common triggers → files:

- "minimalist", "editorial", "Notion/Linear/Vercel feel", "quiet premium",
  "document-style" → `references/styles/minimalist.md`
- "brutalist", "Swiss", "terminal", "raw", "industrial", "hard-edged" →
  `references/styles/brutalist.md`
- "Lusion feel", "immersive", "WebGL-first", "cinematic portfolio",
  "scrollytelling", "shader-driven", "creative studio", "award-worthy" →
  `references/styles/lusion.md`

Check `references/styles/` for other files as they get added. If none match
what the user described, stay on the section 1–4 defaults and ask whether
they want to add a new style file (see `references/styles/README.md` for
the format) — don't invent a style silently.

Two rules that always apply, even under a style override:

- Extract tokens first (section 1) — if the project already has a design
  system, a style pick doesn't override that; it informs *new* decisions
  within it.
- Contrast still gets verified (section 2) — a style file's palette is a
  starting point, not a guarantee for a specific pair.
