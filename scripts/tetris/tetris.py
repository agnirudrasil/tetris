import pygame
import tetriminos
import colors
import os
from random import shuffle
import time
import board
import math
from itertools import permutations

pygame.init()
pygame.mixer.init()

pygame.mixer.music.load("assets/music/Tetris.mp3")
pygame.mixer.music.set_volume(0.25)
pygame.mixer.music.play(loops=-1)

gap = 40
font = pygame.font.Font('assets/fonts/Square.ttf', 40)
ROWS, COLS = 20, 10
fall_time = 0
WIDTH, HEIGHT = (gap * 10) + (gap * 5 + 10), gap * 20
os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % ((1920 - WIDTH) // 2, (1080 - HEIGHT) // 2)
running = True
clock = pygame.time.Clock()
path = "assets/textures/shiny_pieces"
TETRIMINOS = []
choices = list(permutations(range(0, 7)))
next_piece_surf = pygame.Surface((gap * 5 + 10, HEIGHT))
CURRENT = None
state = board.Board(gap, path, ROWS, COLS)
HELD = None
line = 0
level = 0
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Tetris")
screen.fill((255, 255, 255))
score = 0


def held():
    global CURRENT, HELD
    CURRENT, HELD = HELD, CURRENT
    if CURRENT is None:
        switch_tetriminos()


def gen_tetriminos():
    shuffle(choices)
    choice = choices[0]
    for i in choice:
        if i == 0:
            TETRIMINOS.append(tetriminos.Green(gap, path, 4, 0))
        if i == 1:
            TETRIMINOS.append(tetriminos.Yellow(gap, path, 4, 0))
        if i == 2:
            TETRIMINOS.append(tetriminos.Red(gap, path, 4, 0))
        if i == 3:
            TETRIMINOS.append(tetriminos.Purple(gap, path, 4, 0))
        if i == 4:
            TETRIMINOS.append(tetriminos.Blue(gap, path, 4, 0))
        if i == 5:
            TETRIMINOS.append(tetriminos.Orange(gap, path, 4, 0))
        if i == 6:
            TETRIMINOS.append(tetriminos.Teal(gap, path, 4, 0))


def switch_tetriminos():
    global CURRENT
    CURRENT = TETRIMINOS.pop(0)


def reset_display(sprite):
    screen.fill((36, 36, 36))
    sprite.draw(screen)
    state.draw_board(screen)
    for i in range(0, 20):
        pygame.draw.line(screen, (230, 230, 230), (0, i * gap), (WIDTH - (gap * 4 + 10), i * gap))
        pygame.draw.line(screen, (230, 230, 230), (i * gap, 0), (i * gap, HEIGHT))
    next_piece_surf.fill((36, 36, 36))
    next_piece_surf.blit(font.render('HELD', True, (230, 230, 230)), (((gap * 5 + 10) - font.size('HELD')[0]) // 2, 0))
    for index, tetrimino in enumerate(TETRIMINOS):
        tetrimino.draw_preview(next_piece_surf, tetrimino.resource_location, (40, (index + 3.95) * 120))
    if HELD is None:
        pass
    else:
        HELD.draw_preview(next_piece_surf, HELD.resource_location, (40, 40))
    pygame.draw.rect(next_piece_surf, (230, 230, 230), (40, 40, 160, 2 * gap), 3)
    next_piece_surf.blit(font.render('Score', True, (230, 230, 230)), (((gap * 5 + 10) - font.size('Score')[0]) // 2, 4 * 40))
    next_piece_surf.blit(font.render(str(score), True, (230, 230, 230)), (((gap * 5 + 10) - font.size(str(score))[0]) // 2, 5 * 40))
    next_piece_surf.blit(font.render('Level', True, (230, 230, 230)), (((gap * 5 + 10) - font.size('Level')[0]) // 2, 6 * 40))
    next_piece_surf.blit(font.render(str(level), True, (230, 230, 230)),
                         (((gap * 5 + 10) - font.size(str(level))[0]) // 2, 7 * 40))
    next_piece_surf.blit(font.render('Lines', True, (230, 230, 230)), (((gap * 5 + 10) - font.size('Lines')[0]) // 2, 8 * 40))
    next_piece_surf.blit(font.render(str(line), True, (230, 230, 230)),
                         (((gap * 5 + 10) - font.size(str(line))[0]) // 2, 9 * 40))
    next_piece_surf.blit(font.render('Next', True, (230, 230, 230)), (((gap * 5 + 10) - font.size('Next')[0]) // 2, 10.85 * 40))
    pygame.draw.rect(next_piece_surf, (0, 0, 0), (40, 3.95 * 120, 160, 8 * gap), 3)
    screen.blit(next_piece_surf, (gap * 10, 0))
    pygame.draw.line(screen, (0, 0, 0), (gap * 10, 0), (gap * 10, HEIGHT), 2)
    pygame.display.flip()


for i in range(0, 7):
    gen_tetriminos()

switch_tetriminos()
switch = False
start = time.time()
counter = 0
held_count = 0

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP or event.key == pygame.K_x:
                CURRENT.rotate(False)
            if event.key == pygame.K_z or event.key == pygame.K_LCTRL:
                CURRENT.rotate()
            if event.key == pygame.K_c:
                if held_count == 0:
                    held()
                    held_count += 1

    score += CURRENT.handle_key_presses(state, CURRENT, pygame.key.get_pressed(), CURRENT.coords)

    line_count = state.check_line()
    line += line_count
    level = line // 10
    if line_count == 1:
        score += 40 * (level + 1)
    if line_count == 2:
        score += 100 * (level + 1)
    if line_count == 3:
        score += 300 * (level + 1)
    if line_count == 4:
        score += 1200 * (level + 1)

    reset_display(CURRENT)

    fall_time = (math.pow((0.8 - ((level - 1) * 0.007)), (level - 1))) if level <= 8 \
        else (math.pow((0.8 - ((9 - 1) * 0.007)), (9 - 1)))

    print(fall_time)

    if time.time() - start >= fall_time:
        start = time.time()
        CURRENT.update(CURRENT.coords)
        if CURRENT.boundary_y(CURRENT.coords) or state.check_spot_free_y(CURRENT):
            score_ = 0
            CURRENT.kill()
            held_count = 0
            counter += 1
            if counter >= 6:
                gen_tetriminos()
            state.change_spot_color(CURRENT)
            switch_tetriminos()

    if state.is_game_over():
        break

    pygame.display.flip()
    clock.tick(60)
pygame.quit()
