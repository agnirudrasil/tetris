import pygame
from scripts.multiplayer import network

screen = pygame.display.set_mode((1280, 720))


def reset_display():
    screen.fill((255, 255, 255))


n = network.Network()
player = int(n.get_p())
print("Your are player ", player)
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()
