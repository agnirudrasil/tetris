from PIL import Image


def green():
    piece = Image.new('RGBA', (40 * 3, 40 * 2), (255, 255, 255, 1))
    color = Image.open("assets/textures/lego_pieces/green.png")
    piece.paste(color, (40, 0), mask=color)
    piece.paste(color, (2 * 40, 0), mask=color)
    piece.paste(color, (0, 40), mask=color)
    piece.paste(color, (40, 40), mask=color)
    piece.save("assets/textures/lego_pieces/green_piece.png")


def orange():
    piece = Image.new('RGBA', (40 * 3, 40 * 2), (255, 255, 255, 1))
    color = Image.open("assets/textures/lego_pieces/orange.png")
    piece.paste(color, (2 * 40, 0), mask=color)
    piece.paste(color, (0, 40), mask=color)
    piece.paste(color, (40, 40), mask=color)
    piece.paste(color, (2 * 40, 40), mask=color)
    piece.save("assets/textures/lego_pieces/orange_piece.png")


def violet():
    piece = Image.new('RGBA', (40 * 3, 40 * 2), (255, 255, 255, 1))
    color = Image.open("assets/textures/lego_pieces/violet.png")
    piece.paste(color, (40, 0), mask=color)
    piece.paste(color, (0, 40), mask=color)
    piece.paste(color, (40, 40), mask=color)
    piece.paste(color, (2 * 40, 40), mask=color)
    piece.save("assets/textures/lego_pieces/violet_piece.png")


def red():
    piece = Image.new('RGBA', (40 * 3, 40 * 2), (255, 255, 255, 1))
    color = Image.open("assets/textures/lego_pieces/red.png")
    piece.paste(color, (0, 0), mask=color)
    piece.paste(color, (40, 0), mask=color)
    piece.paste(color, (40, 40), mask=color)
    piece.paste(color, (2 * 40, 40), mask=color)
    piece.save("assets/textures/lego_pieces/red_piece.png")


def blue():
    piece = Image.new('RGBA', (40 * 3, 40 * 2), (255, 255, 255, 1))
    color = Image.open("assets/textures/lego_pieces/blue.png")
    piece.paste(color, (0, 0), mask=color)
    piece.paste(color, (0, 40), mask=color)
    piece.paste(color, (40, 40), mask=color)
    piece.paste(color, (2 * 40, 40), mask=color)
    piece.save("assets/textures/lego_pieces/blue_piece.png")


def teal():
    piece = Image.new('RGBA', (40 * 4, 40), (255, 255, 255, 1))
    color = Image.open("assets/textures/lego_pieces/teal.png")
    piece.paste(color, (0, 0), mask=color)
    piece.paste(color, (40, 0), mask=color)
    piece.paste(color, (2 * 40, 0), mask=color)
    piece.paste(color, (3 * 40, 0), mask=color)
    piece.save("assets/textures/lego_pieces/teal_piece.png")


def yellow():
    piece = Image.new('RGBA', (40 * 2, 40 * 2), (255, 255, 255, 1))
    color = Image.open("assets/textures/lego_pieces/yellow.png")
    piece.paste(color, (0, 0), mask=color)
    piece.paste(color, (40, 0), mask=color)
    piece.paste(color, (0, 40), mask=color)
    piece.paste(color, (40, 40), mask=color)
    piece.save("assets/textures/lego_pieces/yellow_piece.png")


def gen_pieces():
    yellow()
    teal()
    red()
    orange()
    blue()
    violet()
    green()


gen_pieces()
