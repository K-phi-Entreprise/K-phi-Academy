"""K-φ Academy lesson video, F1.1: One system of record for FP&A, Cash and Build.
1920x1080, 30 fps, silent captions on screen (and as a WebVTT file), sound bed added by ffmpeg."""
import sys, os, math, subprocess
import numpy as np
from PIL import Image, ImageDraw, ImageFilter
import diagram3 as D
from diagram3 import Canvas, ease, eo, back, clamp, lerp, lerp2, font, BG, YEL, WHITE, GREY, DIM, PANEL, PANEL2

W, H, FPS = 1920, 1080, 30
D.W, D.H = W, H
DUR = 70.0; N = int(DUR * FPS)
F_TITLE = font("Bold", 76); F_H = font("SemiBold", 44); F_L = font("SemiBold", 34); F_S = font("Regular", 28)
F_CAP = font("Medium", 38); F_MONO = font("Medium", 26); F_BIG = font("Bold", 64); F_K = font("Bold", 96); F_KS = font("Bold", 40)
RED = (255, 122, 122); TEAL = (54, 214, 160)
BAND = [(197, 179, 88), (54, 214, 160), (83, 74, 183), (230, 0, 126)]  # the K-φ brand aurora

_BAND = None
def band_img():
    global _BAND
    if _BAND: return _BAND
    w, h = 900, 260
    xs = np.linspace(0, 1, w)[None, :, None]; cols = np.array(BAND, float)
    idx = np.clip(xs * (len(cols) - 1), 0, len(cols) - 1.0001); i0 = idx.astype(int); f = idx - i0
    rgb = cols[i0[..., 0]] * (1 - f) + cols[i0[..., 0] + 1] * f
    rgb = np.repeat(rgb, h, axis=0)
    a = (np.sin(np.pi * np.linspace(0, 1, w))[None, :] ** 1.5) * (np.sin(np.pi * np.linspace(0, 1, h))[:, None] ** 2)
    img = np.dstack([rgb, 255 * a]).astype("uint8")
    _BAND = Image.fromarray(img, "RGBA"); return _BAND

def mark(cv, img, xy, f, a, sweep=None):
    """The K-φ mark in brand yellow; `sweep` in (0,1) runs the brand aurora across it once."""
    cv.text(xy, "K-φ", f, YEL, a)
    if sweep is None or not (0 < sweep < 1) or a <= 0: return
    bb = ImageDraw.Draw(Image.new("L", (1, 1))).textbbox(xy, "K-φ", font=f, anchor="mm")
    x0, y0, x1, y1 = [int(v) for v in bb]; pad = 16; w, h = x1 - x0 + 2 * pad, y1 - y0 + 2 * pad
    m = Image.new("L", (w, h), 0); ImageDraw.Draw(m).text((xy[0] - x0 + pad, xy[1] - y0 + pad), "K-φ", font=f, fill=255, anchor="mm")
    b = band_img().resize((int(w * 0.9), h)); bx = int(lerp(-b.width, w, sweep))
    layer = Image.new("RGBA", (w, h), (0, 0, 0, 0)); layer.alpha_composite(b, (bx, 0))
    la = np.array(layer.split()[3], float) * (np.array(m) / 255.0) * a * min(1.0, 3 * math.sin(math.pi * sweep))
    layer.putalpha(Image.fromarray(la.astype("uint8"), "L"))
    glow = layer.filter(ImageFilter.GaussianBlur(16)); glow.putalpha(Image.fromarray((np.array(glow.split()[3], float) * 0.6).astype("uint8"), "L"))
    img.alpha_composite(glow, (x0 - pad, y0 - pad)); img.alpha_composite(layer, (x0 - pad, y0 - pad))

def win(t, t0, t1, fi=0.5, fo=0.5): return clamp((t - t0) / fi) * clamp((t1 - t) / fo)

CAPS = [
    (0.8, 5.2, "F1.1 · One system of record for FP&A, Cash and Build"),
    (5.4, 10.6, "Most finance teams run on a ledger, a few bank portals, and many spreadsheets."),
    (10.8, 16.8, "The logic that matters often lives in those spreadsheets, outside any system."),
    (17.0, 23.8, "K-φ brings that work into one system of record."),
    (24.0, 30.8, "FP&A for the ledger and the plan. Cash for banks and invoices. Build for your own logic."),
    (31.0, 37.0, "A figure is imported once and reused everywhere."),
    (37.2, 42.8, "So the P&L, the cash forecast and your extension always agree."),
    (43.0, 49.0, "In the app, the three workspaces are one click apart."),
    (49.2, 54.8, "Switch workspaces with the tabs at the top of the left panel."),
    (55.0, 61.8, "Custom logic belongs inside the system that holds the data."),
    (62.0, 66.8, "Next: F1.2, a tour of the interface."),
]

