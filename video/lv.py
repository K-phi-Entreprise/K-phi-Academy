"""K-φ Academy lesson videos: a small scene engine.
A lesson is a list of scenes; each scene has a type, a duration and its captions.
Usage: python3 lv.py <lesson-code> <out.mp4>    |    python3 lv.py <lesson-code> preview"""
import sys, math, subprocess, importlib
import numpy as np
from PIL import Image, ImageDraw
import diagram3 as D
from diagram3 import Canvas, ease, eo, back, clamp, lerp, lerp2, font, BG, YEL, WHITE, GREY, DIM, PANEL, PANEL2
from lesson_f11 import mark

W, H, FPS = 1920, 1080, 30
D.W, D.H = W, H
F_TITLE = font("Bold", 76); F_H = font("SemiBold", 48); F_L = font("SemiBold", 36); F_S = font("Regular", 30)
F_CAP = font("Medium", 38); F_MONO = font("Medium", 26); F_BIG = font("Bold", 70); F_K = font("Bold", 96)
RED = (255, 122, 122); TEAL = (54, 214, 160); SHOTS = "shots/"
_m = ImageDraw.Draw(Image.new("L", (1, 1)))
def tw(txt, f): b = _m.textbbox((0, 0), txt, font=f); return b[2] - b[0]
def win(t, t0, t1, fi=0.5, fo=0.5): return clamp((t - t0) / fi) * clamp((t1 - t) / fo)
_IMG = {}
def shot(name):
    if name not in _IMG: _IMG[name] = Image.open(SHOTS + name + ".png").convert("RGBA").resize((W, H))
    return _IMG[name]

def heading(cv, s, a, y=150):
    if s.get("eyebrow"): cv.text((160, y - 56), s["eyebrow"], F_MONO, GREY, a, anchor="lm")
    if s.get("heading"): cv.text((160, y), s["heading"], F_H, WHITE, a, anchor="lm")

def sc_title(cv, img, t, d, s, a):
    mark(cv, img, (W / 2, 300), F_K, a, sweep=(t - 0.4) / 2.4)
    cv.text((W / 2, 390), "ACADEMY", F_MONO, GREY, a)
    y = 540 + 24 * (1 - eo((t - 0.3) / 0.8))
    cv.text((W / 2, y), s["l1"], F_TITLE, WHITE, a * clamp((t - 0.3) / 0.6))
    cv.text((W / 2, y + 92), s["l2"], F_TITLE, YEL, a * clamp((t - 0.6) / 0.6))
    cv.text((W / 2, y + 190), s["meta"], F_MONO, GREY, a * clamp((t - 0.9) / 0.6))

def sc_bullets(cv, img, t, d, s, a):
    heading(cv, s, a)
    items = s["items"]; gap = s.get("gap", 110); y0 = s.get("y0", 300)
    for k, it in enumerate(items):
        t0 = s.get("at", [0.6 + k * 1.2 for _ in items])[k] if "at" in s else 0.6 + k * s.get("step", 1.4)
        ak = a * clamp((t - t0) / 0.5); dx = 30 * (1 - eo((t - t0) / 0.6))
        if ak <= 0: continue
        y = y0 + k * gap; hot = s.get("hot") == k
        if isinstance(it, tuple): head, sub = it
        else: head, sub = it, None
        cv.rrect((160 + dx, y - 44, W - 160 + dx, y + 44), 16, fill=PANEL2, outline=(YEL if hot else DIM), width=2 if not hot else 3, a=ak)
        cv.text((200 + dx, y), head, F_L, YEL if hot else WHITE, ak, anchor="lm")
        if sub: cv.text((W - 200 + dx, y), sub, F_S, GREY, ak, anchor="rm")

def sc_table(cv, img, t, d, s, a):
    heading(cv, s, a)
    cols = s["cols"]; rows = s["rows"]; x0, x1 = 160, W - 160; widths = s.get("widths", [1] * len(cols))
    tot = sum(widths); xs = [x0]
    for w_ in widths: xs.append(xs[-1] + (x1 - x0) * w_ / tot)
    y = 270
    cv.rrect((x0, y - 34, x1, y + 34), 12, fill=PANEL, a=a)
    for c, name in enumerate(cols): cv.text((xs[c] + 28, y), name.upper(), F_MONO, GREY, a, anchor="lm")
    for r, row in enumerate(rows):
        t0 = 0.7 + r * s.get("step", 1.0); ar = a * clamp((t - t0) / 0.45)
        if ar <= 0: continue
        yy = y + 90 + r * 92; hot = s.get("hot") == r and t > s.get("hot_at", 0)
        cv.rrect((x0, yy - 40, x1, yy + 40), 12, fill=PANEL2, outline=(YEL if hot else DIM), width=3 if hot else 1, a=ar)
        for c, cell in enumerate(row): cv.text((xs[c] + 28, yy), cell, F_L if c == 0 else F_S, (YEL if c == 0 else WHITE), ar, anchor="lm")

