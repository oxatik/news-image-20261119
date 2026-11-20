# Draw "The World in One Day" — Thursday 19 November 2026
# Pure Pillow, deterministic, 1024x1024, no network, no clock, no random.
from PIL import Image, ImageDraw, ImageFont
from pathlib import Path

W = H = 1024
PAPER   = (246, 241, 229)
INK     = (26, 22, 18)
MUTED   = (96, 88, 78)
FAINT   = (150, 140, 126)
RULE    = (176, 166, 148)
RED     = (164, 26, 22)
NAVY    = (18, 46, 80)
GOLD    = (186, 142, 44)
CARD    = (250, 246, 236)

ASIA     = (172, 32, 32)
MIDEAST  = (198, 96, 12)
EUROPE   = (24, 76, 148)
AMERICAS = (104, 48, 148)
OCEANIA  = (10, 112, 122)
GLOBAL   = (70, 72, 74)

FD = Path(r"C:\Windows\Fonts")

def F(name, size):
    return ImageFont.truetype(str(FD / name), size)

def tSerif(b, s):  return F("timesbd.ttf" if b else "times.ttf", s)
def tSans(b, s):   return F("arialbd.ttf" if b else "arial.ttf", s)
def tGeoI(s):      return F("georgiai.ttf", s)

im = Image.new("RGB", (W, H), PAPER)
d  = ImageDraw.Draw(im)

def text(xy, s, font, fill=INK, anchor="la"):
    d.text(xy, s, font=font, fill=fill, anchor=anchor)

def tw(s, font):
    return d.textlength(s, font=font)

def wrap(s, font, maxw):
    words, lines, cur = s.split(), [], ""
    for w in words:
        t = (cur + " " + w).strip()
        if tw(t, font) <= maxw:
            cur = t
        else:
            if cur:
                lines.append(cur)
            cur = w
    if cur:
        lines.append(cur)
    return lines

def rrect(xy, r, fill=None, outline=None, width=1):
    d.rounded_rectangle(xy, radius=r, fill=fill, outline=outline, width=width)

def hline(y, x0=8, x1=W-8, c=RULE, w=1):
    d.rectangle([x0, y, x1, y + w - 1], fill=c)

def tag(x, y, label, color, h=16):
    w = tw(label, tSans(True, 9)) + 10
    rrect([x, y, x + w, y + h], 3, fill=color)
    text((x + 5, y + 4), label, tSans(True, 9), (255, 255, 255))
    return w

# ---------------------------------------------------------------- header
d.rectangle([0, 0, W, 6], fill=RED)
text((10, 12), "THE WORLD IN ONE DAY", tSans(True, 9), RED)
tw_r = "EVERY REGION  ·  ONE IMAGE  ·  DRAWN IN CODE"
text((W - 10 - tw(tw_r, tSans(True, 9)), 12), tw_r, tSans(True, 9), MUTED)

text((10, 26), "Thursday 19 November 2026", tSerif(True, 54), INK)
kick = "First US–China–Russia summit  ·  Myanmar genocide ruling  ·  Record IPO  ·  COP31 drops fossil fuels"
text((10, 88), kick, tGeoI(14), RED)
hline(110, 8, W-8, INK, 2)
hline(113, 8, W-8, INK, 1)

# ---------------------------------------------------------------- stats
stats = [
    ("3",       "presidents, one table",   ASIA),
    ("9–6",     "World Court on Myanmar",  EUROPE),
    ("$83",     "Anthropic IPO, a record", AMERICAS),
    ("+17%",    "first-day Nasdaq jump",   AMERICAS),
    ("13 yrs",  "wait for GTA VI ends",    OCEANIA),
]
sx, sw = 8, (W - 16) / 5
for i, (num, lab, col) in enumerate(stats):
    x0 = sx + i * sw
    if i:
        d.rectangle([x0, 122, x0, 152], fill=RULE)
    text((x0 + 10, 118), num, tSans(True, 22), col)
    text((x0 + 10, 144), lab, tSans(False, 9), MUTED)

