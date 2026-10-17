# Immersive / Lusion

WebGL-driven cinematic canvas. The page *is* a scene: a fixed 3D background
reacts to cursor and scroll, content floats over it as a thin typographic
layer, motion is continuous rather than triggered. Deep monochrome dark canvas
+ one electric accent + oversized display type. Reference sites: lusion.co,
active-theory.com, basement.studio, studiofreight.com.

**Fits:** creative studio and agency portfolios, product launches with wow-
first budget, personal folios for creative developers, brand/experience sites
that can afford GPU cost.
**Doesn't fit:** dense B2B SaaS, forms-heavy apps, docs sites, e-commerce
catalogs, anything shipping to low-end devices or with strict a11y-first
mandates (WebGL background is a hard reduce-motion fallback problem).

## Typography

- **Display:** oversized editorial or geometric sans — PP Editorial New,
  Migra, Neue Machina, PP Neue Montreal, Söhne. 160–320px on desktop, tight
  or negative letter-spacing.
- **Body:** the same family in Light/Regular, or one contrasting geometric
  sans. Keep the family list to two.
- **Mono for chrome:** JetBrains Mono, Söhne Mono, Berkeley Mono — for
  coordinates, timestamps, section numbers, footer meta.
- **Reveal is the anim:** word-by-word or char-by-char translateY reveal on
  scroll via GSAP SplitText or Framer Motion staggered children. Never a
  plain fade-in at these sizes.
- **Avoid:** Inter/Roboto/Open Sans at display sizes — they read as SaaS.

## Color

- **Canvas:** near-black, slightly cool or warm — `#0A0A0A`, `#0E0E10`, or
  `#0B0D12`. Not pure `#000` (kills depth perception under WebGL).
- **Text primary:** `#F5F5F5` or `#EFEFEF`. Muted: `#7C7C7C`–`#9A9A9A`.
- **Hairlines:** `rgba(255,255,255,0.08)` for divider borders, `0.12` for
  card outlines. No solid mid-grays.
- **One electric accent — pick exactly one** and use it sparingly for
  hover-state, glow, or highlight text: neon green `#00FF88`, hot orange
  `#FF3D00`, cobalt `#5B8CFF`, or pale yellow `#FFF9A0`. Two accents kills
  the mood.
- Optional radial glow behind hero headline in the accent color at 8–15%
  opacity — that's the entire "brand color moment."

## Layout

- **Hero:** `100vh`, WebGL Canvas as fixed background layer (`position:
  fixed; inset: 0; z-index: 0`), content in an overlay flex layer above it.
- **Content columns:** 12-col grid but sections span 5–7 cols asymmetrically
  — no even 6/6 splits.
- **Projects grid:** oversized cards with video/WebGL previews on hover,
  2 or 3 across max — density is the enemy.
- **Radii:** pick one direction — `0` (hard-edged, more editorial) or
  `rounded-2xl` (softer, more product) — and hold it everywhere.
- **Vertical rhythm:** 128–192px between sections on desktop, 64–96px on
  mobile. This style needs breathing room.

## Motion

- **Continuous background motion is the point:** shader-driven distortion
  responding to mouse position, GPU particles with scroll-driven bias, or a
  slow-orbiting 3D geometry. It never fully stops.
- **Smooth scroll:** Lenis (or equivalent). Native scroll alone reads wrong.
- **Text reveal:** SplitText per-word `translateY(100%) → 0` with
  50–80ms stagger, cubic-bezier ease.
- **Cursor:** magnetic on interactive elements, subtle lens/distortion
  overlay on hover cards.
- **Scroll-linked:** GSAP ScrollTrigger for section pinning and camera path
  moves through the 3D scene.
- **`prefers-reduced-motion` is non-negotiable:** replace the WebGL canvas
  with a static gradient or single hero image, disable SplitText reveals
  (fall back to opacity fade), disable Lenis (return to native scroll),
  disable cursor effects. This isn't optional for this style.

## Forbidden

Light/pastel color themes (kill immersion), stock 3D hero illustrations
without motion, gradient banners that don't animate, static hero video
autoplaying without a WebGL layer, generic Inter body at display sizes,
symmetric 6/6 hero splits, bento grids without hover motion, glassmorphic
overlays, Heroicons/Feather chrome (reads UI-kit), multiple accent colors,
carousels with dots.

## When someone asks for this

- "Lusion feel", "immersive", "WebGL-first"
- "cinematic portfolio", "scrollytelling", "scroll-driven"
- "3D background", "shader-driven", "particle background"
- "creative studio site", "agency portfolio", "award-worthy"
- "portfolio like lusion.co / active-theory / basement.studio"
- "premium creative", "wow-first landing"

Curated from public references at lusion.co, active-theory.com,
basement.studio, studiofreight.com, and adjacent creative-dev studios.