def sc_flow(cv, img, t, d, s, a):
    heading(cv, s, a)
    nodes = s["nodes"]; n = len(nodes); y = s.get("y", 560); x0, x1 = 300, W - 300
    xs = [lerp(x0, x1, k / (n - 1)) for k in range(n)]; bw = min(300, (x1 - x0) / (n - 1) * 0.42)
    for k, nd in enumerate(nodes):
        t0 = 0.6 + k * s.get("step", 1.3); ak = a * clamp((t - t0) / 0.5)
        if k > 0:
            p = eo((t - t0 + 0.4) / 0.6)
            if p > 0:
                pa, pb = (xs[k - 1] + bw, y), (xs[k] - bw, y); q = lerp2(pa, pb, p)
                cv.line([pa, q], YEL, 10, a * 0.14, blur=4); cv.line([pa, q], YEL, 3, a * 0.9)
                if p >= 1: ph = (t * 0.6 + k * 0.3) % 1; D.spark(cv, lerp2(pa, pb, ph), math.sin(math.pi * ph) ** 0.6, a)
        if ak <= 0: continue
        head, sub = nd if isinstance(nd, tuple) else (nd, "")
        hot = s.get("hot") == k and t > s.get("hot_at", 0)
        col = s.get("color", {}).get(k)
        cv.rrect((xs[k] - bw, y - 90, xs[k] + bw, y + 90), 20, fill=PANEL2, outline=(col or (YEL if hot else DIM)), width=3, a=ak)
        cv.text((xs[k], y - 24), head, F_L, (col or (YEL if hot else WHITE)), ak)
        if sub: cv.text((xs[k], y + 30), sub, F_S, GREY, ak)
    if s.get("note"): cv.text((W / 2, y + 190), s["note"], F_L, YEL, a * clamp((t - s.get("note_at", 3)) / 0.5))

def sc_shot(cv, img, t, d, s, a):
    src = shot(s["img"]); bx = s.get("focus")  # (x0, y0, x1, y1) in screenshot pixels
    zt = ease((t - 0.8) / max(1.0, d - 2.5)); zmax = s.get("zoom", 1.6)
    if bx: fx, fy = (bx[0] + bx[2]) / 2, (bx[1] + bx[3]) / 2
    else: fx, fy = W / 2, H / 2
    z = 1 + (zmax - 1) * zt; cxx, cyy = lerp(W / 2, fx, zt), lerp(H / 2, fy, zt)
    cw, ch = W / z, H / z; x0 = clamp(cxx - cw / 2, 0, W - cw); y0 = clamp(cyy - ch / 2, 0, H - ch)
    crop = src.crop((int(x0), int(y0), int(x0 + cw), int(y0 + ch))).resize((W, H), Image.BILINEAR)
    crop.putalpha(Image.fromarray((np.array(crop.split()[3], float) * a).astype("uint8"), "L")); img.alpha_composite(crop)
    if bx and t > s.get("ring_at", 1.6):
        ar = a * clamp((t - s.get("ring_at", 1.6)) / 0.4)
        r0 = ((bx[0] - x0) * z, (bx[1] - y0) * z, (bx[2] - x0) * z, (bx[3] - y0) * z)
        cv.rrect(r0, 14, outline=YEL, width=5, a=ar * (0.75 + 0.25 * math.sin(t * 5)))
        if s.get("label"):
            lx = r0[2] + 30 if r0[2] + 30 + tw(s["label"], F_H) < W - 40 else r0[0] - 30 - tw(s["label"], F_H)
            ly = (r0[1] + r0[3]) / 2; lx = max(40, lx)
            cv.rrect((lx - 18, ly - 38, lx + tw(s["label"], F_H) + 18, ly + 38), 14, fill=(6, 8, 16), a=ar * 0.88)
            cv.text((lx, ly), s["label"], F_H, YEL, ar, anchor="lm")

