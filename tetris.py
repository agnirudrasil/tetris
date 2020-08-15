import pygame
import tetriminos
import colors
from random import shuffle
import time
import board
from itertools import permutations

pygame.init()
pygame.mixer.init()

pygame.mixer.music.load("assets/music/Tetris.mp3")
pygame.mixer.music.set_volume(0.25)
pygame.mixer.music.play(loops=-1)

gap = 40
ROWS, COLS = 20, 10
fall_time = 0
WIDTH, HEIGHT = (gap * 10) + (gap * 5 + 10), gap * 20
running = True
clock = pygame.time.Clock()
path = "assets/textures/pixel_art_style"
TETRIMINOS = []
choices = list(permutations(range(0, 7)))
next_piece_surf = pygame.Surface((gap * 5 + 10, HEIGHT))
CURRENT = None
state = board.Board(gap, path, ROWS, COLS)
HELD = None
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Tetris")
screen.fill((255, 255, 255))


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
    screen.fill(colors.WHITE)
    sprite.draw(screen)
    state.draw_board(screen)
    for i in range(0, 20):
        pygame.draw.line(screen, (0, 0, 0), (0, i * gap), (WIDTH - (gap * 4 + 10), i * gap))
        pygame.draw.line(screen, (0, 0, 0), (i * gap, 0), (i * gap, HEIGHT))
    next_piece_surf.fill(colors.WHITE)

    for index, tetrimino in enumerate(TETRIMINOS):
        tetrimino.draw_preview(next_piece_surf, tetrimino.resource_location, (40, (index + 3.95) * 120))
    if HELD is None:
        pass
    else:
        HELD.draw_preview(next_piece_surf, HELD.resource_location, (40, 40))
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
    CURRENT.handle_key_presses(state, CURRENT, pygame.key.get_pressed(), CURRENT.coords)

    reset_display(CURRENT)
    state.check_line()

    if time.time() - start >= 1:
        start = time.time()
        CURRENT.update(CURRENT.coords)
        if CURRENT.boundary_y(CURRENT.coords) or state.check_spot_free_y(CURRENT):
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
    clock.tick(20)

pygame.quit()
