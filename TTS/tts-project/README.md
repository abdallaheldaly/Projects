# Text to MP3

A Python project that converts **English or Arabic (Fusha or Egyptian)** text, up to roughly
35,000 words, into a single MP3 file. It has an HTML interface that runs from the terminal.

---

## 1) Installation (once)

Requires Python 3.8 or newer (check with `python3 --version`) and an internet connection.

```bash
cd tts_project
python3 -m venv venv

# Linux / macOS
source venv/bin/activate
# Windows
venv\Scripts\activate

pip install -r requirements.txt
```

## 2) Run

```bash
python app.py
```

The browser opens automatically at http://127.0.0.1:5000

Options:

| Command | Purpose |
|---|---|
| `python app.py --port 8080` | use a different port |
| `python app.py --no-browser` | do not open the browser automatically |
| `python app.py --host 0.0.0.0` | open it from a phone or another device on the same Wi-Fi (`http://DEVICE-IP:5000`) |

Press `Ctrl+C` in the terminal to stop.

## 3) Using the page

1. Paste your text, click **Open .txt file**, or drag a `.txt` file onto the text box.
2. Choose the language, engine, voice and speed.
3. Click **Convert to MP3** and watch the progress bar (you can click **Cancel**).
4. When it finishes, listen in the player and click **Download MP3**.

## 4) Supported languages

| Language | CLI code | Engine | Voices |
|---|---|---|---|
| English | `en` | edge / gtts | Aria, Guy, Jenny, Sonia, Ryan, Natasha, Neerja |
| Arabic - Fusha | `ar` | edge / gtts | Hamed, Zariyah (Saudi), Hamdan, Fatima (UAE) |
| Arabic - Egyptian | `ar-eg` | **edge only** | Salma (female), Shakir (male) |

- In the page, pick **Language**. If you paste Arabic text while the page is on English, it
  switches to Fusha automatically; you can choose Egyptian manually.
- "Egyptian" means a voice with an Egyptian accent (Salma / Shakir) reading the Arabic text you
  provide, whether Fusha or colloquial. gTTS has no Egyptian voice, so this option works with
  the Edge engine only.
- Known limits: Arabic text without diacritics may have some words mispronounced, and text
  that mixes Arabic and English may have its English parts read incorrectly. For mixed text,
  convert the two languages separately.

## 5) Without the web page

**Command line:**
```bash
python cli.py "Hello world" -o hello.mp3
python cli.py -f book.txt --voice en-GB-RyanNeural --speed 1.1 -o book.mp3
python cli.py "Hello" --engine gtts -o g.mp3

# Arabic (Fusha / Egyptian), text read from a file
python cli.py -f arabic.txt --lang ar -o fusha.mp3
python cli.py -f arabic.txt --lang ar-eg --voice ar-EG-ShakirNeural -o egyptian.mp3
```

**From Python code:**
```python
from tts_engine import synthesize

synthesize(open("book.txt", encoding="utf-8").read(),
           lang="en", voice="en-US-GuyNeural", out_path="book.mp3",
           progress=lambda i, n: print(f"{i}/{n}"))
```

---

## How it works

```
Browser (index.html)         Server (app.py)                 Engine (tts_engine.py)
────────────────────         ───────────────                 ──────────────────────
1. POST /api/jobs      ───►  creates a job, starts a   ───►  splits the text into parts (~2500
   (text + options)          thread, returns a job id         characters, at sentence ends)
2. every second:                                              each part ──► edge-tts / gTTS ──► part.mp3
   GET /api/jobs/<id>  ◄───  done / total / status     ◄───   after each part: progress(i, n)
3. when status = done:                                        joins all parts into one MP3 file
   GET /api/jobs/<id>/audio ◄── the file from outputs/
```

**Why split the text?** Speech services handle short texts better, and splitting gives us a
progress bar, cancellation, and automatic retries (each part is retried twice if the network
fails).

**Why a background job?** A long text can take minutes, and the browser should not wait on a
single long request. The page polls for progress every second instead.

**Engines:**
- **edge**: Microsoft neural voices, higher quality, with voice and speed selection.
- **gtts**: Google Translate voice, simpler, no voice choice, English and Arabic Fusha only.

Both send your text to an online service, so an internet connection is required and you
should not use them for confidential text.

## Project structure

```
tts_project/
├── app.py              # server + API + terminal launcher
├── templates/
│   └── index.html      # the interface (HTML/CSS/JS)
├── tts_engine.py       # splitting + conversion + joining
├── cli.py              # command line
├── requirements.txt
└── outputs/            # files produced by the web page
```

## Common settings (in `tts_engine.py`)

| Setting | Default | Meaning |
|---|---|---|
| `MAX_CHARS` | 200,000 | maximum text length |
| `CHUNK_CHARS` | 2500 | size of one part |
| `RETRIES` | 2 | retries per part |
| `LANGUAGES` | en / ar / ar-eg | add any voice from `edge-tts --list-voices` under its language |

## Troubleshooting

- **`TypeError: unsupported operand type(s) for |`**: caused by Python older than 3.10. It is
  fixed in this version; if you still see it, you are running an older copy of the project.
- **"Conversion failed"**: check your internet connection, then retry or switch the engine to gtts.
- **Port already in use**: use `--port 8080`.
- **`outputs/` is getting big**: delete files you do not need; there is no automatic cleanup.
- **A slight click between parts in some players**: parts are joined by direct concatenation.
  If you hear it, add a pydub + ffmpeg based join.