def sc_compare(cv, img, t, d, s, a):
    heading(cv, s, a)
    for c, (title, items, col) in enumerate([(s["left"], s["litems"], TEAL), (s["right"], s["ritems"], RED)]):
        x = 160 + c * 820; ac = a * clamp((t - 0.5 - c * 0.8) / 0.5)
        cv.rrect((x, 240, x + 780, 880), 20, fill=PANEL2, outline=col, width=3, a=ac)
        cv.text((x + 40, 300), title, F_H, col, ac, anchor="lm")
        for k, it in enumerate(items):
            ak = ac * clamp((t - 1.0 - c * 0.8 - k * 0.6) / 0.4)
            cv.text((x + 40, 400 + k * 90), ("✓  " if c == 0 else "×  ") + it, F_L, WHITE, ak, anchor="lm")

def sc_checklist(cv, img, t, d, s, a):
    heading(cv, s, a)
    for k, it in enumerate(s["items"]):
        t0 = 0.8 + k * s.get("step", 1.6); ak = a * clamp((t - t0) / 0.4); y = 320 + k * 120
        if ak <= 0: continue
        cv.rrect((160, y - 46, W - 160, y + 46), 16, fill=PANEL2, outline=DIM, width=2, a=ak)
        tk = a * clamp((t - t0 - 0.6) / 0.3); cx = 220
        cv.rrect((cx - 24, y - 24, cx + 24, y + 24), 8, outline=TEAL, width=3, a=ak)
        if tk > 0: cv.line([(cx - 12, y), (cx - 3, y + 10), (cx + 14, y - 10)], TEAL, 5, tk)
        cv.text((280, y), it, F_L, WHITE, ak, anchor="lm")

def sc_quote(cv, img, t, d, s, a):
    cv.text((W / 2, 380), s["l1"], F_TITLE, WHITE, a * clamp((t - 0.2) / 0.6))
    cv.text((W / 2, 470), s["l2"], F_TITLE, YEL, a * clamp((t - 0.6) / 0.6))
    for k, p in enumerate(s.get("points", [])):
        ak = a * clamp((t - 1.8 - k * 0.7) / 0.5); y = 620 + k * 78; x = W / 2 - 560
        cv.text((x, y), "→", F_L, YEL, ak, anchor="lm"); cv.text((x + 60, y), p, F_L, WHITE, ak, anchor="lm")

def sc_end(cv, img, t, d, s, a):
    mark(cv, img, (W / 2, 420), F_K, a, sweep=(t - 0.5) / 2.4)
    cv.text((W / 2, 510), "ACADEMY", F_MONO, GREY, a)
    cv.text((W / 2, 640), s["next"], F_H, WHITE, a * clamp((t - 0.6) / 0.6))
    cv.text((W / 2, 710), "academy.k-phi.com", F_MONO, GREY, a * clamp((t - 1.0) / 0.6))

SCENES = {k[3:]: v for k, v in globals().items() if k.startswith("sc_")}

def timeline(lesson):
    out, t = [], 0.0
    for s in lesson["scenes"]:
        out.append((t, t + s["d"], s)); t += s["d"]
    return out, t

def captions(lesson):
    tl, _ = timeline(lesson); caps = []
    for t0, t1, s in tl:
        cs = s.get("cap", [])
        if isinstance(cs, str): cs = [cs]
        n = len(cs)
        for k, c in enumerate(cs):
            a = t0 + 0.3 + (t1 - t0 - 0.5) * k / max(1, n); b = t0 + 0.3 + (t1 - t0 - 0.5) * (k + 1) / max(1, n) - 0.2
            caps.append((a, b, c))
    return caps

def narrated(lesson):
    """Time every scene to its narration: captions run back to back at the pace of the voice,
    and a scene lasts at least as long as what is said in it."""
    import copy, narrate
    L = copy.deepcopy(lesson); clips, caps, t = [], [], 0.0
    tl = []
    for s in L["scenes"]:
        cs = s.get("cap", [])
        if isinstance(cs, str): cs = [cs]
        audio = [narrate.line(c) for c in cs]
        lead = 0.9 if s["type"] in ("title", "end") else 0.6
        need = lead + sum(len(a) / narrate.SR + 0.45 for a in audio) + 0.5
        d = max(s["d"], need); s["d"] = d
        u = t + lead
        for c, a in zip(cs, audio):
            dur = len(a) / narrate.SR
            clips.append((u, a)); caps.append((u - 0.15, u + dur + 0.25, c)); u += dur + 0.45
        tl.append((t, t + d, s)); t += d
    return L, tl, t, caps, clips