hline(160)

# ---------------------------------------------------------------- flags
def flag_us(x, y, w, h):
    d.rectangle([x, y, x+w, y+h], fill=(255,255,255))
    for i in (0, 2, 4):
        d.rectangle([x, y+i*h/5, x+w, y+(i+1)*h/5], fill=(178,34,34))
    d.rectangle([x, y, x+w*0.44, y+h*0.52], fill=(24,48,96))
    text((x+w*0.22, y+h*0.26), "★", tSans(True, 7), (255,255,255), anchor="mm")

def flag_cn(x, y, w, h):
    d.rectangle([x, y, x+w, y+h], fill=(206, 32, 32))
    text((x+4, y+1), "★", tSans(True, 13), (255, 214, 64))

def flag_ru(x, y, w, h):
    d.rectangle([x, y, x+w, y+h/3], fill=(255,255,255))
    d.rectangle([x, y+h/3, x+w, y+2*h/3], fill=(0, 82, 148))
    d.rectangle([x, y+2*h/3, x+w, y+h], fill=(206, 32, 32))

def leader(cx, base, skin, hair, suit, tie):
    d.polygon([(cx-16, base), (cx-14, base-22), (cx+14, base-22), (cx+16, base)], fill=suit)
    d.ellipse([cx-11, base-46, cx+11, base-24], fill=skin)
    d.chord([cx-11, base-48, cx+11, base-32], 180, 360, fill=hair)
    d.polygon([(cx-2, base-22), (cx+2, base-22), (cx, base-8)], fill=tie)

def card(x0, y0, x1, y1, fill=CARD):
    rrect([x0, y0, x1, y1], 6, fill=fill, outline=RULE, width=1)

# ---------------------------------------------------------------- lead — summit
lx0, ly0, lx1, ly1 = 8, 168, 622, 378
card(lx0, ly0, lx1, ly1)
d.rectangle([lx0, ly0, lx0+4, ly1], fill=ASIA)
tag(lx0+14, ly0+10, "SHENZHEN  ·  SUMMIT", ASIA)
text((lx1-12, ly0+10), "01", tSans(True, 11), FAINT, anchor="rt")

