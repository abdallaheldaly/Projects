"""
Web GUI (HTML) that runs from the terminal:

    python app.py                  # opens the browser at http://127.0.0.1:5000
    python app.py --port 8080
    python app.py --no-browser
    python app.py --host 0.0.0.0   # reach it from a phone / another device on the same network

How it works: long texts take a while, so the page starts a background "job"
and polls the server every second for progress. When the job finishes, the
page shows an audio player and a download button.
"""
from __future__ import annotations

import argparse
import threading
import uuid
import webbrowser

from flask import Flask, jsonify, render_template, request, send_file

from tts_engine import (DEFAULT_LANG, LANGUAGES, MAX_CHARS, OUTPUT_DIR, Cancelled,
                        TTSError, count_words, synthesize)

app = Flask(__name__)
JOBS: dict[str, dict] = {}


@app.get("/")
def index():
    return render_template("index.html", languages=LANGUAGES,
                           default_lang=DEFAULT_LANG, max_chars=MAX_CHARS)


def _run_job(job_id, text, engine, voice, speed, lang):
    job = JOBS[job_id]

    def progress(i, n):
        job.update(done=i, total=n)

    try:
        path = synthesize(text, engine, voice, speed,
                          out_path=OUTPUT_DIR / f"{job_id}.mp3",
                          progress=progress, cancel=job["cancel"], lang=lang)
        job.update(status="done", path=str(path))
    except Cancelled:
        job.update(status="cancelled")
    except TTSError as e:
        job.update(status="error", error=str(e))
    except Exception as e:
        job.update(status="error", error=f"Unexpected error: {e}")


@app.post("/api/jobs")
def create_job():
    d = request.get_json(silent=True) or {}
    text = (d.get("text") or "").strip()
    if not text:
        return jsonify(error="The text is empty."), 400
    if len(text) > MAX_CHARS:
        return jsonify(error=f"The text is too long (maximum {MAX_CHARS:,} characters)."), 400
    try:
        speed = max(0.5, min(2.0, float(d.get("speed", 1.0))))
    except (TypeError, ValueError):
        speed = 1.0
    engine = d.get("engine", "edge")
    if engine not in ("edge", "gtts"):
        engine = "edge"
    lang = d.get("lang", DEFAULT_LANG)
    if lang not in LANGUAGES:
        lang = DEFAULT_LANG
    if engine == "gtts" and LANGUAGES[lang]["gtts"] is None:
        return jsonify(error="Egyptian Arabic is only available with the Edge engine."), 400
    voice = d.get("voice")
    if voice not in LANGUAGES[lang]["voices"]:
        voice = LANGUAGES[lang]["default"]

    job_id = uuid.uuid4().hex
    JOBS[job_id] = dict(status="running", done=0, total=0, cancel=threading.Event(),
                        words=count_words(text))
    threading.Thread(target=_run_job, args=(job_id, text, engine, voice, speed, lang),
                     daemon=True).start()
    return jsonify(id=job_id)


@app.get("/api/jobs/<job_id>")
def job_status(job_id):
    j = JOBS.get(job_id)
    if not j:
        return jsonify(error="Job not found."), 404
    return jsonify(status=j["status"], done=j["done"], total=j["total"],
                   error=j.get("error"))


@app.post("/api/jobs/<job_id>/cancel")
def job_cancel(job_id):
    j = JOBS.get(job_id)
    if j:
        j["cancel"].set()
    return jsonify(ok=True)


@app.get("/api/jobs/<job_id>/audio")
def job_audio(job_id):
    j = JOBS.get(job_id)
    if not j or j["status"] != "done":
        return jsonify(error="The file is not ready."), 404
    return send_file(j["path"], mimetype="audio/mpeg", download_name="speech.mp3",
                     as_attachment=request.args.get("download") == "1")


def main():
    p = argparse.ArgumentParser(description="Text to MP3 - web GUI")
    p.add_argument("--host", default="127.0.0.1")
    p.add_argument("--port", type=int, default=5000)
    p.add_argument("--no-browser", action="store_true", help="do not open the browser automatically")
    a = p.parse_args()

    url = f"http://{'127.0.0.1' if a.host == '0.0.0.0' else a.host}:{a.port}"
    print(f"\n  Running at: {url}\n  Press Ctrl+C to stop\n")
    if not a.no_browser:
        threading.Timer(1.0, lambda: webbrowser.open(url)).start()
    app.run(host=a.host, port=a.port, threaded=True)


if __name__ == "__main__":
    main()
