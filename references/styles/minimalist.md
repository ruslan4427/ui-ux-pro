# Minimalist / editorial

Notion-adjacent, document-style, ultra-restrained. Whitespace is the primary
element; type does the second-most work; color does the least.

**Fits:** knowledge tools, writing/reading apps, premium B2B where "quiet
confidence" is the brand read, portfolios, docs sites.
**Doesn't fit:** dense data dashboards, entertainment/consumer, anything where
users need at-a-glance scanability of many parallel elements.

## Typography

- **Sans display/body:** Geist Sans, Switzer, or SF Pro Display. Weight
  range 400–600, rarely bolder.
- **Optional serif accent:** Lyon Text, Newsreader, or Instrument Serif — for
  hero headlines or long-form article body. One serif per interface, max.
- **Mono for code/labels:** Geist Mono or JetBrains Mono.
- **Avoid:** Inter, Roboto, Open Sans. They read as SaaS-default and undercut
  the "hand-picked" feel this style depends on.
- **Icon set:** Phosphor or Radix. Avoid Lucide/Feather/Heroicons — they're
  the visual equivalent of Inter here.

Note: this contradicts `references/typography.md`'s Inter recommendation.
That's intentional — Inter is the safe *default*; this style is an
intentional override for projects going editorial/minimalist.

## Color

- **Canvas:** `#FFFFFF` (crisp) or `#F7F6F3` (paper-warm).
- **Text primary:** `#111111`. Secondary: `#787774`.
- **Borders:** `#EAEAEA` or `rgba(0,0,0,0.06)` — 1px, hairline.
- **Spot pastels for tags/callouts** (used sparingly, never for large fills):
  pale red `#FDEBEC`, blue `#E1F3FE`, green `#EDF3EC`, yellow `#FBF3DB`.
- No gradients. No neon. No dark saturated brand colors dominating layout.

## Layout

- Asymmetric bento grids with hairline `#EAEAEA` borders — no shadows
  separating cards, borders alone.
- Content width: `max-w-4xl` to `max-w-5xl` for reading; wider only for
  gallery/grid views.
- Vertical rhythm: `py-24` to `py-32` between major sections. Whitespace
  is a feature, not slack.
- Card interior padding: 24–40px. Border-radius: 8–12px (soft but not
  pillowy).

## Motion

- Scroll-entry: `translateY(12px)` + opacity fade over 600ms with a gentle
  cubic-bezier ease. That's it — one motion pattern for content reveal.
- Card hover: shadow shift `0 → 0 2px 8px rgba(0,0,0,0.04)` over 200ms.
- Only animate `transform` and `opacity`. Never animate layout properties.
- Always respect `prefers-reduced-motion`.

## Forbidden

Gradients, glassmorphism, heavy shadows, `rounded-full` containers,
emojis in UI chrome, clichéd copy ("Elevate", "Seamless", "Game-changer",
"Unlock"), stock 3D illustrations, auto-playing carousels.

## When someone asks for this

- "make it feel like Notion/Linear/Vercel"
- "editorial", "quiet", "premium but not corporate"
- "less SaaS-looking", "document-style", "reading app feel"
- "warm minimal", "paper feel"

Curated from public references; pattern originally articulated in
Leonxlnx/taste-skill's minimalist variant.
