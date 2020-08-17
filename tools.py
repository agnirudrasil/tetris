import numpy
import pygame
import pyautogui
from random import randint as rint

from PIL import Image
from PIL import ImageDraw


class Reset:
    def __init__(self):
        self.surf = pygame.image.load("assets/icons/reset.png").convert_alpha()
        self.rect = self.surf.get_rect(top=6 * 32)
        self.select = False

    def draw(self, surface):
        surface.blit(self.surf, self.rect)

    def selected(self, pos, canvas, *tools):
        if self.rect.collidepoint(pos) and self.select is False:
            self.select = False
            for tool in tools:
                tool.select = False
                tool.unselect()
            return [72, 40]
        return canvas


class Pencil:
    def __init__(self):
        self.surf = pygame.image.load("assets/icons/pencil_selected.png").convert_alpha()
        self.rect = self.surf.get_rect()
        self.select = True

    def draw(self, surface):
        surface.blit(self.surf, self.rect)

    def selected(self, pos, *tools):
        if self.rect.collidepoint(pos) and self.select is False:
            for tool in tools:
                tool.select = False
                tool.unselect()
            self.surf = pygame.image.load("assets/icons/pencil_selected.png").convert_alpha()

            self.select = True
        elif self.rect.collidepoint(pos) and self.select is True:
            self.surf = pygame.image.load("assets/icons/pencil.png").convert_alpha()
            self.select = False

    def unselect(self):
        if self.select is False:
            self.surf = pygame.image.load("assets/icons/pencil.png").convert_alpha()

    def select_(self):
        if self.select is True:
            self.surf = pygame.image.load("assets/icons/pencil_selected.png").convert_alpha()

    def function(self, pos, canvas, canvas_pos, color):
        if self.select is True:
            diff = canvas_pos[0] - 72, canvas_pos[1] - 40
            clicked_pos = int(round((pos[0] - diff[0]) / (640 / 40) - 5, 0)), \
                          int(round((pos[1] - diff[1]) / (640 / 40) - 3, 0))
            if clicked_pos[0] >= 0 and clicked_pos[1] >= 0:
                try:
                    canvas[clicked_pos[0]][clicked_pos[1]] = color
                except IndexError:
                    pass
        return canvas


class Eraser:
    def __init__(self):
        self.surf = pygame.image.load("assets/icons/eraser.png").convert_alpha()
        self.rect = self.surf.get_rect(top=32)
        self.select = False

    def draw(self, surface):
        surface.blit(self.surf, self.rect)

    def selected(self, pos, *tools):
        if self.rect.collidepoint(pos) and self.select is False:
            for tool in tools:
                tool.select = False
                tool.unselect()
            self.surf = pygame.image.load("assets/icons/eraser_selected.png").convert_alpha()

            self.select = True
        elif self.rect.collidepoint(pos) and self.select is True:
            self.surf = pygame.image.load("assets/icons/eraser.png").convert_alpha()
            self.select = False

    def unselect(self):
        if self.select is False:
            self.surf = pygame.image.load("assets/icons/eraser.png").convert_alpha()

    def function(self, pos, canvas):
        if self.select is True:
            clicked_pos = int(round(pos[0] / (640 / 40) - 5, 0)), int(round(pos[1] / (640 / 40) - 3, 0))
            if clicked_pos[0] >= 0 and clicked_pos[1] >= 0:
                try:
                    canvas[clicked_pos[0]][clicked_pos[1]] = [255, 255, 255]
                except IndexError:
                    pass
        return canvas


