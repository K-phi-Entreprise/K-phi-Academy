import sys, math, subprocess
import numpy as np
from PIL import Image, ImageDraw, ImageFont, ImageFilter

W, H, FPS, DUR = 1920, 1080, 30, 10.0
N = int(DUR * FPS)
BG = (11, 15, 26); YEL = (230, 255, 0); WHITE = (240, 242, 246); GREY = (150, 158, 175)
DIM = (80, 88, 108); PANEL = (18, 24, 40); PANEL2 = (28, 36, 58)
FD = "/usr/share/fonts/opentype/inter/"
def font(w, s): return ImageFont.truetype(FD + f"InterDisplay-{w}.otf", s)
F_L = font("SemiBold", 34); F_S = font("Regular", 30); F_K = font("Bold", 72); F_CAP = font("Medium", 40); F_T = font("SemiBold", 38)

def ease(t): return 0 if t <= 0 else 1 if t >= 1 else (1 - math.cos(math.pi * t)) / 2
def eo(t): return 0 if t <= 0 else 1 if t >= 1 else 1 - (1 - t) ** 3
def back(t):  # ease-out with a slight overshoot
    if t <= 0: return 0
    if t >= 1: return 1
    c = 1.4; return 1 + (c + 1) * (t - 1) ** 3 + c * (t - 1) ** 2
def clamp(x, a=0, b=1): return max(a, min(b, x))
def lerp(a, b, t): return a + (b - a) * t
def lerp2(a, b, t): return (lerp(a[0], b[0], t), lerp(a[1], b[1], t))

class Canvas:
    def __init__(self, img): self.img = img
    def _blit(self, box, fn, blur=0):
        x0, y0, x1, y1 = [int(v) for v in box]; m = 4 + blur * 3
        x0 = max(0, x0 - m); y0 = max(0, y0 - m); x1 = min(W, x1 + m); y1 = min(H, y1 + m)
        if x1 <= x0 or y1 <= y0: return
        L = Image.new("RGBA", (x1 - x0, y1 - y0), (0, 0, 0, 0)); fn(ImageDraw.Draw(L), -x0, -y0)
        if blur: L = L.filter(ImageFilter.GaussianBlur(blur))
        self.img.alpha_composite(L, (x0, y0))
    def rrect(self, box, r, fill=None, outline=None, width=2, a=1.0, blur=0):
        if a <= 0: return
        A = int(255 * clamp(a))
        self._blit(box, lambda d, ox, oy: d.rounded_rectangle((box[0] + ox, box[1] + oy, box[2] + ox, box[3] + oy), radius=r,
                   fill=fill + (A,) if fill else None, outline=outline + (A,) if outline else None, width=width), blur)
    def text(self, xy, txt, f, color, a=1.0, anchor="mm"):
        if a <= 0: return
        A = int(255 * clamp(a)); bb = ImageDraw.Draw(Image.new("L", (1, 1))).textbbox(xy, txt, font=f, anchor=anchor)
        self._blit(bb, lambda d, ox, oy: d.text((xy[0] + ox, xy[1] + oy), txt, font=f, fill=color + (A,), anchor=anchor))
    def line(self, pts, color, width, a=1.0, blur=0):
        if a <= 0 or len(pts) < 2: return
        A = int(255 * clamp(a)); xs = [p[0] for p in pts]; ys = [p[1] for p in pts]
        self._blit((min(xs) - width * 3, min(ys) - width * 3, max(xs) + width * 3, max(ys) + width * 3),
                   lambda d, ox, oy: d.line([(x + ox, y + oy) for x, y in pts], fill=color + (A,), width=width, joint="curve"), blur)
    def poly(self, pts, color, a=1.0):
        if a <= 0: return
        A = int(255 * clamp(a)); xs = [p[0] for p in pts]; ys = [p[1] for p in pts]
        self._blit((min(xs), min(ys), max(xs), max(ys)), lambda d, ox, oy: d.polygon([(x + ox, y + oy) for x, y in pts], fill=color + (A,)))
    def dot(self, c, r, color, a=1.0, blur=0):
        if a <= 0: return
        A = int(255 * clamp(a))
        self._blit((c[0] - r, c[1] - r, c[0] + r, c[1] + r), lambda d, ox, oy: d.ellipse((c[0] - r + ox, c[1] - r + oy, c[0] + r + ox, c[1] + r + oy), fill=color + (A,)), blur)

