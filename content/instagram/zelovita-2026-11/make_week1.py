import os, sys, subprocess, glob
from PIL import Image, ImageDraw
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from render import serif, sans, fit, spaced, CREAM, SAND, TEAL, INK, MUTED, ORANGE
from week1 import WEEK1
from content import H

SW, SH = 1080, 1920
OUT = sys.argv[1]

def story(s, path):
    img = Image.new("RGB", (SW, SH), CREAM); d = ImageDraw.Draw(img)
    d.ellipse([SW - 420, -300, SW + 300, 420], fill=SAND)
    d.ellipse([-260, SH - 380, 360, SH + 240], fill=SAND)
    spaced(d, (100, 250), "ZELOVITA", sans(32, 500), TEAL, 7)
    y = 700
    spaced(d, (100, y), s["kicker"], sans(34, 500), ORANGE, 6); y += 90
    f, ls, sz = fit(d, s["title"], lambda z: serif(z, 600), SW - 200, 520, 120, 70, 1.05)
    for l in ls:
        d.text((100, y), l, font=f, fill=TEAL, features=["lnum"]); y += sz * 1.05
    y += 50; d.line([(100, y), (240, y)], fill=ORANGE, width=5); y += 70
    f, ls, sz = fit(d, s["body"], lambda z: sans(z, 400), SW - 200, 360, 50, 34, 1.45)
    for l in ls:
        d.text((100, y), l, font=f, fill=INK); y += sz * 1.45
    d.text((100, SH - 300), H, font=sans(36, 400), fill=MUTED)
    img.save(path, "JPEG", quality=92)

def reel(carousel, path, tmp):
    os.makedirs(tmp, exist_ok=True)
    frames = sorted(glob.glob(os.path.join(os.path.dirname(OUT), "out", carousel, "*.jpg")))
    for i, f in enumerate(frames):
        bg = Image.new("RGB", (SW, SH), CREAM)
        bg.paste(Image.open(f), (0, (SH - 1350) // 2))
        bg.save(os.path.join(tmp, f"f{i:02d}.jpg"), quality=95)
    n = len(frames); dur = 3.0; fade = 0.5
    inputs = []
    for i in range(n):
        inputs += ["-loop", "1", "-t", str(dur + (fade if i < n - 1 else 0)), "-i", os.path.join(tmp, f"f{i:02d}.jpg")]
    fc, last, off = "", "[0:v]", 0.0
    for i in range(1, n):
        off += dur
        fc += f"{last}[{i}:v]xfade=transition=fade:duration={fade}:offset={off - fade * 0 :.2f}[v{i}];"
        last = f"[v{i}]"
    fc += f"{last}format=yuv420p,fps=30[out]"
    # silent stereo track (some players expect audio)
    cmd = ["ffmpeg", "-y", "-loglevel", "error"] + inputs + ["-f", "lavfi", "-i", "anullsrc=r=44100:cl=stereo",
           "-filter_complex", fc, "-map", "[out]", "-map", f"{n}:a", "-shortest",
           "-c:v", "libx264", "-preset", "veryfast", "-crf", "20", "-c:a", "aac", "-b:a", "128k",
           "-movflags", "+faststart", path]
    subprocess.run(cmd, check=True)

os.makedirs(OUT, exist_ok=True)
for day in WEEK1:
    k = day["date"]
    story(day["story"], os.path.join(OUT, f"story-{k}.jpg"))
    reel(day["carousel"], os.path.join(OUT, f"reel-{k}.mp4"), f"/tmp/reel-{k}")
print("ok")
