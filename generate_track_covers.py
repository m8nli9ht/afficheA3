from pathlib import Path
import math
import random

from PIL import Image, ImageDraw, ImageFont


SIZE = 1200
ASSETS = Path(__file__).parent / "assets"
FONT_SANS = r"C:\Windows\Fonts\arial.ttf"
FONT_BOLD = r"C:\Windows\Fonts\arialbd.ttf"
FONT_SERIF = r"C:\Windows\Fonts\georgiab.ttf"


def font(path, size):
    try:
        return ImageFont.truetype(path, size)
    except OSError:
        return ImageFont.truetype(FONT_BOLD, size)


def cover(background, number, subtitle, ink):
    image = Image.new("RGB", (SIZE, SIZE), background)
    draw = ImageDraw.Draw(image)
    draw.rectangle((38, 38, SIZE - 38, SIZE - 38), outline=ink, width=3)
    draw.text((72, 68), "LIVING ROOT BRIDGES", font=font(FONT_BOLD, 25), fill=ink)
    draw.text((SIZE - 72, 68), number, font=font(FONT_BOLD, 25), fill=ink, anchor="ra")
    draw.line((72, 112, SIZE - 72, 112), fill=ink, width=2)
    draw.text((72, SIZE - 116), subtitle.upper(), font=font(FONT_BOLD, 25), fill=ink)
    draw.text((72, SIZE - 76), "NEO NHAC VANG", font=font(FONT_SANS, 17), fill=ink)
    return image, draw


def save(image, name):
    image.save(ASSETS / name, format="PNG", optimize=True)


def make_pilgrim():
    image, draw = cover("#20353b", "01 / 05", "The ascent", "#f3e8cc")
    draw.ellipse((720, 185, 1000, 465), fill="#d68c54")
    draw.polygon([(70, 760), (285, 475), (440, 680), (610, 390), (865, 720),
                  (1030, 490), (1130, 700), (1130, 1050), (70, 1050)], fill="#3d6260")
    draw.polygon([(70, 865), (295, 625), (470, 810), (685, 550), (915, 845),
                  (1080, 650), (1130, 745), (1130, 1050), (70, 1050)], fill="#769079")
    for y in (730, 790, 850, 910, 970):
        draw.arc((155, y - 120, 725, y + 160), 205, 345, fill="#e3bd80", width=5)
    route = [(185, 915), (320, 870), (420, 810), (510, 770), (585, 680),
             (665, 650), (730, 565), (815, 525), (860, 435)]
    draw.line(route, fill="#f3e8cc", width=15, joint="curve")
    draw.line([(x, y + 15) for x, y in route], fill="#c7724e", width=4, joint="curve")
    draw.ellipse((835, 405, 863, 433), fill="#20353b")
    draw.line((849, 430, 849, 483), fill="#20353b", width=12)
    draw.line((849, 448, 824, 469), fill="#20353b", width=9)
    draw.line((849, 448, 870, 468), fill="#20353b", width=9)
    save(image, "track-01.png")


def make_unworn_dress():
    image, draw = cover("#eee2d0", "02 / 05", "The unworn dress", "#3a2932")
    draw.rectangle((72, 150, 1128, 1035), fill="#d3b59f")
    draw.ellipse((210, 195, 990, 975), fill="#e4cbbb")
    draw.line([(555, 275), (600, 225), (645, 275), (865, 375)], fill="#3a2932", width=12, joint="curve")
    draw.line([(555, 275), (335, 375), (865, 375)], fill="#3a2932", width=12, joint="curve")
    draw.arc((580, 190, 620, 250), 180, 360, fill="#3a2932", width=10)
    draw.polygon([(440, 378), (530, 400), (600, 365), (670, 400), (758, 378),
                  (720, 510), (815, 920), (600, 970), (385, 920), (480, 510)], fill="#874556")
    draw.polygon([(530, 400), (600, 365), (670, 400), (635, 520), (600, 610), (565, 520)], fill="#d98c74")
    draw.line((600, 408, 600, 923), fill="#f0d9c1", width=7)
    draw.line((480, 540, 390, 915), fill="#d7a17e", width=7)
    draw.line((720, 540, 810, 915), fill="#d7a17e", width=7)
    for box in ((160, 280, 1040, 920), (210, 330, 990, 870), (260, 380, 940, 820)):
        draw.arc(box, 15, 330, fill="#3a2932", width=3)
    draw.ellipse((830, 840, 870, 880), fill="#d68c54")
    save(image, "track-02.png")