# sources: scattered start -> tidy column once connected
SOURCES = [("ERP", (150, 300)), ("Banks", (470, 170)), ("CRM", (190, 610)), ("Google Sheets", (520, 470)),
           ("Excel", (240, 850)), ("Payments", (560, 760))]
COL_X = 430; COL_Y0 = 215; COL_DY = 130
NODE_W = 300; NODE_H = 76
HUB = (960, 540); HUB_HW, HUB_HH = 290, 330
APP = (1600, 540); APP_HW, APP_HH = 250, 330

AUR = None
def aurora_band():
    global AUR
    if AUR is not None: return AUR
    bw, bh = 460, 220
    xs = np.arange(bw); ys = np.arange(bh)
    X, Y = np.meshgrid(xs, ys)
    # palette ribbon: violet -> teal -> green -> teal -> violet across X, with ripples
    u = (X / bw) * 2 - 1
    rip = 0.5 + 0.5 * np.sin(X / 38 + Y / 60)
    stops = [(-1.0, (190, 70, 255)), (-0.45, (0, 200, 200)), (0.0, (90, 255, 110)), (0.45, (0, 200, 200)), (1.0, (190, 70, 255))]
    su = np.array([s[0] for s in stops]); sc = np.array([s[1] for s in stops], float)
    r = np.interp(u, su, sc[:, 0]); gg = np.interp(u, su, sc[:, 1]); b = np.interp(u, su, sc[:, 2])
    a = (1 - 0.55 * u ** 2) * (0.8 + 0.2 * rip) * 255
    arr = np.stack([r, gg, b, a], -1).clip(0, 255).astype("uint8")
    AUR = Image.fromarray(arr, "RGBA").filter(ImageFilter.GaussianBlur(6))
    return AUR

