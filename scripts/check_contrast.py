#!/usr/bin/env python3
"""WCAG contrast ratio checker for a foreground/background color pair.

Usage: python3 check_contrast.py <#fg-hex> <#bg-hex>
"""
import sys


def to_rgb(hex_color: str) -> tuple[float, float, float]:
    h = hex_color.lstrip("#")
    if len(h) == 3:
        h = "".join(c * 2 for c in h)
    r, g, b = (int(h[i : i + 2], 16) for i in (0, 2, 4))
    return r / 255, g / 255, b / 255


def linearize(c: float) -> float:
    return c / 12.92 if c <= 0.03928 else ((c + 0.055) / 1.055) ** 2.4


def relative_luminance(rgb: tuple[float, float, float]) -> float:
    r, g, b = (linearize(c) for c in rgb)
    return 0.2126 * r + 0.7152 * g + 0.0722 * b


def contrast_ratio(fg: str, bg: str) -> float:
    l1 = relative_luminance(to_rgb(fg))
    l2 = relative_luminance(to_rgb(bg))
    lighter, darker = max(l1, l2), min(l1, l2)
    return (lighter + 0.05) / (darker + 0.05)


def verdict(ratio: float) -> str:
    checks = [
        ("AA, normal text (>= 4.5)", ratio >= 4.5),
        ("AA, large text (>= 3.0)", ratio >= 3.0),
        ("AAA, normal text (>= 7.0)", ratio >= 7.0),
        ("AAA, large text (>= 4.5)", ratio >= 4.5),
    ]
    return "\n".join(f"  {'PASS' if ok else 'FAIL'}  {label}" for label, ok in checks)


def main():
    if len(sys.argv) != 3:
        print("Usage: check_contrast.py <#fg-hex> <#bg-hex>")
        sys.exit(1)

    fg, bg = sys.argv[1], sys.argv[2]
    ratio = contrast_ratio(fg, bg)
    print(f"{fg} on {bg} -> ratio {ratio:.2f}:1\n")
    print(verdict(ratio))


if __name__ == "__main__":
    main()