def make_frangipani_home():
    image, draw = cover("#1e4f4b", "03 / 05", "The flower at home", "#f4e7c8")
    draw.polygon([(180, 700), (600, 390), (1020, 700), (1020, 1000), (180, 1000)], fill="#d58a61")
    draw.polygon([(125, 710), (600, 320), (1075, 710), (1015, 760),
                  (600, 430), (185, 760)], fill="#f0d49d")
    draw.rectangle((450, 700, 750, 1000), fill="#315b53")
    draw.arc((450, 625, 750, 790), 180, 360, fill="#f3e8cc", width=16)
    flower = Image.new("RGBA", (420, 420), (0, 0, 0, 0))
    for angle in range(0, 360, 72):
        petal = Image.new("RGBA", (180, 270), (0, 0, 0, 0))
        ImageDraw.Draw(petal).ellipse((30, 12, 150, 250), fill="#fff0d1", outline="#d8b98d", width=4)
        flower.alpha_composite(petal.rotate(angle, resample=Image.Resampling.BICUBIC), (120, 75))
    ImageDraw.Draw(flower).ellipse((174, 174, 246, 246), fill="#d66d50")
    image.paste(flower, (590, 145), flower)
    draw = ImageDraw.Draw(image)
    for inset in (0, 38, 76):
        draw.arc((475 + inset, 70 + inset, 900 - inset, 495 - inset), 190, 345, fill="#edc887", width=4)
    save(image, "track-03.png")


def make_sim_hills():
    image, draw = cover("#392d4d", "04 / 05", "The sim hills", "#f6e6c5")
    draw.ellipse((770, 205, 960, 395), fill="#e9b866")
    draw.polygon([(70, 700), (270, 480), (470, 690), (700, 390), (960, 700),
                  (1130, 510), (1130, 1040), (70, 1040)], fill="#67516f")
    draw.polygon([(70, 820), (300, 620), (500, 790), (740, 560), (960, 810),
                  (1120, 650), (1130, 1040), (70, 1040)], fill="#9a6271")
    draw.polygon([(70, 930), (350, 760), (590, 910), (850, 690), (1130, 900),
                  (1130, 1040), (70, 1040)], fill="#d48366")
    for inset in (0, 38, 76):
        draw.arc((120 + inset, 555 + inset, 790 + inset, 1050 + inset), 200, 340, fill="#f0d39e", width=4)
    random.seed(404)
    for _ in range(75):
        x, y, radius = random.randint(110, 1090), random.randint(820, 1030), random.randint(5, 10)
        draw.ellipse((x - radius, y - radius, x + radius, y + radius),
                     fill=random.choice(("#f4e1be", "#f0bd77", "#e8a28b")))
    save(image, "track-04.png")


def make_call_response():
    image, draw = cover("#e9b650", "05 / 05", "The call and answer", "#272c36")
    draw.rectangle((72, 150, 585, 1035), fill="#c85f4a")
    draw.rectangle((615, 150, 1128, 1035), fill="#e9b650")
    draw.ellipse((205, 365, 425, 585), fill="#f0d6b4")
    draw.polygon([(155, 935), (165, 720), (230, 605), (400, 605), (485, 760), (500, 935)], fill="#27363b")
    draw.polygon([(390, 435), (455, 465), (430, 505), (395, 500)], fill="#27363b")
    draw.ellipse((780, 365, 1000, 585), fill="#27363b")
    draw.polygon([(690, 770), (775, 605), (950, 605), (1035, 730), (1045, 935), (680, 935)], fill="#f0d6b4")
    draw.polygon([(770, 460), (735, 485), (760, 520), (795, 505)], fill="#f0d6b4")
    for y, width in ((550, 5), (620, 8), (690, 5), (760, 8)):
        draw.arc((350, y - 45, 850, y + 45), 200, 340, fill="#f4e6c7", width=width)
    draw.text((470, 250), "?", font=font(FONT_SERIF, 150), fill="#f4e6c7", anchor="mm")
    draw.text((735, 250), "!", font=font(FONT_SERIF, 150), fill="#27363b", anchor="mm")
    random.seed(505)
    for x in range(250, 960, 48):
        draw.line((x, 990, x, 990 - random.randint(12, 42)), fill="#272c36", width=5)
    save(image, "track-05.png")


if __name__ == "__main__":
    ASSETS.mkdir(exist_ok=True)
    make_pilgrim()
    make_unworn_dress()
    make_frangipani_home()
    make_sim_hills()
    make_call_response()