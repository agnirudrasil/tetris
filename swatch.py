from PIL import Image, ImageDraw
import pygame
import numpy

screen = pygame.display.set_mode((500, 340))
gradient = pygame.Surface((255, 255))
hue = pygame.Surface((20, 255))
gradient = [[[0, 0, 0] for i in range(255)] for j in range(255)]
hue_image = Image.new('RGB', (20, 255), "#FFFFFF")
draw_hue = ImageDraw.Draw(hue_image)

r = g = b = 0
unit = 255 / 6


def reset_display():
    hue.blit(pygame.image.fromstring(hue_image.tobytes(), hue_image.size, hue_image.mode), (0, 0))
    screen.fill((83, 83, 83))
    gradient.fill((255, 255, 255))
    screen.blit(hue, (295, 20))
    screen.blit(gradient, (20, 20))


running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    reset_display()
    pygame.display.flip()

pygame.quit()
