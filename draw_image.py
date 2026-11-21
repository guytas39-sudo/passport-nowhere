#!/usr/bin/env python3
"""Draw the entry image: an invented passport spread, 1024 x 1024.

A two-page open passport for the Republic of Taravo (a country that does not
exist), drawn with Pillow: data page on the left, visas and stamps on the
right. Every word is real, spelled text; the portrait is a drawn silhouette,
not a photo of any person. All dates are internally consistent: the passport
was issued 14 MAR 2023 and expires 13 MAR 2033; every stamp falls between.
Run:  python3 draw_image.py
Writes entry.png (1024 x 1024) next to this file, deterministically.
"""
from PIL import Image, ImageDraw, ImageFont

W = H = 1024
NAVY = (18, 38, 60)
PAPER = (246, 241, 226)
INK = (24, 38, 56)
GREY = (96, 104, 116)
TEAL = (40, 90, 96)
STAMP_RED = (158, 58, 48)
STAMP_TEAL = (44, 96, 100)
GOLD = (150, 116, 52)
PORTRAIT_BG = (203, 212, 220)
SILHOUETTE = (52, 72, 96)
MRZ_BG = (232, 236, 240)

FONT_DIR = "/usr/share/fonts/truetype/dejavu"


def F(name, size):
    return ImageFont.truetype(f"{FONT_DIR}/{name}", size)


F_TITLE = F("DejaVuSerif-Bold.ttf", 26)
F_SUB = F("DejaVuSans.ttf", 13)
F_LABEL = F("DejaVuSans-Bold.ttf", 12)
F_VALUE = F("DejaVuSans-Bold.ttf", 19)
F_VALUE_SM = F("DejaVuSans-Bold.ttf", 16)
F_MRZ = F("DejaVuSansMono.ttf", 15)
F_STAMP_H = F("DejaVuSans-Bold.ttf", 15)
F_STAMP = F("DejaVuSans.ttf", 13)
F_STAMP_D = F("DejaVuSans-Bold.ttf", 13)
F_CIRC = F("DejaVuSans-Bold.ttf", 16)
F_CIRC_SM = F("DejaVuSans.ttf", 10)
F_COND_H = F("DejaVuSans-Bold.ttf", 13)
F_COND = F("DejaVuSans.ttf", 14)
F_FEE = F("DejaVuSans-Bold.ttf", 15)
F_NOTE = F("DejaVuSans.ttf", 11)


def wrapped(draw, text, fnt, width):
    out, cur = [], ""
    for word in text.split():
        trial = (cur + " " + word).strip()
        if draw.textlength(trial, font=fnt) <= width:
            cur = trial
        else:
            if cur:
                out.append(cur)
            cur = word
    if cur:
        out.append(cur)
    return out


def centered(draw, x0, x1, y, text, fnt, fill):
    w = draw.textlength(text, font=fnt)
    draw.text(((x0 + x1 - w) / 2, y), text, font=fnt, fill=fill)


img = Image.new("RGB", (W, H), NAVY)
d = ImageDraw.Draw(img)

# ---- the two pages ----
LX0, LX1, RX0, RX1, PY0, PY1 = 28, 500, 524, 996, 28, 996
d.rectangle([LX0, PY0, LX1, PY1], fill=PAPER)
d.rectangle([RX0, PY0, RX1, PY1], fill=PAPER)
d.rectangle([LX0, PY0, LX1, PY1], outline=NAVY, width=2)
d.rectangle([RX0, PY0, RX1, PY1], outline=NAVY, width=2)

# ================= LEFT PAGE: data page =================
# header
centered(d, LX0, LX1, 48, "REPUBLIC OF TARAVO", F_TITLE, INK)
centered(d, LX0, LX1, 84, "PASSPORT  ·  PASSEPORT", F_SUB, GREY)
d.line([(LX0 + 24, 112), (LX1 - 24, 112)], fill=NAVY, width=2)
centered(d, LX0, LX1, 122, "TYPE  P      CODE  TAR      No.  T12345678", F_SUB, INK)

