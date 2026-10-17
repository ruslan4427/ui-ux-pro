# Industrial brutalist / tactical

Swiss-print rigor meets terminal/monitoring UI. Hard grids, extreme type-scale
contrast, mechanical color, zero softness. The opposite side of the taste
spectrum from `minimalist.md` — never mix the two.

**Fits:** developer tools, ops/monitoring dashboards, music/streetwear brands,
crypto/protocol projects, editorial with strong POV, art/design agency sites.
**Doesn't fit:** consumer apps requiring warmth or trust (banking, health,
family/kids), most B2B SaaS, e-commerce for mainstream goods.

## Typography

- **Display:** Heavy neo-grotesque at massive scale — Neue Haas Grotesk
  Display Black, Inter Black, or ABC Diatype Bold. Tight or slightly negative
  letter-spacing at display sizes.
- **Body:** Same or lighter weight of the display face. Keep the family
  narrow — one voice.
- **Data/labels:** Monospace — JetBrains Mono, IBM Plex Mono, Berkeley Mono.
  Frequently ALL-CAPS for labels and system-status text.
- Type scale should feel violent — display 96–200px next to body 14–16px.

## Color

Choose one mode; don't mix.

- **Swiss print (light):** bg `#F4F4F0` · fg `#050505` · single accent
  `#E61919` (Swiss red).
- **Tactical dark:** bg `#0A0A0A` · fg `#EAEAEA` · same red accent, or amber
  `#FFB000` for terminal feel.
- No secondary neutrals blending gradients. Text is one color, background is
  one color, accent is one color. Discipline.

## Layout

- Strict CSS Grid, borders visible — `1–2px solid` compartmentalizing every
  zone. Reads as a printed spec sheet.
- **No border-radius anywhere.** 90-degree corners, always.
- Extreme density alternating with vast negative space — dense metadata
  blocks next to hero cells with only a single glyph.
- Full-bleed content, edge-to-edge. No coddling max-widths.

## Motion

- Cursor/pointer-tracked halftone overlays, CRT scanlines via
  `repeating-linear-gradient`, subtle SVG grain overlay applied globally.
- Type: rare glitch/flicker on load; monospace counters that tick.
- Motion should feel mechanical, not friendly. No spring physics.
- Respect `prefers-reduced-motion` — replace grain/scanlines with static.

## Forbidden

Gradients (except linear halftone effects), soft shadows, translucency,
`border-radius`, floating/glassmorphic elements, illustrated mascots, pastel
accents, cursive/handwritten fonts, decorative dingbats.

## When someone asks for this

- "brutalist", "raw", "terminal aesthetic"
- "Swiss design", "Bauhaus", "no fluff"
- "hard-edged", "make it feel serious/technical/industrial"
- "monospace-first", "print feel"

Curated from public references; pattern originally articulated in
Leonxlnx/taste-skill's brutalist variant.