SRC = [("General ledger", (330, 260)), ("Bank portals", (1560, 230)), ("Budget.xlsx", (520, 700)),
       ("Cash forecast.xlsx", (1000, 520)), ("Covenant test.xlsx", (1420, 690)), ("Margin calls.xlsx", (830, 390))]
COLS = [("FP&A", ["Statements", "KPIs", "Budget", "Forecast", "Valuation"], (470, 560)),
        ("Cash", ["Banks", "Cash position", "Receivables & payables", "Cash forecast"], (960, 560)),
        ("Build", ["Your own logic", "Extensions", "Writes back"], (1450, 560))]

UI = None
def ui():
    global UI
    if UI is None: UI = Image.open(sys.argv[3] if len(sys.argv) > 3 else "ui_home_hover.png").convert("RGBA").resize((W, H))
    return UI

def caption(cv, t):
    for t0, t1, txt in CAPS:
        a = win(t, t0, t1, 0.35, 0.3)
        if a <= 0: continue
        bb = ImageDraw.Draw(Image.new("L", (1, 1))).textbbox((W / 2, 1000), txt, font=F_CAP, anchor="mm")
        cv.rrect((bb[0] - 28, bb[1] - 18, bb[2] + 28, bb[3] + 18), 14, fill=(6, 8, 16), a=0.72 * a)
        cv.text((W / 2, 1000), txt, F_CAP, WHITE, a)

