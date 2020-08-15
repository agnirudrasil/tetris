from PIL import Image
from random import shuffle

pack = Image.new('RGBA', (120, 200), (255, 255, 255, 1))
blocks = [Image.open("assets/textures/lego_pieces/red.png"),
          Image.open("assets/textures/lego_pieces/green.png"),
          Image.open("assets/textures/lego_pieces/blue.png"),
          Image.open("assets/textures/lego_pieces/violet.png"),
          Image.open("assets/textures/lego_pieces/yellow.png"),
          Image.open("assets/textures/lego_pieces/teal.png"),
          Image.open("assets/textures/lego_pieces/orange.png")]

shuffle(blocks)

pack.paste(blocks[0], (0, 0), mask=blocks[0])
pack.paste(blocks[1], (40, 0), mask=blocks[0])
pack.paste(blocks[2], (2 * 40, 0), mask=blocks[0])
pack.paste(blocks[3], (40, 40), mask=blocks[0])
pack.paste(blocks[4], (40, 2 * 40), mask=blocks[0])
pack.paste(blocks[5], (40, 3 * 40), mask=blocks[0])
pack.paste(blocks[6], (40, 4 * 40), mask=blocks[0])

pack.save("assets/textures/lego_pieces/pack.png")