# portrait box (drawn silhouette: head, shoulders, wide-brim hat).
# The silhouette is drawn on its own layer clipped to the box, so nothing
# can spill over the box edge or the fields below it.
PX0, PY0p, PX1, PY1p = 52, 156, 212, 356
d.rectangle([PX0, PY0p, PX1, PY1p], fill=PORTRAIT_BG)
d.rectangle([PX0, PY0p, PX1, PY1p], outline=NAVY, width=2)
pw, ph = PX1 - PX0, PY1p - PY0p
portrait = Image.new("RGBA", (pw, ph), (0, 0, 0, 0))
p = ImageDraw.Draw(portrait)
# shoulders
p.ellipse([8, 140, pw - 8, 236], fill=SILHOUETTE + (255,))
# neck + head
p.rectangle([66, 96, pw - 66, 136], fill=SILHOUETTE + (255,))
p.ellipse([38, 40, pw - 38, 116], fill=SILHOUETTE + (255,))
# wide-brim hat: brim then dome
p.ellipse([16, 32, pw - 16, 54], fill=SILHOUETTE + (255,))
p.pieslice([44, 2, pw - 44, 60], start=180, end=360,
           fill=SILHOUETTE + (255,))
img.paste(portrait, (PX0, PY0p), portrait)


def field(x, y, label, value, fnt=F_VALUE, width=236):
    d.text((x, y), label, font=F_LABEL, fill=GREY)
    d.text((x, y + 16), value, font=fnt, fill=INK)


# fields to the right of the portrait
field(232, 156, "SURNAME", "MEREK")
field(232, 204, "GIVEN NAMES", "ANA LYS")
field(232, 252, "NATIONALITY", "TARAVESE")
field(232, 300, "SEX", "F")

# fields below the portrait, two columns
field(52, 384, "DATE OF BIRTH", "02 JUN 1994")
field(280, 384, "PLACE OF BIRTH", "PORT LYSA")
field(52, 432, "DATE OF ISSUE", "14 MAR 2023")
field(280, 432, "DATE OF EXPIRY", "13 MAR 2033")
field(52, 480, "AUTHORITY", "HARBOUR OFFICE, PORT LYSA",
      fnt=F_VALUE_SM, width=424)
field(52, 528, "LANGUAGES", "TARAVESE  ·  ENGLISH")

d.line([(LX0 + 24, 588), (LX1 - 24, 588)], fill=GOLD, width=2)
centered(d, LX0, LX1, 600, "THIS PASSPORT REMAINS THE PROPERTY", F_SUB, GREY)
centered(d, LX0, LX1, 620, "OF THE REPUBLIC OF TARAVO", F_SUB, GREY)

# small coat of arms: ring with a star-ish mark (four-point star from polygons)
cx, cy, r = 236, 700, 52
d.ellipse([cx - r, cy - r, cx + r, cy + r], outline=NAVY, width=3)
d.ellipse([cx - r + 8, cy - r + 8, cx + r - 8, cy + r - 8],
          outline=GOLD, width=2)
d.polygon([(cx, cy - 28), (cx + 7, cy - 7), (cx + 28, cy),
           (cx + 7, cy + 7), (cx, cy + 28), (cx - 7, cy + 7),
           (cx - 28, cy), (cx - 7, cy - 7)], fill=NAVY)
d.text((cx - 6, cy + 30), "TAR", font=F_LABEL, fill=NAVY)

# machine-readable zone
d.rectangle([LX0 + 24, 800, LX1 - 24, 880], fill=MRZ_BG)
mrz1 = "P<TARMEREK<<ANA<LYS" + "<" * (44 - len("P<TARMEREK<<ANA<LYS"))
mrz2 = "T12345678TAR940602F3303131" + "<" * (44 - len("T12345678TAR940602F3303131"))
d.text((LX0 + 30, 812), mrz1, font=F_MRZ, fill=INK)
d.text((LX0 + 30, 842), mrz2, font=F_MRZ, fill=INK)
d.text((LX0 + 24, 892), "P<TAR  ·  MRZ  ·  ICAO 9303", font=F_NOTE, fill=GREY)

# ================= RIGHT PAGE: visas and stamps =================
centered(d, RX0, RX1, 48, "VISAS", F_TITLE, INK)
centered(d, RX0, RX1, 84, "VISAS  ·  ENDORSEMENTS", F_SUB, GREY)
d.line([(RX0 + 24, 112), (RX1 - 24, 112)], fill=NAVY, width=2)


