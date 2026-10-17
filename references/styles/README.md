# Style references

Each `<style>.md` here defines an intentional taste direction — typography,
color, layout, motion, and what's forbidden. Loaded on demand when the user
asks for that direction ("make it minimalist", "brutalist feel", etc.),
not by default.

## Adding a new style

Drop a new `<name>.md` in this directory. It should have these sections in
this order so a style pick is comparable to the others:

1. **One-paragraph identity** — what this style *is*, not what it isn't.
2. **Fits / Doesn't fit** — two lines. Refuse to be everything.
3. **Typography** — display + body + labels; allowed and banned faces.
4. **Color** — canvas, text primary/secondary, borders, accents. Actual hex
   values. Note contrast ratios if unusual.
5. **Layout** — grid discipline, spacing rhythm, container widths, radii.
6. **Motion** — one paragraph. Include a `prefers-reduced-motion` note.
7. **Forbidden** — the anti-patterns that define the style by their absence.
8. **When someone asks for this** — phrasings a real user would use, so the
   right file gets picked up.

Aim for ~50 lines. If a style takes 200 lines to describe, it's actually
two styles.

## Compatibility with root references

A style can (and often will) override the defaults in the root `references/`
files — for example `minimalist.md` bans Inter, which `typography.md`
recommends as the safe default. That's fine and intentional: the style is a
deliberate override for projects going that direction.

Always run the actual color pairs you ship through
`../../scripts/check_contrast.py`. The hex values in these files are the
starting point, not the guarantee — a specific combination on a specific
component still needs verification.
