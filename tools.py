import pygame
import pyautogui


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

    def function(self, pos, canvas, color):
        if self.select is True:
            clicked_pos = int(round(pos[0] / (640 / 40) - 5, 0)), int(round(pos[1] / (640 / 40) - 3, 0))
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
        if self.select is True and pos[1] >= 0 and pos[0] >= 0:
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
        self.select = False

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


class Hand:
    def __init__(self):
        self.surf = pygame.image.load("assets/icons/hand.png").convert_alpha()
        self.rect = self.surf.get_rect(top=3 * 32)
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


class Zoom:
    def __init__(self):
        self.surf = pygame.image.load("assets/icons/zoom.png").convert_alpha()
        self.rect = self.surf.get_rect(top=4 * 32)
        self.select = False

    def draw(self, surface):
        surface.blit(self.surf, self.rect)

    def selected(self, pos, *tools):
        if self.rect.collidepoint(pos) and self.select is False:
            for tool in tools:
                tool.select = False
                tool.unselect()
            self.surf = pygame.image.load("assets/icons/zoom_selected.png").convert_alpha()

            self.select = True
        elif self.rect.collidepoint(pos) and self.select is True:
            self.surf = pygame.image.load("assets/icons/zoom.png").convert_alpha()
            self.select = False

    def unselect(self):
        if self.select is False:
            self.surf = pygame.image.load("assets/icons/zoom.png").convert_alpha()


class Gradient:
    def __init__(self):
        self.surf = pygame.image.load("assets/icons/gradient.png").convert_alpha()
        self.rect = self.surf.get_rect(top=5 * 32)
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


class Eyedropper:
    def __init__(self):
        self.surf = pygame.image.load("assets/icons/eyedropper.png").convert_alpha()
        self.rect = self.surf.get_rect(top=6 * 32)
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
