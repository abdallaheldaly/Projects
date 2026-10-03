"""Command-line usage:
    python cli.py "Hello world" -o hello.mp3
    python cli.py -f story.txt --voice en-GB-RyanNeural --speed 1.1
    python cli.py -f arabic.txt --lang ar -o fusha.mp3        # Arabic (Fusha)
    python cli.py -f arabic.txt --lang ar-eg -o egyptian.mp3  # Arabic (Egyptian)
"""
from __future__ import annotations

import argparse
import sys

from tts_engine import LANGUAGES, TTSError, synthesize


def main():
    p = argparse.ArgumentParser(description="Text to MP3 (English / Arabic Fusha / Arabic Egyptian)")
    p.add_argument("text", nargs="?", help="the text to convert")
    p.add_argument("-f", "--file", help="read the text from a .txt file")
    p.add_argument("-o", "--out", default="output.mp3", help="output MP3 file name")
    p.add_argument("--lang", choices=list(LANGUAGES), default="en",
                   help="en = English | ar = Arabic Fusha | ar-eg = Arabic Egyptian (edge only)")
    p.add_argument("--engine", choices=["edge", "gtts"], default="edge")
    p.add_argument("--voice", help="voice name. Available: " + " | ".join(
        f"{k}: {', '.join(v['voices'])}" for k, v in LANGUAGES.items()))
    p.add_argument("--speed", type=float, default=1.0, help="0.5 - 2.0")
    a = p.parse_args()

    if a.file:
        text = open(a.file, encoding="utf-8").read()
    elif a.text:
        text = a.text
    else:
        p.error("provide some text or use -f file.txt")

    try:
        path = synthesize(text, a.engine, a.voice, a.speed, a.out, lang=a.lang,
                          progress=lambda i, n: print(f"\rPart {i}/{n}", end="", flush=True))
        print()
        print(f"Saved: {path}")
    except TTSError as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
