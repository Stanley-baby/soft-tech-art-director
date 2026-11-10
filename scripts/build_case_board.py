#!/usr/bin/env python3
"""Build a dependency-free SVG Case Board from 3–4 reference images."""

import argparse
import base64
import html
import json
import mimetypes
from pathlib import Path


WIDTH = 1600
HEIGHT = 1200
MARGIN = 40
HEADER = 106
GAP = 18
BG = "#F3F0EA"
INK = "#17151B"
MUTED = "#6F6875"
PANEL = "#FFFFFF"
RULE = "#D9D2DD"
ACCENT = "#6E42D3"


def esc(value):
    return html.escape(str(value), quote=True)


def data_uri(path):
    source = Path(path)
    mime = mimetypes.guess_type(source.name)[0] or "application/octet-stream"
    encoded = base64.b64encode(source.read_bytes()).decode("ascii")
    return f"data:{mime};base64,{encoded}"


def shorten(value, limit):
    text = str(value)
    return text if len(text) <= limit else text[: limit - 1] + "…"


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--spec", required=True)
    parser.add_argument("--output", required=True)
    args = parser.parse_args()

    spec = json.loads(Path(args.spec).read_text(encoding="utf-8"))
    refs = spec.get("references", [])
    if not 3 <= len(refs) <= 4:
        raise SystemExit("Case Board requires 3 or 4 references")
    for ref in refs:
        if not Path(ref["path"]).is_file():
            raise SystemExit(f"Missing reference: {ref['path']}")

    card_w = (WIDTH - 2 * MARGIN - GAP) // 2
    card_h = (HEIGHT - HEADER - MARGIN - GAP) // 2
    image_h = card_h - 72

    svg = [
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{WIDTH}" height="{HEIGHT}" viewBox="0 0 {WIDTH} {HEIGHT}">',
        f'<rect width="100%" height="100%" fill="{BG}"/>',
        "<style>",
        ".title{font:700 38px Arial,Helvetica,sans-serif}.sub{font:400 18px Arial,Helvetica,sans-serif}",
        ".role{font:700 18px Arial,Helvetica,sans-serif}.meta{font:400 14px Arial,Helvetica,sans-serif}",
        "</style>",
        f'<text x="{MARGIN}" y="58" class="title" fill="{INK}">{esc(spec.get("title", "CASE REFERENCE BOARD"))}</text>',
        f'<text x="{MARGIN}" y="86" class="sub" fill="{MUTED}">{esc(spec.get("subtitle", "Visual reference system"))}</text>',
        f'<line x1="{MARGIN}" y1="{HEADER - 10}" x2="{WIDTH - MARGIN}" y2="{HEADER - 10}" stroke="{RULE}" stroke-width="2"/>',
        "<defs>",
    ]

    for i in range(4):
        svg.append(
            f'<clipPath id="clip-{i}"><rect width="{card_w - 28}" height="{image_h - 14}" rx="12"/></clipPath>'
        )
    svg.append("</defs>")

    for i, ref in enumerate(refs):
        col, row = i % 2, i // 2
        x = MARGIN + col * (card_w + GAP)
        y = HEADER + row * (card_h + GAP)
        image_x, image_y = x + 14, y + 14
        svg.extend(
            [
                f'<rect x="{x}" y="{y}" width="{card_w}" height="{card_h}" rx="18" fill="{PANEL}" stroke="{RULE}" stroke-width="2"/>',
                (
                    f'<g transform="translate({image_x} {image_y})">'
                    f'<image href="{data_uri(ref["path"])}" width="{card_w - 28}" height="{image_h - 14}" '
                    f'preserveAspectRatio="xMidYMid slice" clip-path="url(#clip-{i})"/></g>'
                ),
                f'<text x="{x + 20}" y="{y + image_h + 28}" class="role" fill="{INK}">{esc(shorten(ref.get("role", "REFERENCE").upper(), 42))}</text>',
                f'<text x="{x + 20}" y="{y + image_h + 54}" class="meta" fill="{MUTED}">{esc(ref.get("id", ""))}</text>',
            ]
        )
        emphasis = ref.get("emphasis") or ref.get("weight")
        if emphasis not in (None, ""):
            label = f"{emphasis}%" if str(emphasis).isdigit() else str(emphasis)
            svg.append(
                f'<text x="{x + card_w - 20}" y="{y + image_h + 28}" text-anchor="end" class="role" fill="{ACCENT}">{esc(label)}</text>'
            )

    if len(refs) == 3:
        x = MARGIN + card_w + GAP
        y = HEADER + card_h + GAP
        svg.extend(
            [
                f'<rect x="{x}" y="{y}" width="{card_w}" height="{card_h}" rx="18" fill="none" stroke="{RULE}" stroke-width="2"/>',
                f'<text x="{x + 28}" y="{y + 54}" class="role" fill="{MUTED}">OPEN ROLE</text>',
                f'<text x="{x + 28}" y="{y + 88}" class="meta" fill="{MUTED}">Add a reference only when it controls a distinct role.</text>',
            ]
        )

    svg.append("</svg>")
    output = Path(args.output)
    if output.suffix.lower() != ".svg":
        raise SystemExit("Case Board output must use the .svg extension")
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text("\n".join(svg), encoding="utf-8")
    print(output)


if __name__ == "__main__":
    main()
