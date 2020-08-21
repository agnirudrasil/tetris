import time
import pygame
import datetime
import os
import random
import pickle
import users


pygame.font.init()
pygame.init()
os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % ((1920 - 480) // 2, (1080 - 640) // 2)

screen = pygame.display.set_mode((480, 640), pygame.NOFRAME)


users.check_user_exist()

with open('data/user.tetrisprofile', 'rb') as f:
    user_profile = pickle.load(f)


THEME_SELECTOR = pygame.image.load('assets/menu/theme_selector.png')
PROFILE_CREATE = pygame.image.load('assets/menu/create_profile.png')
MAIN = pygame.image.load("assets/menu/main_menu.png")
current_page = 0

pygame.display.set_caption('Play Tetris!')
img = MAIN
date_font = pygame.font.Font('assets/fonts/koliko-Regular.ttf', 19)
token = -1
running = True
solo = pygame.rect.Rect([108, 251, 263, 91])
multiplayer = pygame.Rect([108, 376, 263, 90])
theme_creator = pygame.Rect([108, 500, 263, 91])
theme_select = pygame.Rect([105, 494, 275, 70])
theme = pygame.Rect([287, 12, 49, 50])
profile = pygame.Rect([10, 16, 175, 35])
arrow_left = pygame.Rect([16, 193, 91, 127])
arrow_right = pygame.Rect([365, 199, 91, 127])
quit_btn = pygame.Rect([430, 590, 35, 35])
back_profile = pygame.Rect([396, 140, 47, 47])
create = pygame.Rect([165, 351, 162, 46])
index = 0
text = '_'
pygame.draw.rect(screen, (0, 0, 0), solo, 5)


def textbox(_text):
    font = pygame.font.Font('assets/fonts/koliko-Regular.ttf', 25)
    screen.blit(font.render(_text, True, (0, 0, 0)), (94, 290))


def display_themes_util():
    available_themes = os.listdir('assets/textures/')
    available_themes_ = [available_themes[i].split('_') for i in range(0, len(available_themes))]
    themes = []
    for _index, _theme in enumerate(available_themes_):
        __theme__ = ""
        for __theme in _theme:
            __theme__ += __theme.capitalize() + " "
        themes.append([__theme__.strip(), 'assets/textures/' + available_themes[_index] + '/pack.png'])
    return themes


def display_themes(_index):
    themes = display_themes_util()
    font_theme = pygame.font.Font('assets/fonts/koliko-Regular.ttf', 60)
    try:
        _theme = themes[_index]
        screen.blit(font_theme.render(_theme[0], True, (255, 255, 255)), ((480 - font_theme.size(_theme[0])[0]) // 2, 395))
        screen.blit(pygame.transform.scale(pygame.image.load(_theme[1]), (int(120 * 0.75), int(200 * 0.75))), (195, 189))
    except IndexError:
        pass


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
    if current_page == 0:
        screen.blit(date_font.render(f"{datetime.datetime.now().strftime('%d %b, %Y')}", True, (255, 255, 255)),
                    (350, 23))
        screen.blit(date_font.render(f"{datetime.datetime.now().strftime('%I:%M:%S %p')}", True, (255, 255, 255)),
                    (350, 50))
        screen.blit(date_font.render(f'{time_of_day()}', True, (255, 255, 255)), (55, 17))
        screen.blit(date_font.render(f'{user_profile.username}', True, (255, 255, 255)), (55, 37))
    if current_page == 1:
        display_themes(index)
    if current_page == 2:
        textbox(text)


while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                if current_page == 0:
                    index = 0
                    if quit_btn.collidepoint(event.pos):
                        running = False
                    if solo.collidepoint(event.pos):
                        token = 0
                        os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % ((1920 - 311) // 2, (1080 - 216) // 2)
                        screen = pygame.display.set_mode((311, 216), pygame.NOFRAME)
                        screen.blit(pygame.image.load('assets/menu/splash.png'), (0, 0))
                        pygame.display.flip()
                        time.sleep(random.randint(1, 10))
                        running = False
                    if multiplayer.collidepoint(event.pos):
                        token = 0
                        os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % ((1920 - 311) // 2, (1080 - 216) // 2)
                        screen = pygame.display.set_mode((311, 216), pygame.NOFRAME)
                        screen.blit(pygame.image.load('assets/menu/splash.png'), (0, 0))
                        pygame.display.flip()
                        time.sleep(5)
                        running = False
                    if theme_creator.collidepoint(event.pos):
                        token = 1
                        running = False
                    if theme.collidepoint(event.pos):
                        current_page = 1
                        img = THEME_SELECTOR
                    if profile.collidepoint(event.pos):
                        img = PROFILE_CREATE
                        current_page = 2
                if current_page == 1:
                    if theme_select.collidepoint(event.pos):
                        current_page = 0
                        img = MAIN
                    if arrow_left.collidepoint(event.pos):
                        if index - 1 < 0:
                            index = 0
                        else:
                            index -= 1
                    if arrow_right.collidepoint(event.pos):
                        if index + 1 >= len(os.listdir('assets/textures/')):
                            index = len(os.listdir('assets/textures/')) - 1
                        else:
                            index += 1
                if current_page == 2:
                    if back_profile.collidepoint(event.pos):
                        current_page = 0
                        img = MAIN
                        text = '_'
                    if create.collidepoint(event.pos):
                        current_page = 0
                        img = MAIN
                        text = text[:-1]
                        print(text)
        if current_page == 2:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_BACKSPACE:
                    text = text[:-2] + '_'
                else:
                    text = text[:-1]
                    text += event.unicode + '_'

    if running is True:
        reset_display()
    pygame.display.flip()

pygame.quit()

if token == 0:
    import tetris
if token == 1:
    import paint_program