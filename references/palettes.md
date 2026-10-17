# Palettes

**Last refreshed:** 2026-09-20

Every palette below: one accent, a neutral scale, a background/surface pair.
Text/muted colors are verified against the background for AA normal text
(>=4.5:1). **Accent colors are not** — an accent is often used as a solid
fill (button background) with text *on top of it*, not as text color on the
page background, so its own contrast ratio depends on what you put on it.
Always run the exact pair you're about to ship through
`scripts/check_contrast.py` — don't trust the number below for a use it
wasn't checked for.

## Warm neutral + gold
Background `#f5f0e8` · Text `#1a1208` (16.33:1, passes AAA) · Accent `#C9A84C`
Accent on background is only **2.01:1** — too low for gold *text* on cream.
Use gold as a filled button/badge background with dark text (`#1a1208`) on
top, never as text color directly on the cream background.
Fits: hospitality, boutique services, premium/handcrafted positioning.
(This is the noble-saas palette — don't propose a variant of it elsewhere
without checking it's actually a different project.)

## Warm dark + amber
Background `#111210` · Text `#f0ece3` (15.93:1, passes AAA) · Accent `#f59e0b` (8.75:1 on bg, passes AAA — safe as text or fill)
Warm near-black avoids the halation of pure `#000`. Amber accent reads as a
"glow" against the dark ground, not a clash.
Fits: dark-mode-first SaaS tools, media/entertainment, developer products.

## Slate + deep indigo
Background `#f8f8fb` · Text `#0f1117` (17.80:1, passes AAA) · Accent `#4f52e7` (5.36:1 on bg, passes AA normal text — safe as a link/text color)
Cool-neutral background with a geometric-precision feel. Indigo reads more
contemporary than royal blue; high contrast keeps it crisp at data density.
Fits: SaaS dashboards, fintech, AI tools, developer products.

## Paper + forest green
Background `#faf9f6` · Text `#1c2b22` (14.07:1, passes AAA) · Accent `#3f7d5c` (4.64:1 on bg, passes AA normal text)
Fits: sustainability, wellness, food/agriculture brands.

## Warm dark violet
Background `#100e14` · Text `#e8e4f0` (15.33:1, passes AAA) · Accent `#a855f7` (4.85:1 on bg, passes AA normal text — safe as text or fill)
Dark near-black with a warm purple tint. Violet accent aligns with the
dominant CTA direction in 2026 AI and creative-tool products.
Fits: AI products, creative tools, community platforms, developer tools.

## Choosing between these

- Match the accent's saturation to how often it appears — a loud accent used
  on every button stops reading as an accent.
- Never pick a palette because it looks good in isolation — check the
  accent-on-background contrast for the actual text size it'll carry.
- If the project already has tokens (`extract_tokens.py` found something),
  none of this applies — extend what's there instead.