class Marquee:
    def __init__(self):
        self.surf = pygame.image.load("assets/icons/marquee.png").convert_alpha()
        self.rect = self.surf.get_rect(top=2 * 32)
        self.initial = [0, 0]
        self.rect_select = [0, 0, 0, 0]
        self.diff = [0, 0]
        self.select = False
        self.selection = [0, 0, 0, 0]

    def draw(self, surface):
        surface.blit(self.surf, self.rect)

    def selected(self, pos, *tools):
        if self.rect.collidepoint(pos) and self.select is False:
            for tool in tools:
                tool.select = False
                tool.unselect()
            self.surf = pygame.image.load("assets/icons/marquee_selected.png").convert_alpha()

            self.select = True
        elif self.rect.collidepoint(pos) and self.select is True:
            self.surf = pygame.image.load("assets/icons/marquee.png").convert_alpha()
            self.select = False

    def unselect(self):
        if self.select is False:
            self.surf = pygame.image.load("assets/icons/marquee.png").convert_alpha()

    def set_initial(self, pos, canvas_pos):
        diff = canvas_pos[0] - 72, canvas_pos[1] - 40
        self.initial = int(round((pos[0] - diff[0]) / (640 / 40) - 5, 0)), \
                       int(round((pos[1] - diff[1]) / (640 / 40) - 3, 0))
        return [0, 0, 0, 0]

    def function(self, pos, canvas_pos):
        if self.select is True and pos[0] >= 72 and pos[1] >= 40:
            diff = canvas_pos[0] - 72, canvas_pos[1] - 40
            clicked_pos = int(round((pos[0] - diff[0]) / (640 / 40) - 5, 0)), \
                          int(round((pos[1] - diff[1]) / (640 / 40) - 3, 0))
            self.diff = [(self.initial[0] - clicked_pos[0] + 1) * -1, (self.initial[1] - clicked_pos[1] + 1) * -1]
            self.selection = [self.initial[0], self.initial[1],
                              self.initial[0] + self.diff[0], self.initial[1] + self.diff[1]]
            self.rect_select = [self.initial[0] * (640 // 40), self.initial[1] * (640 // 40),
                                self.diff[0] * (640 // 40), self.diff[1] * (640 // 40)]
        return self.rect_select

    def color_selection(self, color, canvas, delete=False):
        if not delete:
            for i in range(self.selection[0], self.selection[2]):
                for j in range(self.selection[1], self.selection[3]):
                    canvas[i][j] = color
            self._unselect()
            return canvas
        else:
            for i in range(self.selection[0], self.selection[2]):
                for j in range(self.selection[1], self.selection[3]):
                    canvas[i][j] = [255, 255, 255]
            self._unselect()
            return canvas

    def _unselect(self):
        self.rect_select = [0, 0, 0, 0]


class Hand:
    def __init__(self):
        self.surf = pygame.image.load("assets/icons/hand.png").convert_alpha()
        self.rect = self.surf.get_rect(top=3 * 32)
        self.initial = [0, 0]
        self.new_pos = [0, 0]
        self.select = False

    def draw(self, surface):
        surface.blit(self.surf, self.rect)

    def selected(self, pos, *tools):
        if self.rect.collidepoint(pos) and self.select is False:
            for tool in tools:
                tool.select = False
                tool.unselect()
            self.surf = pygame.image.load("assets/icons/hand_selected.png").convert_alpha()

            self.select = True
        elif self.rect.collidepoint(pos) and self.select is True:
            self.surf = pygame.image.load("assets/icons/hand.png").convert_alpha()
            self.select = False

    def unselect(self):
        if self.select is False:
            self.surf = pygame.image.load("assets/icons/hand.png").convert_alpha()

    def set_initial(self, pos):
        if self.select is True:
            if pos[0] > 72 and pos[1] > 40:
                self.initial = int(round(pos[0] / (640 / 40) - 5, 0)), int(round(pos[1] / (640 / 40) - 3, 0))

    def function(self, pos):
        if self.select is True and pos[0] >= 72 and pos[1] >= 40:
            clicked_pos = int(round(pos[0] / (640 / 40) - 5, 0)), int(round(pos[1] / (640 / 40) - 3, 0))
            diff = [(self.initial[0] - clicked_pos[0]) * -1, (self.initial[1] - clicked_pos[1]) * -1]
            print(diff)
            self.new_pos = [diff[0] * (640 // 40), diff[1] * (640 // 40)]
        return self.new_pos


class Gradient:
    def __init__(self):
        self.surf = pygame.image.load("assets/icons/gradient.png").convert_alpha()
        self.rect = self.surf.get_rect(top=4 * 32)
        self.select = False

    def draw(self, surface):
        surface.blit(self.surf, self.rect)

    def selected(self, pos, *tools):
        if self.rect.collidepoint(pos) and self.select is False:
            for tool in tools:
                tool.select = False
                tool.unselect()
            self.surf = pygame.image.load("assets/icons/gradient_selected.png").convert_alpha()

            self.select = True
        elif self.rect.collidepoint(pos) and self.select is True:
            self.surf = pygame.image.load("assets/icons/gradient.png").convert_alpha()
            self.select = False

    def unselect(self):
        if self.select is False:
            self.surf = pygame.image.load("assets/icons/gradient.png").convert_alpha()

    def function(self):
        img = Image.new("RGB", (40, 40), "#FFFFFF")
        draw = ImageDraw.Draw(img)

        r, g, b = rint(0, 255), rint(0, 255), rint(0, 255)
        dr = (rint(0, 255) - r) / 40.
        dg = (rint(0, 255) - g) / 40.
        db = (rint(0, 255) - b) / 40.
        for i in range(40):
            r, g, b = r + dr, g + dg, b + db
            draw.line((i, 0, i, 40), fill=(int(r), int(g), int(b)))

        return numpy.array(img).tolist()


class Eyedropper:
    def __init__(self):
        self.surf = pygame.image.load("assets/icons/eyedropper.png").convert_alpha()
        self.rect = self.surf.get_rect(top=5 * 32)
        self.select = False

    def draw(self, surface):
        surface.blit(self.surf, self.rect)

    def selected(self, pos, *tools):
        if self.rect.collidepoint(pos) and self.select is False:
            for tool in tools:
                tool.select = False
                tool.unselect()
            self.surf = pygame.image.load("assets/icons/eyedropper_selected.png").convert_alpha()

            self.select = True
        elif self.rect.collidepoint(pos) and self.select is True:
            self.surf = pygame.image.load("assets/icons/eyedropper.png").convert_alpha()
            self.select = False

    def unselect(self):
        if self.select is False:
            self.surf = pygame.image.load("assets/icons/eyedropper.png").convert_alpha()

    def function(self):
        if self.select is True:
            color = pyautogui.pixel(pyautogui.position()[0], pyautogui.position()[1])
            return color
