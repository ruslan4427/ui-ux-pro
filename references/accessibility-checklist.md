# Accessibility checklist

Static rules — these don't go stale, so they're not part of the scheduled
refresh. Run through this before marking any UI work done.

## Color contrast

- Body text vs background: **4.5:1** minimum (WCAG AA). Verify with
  `scripts/check_contrast.py`.
- Large text (18px+ regular, or 14px+ bold) vs background: **3:1** minimum.
- Icons and UI borders that carry meaning (not decorative): **3:1** minimum
  against adjacent colors.
- Never rely on color alone to convey state (error/success/selected) — pair
  with an icon, label, or shape change.

## Touch and click targets

- Minimum **44x44px** hit area on any interactive element (buttons, links,
  form controls) — this is an Apple HIG / WCAG 2.5.5 baseline, not optional
  on mobile-facing UI.
- Adjacent tap targets need at least 8px of spacing to avoid mis-taps.

## Keyboard and focus

- Every interactive element must be reachable by Tab, in a logical order.
- A visible focus ring on every focusable element — never `outline: none`
  without a replacement focus style.
- Modals/sheets trap focus while open and return it to the trigger on close.
- Escape closes dismissible overlays.

## Semantic markup and ARIA

- Use native elements (`<button>`, `<a>`, `<label>`) before reaching for
  `role="..."` — native elements carry behavior ARIA can't replicate.
- Every form input has a associated `<label>` (or `aria-label` when a visible
  label isn't in the design).
- Images convey meaning → `alt` text. Purely decorative → `alt=""`.
- Live-updating content (toasts, async status) uses `aria-live`.
- Icon-only buttons get `aria-label`.

## Motion

- Respect `prefers-reduced-motion` — provide a reduced/no-motion variant for
  any non-essential animation.
- Avoid flashing content more than 3 times per second (seizure risk).

## Text and layout

- Body text should reflow and stay readable at 200% browser zoom without
  horizontal scrolling.
- Line length: aim for 45–75 characters per line for long-form text.
- Don't disable pinch-zoom on mobile viewports.
