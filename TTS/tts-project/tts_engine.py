"""
tts_engine.py
Text-to-speech engine: English / Arabic (Fusha) / Arabic (Egyptian) -> MP3.

- Handles very long texts: the text is split into parts at sentence boundaries,
  each part is converted separately, then all parts are joined into one MP3.
- Engines: "edge" (high quality, all languages) and "gtts" (basic; English and
  Arabic Fusha only). Both need an internet connection.
"""
from __future__ import annotations

import asyncio
import re
import shutil
import tempfile
import uuid
from pathlib import Path
from typing import Callable, Optional

OUTPUT_DIR = Path(__file__).parent / "outputs"
OUTPUT_DIR.mkdir(exist_ok=True)

MAX_CHARS = 200_000      # roughly 35,000 words
CHUNK_CHARS = 2500       # size of one part
RETRIES = 2              # retries per part on network errors

# "gtts" is the gTTS language code, or None if gTTS does not support it
# (Egyptian Arabic, for example).
LANGUAGES = {
    "en": {
        "label": "English",
        "gtts": "en",
        "default": "en-US-AriaNeural",
        "voices": {
            "en-US-AriaNeural": "Aria (US, Female)",
            "en-US-GuyNeural": "Guy (US, Male)",
            "en-US-JennyNeural": "Jenny (US, Female)",
            "en-GB-SoniaNeural": "Sonia (UK, Female)",
            "en-GB-RyanNeural": "Ryan (UK, Male)",
            "en-AU-NatashaNeural": "Natasha (Australia, Female)",
            "en-IN-NeerjaNeural": "Neerja (India, Female)",
        },
    },
    "ar": {
        "label": "Arabic - Fusha (Modern Standard)",
        "gtts": "ar",
        "default": "ar-SA-HamedNeural",
        "voices": {
            "ar-SA-HamedNeural": "Hamed (Saudi, Male)",
            "ar-SA-ZariyahNeural": "Zariyah (Saudi, Female)",
            "ar-AE-HamdanNeural": "Hamdan (UAE, Male)",
            "ar-AE-FatimaNeural": "Fatima (UAE, Female)",
        },
    },
    "ar-eg": {
        "label": "Arabic - Egyptian",
        "gtts": None,
        "default": "ar-EG-SalmaNeural",
        "voices": {
            "ar-EG-SalmaNeural": "Salma (Egypt, Female)",
            "ar-EG-ShakirNeural": "Shakir (Egypt, Male)",
        },
    },
}
DEFAULT_LANG = "en"

# Kept for backward compatibility
VOICES = LANGUAGES["en"]["voices"]
DEFAULT_VOICE = LANGUAGES["en"]["default"]

ProgressCB = Callable[[int, int], None]   # (current part, total parts)


class TTSError(Exception):
    pass


class Cancelled(TTSError):
    pass


def count_words(text: str) -> int:
    return len(text.split())


def _clean(text: str) -> str:
    text = re.sub(r"\s+", " ", (text or "")).strip()
    if not text:
        raise TTSError("The text is empty.")
    if len(text) > MAX_CHARS:
        raise TTSError(f"The text is too long (maximum {MAX_CHARS:,} characters).")
    return text


def split_text(text: str, limit: int = CHUNK_CHARS) -> list:
    """Split text into parts of at most `limit` characters, at sentence ends.

    Sentence-ending punctuation includes the Arabic question mark, semicolon
    and comma, so Arabic text is split correctly too.
    """
    sentences = re.split(r"(?<=[.!?;:\u061F\u061B\u06D4])\s+", text)
    chunks, cur = [], ""

    def flush():
        nonlocal cur
        if cur.strip():
            chunks.append(cur.strip())
        cur = ""

    for s in sentences:
        # A sentence longer than the limit: cut at a comma (Latin or Arabic),
        # then at a space.
        while len(s) > limit:
            cut = max(s.rfind(",", 0, limit), s.rfind("\u060C", 0, limit),
                      s.rfind(" ", 0, limit))
            cut = cut if cut > 0 else limit
            piece, s = s[:cut + 1], s[cut + 1:].lstrip()
            if len(cur) + len(piece) + 1 > limit:
                flush()
            cur += (" " if cur else "") + piece
            flush()
        if len(cur) + len(s) + 1 > limit:
            flush()
        cur += (" " if cur else "") + s
    flush()
    return chunks


def _rate_str(speed: float) -> str:
    return f"{int(round((speed - 1.0) * 100)):+d}%"


async def _edge_save(text, voice, speed, path):
    import edge_tts
    await edge_tts.Communicate(text, voice, rate=_rate_str(speed)).save(str(path))


def _synth_chunk(text: str, engine: str, voice: str, speed: float, path: Path,
                 lang: str = "en"):
    last = None
    for _ in range(RETRIES + 1):
        try:
            if engine == "edge":
                asyncio.run(_edge_save(text, voice, speed, path))
            elif engine == "gtts":
                from gtts import gTTS
                gTTS(text=text, lang=LANGUAGES[lang]["gtts"],
                     slow=(speed < 0.9)).save(str(path))
            else:
                raise TTSError(f"Unknown engine: {engine}")
            if path.exists() and path.stat().st_size > 0:
                return
            last = TTSError("The output file is empty.")
        except TTSError:
            raise
        except Exception as e:  # network / service error
            last = e
    raise TTSError(f"Conversion failed (check your internet connection): {last}")


def synthesize(text: str, engine: str = "edge", voice: Optional[str] = None,
               speed: float = 1.0, out_path=None,
               progress: Optional[ProgressCB] = None, cancel=None,
               lang: str = DEFAULT_LANG) -> Path:
    """
    Convert text of any length into a single MP3 file and return its path.

    lang:     "en" English | "ar" Arabic Fusha | "ar-eg" Arabic Egyptian (edge only)
    progress: progress(i, n) is called after each part.
    cancel:   a threading.Event; when set, the conversion stops.
    """
    if lang not in LANGUAGES:
        raise TTSError(f"Unsupported language: {lang}")
    if engine == "gtts" and LANGUAGES[lang]["gtts"] is None:
        raise TTSError("Egyptian Arabic is only available with the Edge engine "
                       "(gTTS has no Egyptian voice).")
    voice = voice or LANGUAGES[lang]["default"]

    text = _clean(text)
    chunks = split_text(text)
    final = Path(out_path) if out_path else OUTPUT_DIR / f"{uuid.uuid4().hex}.mp3"
    final.parent.mkdir(parents=True, exist_ok=True)

    tmp = Path(tempfile.mkdtemp(prefix="tts_"))
    try:
        parts = []
        for i, chunk in enumerate(chunks, 1):
            if cancel is not None and cancel.is_set():
                raise Cancelled("Cancelled.")
            part = tmp / f"{i:05d}.mp3"
            _synth_chunk(chunk, engine, voice, speed, part, lang)
            parts.append(part)
            if progress:
                progress(i, len(chunks))

        # Join the parts (MP3 files from the same source can be concatenated directly)
        with open(final, "wb") as out:
            for p in parts:
                out.write(p.read_bytes())
    finally:
        shutil.rmtree(tmp, ignore_errors=True)

    return final