ay = ly0 + 30
d.rectangle([lx0+14, ay, lx1-14, ay+108], fill=NAVY)
fw, fh = 48, 32
flag_us(lx0+36,  ay+10, fw, fh)
flag_cn(lx0+104, ay+8,  fw, fh)
flag_ru(lx0+172, ay+10, fw, fh)
text((lx0+244, ay+12), "APEC 2026 · SHENZHEN", tSans(True, 9), (255,255,255))
chips = [("NUKES", "risk"), ("OIL", "refining"), ("UN", "reform"), ("ICC", "limits")]
for i, (a, b) in enumerate(chips):
    cx = lx0+244 + (i % 2) * 100
    cy = ay+28 + (i // 2) * 28
    rrect([cx, cy, cx+92, cy+24], 4, outline=(120,150,190), width=1)
    text((cx+7, cy+3), a, tSans(True, 8), (255,214,64))
    text((cx+7, cy+12), b, tSans(False, 8), (220,228,240))

lb = ay + 104
leader(lx0+70,  lb, (232, 190, 150), (226, 176, 96), (30, 48, 84), (180, 30, 30))
leader(lx0+150, lb, (226, 178, 128), (24, 20, 16),   (40, 44, 52), (160, 20, 20))
leader(lx0+230, lb, (228, 196, 168), (168, 148, 120), (36, 40, 48), (150, 24, 24))
d.rectangle([lx0+40, lb-2, lx0+260, lb+4], fill=(90, 64, 40))
# names live in the headline; labels under the figures fell outside the navy box

hy = ay + 128
text((lx0+14, hy), "Trump, Xi and Putin hold first three-way summit", tSans(True, 21), INK)
body = ("The three presidents signed a four-point “Declaration on Peace” in Shenzhen — "
        "nuclear risk, oil, UN reform and ICC limits. Trump called Putin “my friend.” — Reuters")
by = hy + 27
for i, ln in enumerate(wrap(body, tSans(False, 11.5), lx1-lx0-28)):
    text((lx0+14, by + i*15), ln, tSans(False, 11.5), (52, 46, 40))

# ---------------------------------------------------------------- lead — ICJ
rx0, ry0, rx1, ry1 = 630, 168, 1016, 378
card(rx0, ry0, rx1, ry1)
d.rectangle([rx0, ry0, rx0+4, ry1], fill=EUROPE)
tag(rx0+14, ry0+10, "THE HAGUE  ·  WORLD COURT", EUROPE)
text((rx1-12, ry0+10), "02", tSans(True, 11), FAINT, anchor="rt")

d.rectangle([rx0+14, ry0+32, rx1-14, ry0+140], fill=(224, 232, 240))
bx, bw = rx0+40, 90
d.rectangle([bx, ry0+88, bx+bw, ry0+138], fill=(168, 158, 142))
d.polygon([(bx-6, ry0+88), (bx+bw/2, ry0+66), (bx+bw+6, ry0+88)], fill=(140, 128, 110))
for i in range(4):
    d.rectangle([bx+10+i*18, ry0+94, bx+18+i*18, ry0+136], fill=(210, 200, 184))
text((bx+bw+16, ry0+70), "9 – 6", tSans(True, 26), EUROPE)
text((bx+bw+16, ry0+106), "judges, binding", tSans(False, 9), MUTED)
scx, scy = rx0+268, ry0+88
d.rectangle([scx-2, scy, scx+2, scy+48], fill=(90, 80, 66))
d.rectangle([scx-22, scy+48, scx+22, scy+52], fill=(90, 80, 66))
d.line([scx-26, scy+6, scx+26, scy+6], fill=(90, 80, 66), width=2)
d.ellipse([scx-34, scy+6, scx-14, scy+20], outline=(90, 80, 66), width=2)
d.ellipse([scx+14, scy+6, scx+34, scy+20], outline=(90, 80, 66), width=2)

text((rx0+14, ry0+146), "World Court: Myanmar committed genocide", tSans(True, 18), INK)
body2 = ("Judges ruled 9–6 that the 2017 Rohingya crackdown was genocide — the first state found "
         "in breach of the 1948 Convention. About 10,000 died; 730,000 fled. — ICJ / AP")
by2 = ry0 + 172
for i, ln in enumerate(wrap(body2, tSans(False, 11), rx1-rx0-28)):
    text((rx0+14, by2 + i*14), ln, tSans(False, 11), (52, 46, 40))

# ---------------------------------------------------------------- icons
def ic_chart(x, y, w, h, c):
    d.line([x+14, y+12, x+14, y+h-12], fill=c, width=2)
    d.line([x+14, y+h-12, x+w-14, y+h-12], fill=c, width=2)
    bars = [0.35, 0.5, 0.42, 0.65, 0.88]
    bw = (w - 40) / 5
    for i, v in enumerate(bars):
        bh = (h - 30) * v
        d.rectangle([x+20+i*bw, y+h-12-bh, x+20+i*bw+bw*0.6, y+h-12], fill=c)
    d.polygon([(x+w-28, y+14), (x+w-14, y+14), (x+w-21, y+26)], fill=RED)

def ic_cop(x, y, w, h, c):
    d.rectangle([x+w/2-36, y+8, x+w/2+36, y+h-10], fill=(252,250,244), outline=(160,150,130), width=1)
    text((x+w/2, y+14), "DRAFT DEAL", tSans(True, 8), c, anchor="mt")
    text((x+w/2, y+30), "FOSSIL FUELS", tSans(True, 9), (80,80,80), anchor="mt")
    d.line([x+w/2-32, y+36, x+w/2+32, y+26], fill=RED, width=3)
    text((x+w/2, y+50), "$120bn aid — dropped", tSans(False, 8), RED, anchor="mt")

def ic_gta(x, y, w, h, c):
    text((x+w/2, y+h/2-8), "VI", tSerif(True, 46), (230, 60, 40), anchor="mm")
    text((x+w/2, y+h/2+20), "OUT NOW · PS5 · XBOX", tSans(True, 8), c, anchor="mm")

def ic_bridge(x, y, w, h, c):
    d.rectangle([x+10, y+h-18, x+w-10, y+h-10], fill=(70, 110, 160))
    d.rectangle([x+10, y+h-30, x+w-10, y+h-24], fill=c)
    d.arc([x+30, y+h-52, x+w-30, y+h-16], 180, 360, fill=c, width=3)
    d.rectangle([x+28, y+14, x+34, y+h-24], fill=c)
    d.rectangle([x+w-34, y+14, x+w-28, y+h-24], fill=c)
    d.polygon([(x+w/2-8, y+10), (x+w/2+2, y+10), (x+w/2-4, y+24),
               (x+w/2+6, y+24), (x+w/2-8, y+44), (x+w/2-2, y+28), (x+w/2-12, y+28)], fill=GOLD)

def ic_missile(x, y, w, h, c):
    d.rectangle([x+8, y+8, x+w-8, y+h-8], fill=(20, 40, 70))
    d.rectangle([x+w/2-10, y+h-28, x+w/2+10, y+h-12], fill=(180, 160, 130))
    d.polygon([(x+22, y+18), (x+68, y+32), (x+22, y+38)], fill=(220, 70, 50))
    d.ellipse([x+62, y+26, x+78, y+42], outline=(240, 200, 80), width=2)
    text((x+16, y+h-16), "RIYADH", tSans(True, 8), (255,255,255))

def ic_gaza(x, y, w, h, c):
    d.rectangle([x+10, y+h-22, x+w-10, y+h-12], fill=(190, 170, 130))
    d.rounded_rectangle([x+22, y+h-34, x+78, y+h-18], 4, fill=c)
    d.rectangle([x+40, y+h-46, x+58, y+h-32], fill=c)
    d.rectangle([x+56, y+h-42, x+86, y+h-36], fill=c)
    for i in range(4):
        d.ellipse([x+26+i*14, y+h-20, x+36+i*14, y+h-12], fill=(50, 50, 50))
    for i in range(5):
        d.rectangle([x+w-30, y+12+i*10, x+w-14, y+16+i*10], fill=c)

def ic_cyclone(x, y, w, h, c):
    cx, cy = x+w/2, y+h/2
    for i, r in enumerate((9, 16, 23)):
        d.arc([cx-r, cy-r, cx+r, cy+r], 20+i*40, 300+i*40, fill=c, width=3)
    d.ellipse([cx-4, cy-4, cx+4, cy+4], fill=c)
    text((x+12, y+8), "AKVAN", tSans(True, 8), c)

def ic_flags2(x, y, w, h, c):
    d.rectangle([x+16, y+12, x+50, y+24], fill=(255,255,255))
    d.rectangle([x+16, y+12, x+50, y+18], fill=(178,34,34))
    d.rectangle([x+16, y+24, x+50, y+36], fill=(24,48,96))
    d.line([x+18, y+36, x+18, y+62], fill=(90,70,50), width=2)
    d.rectangle([x+w-50, y+12, x+w-16, y+22], fill=(255,204,0))
    d.rectangle([x+w-50, y+22, x+w-16, y+32], fill=(0,56,168))
    d.rectangle([x+w-50, y+32, x+w-16, y+42], fill=(206,32,32))
    d.line([x+w-18, y+42, x+w-18, y+62], fill=(90,70,50), width=2)
    text((x+w/2, y+70), "MILITARY TIES", tSans(True, 8), c, anchor="mt")

def ic_jobs(x, y, w, h, c):
    text((x+w/2, y+h/2-8), "4.9%", tSans(True, 28), c, anchor="mm")
    text((x+w/2, y+h/2+18), "five-year high", tSans(False, 9), MUTED, anchor="mm")
    for i in range(3):
        d.ellipse([x+16+i*14, y+h-18, x+24+i*14, y+h-10], fill=c)

# ---------------------------------------------------------------- grid
def story(x0, y0, x1, y1, num, region, color, headline, body, src, icon):
    card(x0, y0, x1, y1)
    d.rectangle([x0, y0, x0+3, y1], fill=color)
    tag(x0+12, y0+8, region, color)
    text((x1-10, y0+8), num, tSans(True, 11), FAINT, anchor="rt")
    iz = (x0+12, y0+28, x1-12, y0+92)
    d.rectangle([iz[0], iz[1], iz[2], iz[3]], fill=(238, 232, 218))
    icon(iz[0], iz[1], iz[2]-iz[0], iz[3]-iz[1], color)
    text((x0+12, y0+98), headline, tSans(True, 14), INK)
    yy = y0 + 118
    for i, ln in enumerate(wrap(body, tSans(False, 10.5), x1-x0-24)):
        if yy + 13 > y1 - 18:
            break
        text((x0+12, yy), ln, tSans(False, 10.5), (56, 50, 44))
        yy += 13
    text((x0+12, y1-15), src, tSans(False, 9), FAINT)

cw = (W - 16 - 16) / 3
xs = [8, 8 + cw + 8, 8 + 2*(cw + 8)]

gy0, gy1 = 386, 562
story(xs[0], gy0, xs[0]+cw, gy1, "03", "NEW YORK  ·  MARKETS", AMERICAS,
      "Anthropic’s record IPO hits Nasdaq",
      "Priced at $83 a share — above the $70–78 range — the Claude maker’s listing is the largest on record. Shares jumped about 17% on debut.",
      "WSJ · AP", ic_chart)

story(xs[1], gy0, xs[1]+cw, gy1, "04", "ANTALYA  ·  CLIMATE", GLOBAL,
      "COP31 draft drops fossil fuels",
      "A slimmed-down draft deleted any mention of ending fossil-fuel use and dropped a proposed $120bn adaptation target. Talks close Friday.",
      "Reuters · RTE", ic_cop)

story(xs[2], gy0, xs[2]+cw, gy1, "05", "WORLDWIDE  ·  GAMES", OCEANIA,
      "GTA VI is out, 13 years on",
      "Grand Theft Auto VI launched at midnight local time on PS5 and Xbox Series X|S — 13 years after GTA V. Reviews call it a generation leap.",
      "Rockstar · PlayStation Blog", ic_gta)

gy0b, gy1b = 570, 746
story(xs[0], gy0b, xs[0]+cw, gy1b, "06", "CRIMEA  ·  WAR", EUROPE,
      "Crimean Bridge hit a third time",
      "Ukraine struck the bridge with Neptune missiles — the third attack in a week. Railway traffic was halted. Kyiv says the rail span was hit.",
      "ABC · Kyiv Independent", ic_bridge)

story(xs[1], gy0b, xs[1]+cw, gy1b, "07", "SAUDI ARABIA  ·  GULF", MIDEAST,
      "Houthi fire damages Riyadh tower",
      "A Houthi attack hit a tower in Riyadh’s financial district, causing damage but no injuries, Saudi officials said. Missiles were intercepted.",
      "Al Jazeera", ic_missile)

story(xs[2], gy0b, xs[2]+cw, gy1b, "08", "GAZA  ·  CEASEFIRE", MIDEAST,
      "Israeli tanks push past Yellow Line",
      "Tanks and bulldozers moved west of the ceasefire “Yellow Line”. About two-thirds of Gaza is now occupied; 1,600+ have been killed since the truce.",
      "Democracy Now! · AP", ic_gaza)

gy0c, gy1c = 754, 878
h3 = gy1c - gy0c

def story_s(x0, y0, x1, y1, num, region, color, headline, body, src, icon):
    card(x0, y0, x1, y1)
    d.rectangle([x0, y0, x0+3, y1], fill=color)
    tag(x0+12, y0+7, region, color, h=15)
    text((x1-10, y0+7), num, tSans(True, 11), FAINT, anchor="rt")
    icon(x1-84, y0+10, 72, h3-18, color)
    text((x0+12, y0+28), headline, tSans(True, 13.5), INK)
    yy = y0 + 48
    for i, ln in enumerate(wrap(body, tSans(False, 10.5), x1-x0-100)):
        if yy + 13 > y1 - 18:
            break
        text((x0+12, yy), ln, tSans(False, 10.5), (56, 50, 44))
        yy += 13
    text((x0+12, y1-14), src, tSans(False, 9), FAINT)

story_s(xs[0], gy0c, xs[0]+cw, gy1c, "09", "ODISHA  ·  STORM", ASIA,
        "Cyclone Akvan nears India",
        "Odisha evacuated 47,000+ people ahead of Cyclone Akvan, the third cyclone in 24 days, expected to cross near Gopalpur on Friday.",
        "Reuters", ic_cyclone)

story_s(xs[1], gy0c, xs[1]+cw, gy1c, "10", "VENEZUELA  ·  AMERICAS", AMERICAS,
        "US, Venezuela restore army ties",
        "Hegseth visited Caracas and signed a military-cooperation deal months after US forces abducted President Maduro in January.",
        "Democracy Now!", ic_flags2)

story_s(xs[2], gy0c, xs[2]+cw, gy1c, "11", "AUSTRALIA  ·  ECONOMY", OCEANIA,
        "Jobless rate hits 4.9 per cent",
        "Unemployment jumped to a five-year high of 4.9% in October as 17,800 more people joined the jobless queue. The AUD fell.",
        "ABS · ABC News", ic_jobs)

# ---------------------------------------------------------------- ticker
hline(886)
text((8, 892), "ALSO ON THURSDAY 19 NOVEMBER 2026", tSans(True, 10), RED)

tick = [
    ("US",  "Democrats nominate Jeffries for Speaker, 251–11 — first Black nominee.", "AP"),
    ("US",  "Tusk, on Trump and Putin: “God, protect us from such friends.”", "DN"),
    ("YEM", "UN relief chief: aid must be allowed into Yemen.", "UN News"),
    ("USA", "DHS grilled over the FAA ground-stop that cancelled 18,000 flights.", "C-SPAN"),
    ("IRN", "Study: AI models used in the Iran war flagged civilian sites as targets.", "Vals AI"),
    ("VEN", "Hegseth: the oil deal makes the Strait of Hormuz “a nonfactor.”", "DN"),
]
colw = (W - 16) / 2
for i, (pl, tx, src) in enumerate(tick):
    col, row = divmod(i, 3)
    x = 8 + col * colw
    y = 916 + row * 18
    text((x, y), pl, tSans(True, 9), RED)
    text((x + 34, y), tx, tSans(False, 10), INK)
    text((x + colw - 4, y), src, tSans(False, 9), FAINT, anchor="rt")

hline(972)

# ---------------------------------------------------------------- date check
d.rectangle([8, 974, W-8, 1006], fill=(22, 60, 40))
text((18, 980), "DATE CHECK", tSans(True, 12), (140, 230, 160))
text((110, 980), "Every story on this page happened, or was first reported, on Thursday 19 November 2026.",
     tSans(False, 10), (230, 244, 232))

text((8, 1012), "Not this day: Crimea Bridge 2022/23 · Houthi salvos of Oct/11 Nov · GTA V (2013) · Paris COP21 (2015)",
     tSans(False, 8), MUTED)
text((W-8, 1012), "Drawn in code · Reuters, AP, AFP, WSJ, Al Jazeera, ABC, Kyiv Independent, ICJ, ABS, Rockstar, DN",
     tSans(False, 8), MUTED, anchor="rt")

d.rectangle([0, H-2, W, H], fill=RED)

out = Path(__file__).resolve().parent / "entry" / "entry.png"
im.save(out, optimize=True)
print("wrote", out, out.stat().st_size, "bytes")