def logo(cv, img, xy, size_font, a, sweep):
    """K-φ wordmark; `sweep` in [0,1] runs an aurora across the glyphs once (None = plain)."""
    cv.text(xy, "K-φ", size_font, YEL, a)
    if sweep is None or sweep <= 0 or sweep >= 1 or a <= 0: return
    bb = ImageDraw.Draw(Image.new("L", (1, 1))).textbbox(xy, "K-φ", font=size_font, anchor="mm")
    x0, y0, x1, y1 = [int(v) for v in bb]; pad = 10
    w, h = x1 - x0 + 2 * pad, y1 - y0 + 2 * pad
    mask = Image.new("L", (w, h), 0); ImageDraw.Draw(mask).text((pad - 0 + (xy[0] - x0), pad + (xy[1] - y0)), "K-φ", font=size_font, fill=255, anchor="mm")
    band = aurora_band(); bx = int(lerp(-band.width, w, sweep))
    layer = Image.new("RGBA", (w, h), (0, 0, 0, 0)); layer.alpha_composite(band, (bx, (h - band.height) // 2))
    la = np.array(layer.split()[3]).astype(float) * (np.array(mask) / 255.0) * a * min(1.0, 3 * math.sin(math.pi * sweep))
    layer.putalpha(Image.fromarray(la.astype("uint8"), "L"))
    # glow around the glyphs where the aurora is
    glow = layer.filter(ImageFilter.GaussianBlur(14)); ga = np.array(glow.split()[3]).astype(float) * 0.55
    glow.putalpha(Image.fromarray(ga.astype("uint8"), "L"))
    img.alpha_composite(glow, (x0 - pad, y0 - pad)); img.alpha_composite(layer, (x0 - pad, y0 - pad))

def src_pos(k, t):
    s0 = SOURCES[k][1]; s1 = (COL_X, COL_Y0 + k * COL_DY)
    jit = 7 * (1 - ease((t - 2.2) / 0.8))
    p = eo((t - 2.3 - k * 0.06) / 0.9)
    x, y = lerp2(s0, s1, p)
    return (x + jit * math.sin(t * 7 + k * 1.3), y + jit * math.cos(t * 5.5 + k * 2.1))

def arrow(cv, pts, prog, a, color=YEL, width=5):
    if prog <= 0 or a <= 0: return
    segs = [(pts[i], pts[i + 1]) for i in range(len(pts) - 1)]; lens = [math.dist(p, q) for p, q in segs]
    target = sum(lens) * clamp(prog); out = [pts[0]]; acc = 0; p0 = pts[0]; p1 = pts[0]
    for (p, q), l in zip(segs, lens):
        if acc + l >= target:
            f = (target - acc) / l if l else 0; p0, p1 = p, lerp2(p, q, f); out.append(p1); break
        out.append(q); acc += l; p0, p1 = p, q
    cv.line(out, color, width * 3, a * 0.18, blur=6); cv.line(out, color, width, a)
    if prog >= 0.98:
        ang = math.atan2(p1[1] - p0[1], p1[0] - p0[0]); x, y = p1
        cv.poly([(x, y), (x - 24 * math.cos(ang - 0.45), y - 24 * math.sin(ang - 0.45)), (x - 24 * math.cos(ang + 0.45), y - 24 * math.sin(ang + 0.45))], color, a)


def bez(p0, c0, c1, p1, u):
    v = 1 - u
    return (v**3*p0[0] + 3*v*v*u*c0[0] + 3*v*u*u*c1[0] + u**3*p1[0],
            v**3*p0[1] + 3*v*v*u*c0[1] + 3*v*u*u*c1[1] + u**3*p1[1])
def curve_pts(p0, p1, prog, n=40):
    dx = p1[0] - p0[0]; c0, c1 = (p0[0] + 0.55 * dx, p0[1]), (p1[0] - 0.35 * dx, p1[1])
    return [bez(p0, c0, c1, p1, u * clamp(prog)) for u in [i / n for i in range(n + 1)]]
def curve_at(p0, p1, u):
    dx = p1[0] - p0[0]
    return bez(p0, (p0[0] + 0.55 * dx, p0[1]), (p1[0] - 0.35 * dx, p1[1]), p1, u)
def poly_at(pts, u):
    segs = [(pts[i], pts[i + 1]) for i in range(len(pts) - 1)]; lens = [math.dist(p, q) for p, q in segs]
    target = sum(lens) * clamp(u); acc = 0
    for (p, q), l in zip(segs, lens):
        if acc + l >= target: return lerp2(p, q, (target - acc) / l if l else 0)
        acc += l
    return pts[-1]
def spark(cv, p, fa, a):
    cv.dot(p, 11, YEL, 0.28 * fa * a, blur=4); cv.dot(p, 4, WHITE, 0.95 * fa * a)

def icon(cv, kind, c, a, col=(170, 180, 200)):
    x, y = c
    if kind == "ERP":      # database: three stacked discs
        for j in range(3): cv.rrect((x - 13, y - 13 + j * 9, x + 13, y - 5 + j * 9), 4, outline=col, width=2, a=a)
    elif kind == "Banks":  # building with columns
        cv.poly([(x - 15, y - 6), (x, y - 15), (x + 15, y - 6)], col, a)
        for j in (-10, -3, 4, 11): cv.line([(x + j, y - 3), (x + j, y + 10)], col, 2, a)
        cv.line([(x - 15, y + 13), (x + 15, y + 13)], col, 2, a)
    elif kind == "CRM":    # two people
        cv.dot((x - 6, y - 7), 5, col, a); cv.dot((x + 7, y - 5), 4, col, a)
        cv.rrect((x - 15, y + 1, x + 2, y + 13), 5, fill=col, a=a); cv.rrect((x + 1, y + 3, x + 15, y + 13), 5, fill=col, a=a)
    elif kind in ("Google Sheets", "Excel"):  # grid
        cv.rrect((x - 14, y - 13, x + 14, y + 13), 3, outline=col, width=2, a=a)
        cv.line([(x - 14, y - 4), (x + 14, y - 4)], col, 2, a); cv.line([(x - 14, y + 5), (x + 14, y + 5)], col, 2, a)
        cv.line([(x - 4, y - 13), (x - 4, y + 13)], col, 2, a)
    elif kind == "Payments":  # card
        cv.rrect((x - 15, y - 10, x + 15, y + 10), 3, outline=col, width=2, a=a)
        cv.line([(x - 15, y - 3), (x + 15, y - 3)], col, 4, a)

def frame(i):
    t = i / FPS
    img = Image.new("RGBA", (W, H), BG + (255,)); cv = Canvas(img)
    caps = [(0.0, 2.3, "Your logic lives in spreadsheets. Your data lives everywhere."),
            (2.3, 4.6, "Connect every source once."),
            (4.6, 7.0, "Build on what is already normalised."),
            (7.0, 10.0, "Your bespoke system, inside the one you run.")]
    for t0, t1, c in caps:
        cv.text((W / 2, 1012), c, F_CAP, WHITE, clamp((t - t0) / 0.35) * clamp((t1 - t) / 0.3))

    # hub geometry
    hub_a = clamp((t - 2.0) / 0.5); ex = ease((t - 4.5) / 1.1)
    hw, hh = lerp(150, HUB_HW, ex), lerp(64, HUB_HH, ex)
    pulse = 1 + 0.015 * math.sin(t * 6) * (1 - ex)
    hw *= pulse; hh *= pulse

    # 1+2. sources and curved lines into the Connectors shelf
    shelf_y = HUB[1] - HUB_HH + 172
    for k, (lab, _) in enumerate(SOURCES):
        a = clamp((t - 0.15 - k * 0.16) / 0.4); x, y = src_pos(k, t)
        lp = eo((t - 2.6 - k * 0.1) / 0.8)
        if lp > 0:
            p0 = (x + NODE_W / 2, y)
            ty = lerp(HUB[1] + (y - HUB[1]) * 0.22, shelf_y - 70 + k * 30, ex)
            p1 = (HUB[0] - hw + 2, ty)
            pts = curve_pts(p0, p1, lp)
            cv.line(pts, YEL, 14, hub_a * 0.14, blur=5); cv.line(pts, YEL, 3, hub_a * 0.9)
            if lp < 1: cv.dot(pts[-1], 8, YEL, hub_a, blur=1)
            else:
                for n in range(2):
                    ph = ((t * 0.5 + k * 0.17 + n * 0.5) % 1.0)
                    spark(cv, curve_at(p0, p1, ph), math.sin(math.pi * ph) ** 0.6, 1)
        cv.rrect((x - NODE_W / 2, y - NODE_H / 2, x + NODE_W / 2, y + NODE_H / 2), 18, fill=PANEL2, outline=DIM if lp < 1 else (120, 140, 60), width=3, a=a)
        icon(cv, lab, (x - NODE_W / 2 + 36, y), a)
        cv.text((x - NODE_W / 2 + 68, y), lab, F_L, WHITE, a, anchor="lm")

    # 3. hub
    if hub_a > 0:
        x, y = HUB
        cv.rrect((x - hw, y - hh, x + hw, y + hh), 28, fill=YEL, a=hub_a * 0.10, blur=18)
        cv.rrect((x - hw, y - hh, x + hw, y + hh), 26, fill=PANEL, outline=YEL, width=4, a=hub_a)
        if ex < 0.5: logo(cv, img, (x, y), F_K, hub_a * (1 - ex * 2), None)
        else:
            la = (ex - 0.5) * 2
            logo(cv, img, (x, y - hh + 56), F_K, la, (t - 5.7) / 1.0)
            rows = [("Connectors", "any source, normalised once"),
                    ("Pre-built blocks", "cash · forecast · scenarios"),
                    ("Data library", "FX · rates · curves")]
            for j, (h, s) in enumerate(rows):
                aj = clamp((ex - 0.55 - j * 0.12) / 0.3); ry = y - hh + 172 + j * 168
                sl = (1 - back(aj)) * 40
                cv.rrect((x - hw + 28, ry - 58 + sl, x + hw - 28, ry + 58 + sl), 16, fill=PANEL2, outline=DIM, width=2, a=aj)
                cv.text((x, ry - 20 + sl), h, F_L, YEL, aj); cv.text((x, ry + 24 + sl), s, F_S, GREY, aj)

    # 4. bespoke system
    app_a = clamp((t - 6.8) / 0.4); x, y, ahw, ahh = APP[0], APP[1], APP_HW, APP_HH
    fwd = [(HUB[0] + HUB_HW, HUB[1] - 90), (APP[0] - ahw, APP[1] - 90)]
    arrow(cv, fwd, eo((t - 6.9) / 0.6), app_a)
    if t > 7.6:
        for n in range(2):
            ph = ((t * 0.9 + n * 0.5) % 1.0); spark(cv, poly_at(fwd, ph), math.sin(math.pi * ph) ** 0.6, 1)
    cv.rrect((x - ahw, y - ahh, x + ahw, y + ahh), 26, fill=PANEL, outline=WHITE, width=3, a=app_a * 0.85)
    cv.text((x, y - ahh + 52), "Your bespoke system", F_T, WHITE, app_a)
    cv.text((x, y - ahh + 96), "built from Claude, in days", F_S, GREY, app_a)
    tiles = [("Your sources", "through connectors"), ("Your logic", "described, not coded"),
             ("Blocks you reuse", "cash · forecast · scenarios"), ("Market data", "from the Data library"),
             ("Your results", "written back into K-φ")]
    asm = (t - 7.25) / 1.4
    for j, (h, s) in enumerate(tiles):
        aj = clamp((asm - j * 0.13) / 0.32)
        if aj <= 0: continue
        ty = y - ahh + 166 + j * 104; sx = lerp(x - 420, x, back(aj)); last = j == 4
        cv.rrect((sx - ahw + 26, ty - 42, sx + ahw - 26, ty + 42), 14, fill=PANEL2, outline=YEL if last else DIM, width=2, a=app_a * aj)
        cv.text((sx - ahw + 46, ty - 14), h, F_L, WHITE, app_a * aj, anchor="lm")
        cv.text((sx - ahw + 46, ty + 22), s, F_S, YEL if last else GREY, app_a * aj, anchor="lm")
    wb = eo((t - 8.85) / 0.6)
    wbp = [(APP[0], APP[1] + ahh), (APP[0], 928), (HUB[0], 928), (HUB[0], HUB[1] + HUB_HH + 2)]
    arrow(cv, wbp, wb, app_a)
    if wb >= 1:
        for n in range(3):
            ph = ((t * 0.7 + n / 3) % 1.0); spark(cv, poly_at(wbp, ph), math.sin(math.pi * ph) ** 0.6, 1)
        # the loop is closed: hub breathes
        g = 0.5 + 0.5 * math.sin((t - 9.45) * 5)
        cv.rrect((HUB[0] - HUB_HW, HUB[1] - HUB_HH, HUB[0] + HUB_HW, HUB[1] + HUB_HH), 28, fill=YEL, a=0.05 * g * clamp((t - 9.45) / 0.3), blur=22)
    cv.text(((APP[0] + HUB[0]) / 2, 958), "writes back", F_S, YEL, clamp((t - 9.35) / 0.3))
    # top-right tag (small logo, no sweep)
    ta = clamp((t - 9.1) / 0.4)
    cv.text((W - 60, 70), "FP&A · Cash · Build", F_L, WHITE, ta, anchor="rm")
    cv.text((W - 408, 70), "K-φ", F_L, YEL, ta, anchor="rm")
    return img.convert("RGB")

if __name__ == "__main__":
    if sys.argv[1] == "preview":
        for tt in [1.2, 3.2, 5.0, 6.1, 8.4, 9.8]:
            frame(int(tt * FPS)).save(f"e_{tt}.png")
    else:
        p = subprocess.Popen(["ffmpeg", "-y", "-loglevel", "error", "-f", "rawvideo", "-pix_fmt", "rgb24", "-s", f"{W}x{H}",
                              "-r", str(FPS), "-i", "-", "-c:v", "libx264", "-crf", "18", "-preset", "veryfast",
                              "-pix_fmt", "yuv420p", sys.argv[2]], stdin=subprocess.PIPE)
        for i in range(N): p.stdin.write(frame(i).tobytes())
        p.stdin.close(); sys.exit(p.wait())
