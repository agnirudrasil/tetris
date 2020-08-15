import pygame

screen = pygame.display.set_mode((1280, 720))
pygame.display.set_caption("Make You own Textures!")
screen.fill(((255, 255, 255)))

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.flip()

pygame.quit()
