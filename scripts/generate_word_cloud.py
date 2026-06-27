#!/usr/bin/env python3
"""Generate word cloud PNG from docs/07_word_cloud.md keyword table."""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DEFAULT_INPUT = ROOT / "docs" / "07_word_cloud.md"
DEFAULT_OUTPUT = ROOT / "docs" / "assets" / "word_cloud.png"

FONT_CANDIDATES = [
    "/System/Library/Fonts/AppleSDGothicNeo.ttc",
    "/System/Library/Fonts/Supplemental/AppleGothic.ttf",
    "/Library/Fonts/Arial Unicode.ttf",
    "C:/Windows/Fonts/malgun.ttf",
    "/usr/share/fonts/truetype/nanum/NanumGothic.ttf",
]


def parse_keywords(markdown: str) -> dict[str, float]:
    lines = markdown.splitlines()
    in_table = False
    frequencies: dict[str, float] = {}

    for line in lines:
        stripped = line.strip()
        if stripped.startswith("## 키워드"):
            in_table = True
            continue
        if in_table and stripped.startswith("## "):
            break
        if not in_table or not stripped.startswith("|"):
            continue
        if re.match(r"^\|\s*-+\s*\|", stripped):
            continue
        if "키워드" in stripped and "가중치" in stripped:
            continue

        cells = [cell.strip() for cell in stripped.strip("|").split("|")]
        if len(cells) < 2:
            continue

        keyword, weight_raw = cells[0], cells[1]
        if not keyword or not weight_raw:
            continue

        try:
            weight = float(weight_raw)
        except ValueError:
            continue
        if weight <= 0:
            continue

        frequencies[keyword] = weight

    return frequencies


def resolve_font() -> str | None:
    for path in FONT_CANDIDATES:
        if Path(path).exists():
            return path
    return None


def generate_word_cloud(frequencies: dict[str, float], output: Path) -> None:
    try:
        from wordcloud import WordCloud
    except ImportError as exc:
        raise SystemExit(
            "wordcloud 패키지가 필요합니다: pip install -r requirements.txt"
        ) from exc

    if not frequencies:
        raise SystemExit("키워드(가중치) 표에 유효한 항목이 없습니다.")

    font_path = resolve_font()
    wc = WordCloud(
        width=1200,
        height=700,
        background_color="white",
        font_path=font_path,
        prefer_horizontal=0.8,
        colormap="viridis",
    )
    image = wc.generate_from_frequencies(frequencies)
    output.parent.mkdir(parents=True, exist_ok=True)
    image.to_file(str(output))


def main() -> None:
    parser = argparse.ArgumentParser(description="Generate word cloud from docs/07")
    parser.add_argument("--input", type=Path, default=DEFAULT_INPUT)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    args = parser.parse_args()

    if not args.input.exists():
        raise SystemExit(f"입력 파일을 찾을 수 없습니다: {args.input}")

    markdown = args.input.read_text(encoding="utf-8")
    frequencies = parse_keywords(markdown)
    generate_word_cloud(frequencies, args.output)
    print(f"생성 완료: {args.output} ({len(frequencies)}개 키워드)")


if __name__ == "__main__":
    main()