def render_frame(lesson, tl, caps, total, i):
    t = i / FPS; img = Image.new("RGBA", (W, H), BG + (255,)); cv = Canvas(img)
    for t0, t1, s in tl:
        if t < t0 - 0.01 or t > t1 + 0.01: continue
        a = win(t, t0, t1, 0.45, 0.45)
        if s["type"] == "end": a *= 1 - clamp((t - (total - 1.0)) / 1.0)
        if a > 0: SCENES[s["type"]](cv, img, t - t0, t1 - t0, s, a)
    for a0, a1, txt in caps:
        ca = win(t, a0, a1, 0.3, 0.25)
        if ca <= 0: continue
        bb = _m.textbbox((W / 2, 1000), txt, font=F_CAP, anchor="mm")
        cv.rrect((bb[0] - 28, bb[1] - 18, bb[2] + 28, bb[3] + 18), 14, fill=(6, 8, 16), a=0.75 * ca)
        cv.text((W / 2, 1000), txt, F_CAP, WHITE, ca)
    return img.convert("RGB")

def vtt(caps, path):
    f = lambda s: f"{int(s // 3600):02d}:{int(s % 3600 // 60):02d}:{s % 60:06.3f}"
    with open(path, "w", encoding="utf-8") as fh:
        fh.write("WEBVTT\n\n")
        for k, (a, b, c) in enumerate(caps, 1): fh.write(f"{k}\n{f(a)} --> {f(b)}\n{c}\n\n")

def bed(total, path):
    subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-f", "lavfi", "-i",
        f"aevalsrc='0.05*sin(2*PI*110*t)*(0.6+0.4*sin(2*PI*0.05*t))+0.035*sin(2*PI*164.8*t)*(0.6+0.4*sin(2*PI*0.07*t+1))+0.03*sin(2*PI*220*t)*(0.5+0.5*sin(2*PI*0.03*t+2))+0.018*sin(2*PI*329.6*t)*(0.5+0.5*sin(2*PI*0.09*t))':s=48000:d={total}",
        "-af", f"lowpass=f=1800,afade=t=in:d=3,afade=t=out:st={total - 4}:d=4,aecho=0.6:0.5:400:0.25,volume=1.4", "-c:a", "aac", "-b:a", "96k", path], check=True)

if __name__ == "__main__":
    code = sys.argv[1]; L = importlib.import_module({"F": "scripts_f", "A": "scripts_a", "P": "scripts_p", "C": "scripts_c"}[code[0]]).LESSONS[code]
    import os
    NARR = os.environ.get("NARRATE", "1") != "0"
    if NARR: L, tl, total, caps, clips = narrated(L)
    else: tl, total = timeline(L); caps = captions(L); clips = []
    if sys.argv[2] == "preview":
        for k, (t0, t1, s) in enumerate(tl):
            render_frame(L, tl, caps, total, int(((t0 + t1) / 2 + 0.6) * FPS)).save(f"/tmp/pv_{code}_{k}.png")
        print(code, f"{total:.0f}s", len(tl), "scenes")
    else:
        out = sys.argv[2]; tmp = out.replace(".mp4", "_v.mp4")
        p = subprocess.Popen(["ffmpeg", "-y", "-loglevel", "error", "-f", "rawvideo", "-pix_fmt", "rgb24", "-s", f"{W}x{H}", "-r", str(FPS), "-i", "-",
                              "-c:v", "libx264", "-crf", "23", "-preset", "veryfast", "-pix_fmt", "yuv420p", tmp], stdin=subprocess.PIPE)
        for i in range(int(total * FPS)): p.stdin.write(render_frame(L, tl, caps, total, i).tobytes())
        p.stdin.close(); p.wait()
        bed(total, out.replace(".mp4", ".m4a"))
        if clips:
            import narrate
            narrate.mix(clips, total, out.replace(".mp4", "_voice.wav"))
            subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-i", tmp, "-i", out.replace(".mp4", "_voice.wav"), "-i", out.replace(".mp4", ".m4a"),
                            "-filter_complex", "[2:a]volume=0.32[b];[1:a]aresample=48000,volume=1.0[v];[v][b]amix=inputs=2:duration=first:normalize=0,loudnorm=I=-16:TP=-1.5:LRA=11[a]",
                            "-map", "0:v", "-map", "[a]", "-c:v", "copy", "-c:a", "aac", "-b:a", "128k", "-movflags", "+faststart", out], check=True)
        else:
            subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-i", tmp, "-i", out.replace(".mp4", ".m4a"), "-c", "copy", "-shortest", "-movflags", "+faststart", out], check=True)
        vtt(caps, out.replace(".mp4", ".vtt"))
        print(out, f"{total:.0f}s")
