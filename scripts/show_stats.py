import datetime
import os
import shutil

from PIL import Image, ImageDraw, ImageFont, ImageOps

from scripts import openfile


def gen_profile_photos(path):
    extention = os.path.splitext(path)[1]
    shutil.copy(path, openfile(f"data/photo{extention}"))
    small = Image.open(openfile(f"data/photo{extention}"))
    small = small.resize((35, 35), Image.ANTIALIAS)
    small.save(openfile(openfile(f"data/small{extention}")), quality=200)

    large = Image.open(openfile(f"data/photo{extention}"))
    large = large.resize((89, 89), Image.ANTIALIAS)
    large.save(openfile(openfile(f"data/large{extention}")), quality=200)


def gen_profile_data(user):
    img = Image.new('RGBA', (480, 640), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)
    font_level = ImageFont.truetype(openfile("assets/fonts/koliko-Regular.ttf"), 18)
    font_score = ImageFont.truetype(openfile("assets/fonts/koliko-Regular.ttf"), 26)
    font_name = ImageFont.truetype(openfile("assets/fonts/koliko-Regular.ttf"), 35)

    bg = Image.open(openfile('assets/menu/stats.png'))
    img.paste(bg, (0, 0), mask=bg)

    level = Image.open(openfile('assets/menu/banner.png'))

    if user[0]["profile_pic"] is True:
        main = Image.open(openfile('assets/menu/main_menu_bk.png'))
        mask = Image.new('L', (35, 35), 0)
        small = Image.open(openfile(f"data/small{user[0]['extention']}"))
        draw_m = ImageDraw.Draw(mask)
        draw_m.ellipse((0, 0) + (35, 35), fill=255)
        small = ImageOps.fit(small, mask.size, centering=(0.5, 0.5))
        small.putalpha(mask)
        main.paste(small, (14, 17), mask=small)
        main.save(openfile('assets/menu/main_menu.png'))
        mask = Image.new('L', (89, 89), 0)
        large = Image.open(openfile(f"data/large{user[0]['extention']}"))
        draw_m = ImageDraw.Draw(mask)
        draw_m.ellipse((0, 0) + (89, 89), fill=255)
        large = ImageOps.fit(large, mask.size, centering=(0.5, 0.5))
        large.putalpha(mask)
        img.paste(large, (195, 128), mask=large)

    img.paste(level, (218, 210), mask=level)

    draw.text(((258 - font_level.getsize(str(user[0]['level']))[0]) / 2 + (230 / 2),  -420 + 640),
              str(user[0]['level']), font=font_level, fill=(255, 255, 255))

    draw.text(((411 - font_level.getsize(str(user[0]['username']))[0]) / 2 + (65 / 2), 640 - 394),
              str(user[0]['username']), font=font_score, fill=(0, 0, 0))

    draw.text(((246 - font_level.getsize(str(user[0]['high_score']))[0]) / 2 + (101 / 2), 640 - 331),
              str(user[0]['high_score']), font=font_name, fill=(0, 0, 0))

    draw.text(((392 - font_level.getsize(str(user[0]['last_score']))[0]) / 2 + (246 / 2), 640 - 331),
              str(user[0]['last_score']), font=font_name, fill=(0, 0, 0))

    name = f"menu_{datetime.datetime.now().strftime('%H%M%S%d%m%Y')}"
    img.save(openfile(f"assets/menu/{name}.png"))

    return f"assets/menu/{name}.png"