def frame(i):
    t = i / FPS
    img = Image.new("RGBA", (W, H), BG + (255,)); cv = Canvas(img)

    # S0 title
    a0 = win(t, 0.0, 5.0, 0.6, 0.6)
    if a0 > 0:
        mark(cv, img, (W / 2, 330), F_K, a0, sweep=(t - 0.6) / 2.4)
        cv.text((W / 2, 420), "ACADEMY", F_MONO, GREY, a0)
        y = 560 + 24 * (1 - eo((t - 0.4) / 0.8))
        cv.text((W / 2, y), "One system of record", F_TITLE, WHITE, a0 * clamp((t - 0.4) / 0.6))
        cv.text((W / 2, y + 92), "for FP&A, Cash and Build", F_TITLE, YEL, a0 * clamp((t - 0.7) / 0.6))
        cv.text((W / 2, y + 190), "Foundation · F1.1 · 6 min", F_MONO, GREY, a0 * clamp((t - 1.0) / 0.6))

    # S1 scattered sources, then S2 they fly into the hub
    if 5.0 <= t < 31.5:
        fly = ease((t - 17.2) / 1.6); a1 = clamp((t - 5.2) / 0.6) * (1 - clamp((t - 18.6) / 0.6))
        hub = (W / 2, 520)
        for k, (lab, (x, y)) in enumerate(SRC):
            ak = a1 * clamp((t - 5.3 - k * 0.25) / 0.5)
            if ak <= 0: continue
            j = 6 * (1 - fly); x += j * math.sin(t * 2.3 + k); y += j * math.cos(t * 1.9 + k * 1.7)
            x, y = lerp2((x, y), hub, fly); s = 1 - 0.6 * fly
            sheet = lab.endswith(".xlsx"); hot = sheet and t > 10.8
            w2, h2 = (len(lab) * 11 + 70) * s, 42 * s
            cv.rrect((x - w2, y - h2, x + w2, y + h2), 16, fill=PANEL2, outline=(RED if hot else DIM), width=3, a=ak)
            if hot: cv.rrect((x - w2, y - h2, x + w2, y + h2), 16, fill=RED, a=ak * 0.06 * (1 + math.sin(t * 4)), blur=12)
            cv.text((x, y), lab, F_L if s > 0.8 else F_S, WHITE, ak)
        # dashed links between sources, the "copy-paste" web
        if a1 > 0 and fly < 0.3:
            for (p, q) in [(0, 2), (0, 3), (1, 3), (3, 4), (2, 5), (5, 3)]:
                pa, pb = SRC[p][1], SRC[q][1]; L = math.dist(pa, pb); n = int(L / 26)
                for s_ in range(0, n, 2):
                    u0, u1 = s_ / n, (s_ + 1) / n
                    cv.line([lerp2(pa, pb, u0), lerp2(pa, pb, u1)], DIM, 3, a1 * 0.7 * (1 - fly / 0.3))
        # hub
        ah = clamp((t - 17.6) / 0.6) * (1 - clamp((t - 31.0) / 0.5))
        if ah > 0:
            ex = ease((t - 19.0) / 1.2); hw, hh = lerp(170, 760, ex), lerp(80, 330, ex); x, y = hub
            cv.rrect((x - hw, y - hh, x + hw, y + hh), 30, fill=YEL, a=ah * 0.08, blur=22)
            cv.rrect((x - hw, y - hh, x + hw, y + hh), 28, fill=PANEL, outline=YEL, width=4, a=ah)
            if ex < 0.5: mark(cv, img, (x, y), F_BIG, ah * (1 - 2 * ex), sweep=(t - 17.8) / 1.4)
            else:
                mark(cv, img, (x, y - hh + 60), F_KS, ah * (ex - 0.5) * 2)
                for c, (name, items, (cx, cy)) in enumerate(COLS):
                    ac = ah * clamp((t - 20.2 - c * 0.5) / 0.5)
                    if ac <= 0: continue
                    sl = (1 - back(clamp((t - 20.2 - c * 0.5) / 0.6))) * 30
                    cv.rrect((cx - 220, cy - 200 + sl, cx + 220, cy + 230 + sl), 18, fill=PANEL2, outline=DIM, width=2, a=ac)
                    cv.text((cx, cy - 160 + sl), name, F_H, YEL, ac)
                    for r, it in enumerate(items):
                        ar = ac * clamp((t - 24.2 - c * 1.6 - r * 0.25) / 0.4)
                        cv.text((cx - 180, cy - 90 + r * 62 + sl), "·  " + it, F_S, WHITE, ar, anchor="lm")

    # S3 one data model: a figure travels to three places
    a3 = win(t, 31.2, 43.0, 0.6, 0.6)
    if a3 > 0:
        src = (360, 500); dst = [(1500, 300, "P&L", "Revenue  4,215,300"), (1500, 520, "Cash forecast", "Collections  +4,215,300"), (1500, 740, "Your extension", "Margin check  ok")]
        cv.rrect((src[0] - 230, src[1] - 90, src[0] + 230, src[1] + 90), 18, fill=PANEL2, outline=YEL, width=3, a=a3)
        cv.text((src[0], src[1] - 34), "Imported once", F_S, GREY, a3)
        cv.text((src[0], src[1] + 18), "Revenue  4,215,300", F_L, WHITE, a3)
        cv.text((src[0], src[1] + 58), "Halden Trading Inc. · USD", F_MONO, GREY, a3)
        for k, (x, y, name, val) in enumerate(dst):
            p = eo((t - 32.2 - k * 0.7) / 1.2)
            if p <= 0: continue
            pts = [D.bez((src[0] + 230, src[1]), (900, src[1]), (1100, y), (x - 250, y), u * p) for u in [j / 40 for j in range(41)]]
            cv.line(pts, YEL, 12, a3 * 0.12, blur=5); cv.line(pts, YEL, 3, a3 * 0.9)
            if p < 1: cv.dot(pts[-1], 9, YEL, a3)
            else:
                ph = ((t * 0.6 + k * 0.33) % 1.0); D.spark(cv, D.bez((src[0] + 230, src[1]), (900, src[1]), (1100, y), (x - 250, y), ph), math.sin(math.pi * ph) ** 0.6, a3)
            ab = a3 * clamp((t - 33.2 - k * 0.7) / 0.4)
            cv.rrect((x - 250, y - 70, x + 250, y + 70), 16, fill=PANEL2, outline=(TEAL if t > 37.4 else DIM), width=3, a=ab)
            cv.text((x - 220, y - 22), name, F_S, GREY, ab, anchor="lm"); cv.text((x - 220, y + 22), val, F_L, WHITE, ab, anchor="lm")
            if t > 37.4 + k * 0.3:
                ck = ab * clamp((t - 37.4 - k * 0.3) / 0.3); cx, cy = x + 205, y
                cv.dot((cx, cy), 22, TEAL, ck * 0.25); cv.line([(cx - 10, cy), (cx - 2, cy + 9), (cx + 12, cy - 9)], TEAL, 5, ck)

    # S4 the real interface, slow push-in toward the workspace switcher
    a4 = win(t, 43.0, 55.0, 0.8, 0.7)
    if a4 > 0:
        z = 1 + 0.55 * ease((t - 44.5) / 8.0); fx, fy = lerp(W / 2, 300, ease((t - 44.5) / 8.0)), lerp(H / 2, 260, ease((t - 44.5) / 8.0))
        src = ui(); cw, ch = W / z, H / z; x0 = clamp(fx - cw / 2, 0, W - cw); y0 = clamp(fy - ch / 2, 0, H - ch)
        crop = src.crop((int(x0), int(y0), int(x0 + cw), int(y0 + ch))).resize((W, H), Image.LANCZOS)
        crop.putalpha(Image.fromarray((np.array(crop.split()[3], float) * a4).astype("uint8"), "L")); img.alpha_composite(crop)
        if t > 49.2:  # ring around the switcher (top of the left panel)
            ar = a4 * clamp((t - 49.2) / 0.4)
            bx0, by0, bx1, by1 = (8 - x0) * z, (80 - y0) * z, (218 - x0) * z, (130 - y0) * z
            cv.rrect((bx0, by0, bx1, by1), 14, outline=YEL, width=5, a=ar * (0.7 + 0.3 * math.sin(t * 5)))
            lx, ly = bx1 + 34, (by0 + by1) / 2
            cv.rrect((lx - 16, ly - 36, lx + 360, ly + 36), 14, fill=(6, 8, 16), a=ar * 0.85)
            cv.text((lx, ly), "Workspace tabs", F_H, YEL, ar, anchor="lm")

    # S5 thesis + key points
    a5 = win(t, 55.0, 62.0, 0.6, 0.6)
    if a5 > 0:
        cv.text((W / 2, 330), "Custom logic belongs", F_TITLE, WHITE, a5 * clamp((t - 55.2) / 0.6))
        cv.text((W / 2, 420), "inside the system that holds the data.", F_TITLE, YEL, a5 * clamp((t - 55.6) / 0.6))
        pts = ["K-φ is one system of record for FP&A, Cash and Build.", "Data comes in once and is reused across workspaces.", "Custom logic is built inside K-φ, next to the data it uses."]
        for k, ptxt in enumerate(pts):
            ak = a5 * clamp((t - 57.0 - k * 0.6) / 0.5); y = 580 + k * 80
            cv.text((440, y), "→", F_L, YEL, ak, anchor="lm"); cv.text((500, y), ptxt, F_L, WHITE, ak, anchor="lm")

    # S6 end card
    a6 = win(t, 62.0, DUR + 1, 0.6, 0.6) * (1 - clamp((t - (DUR - 1.0)) / 1.0))
    if a6 > 0:
        mark(cv, img, (W / 2, 420), F_K, a6, sweep=(t - 62.6) / 2.4)
        cv.text((W / 2, 510), "ACADEMY", F_MONO, GREY, a6)
        cv.text((W / 2, 640), "Next  ·  F1.2  A tour of the interface", F_H, WHITE, a6 * clamp((t - 62.8) / 0.6))
        cv.text((W / 2, 710), "academy.k-phi.com", F_MONO, GREY, a6 * clamp((t - 63.2) / 0.6))

    caption(cv, t)
    return img.convert("RGB")

