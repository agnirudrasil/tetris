import pygame
import datetime
import os

pygame.font.init()
pygame.init()

screen = pygame.display.set_mode((480, 640))

THEME_SELECTOR = pygame.image.load()

available_themes = os.listdir('assets/textures/')
print(available_themes)
pygame.display.set_caption('Play Tetris!')
img = pygame.image.load("assets/menu/main_menu.png")
date_font = pygame.font.Font('assets/fonts/koliko-Regular.ttf', 19)
token = -1
running = True
solo = pygame.rect.Rect([108, 251, 263, 91])
multiplayer = pygame.Rect([108, 376, 263, 90])
theme_creator = pygame.Rect([108, 500, 263, 91])
theme = pygame.Rect([287, 12, 49, 50])
profile = pygame.Rect([10, 16, 175, 35])
pygame.draw.rect(screen, (0, 0, 0), solo, 5)


def time_of_day():
    if datetime.datetime.now().strftime('%p') == 'AM':
        return 'GOOD MORNING,'
    if datetime.datetime.now().strftime('%p') == 'PM' and int(datetime.datetime.now().strftime('%I')) < 5:
        return 'GOOD AFTERNOON,'
    if datetime.datetime.now().strftime('%p') == 'PM' and 5 <= int(datetime.datetime.now().strftime('%I')) < 9:
        return 'GOOD EVENING,'
    if datetime.datetime.now().strftime('%p') == 'PM' and int(datetime.datetime.now().strftime('%I')) >= 9:
        return 'GOOD NIGHT,'


def reset_display():
    screen.blit(img, (0, 0))
    screen.blit(date_font.render(f"{datetime.datetime.now().strftime('%d %b, %Y')}", True, (255, 255, 255)), (350, 23))
    screen.blit(date_font.render(f"{datetime.datetime.now().strftime('%I:%M:%S %p')}", True, (255, 255, 255)),
                (350, 50))
    screen.blit(date_font.render(f'{time_of_day()}', True, (255, 255, 255)), (55, 17))
    screen.blit(date_font.render(f'AGNIRUDRA SIL', True, (255, 255, 255)), (55, 37))


while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                if solo.collidepoint(event.pos):
                    token = 0
                    running = False
                if multiplayer.collidepoint(event.pos):
                    token = 0
                    running = False
                if theme_creator.collidepoint(event.pos):
                    token = 1
                    running = False
                if theme.collidepoint(event.pos):
                    print('Change Theme')
                if profile.collidepoint(event.pos):
                    print('Profile Settings')
    reset_display()
    pygame.display.flip()

pygame.quit()

if token == 0:
    import tetris
if token == 1:
    import paint_program
