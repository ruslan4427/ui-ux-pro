# Typography pairings

**Last refreshed:** 2026-09-20

A pairing is a display font (headings) + a body font. Don't mix more than
these two in one interface.

## Geist Sans + Geist Mono
Display: Geist Sans (bold) · Body: Geist Sans (regular) · Code/labels: Geist
Mono. Already the noble-saas stack (`next/font/google`) — extend, don't
replace, unless asked to rebrand.

## Inter + Inter
Display: Inter (600–700) · Body: Inter (400). The safest default for
data-dense SaaS UI — excellent hinting at small sizes, huge language
coverage.

## Instrument Serif + Inter
Display: Instrument Serif (400–500) · Body: Inter (400). The strongest
free editorial pairing in 2026 — serif display adds brand differentiation
and warmth against the neutral Inter body. Fits marketing pages, content-led
products, boutique SaaS that wants to break from geometric-sans uniformity.
Don't use it in dense data UI where heading space is constrained.

## Fraunces + Inter
Display: Fraunces (serif, 500–600) · Body: Inter (400). Optical-size serif
with variable axes — deep personality at large sizes, still legible at
medium. Fits hospitality, premium/handcrafted brands, editorial products.
This is the shape of pairing that fits noble-saas's positioning if a serif
display were ever introduced, though the current brief specifies Geist.

## Rules that don't change with trends

- Never pair two serif fonts, or two heavily-stylized display fonts, together
  — one of them should be quiet.
- Body text minimum 16px on the web (14px on dense data tables is the one
  common exception).
- Line height 1.4–1.6 for body text; tighter (1.1–1.25) for large display
  headings.
- Load variable fonts where available — one file covers the full weight
  range instead of shipping 4 separate static files.
- Use `clamp()` for fluid heading sizes across breakpoints rather than
  discrete media-query overrides.