def vtt(path):
    f = lambda s: f"{int(s // 3600):02d}:{int(s % 3600 // 60):02d}:{s % 60:06.3f}"
    with open(path, "w", encoding="utf-8") as fh:
        fh.write("WEBVTT\n\n")
        for k, (t0, t1, txt) in enumerate(CAPS, 1): fh.write(f"{k}\n{f(t0)} --> {f(t1)}\n{txt}\n\n")

if __name__ == "__main__":
    if sys.argv[1] == "preview":
        for tt in [2.5, 8, 13, 22, 28, 35, 40, 47, 52, 58, 64]: frame(int(tt * FPS)).save(f"/tmp/p_{tt}.png")
    else:
        vtt(sys.argv[2].replace(".mp4", ".vtt"))
        p = subprocess.Popen(["ffmpeg", "-y", "-loglevel", "error", "-f", "rawvideo", "-pix_fmt", "rgb24", "-s", f"{W}x{H}", "-r", str(FPS), "-i", "-",
                              "-c:v", "libx264", "-crf", "20", "-preset", "veryfast", "-pix_fmt", "yuv420p", sys.argv[2]], stdin=subprocess.PIPE)
        for i in range(N): p.stdin.write(frame(i).tobytes())
        p.stdin.close(); p.wait()
        # narration, fitted to the fixed caption windows (a line too long is read a little faster)
        import narrate
        clips = []
        for t0, t1, txt in CAPS:
            room = t1 - t0 - 0.35; au = narrate.line(txt); sp = 1.0
            while len(au) / narrate.SR > room and sp < 1.3:
                sp = round(sp + 0.05, 2); au = narrate.line(txt, speed=sp)
            clips.append((t0 + 0.15, au))
        out = sys.argv[2]; base = out.replace(".mp4", "")
        narrate.mix(clips, DUR, base + "_voice.wav")
        import lv
        lv.bed(DUR, base + ".m4a")
        os.replace(out, base + "_v.mp4")
        subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-i", base + "_v.mp4", "-i", base + "_voice.wav", "-i", base + ".m4a",
                        "-filter_complex", "[2:a]volume=0.32[b];[1:a]aresample=48000[v];[v][b]amix=inputs=2:duration=first:normalize=0,loudnorm=I=-16:TP=-1.5:LRA=11[a]",
                        "-map", "0:v", "-map", "[a]", "-c:v", "copy", "-c:a", "aac", "-b:a", "128k", "-movflags", "+faststart", out], check=True)