def make_stamp(kind, place, country, day, month, year, color, angle):
    """One entry stamp on its own layer, rotated, as a rounded rectangle
    with a circular date mark."""
    lw, lh = 200, 132
    layer = Image.new("RGBA", (lw + 40, lh + 40), (0, 0, 0, 0))
    s = ImageDraw.Draw(layer)
    x0, y0, x1, y1 = 20, 20, 20 + lw, 20 + lh
    s.rounded_rectangle([x0, y0, x1, y1], radius=8,
                        outline=color + (255,), width=3)
    s.rounded_rectangle([x0 + 5, y0 + 5, x1 - 5, y1 - 5], radius=6,
                        outline=color + (255,), width=1)
    s.text((x0 + 14, y0 + 12), kind, font=F_STAMP_H, fill=color + (255,))
    s.text((x0 + 14, y0 + 36), place, font=F_STAMP, fill=color + (255,))
    s.text((x0 + 14, y0 + 56), country, font=F_STAMP, fill=color + (255,))
    s.text((x0 + 14, y0 + 78), f"{day} {month} {year}",
           font=F_STAMP_D, fill=color + (255,))
    # circular date mark on the right: the three lines are stacked so the
    # year ends inside the inner ring (radius 26), never touching it.
    ccx, ccy, cr = x1 - 34, y0 + 66, 30
    s.ellipse([ccx - cr, ccy - cr, ccx + cr, ccy + cr],
              outline=color + (255,), width=2)
    s.ellipse([ccx - cr + 4, ccy - cr + 4, ccx + cr - 4, ccy + cr - 4],
              outline=color + (255,), width=1)
    s.text((ccx - 9, ccy - 17), day, font=F_CIRC, fill=color + (255,))
    s.text((ccx - 14, ccy + 3), month, font=F_CIRC_SM, fill=color + (255,))
    s.text((ccx - 12, ccy + 14), year[-2:], font=F_CIRC_SM,
           fill=color + (255,))
    return layer.rotate(angle, resample=Image.BICUBIC, expand=False)


stamps = [
    ("ARRIVAL", "PORT VENN", "VENNAR", "09", "JUL", "2023", STAMP_RED, -7),
    ("DEPARTURE", "PORT VENN", "VENNAR", "24", "JUL", "2023", STAMP_TEAL, 5),
    ("ARRIVAL", "SORREL ISLE", "SORREL", "03", "MAY", "2024", STAMP_RED, 4),
    ("DEPARTURE", "SORREL ISLE", "SORREL", "18", "MAY", "2024", STAMP_TEAL, -5),
]
positions = [(548, 140), (764, 140), (548, 318), (764, 318)]
for spec, (px, py) in zip(stamps, positions):
    img.paste(make_stamp(*spec), (px, py), make_stamp(*spec))

# visa condition box
d.rectangle([RX0 + 24, 520, RX1 - 24, 660], outline=NAVY, width=2)
d.text((RX0 + 40, 534), "CONDITION OF ENTRY", font=F_COND_H, fill=NAVY)
cond = ("The holder may land only at low tide. The harbour master "
        "of the port of entry is to be told before dusk.")
y = 560
for line in wrapped(d, cond, F_COND, RX1 - RX0 - 80):
    d.text((RX0 + 40, y), line, font=F_COND, fill=INK)
    y += 22
d.text((RX0 + 40, y + 8), "VALID WITH THIS PASSPORT ONLY.",
       font=F_COND_H, fill=NAVY)

# fee stamp, rotated. The layer is padded well beyond the rectangle, so
# the -6 degree rotation cannot clip the border at the corners; the paste
# position keeps the stamp centred where it was.
fee = Image.new("RGBA", (340, 120), (0, 0, 0, 0))
f = ImageDraw.Draw(fee)
f.rounded_rectangle([20, 15, 320, 105], radius=8,
                    outline=STAMP_RED + (255,), width=3)
f.text((38, 28), "LANDING FEE — 2 SHELLS", font=F_FEE,
       fill=STAMP_RED + (255,))
f.text((38, 54), "PAID  ·  PORT LYSA", font=F_FEE,
       fill=STAMP_RED + (255,))
fee = fee.rotate(-6, resample=Image.BICUBIC, expand=False)
img.paste(fee, (580, 685), fee)

# bottom note
centered(d, RX0, RX1, 830, "HOLDER'S SIGNATURE", F_LABEL, GREY)
d.line([(RX0 + 60, 872), (RX1 - 60, 872)], fill=INK, width=2)
d.text((RX0 + 60, 884), "Ana Lys Merek", font=F_VALUE_SM, fill=INK)
centered(d, RX0, RX1, 940, "KEPT DRY AT ALL TIMES", F_NOTE, GREY)

img.save("entry.png", format="PNG", optimize=True)
print("wrote entry.png", img.size)
