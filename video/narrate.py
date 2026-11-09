"""Narration for lesson videos: Kokoro-82M (Apache 2.0) through kokoro-onnx, cached per line."""
import os, re, hashlib
import numpy as np, soundfile as sf

TTS_DIR = os.environ.get("KPHI_TTS_DIR", "/tmp/tts")
VOICE = os.environ.get("KPHI_VOICE", "af_heart")
SR = 24000
_K = None

def _k():
    global _K
    if _K is None:
        from kokoro_onnx import Kokoro
        _K = Kokoro(os.path.join(TTS_DIR, "model.onnx"), os.path.join(TTS_DIR, "voices.npz"))
    return _K

SAY = [  # how to say what the captions write
    (r"K-φ", "K phi"), (r"Φ Setup", "Phi Setup"), (r"FP&A", "F P and A"), (r"P&L", "P and L"), (r"AR/AP", "A R and A P"),
    (r"\bBU\b", "B U"), (r"\bLLM\b", "L L M"), (r"\bSSO\b", "S S O"), (r"\bKPIs\b", "K P Is"), (r"\bKPI\b", "K P I"),
    (r"\bDSCR\b", "D S C R"), (r"\bEBITDA\b", "ebitda"), (r"\bMCP\b", "M C P"), (r"\bAPI\b", "A P I"), (r"\bCLI\b", "C L I"),
    (r"\bvs\b", "versus"), (r"\bFX\b", "F X"), (r"\b2FA\b", "two-factor"), (r"(\d),(\d{3})", r"\1\2"),
    (r"\b([A-Z])(\d)\.(\d)\b", r"\1 \2 point \3"), (r" · ", ". "), (r"−", "minus "), (r"\b24 h\b", "24 hours"), (r"\b13-week\b", "thirteen-week"),
    (r"\bLtd\b", "Limited"), (r"\bInc\.", "Inc"), (r"\bSAS\b", "S A S"),
]

def say(text):
    for a, b in SAY: text = re.sub(a, b, text)
    return text

def lang(voice): return "en-gb" if voice.startswith("b") else "en-us"

def line(text, voice=VOICE, speed=1.0):
    """Audio for one caption, as float32 at 24 kHz, cached on disk."""
    spoken = say(text)
    key = hashlib.sha1(f"{voice}|{speed}|{spoken}".encode()).hexdigest()[:16]
    path = os.path.join(TTS_DIR, "cache", key + ".wav")
    if os.path.exists(path):
        a, _ = sf.read(path, dtype="float32"); return a
    os.makedirs(os.path.dirname(path), exist_ok=True)
    a, sr = _k().create(spoken, voice=voice, speed=speed, lang=lang(voice))
    a = np.asarray(a, dtype="float32")
    # trim leading/trailing silence
    nz = np.where(np.abs(a) > 0.01)[0]
    if len(nz): a = a[max(0, nz[0] - 600): nz[-1] + 1200]
    sf.write(path, a, SR); return a

def mix(clips, total, path):
    """clips: list of (start_seconds, audio). Writes a mono wav of `total` seconds."""
    out = np.zeros(int(total * SR) + SR, dtype="float32")
    for t0, a in clips:
        i = int(t0 * SR); out[i:i + len(a)] += a[: max(0, len(out) - i)]
    peak = np.max(np.abs(out)) or 1.0
    sf.write(path, (out / peak * 0.89)[: int(total * SR)], SR)
