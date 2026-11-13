import os, sys
from PIL import Image, ImageDraw, ImageFont
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from content import POSTS, H

W, HT = 1080, 1350
CREAM = (251, 248, 243)
SAND = (240, 233, 222)
TEAL = (14, 77, 74)
TEAL_D = (9, 56, 54)
INK = (40, 52, 51)
MUTED = (118, 132, 128)
ORANGE = (226, 128, 58)
BASE = os.path.dirname(os.path.abspath(__file__))
SERIF = os.path.join(BASE, "fonts", "CormorantGaramond%5Bwght%5D.ttf")
SANS = os.path.join(BASE, "fonts", "Jost%5Bwght%5D.ttf")

def font(path, size, wght):
    f = ImageFont.truetype(path, size)
    f.set_variation_by_axes([wght])
    return f

def serif(s, w=600): return font(SERIF, s, w)
def sans(s, w=400): return font(SANS, s, w)

def wrap(d, text, f, maxw):
    lines, cur = [], ""
    for word in text.split():
        t = (cur + " " + word).strip()
        if d.textlength(t, font=f) <= maxw: cur = t
        else:
            if cur: lines.append(cur)
            cur = word
    if cur: lines.append(cur)
    return lines

def fit(d, text, fn, maxw, maxh, start, minsize, lh):
    s = start
    while s >= minsize:
        f = fn(s); ls = wrap(d, text, f, maxw)
        if len(ls) * s * lh <= maxh: return f, ls, s
        s -= 2
    f = fn(minsize); return f, wrap(d, text, f, maxw), minsize

def spaced(d, xy, text, f, fill, track=4):
    x, y = xy
    for ch in text:
        d.text((x, y), ch, font=f, fill=fill); x += d.textlength(ch, font=f) + track
    return x

def chrome(d, idx, total, dark=False):
    fg = CREAM if dark else TEAL
    mu = (190, 214, 210) if dark else MUTED
    spaced(d, (90, 80), "ZELOVITA", sans(26, 500), fg, 6)
    spaced(d, (90, 118), "BEM-ESTAR SEM COMPLICAÇÃO", sans(18, 400), mu, 3)
    d.line([(90, HT - 140), (W - 90, HT - 140)], fill=mu, width=1)
    d.text((90, HT - 115), H, font=sans(28, 400), fill=mu)
    t = f"{idx}/{total}"
    f = sans(28, 400)
    d.text((W - 90 - d.textlength(t, font=f), HT - 115), t, font=f, fill=mu)

def body_block(d, x, y, body, maxw, maxh, start=44):
    if isinstance(body, list):
        s = start
        while s >= 30:
            f = sans(s, 400); lh = 1.45
            rows = []
            for b in body:
                ls = wrap(d, b, f, maxw - (0 if b[:1].isdigit() else 44))
                rows.append(ls)
            h = sum(len(r) for r in rows) * s * lh + (len(rows) - 1) * s * 0.55
            if h <= maxh: break
            s -= 2
        for ls in rows:
            num = ls and ls[0][:2].rstrip(".").isdigit()
            if not num:
                d.ellipse([x, y + s * 0.42, x + 14, y + s * 0.42 + 14], fill=ORANGE)
            for l in ls:
                d.text((x + (0 if num else 44), y), l, font=f, fill=INK); y += s * lh
            y += s * 0.55
        return y
    f, ls, s = fit(d, body, lambda z: sans(z, 400), maxw, maxh, start, 30, 1.45)
    for l in ls:
        d.text((x, y), l, font=f, fill=INK); y += s * 1.45
    return y

def draw_slide(sl, idx, total):
    t = sl["type"]
    dark = t == "cta"
    img = Image.new("RGB", (W, HT), TEAL if dark else CREAM)
    d = ImageDraw.Draw(img)
    if not dark:
        d.ellipse([W - 330, -230, W + 230, 330], fill=SAND)
    chrome(d, idx, total, dark)
    X, MW = 90, W - 180
    if t == "cover":
        y = 360
        if sl.get("publi"):
            f = sans(24, 500); txt = "#PUBLI  ·  LINK DE AFILIADO"
            tw = sum(d.textlength(c, font=f) + 3 for c in txt)
            d.rounded_rectangle([X, y - 90, X + tw + 44, y - 40], radius=25, outline=ORANGE, width=2)
            spaced(d, (X + 22, y - 80), txt, f, ORANGE, 3)
        spaced(d, (X, y), sl["kicker"], sans(26, 500), ORANGE, 5)
        y += 70
        f, ls, s = fit(d, sl["title"], lambda z: serif(z, 600), MW, 520, 118, 70, 1.05)
        for l in ls:
            d.text((X, y), l, font=f, fill=TEAL, features=["lnum"]); y += s * 1.05
        y += 40
        d.line([(X, y), (X + 120, y)], fill=ORANGE, width=4); y += 50
        y = body_block(d, X, y, sl["body"], MW, 220, 42)
        d.text((X, HT - 230), "deslize para o lado", font=sans(30, 400), fill=MUTED)
    elif t in ("item", "text"):
        y = 300
        if t == "item":
            r = 52
            d.ellipse([X, y, X + 2 * r, y + 2 * r], fill=TEAL)
            n = sl["num"]
            f = sans(46, 500) if n.isdigit() else font("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 46, 400) if False else sans(46, 500)
            if not n.isdigit():
                f = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 48)
            bb = d.textbbox((0, 0), n, font=f)
            d.text((X + r - (bb[2] - bb[0]) / 2 - bb[0], y + r - (bb[3] - bb[1]) / 2 - bb[1]), n, font=f, fill=CREAM)
            y += 2 * r + 50
        else:
            d.line([(X, y + 20), (X + 80, y + 20)], fill=ORANGE, width=4); y += 70
        f, ls, s = fit(d, sl["title"], lambda z: serif(z, 600), MW, 280, 100, 60, 1.08)
        for l in ls:
            d.text((X, y), l, font=f, fill=TEAL, features=["lnum"]); y += s * 1.08
        y += 45
        body_block(d, X, y, sl["body"], MW, HT - 200 - y, 54)
    elif t == "cta":
        y = 430
        d.line([(X, y), (X + 120, y)], fill=ORANGE, width=4); y += 60
        f, ls, s = fit(d, sl["title"], lambda z: serif(z, 600), MW, 300, 110, 70, 1.05)
        for l in ls:
            d.text((X, y), l, font=f, fill=CREAM, features=["lnum"]); y += s * 1.05
        y += 40
        f, ls, s = fit(d, sl["body"], lambda z: sans(z, 400), MW, 240, 44, 30, 1.45)
        for l in ls:
            d.text((X, y), l, font=f, fill=CREAM); y += s * 1.45
        y += 40
        d.text((X, y), sl["sub"], font=sans(32, 500), fill=ORANGE)
    return img

def main(out):
    for p in POSTS:
        od = os.path.join(out, p["id"]); os.makedirs(od, exist_ok=True)
        n = len(p["slides"])
        for i, sl in enumerate(p["slides"], 1):
            draw_slide(sl, i, n).save(os.path.join(od, f"{p['id']}-{i:02d}.jpg"), "JPEG", quality=92)
    print("ok")

if __name__ == "__main__":
    main(sys.argv[1])
