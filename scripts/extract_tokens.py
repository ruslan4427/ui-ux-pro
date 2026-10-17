#!/usr/bin/env python3
"""Find design tokens already in use in a project, so new UI work extends
them instead of inventing a parallel palette.

Usage: python3 extract_tokens.py <project-path>
"""
import re
import sys
from pathlib import Path

HEX_RE = re.compile(r"#(?:[0-9a-fA-F]{3}|[0-9a-fA-F]{6}|[0-9a-fA-F]{8})\b")
CSS_VAR_RE = re.compile(r"(--[\w-]+)\s*:\s*([^;]+);")
THEME_BLOCK_RE = re.compile(r"@theme\s*\{([^}]*)\}", re.DOTALL)

VENDOR_DIRS = {
    "node_modules", ".next", ".git", "dist", "build", "venv", ".venv",
    "site-packages", "__pycache__", ".dart_tool", "vendor", "target",
}


def is_vendor_path(path: Path) -> bool:
    return any(part in VENDOR_DIRS for part in path.parts)


def find_markdown_colors(path: Path) -> list[tuple[str, str]]:
    hits = []
    for name in ("CLAUDE.md", "AGENTS.md"):
        f = path / name
        if not f.exists():
            continue
        for line in f.read_text(errors="ignore").splitlines():
            for m in HEX_RE.finditer(line):
                label = line.split(m.group())[0].strip(" -*`:").strip()
                hits.append((m.group(), f"{name}: {label or line.strip()}"))
    return hits


def find_css_tokens(path: Path) -> list[tuple[str, str]]:
    hits = []
    for f in path.rglob("*.css"):
        if is_vendor_path(f):
            continue
        text = f.read_text(errors="ignore")
        for block in THEME_BLOCK_RE.findall(text):
            for var, val in CSS_VAR_RE.findall(block):
                hits.append((val.strip(), f"{f.relative_to(path)} @theme: {var}"))
        for var, val in CSS_VAR_RE.findall(text):
            if HEX_RE.search(val):
                hits.append((val.strip(), f"{f.relative_to(path)}: {var}"))
    return hits


def find_tailwind_config(path: Path) -> list[tuple[str, str]]:
    hits = []
    for pattern in ("tailwind.config.js", "tailwind.config.ts", "tailwind.config.cjs"):
        f = path / pattern
        if not f.exists():
            continue
        text = f.read_text(errors="ignore")
        for m in re.finditer(r'([\w-]+)\s*:\s*(["\'])(#[0-9a-fA-F]{3,8})\2', text):
            hits.append((m.group(3), f"{pattern}: {m.group(1)}"))
    return hits


def main():
    if len(sys.argv) != 2:
        print("Usage: extract_tokens.py <project-path>")
        sys.exit(1)

    path = Path(sys.argv[1]).expanduser().resolve()
    if not path.is_dir():
        print(f"Not a directory: {path}")
        sys.exit(1)

    found = find_markdown_colors(path) + find_css_tokens(path) + find_tailwind_config(path)

    if not found:
        print("No existing design tokens found — treat this as a new project.")
        print("Pull a starting palette from references/palettes.md instead.")
        return

    print(f"Found {len(found)} token reference(s) in {path}:\n")
    for value, source in found:
        print(f"  {value:<22} {source}")


if __name__ == "__main__":
    main()
