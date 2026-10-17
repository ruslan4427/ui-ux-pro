# Current UI/UX trends

**Last refreshed:** 2026-09-20

Each entry: what it is, when it fits, when it doesn't.

## Layout

- **Bento grids** — asymmetric card grids of varying sizes on one canvas.
  Fits dashboards and landing pages with heterogeneous content. Don't force
  it on data tables or long-form reading content.
- **Card-based architecture that scales** — card grids (Linear/Notion/Vercel
  pattern) absorb new feature surface without restructuring the layout. Fits
  SaaS with 5–50 features; overkill for a single-purpose tool with one
  primary action.
- **Generous whitespace over dense chrome** — fewer visible controls, more
  air; secondary actions move into overflow menus. Fits consumer apps and
  marketing sites; fights against information-dense professional tools where
  density is a feature.
- **Wireframe-as-foreground** — visible grid logic, explicit stroke borders,
  structure worn on the outside (neobrutalist lean). Fits brands that want
  "built, not polished." Doesn't fit enterprise, healthcare, or anything
  where credibility depends on finish.

## Color

- **Warm dark mode over pure-black dark mode** — background in the `#0e–#1a`
  range with a hint of warmth rather than `#000000`. Reduces halation and
  makes elevation systems legible. Fits any dark-first product. Don't use
  pure black unless it's a deliberate stylistic choice (cinema, photography).
- **One saturated accent on a mostly neutral palette** — single accent does
  all the CTA work. High-contrast violet (`#8B5CF6` range) and amber/gold are
  the two dominant accent directions in 2026 SaaS. Fits everything. Breaks
  when a second "accent" is added to compete with the first.
- **Adaptive / context-responsive palettes** — palette shifts by mode
  (light/dark), product area, or user-preference signal. Fits design systems
  with token infrastructure. Don't attempt it without a token layer; hand-coded
  per-component overrides will rot.
- **Elevated neutrals** — warm sand, stone, slate, and cool zinc rather than
  flat gray. Fits premium, editorial, and SaaS products that want warmth
  without loud color. Doesn't distinguish well in very small UI chrome.

## Typography

- **Confident serif revival in display** — editorial serifs (Instrument
  Serif, Fraunces, Playfair Display) at large sizes signal premium/brand
  differentiation after years of geometric-sans uniformity. Fits marketing
  pages, content-led products, hospitality, editorial. Doesn't fit dense
  data UI where space is precious or brands that need to read technical.
- **Variable fonts** for weight/width control across a single file. Mandatory
  for performance-conscious products; one variable font replaces 6–10 static
  weight files. Fits all contexts. No real downside except toolchain learning
  curve.
- **Fluid responsive type with `clamp()`** — size adapts across breakpoints
  without discrete steps. Fits any product targeting a wide viewport range
  (phone to ultrawide). Avoid for components with fixed-size dependencies
  (table cells, fixed-height cards).

## Motion

- **Micro-interactions that explain state** — button press, form success,
  toggle, skeleton→content transitions. Kept under ~200 ms; signal, not
  decoration. Fits all contexts.
- **Scroll-triggered reveals replacing hero animations** — content enters as
  the user scrolls rather than playing an unmissable intro. Fits marketing
  and content pages. Skip on app dashboards where immediate data access
  is more valuable than drama.
- **`prefers-reduced-motion` respected by default** — see
  `accessibility-checklist.md`. Non-negotiable; do it everywhere.

## Components

- **Skeleton loaders over spinners** for content that takes >300 ms.
- **Inline validation** on forms (on-blur or as-you-type) over
  submit-then-error patterns.
- **Transparent AI disclosure** — when AI generates or surfaces content,
  label it clearly (confidence, source, editable state). Fits any product
  with AI output. Hiding AI provenance is both a UX and trust failure.
- **Command palette / `⌘K` interfaces** — keyboard-driven universal search
  and action hub. Fits power-user tools and SaaS apps with many features.
  Don't add it to simple single-purpose tools; it implies complexity.

## What's fading

- Heavy neumorphism — low contrast, accessibility problems, largely
  abandoned outside niche aesthetic projects.
- Auto-playing carousels for primary content — low engagement, accessibility
  friction; prefer a static hero with a clear single CTA.
- Jelly-bounce micro-animations and sparkle hover states — performative
  motion that communicates nothing about state or system intent.
- AI chat widgets on every screen — added as a default rather than a
  considered feature; creates noise and support burden without measurable
  clarity gain.
- Feature-heavy interfaces showing all controls at all times — cognitive
  overload; 2026's consensus is progressive disclosure and fewer default
  visible controls.
