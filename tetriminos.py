import pygame
import numpy
import math
import board

screen = pygame.display.set_mode((0, 0))


class Pieces(pygame.sprite.Sprite):
    def __init__(self, gap, path, x, y):
        super(Pieces, self).__init__()
        self.gap = gap
        self.x = x * self.gap
        self.y = y * self.gap
        self.vel = self.gap
        self.width = self.gap * 10
        self.height = self.gap * 20

    def update(self, coords):
        for coord in coords:
            coord[1] += self.vel

    def boundary_y(self, coords):
        for coord in coords:
            if coord[1] >= self.height:
                return True

    def boundary_y_key(self, coords):
        for coord in coords:
            if coord[1] + self.gap >= self.height:
                return True

    def boundary_x(self, coords, direction):
        max_x = max(coord[0] for coord in coords)
        min_x = min(coord[0] for coord in coords)
        if direction == "left":
            if (min_x - self.vel) >= 0:
                return True
        if direction == "right":
            if (max_x + self.gap + self.vel) <= self.width:
                return True

    def draw_preview(self, surface, resource_location, pos):
        surface.blit(pygame.image.load(resource_location).convert_alpha(), (pos[0], pos[1]))

    def kill_shape(self):
        self.kill()

    def handle_key_presses(self, state, piece, pressed_key, coords):
        if pressed_key[pygame.K_LEFT] and self.boundary_x(coords, "left") and state.check_spot_free_x(piece, "left"):
            for coord in coords:
                coord[0] -= self.vel
        if pressed_key[pygame.K_RIGHT] and self.boundary_x(coords, "right") and state.check_spot_free_x(piece, "right"):
            for coord in coords:
                coord[0] += self.vel
        if pressed_key[pygame.K_DOWN] and not self.boundary_y_key(coords) and not state.check_spot_free_y_key(piece):
            self.update(coords)

    def __len__(self, other):
        return self.__len__()


class Green(Pieces):
    def __init__(self, gap, path, x, y):
        super().__init__(gap, path,  x, y)
        self.surf = pygame.image.load(path + "/green.png").convert_alpha()
        self.name = 'S-Piece'
        self.resource_location = path + "/green_piece.png"
        self.length = 3
        self.thickness = 2
        self.color = "green"
        self.coords = [[self.x + self.gap, self.y], [self.x + 2 * self.gap, self.y],
                       [self.x, self.y + self.gap], [self.x + self.gap, self.y + self.gap]]

    def draw(self, surface):
        for coord in self.coords:
            surface.blit(self.surf, coord)

    def rotate(self, anticlockwise_check=True):
        pivot = numpy.array([self.coords[0]])
        clockwise = numpy.array([[math.cos(math.radians(90)), -math.sin(math.radians(90))],
                                 [math.sin(math.radians(90)), math.cos(math.radians(90))]])
        anticlockwise = numpy.array([[math.cos(math.radians(90)), math.sin(math.radians(90))],
                                     [-math.sin(math.radians(90)), math.cos(math.radians(90))]])
        for index, coord in enumerate(self.coords):
            rel = numpy.subtract(numpy.array([coord]), pivot)
            if anticlockwise_check:
                transformed = numpy.dot(anticlockwise, numpy.squeeze(numpy.asarray(rel)))
            else:
                transformed = numpy.dot(clockwise, numpy.squeeze(numpy.asarray(rel)))
            transformed = numpy.add(pivot, transformed)
            self.coords[index] = list(transformed[0])
        min_x = min(coord[0] for coord in self.coords)
        max_x = max(coord[0] + self.gap for coord in self.coords)
        if min_x < 0:
            diff = abs(min_x)
            for coord in self.coords:
                coord[0] += diff
        elif max_x > self.width:
            diff = max_x - self.width
            for coord in self.coords:
                coord[0] -= diff


class Yellow(Pieces):
    def __init__(self, gap, path, x, y):
        super().__init__(gap, path,  x, y)
        self.surf = pygame.image.load(path + "/yellow.png").convert_alpha()
        self.name = "O-Block"
        self.resource_location = path + "/yellow_piece.png"
        self.length = 2
        self.thickness = 2
        self.color = "yellow"
        self.coords = [[self.x, self.y], [self.x + self.gap, self.y],
                       [self.x, self.y + self.gap], [self.x + self.gap, self.y + self.gap]]

    def draw(self, surface):
        for coord in self.coords:
            surface.blit(self.surf, coord)

    def rotate(self, anticlockwise_check=True):
        pass


class Red(Pieces):
    def __init__(self, gap, path, x, y):
        super().__init__(gap, path,  x, y)
        self.surf = pygame.image.load(path + "/red.png").convert_alpha()
        self.name = "Z-Block"
        self.resource_location = path + "/red_piece.png"
        self.length = 3
        self.thickness = 2
        self.color = "red"
        self.coords = [[self.x, self.y], [self.x + self.gap, self.y],
                       [self.x + self.gap, self.y + self.gap], [self.x + 2 * self.gap, self.y + self.gap]]

    def draw(self, surface):
        for coord in self.coords:
            surface.blit(self.surf, coord)

    def rotate(self, anticlockwise_check=True):
        pivot = numpy.array([self.coords[1]])
        clockwise = numpy.array([[math.cos(math.radians(90)), -math.sin(math.radians(90))],
                                 [math.sin(math.radians(90)), math.cos(math.radians(90))]])
        anticlockwise = numpy.array([[math.cos(math.radians(90)), math.sin(math.radians(90))],
                                     [-math.sin(math.radians(90)), math.cos(math.radians(90))]])
        for index, coord in enumerate(self.coords):
            rel = numpy.subtract(numpy.array([coord]), pivot)
            if anticlockwise_check:
                transformed = numpy.dot(anticlockwise, numpy.squeeze(numpy.asarray(rel)))
            else:
                transformed = numpy.dot(clockwise, numpy.squeeze(numpy.asarray(rel)))
            transformed = numpy.add(pivot, transformed)
            self.coords[index] = list(transformed[0])
        min_x = min(coord[0] - self.gap for coord in self.coords)
        max_x = max(coord[0] + self.gap for coord in self.coords)
        if min_x < 0:
            diff = abs(min_x)
            for coord in self.coords:
                coord[0] += diff
        elif max_x > self.width:
            diff = max_x - self.width
            for coord in self.coords:
                coord[0] -= diff


class Purple(Pieces):
    def __init__(self, gap, path, x, y):
        super().__init__(gap, path,  x, y)
        self.surf = pygame.image.load(path + "/violet.png").convert_alpha()
        self.name = "T-Block"
        self.resource_location = path + "/violet_piece.png"
        self.length = 3
        self.thickness = 2
        self.color = "violet"
        self.coords = [[self.x + self.gap, self.y], [self.x, self.y + self.gap],
                       [self.x + self.gap, self.y + self.gap], [self.x + 2 * self.gap, self.y + self.gap]]

    def draw(self, surface):
        for coord in self.coords:
            surface.blit(self.surf, coord)

    def rotate(self, anticlockwise_check=True):
        pivot = numpy.array([self.coords[2]])
        clockwise = numpy.array([[math.cos(math.radians(90)), -math.sin(math.radians(90))],
                                 [math.sin(math.radians(90)), math.cos(math.radians(90))]])
        anticlockwise = numpy.array([[math.cos(math.radians(90)), math.sin(math.radians(90))],
                                     [-math.sin(math.radians(90)), math.cos(math.radians(90))]])
        for index, coord in enumerate(self.coords):
            rel = numpy.subtract(numpy.array([coord]), pivot)
            if anticlockwise_check:
                transformed = numpy.dot(anticlockwise, numpy.squeeze(numpy.asarray(rel)))
            else:
                transformed = numpy.dot(clockwise, numpy.squeeze(numpy.asarray(rel)))
            transformed = numpy.add(pivot, transformed)
            self.coords[index] = list(transformed[0])
        min_x = min(coord[0] for coord in self.coords)
        max_x = max(coord[0] + self.gap for coord in self.coords)
        if min_x < 0:
            diff = abs(min_x)
            for coord in self.coords:
                coord[0] += diff
        elif max_x > self.width:
            diff = max_x - self.width
            for coord in self.coords:
                coord[0] -= diff


class Blue(Pieces):
    def __init__(self, gap, path, x, y):
        super().__init__(gap, path,  x, y)
        self.surf = pygame.image.load(path + "/blue.png").convert_alpha()
        self.name = "J-Block"
        self.resource_location = path + "/blue_piece.png"
        self.length = 3
        self.thickness = 2
        self.color = "blue"
        self.coords = [[self.x, self.y], [self.x, self.y + self.gap],
                       [self.x + self.gap, self.y + self.gap], [self.x + 2 * self.gap, self.y + self.gap]]

    def draw(self, surface):
        for coord in self.coords:
            surface.blit(self.surf, coord)

    def rotate(self, anticlockwise_check=True):
        pivot = numpy.array([self.coords[1]])
        clockwise = numpy.array([[math.cos(math.radians(90)), -math.sin(math.radians(90))],
                                 [math.sin(math.radians(90)), math.cos(math.radians(90))]])
        anticlockwise = numpy.array([[math.cos(math.radians(90)), math.sin(math.radians(90))],
                                     [-math.sin(math.radians(90)), math.cos(math.radians(90))]])
        for index, coord in enumerate(self.coords):
            rel = numpy.subtract(numpy.array([coord]), pivot)
            if anticlockwise_check:
                transformed = numpy.dot(anticlockwise, numpy.squeeze(numpy.asarray(rel)))
            else:
                transformed = numpy.dot(clockwise, numpy.squeeze(numpy.asarray(rel)))
            transformed = numpy.add(pivot, transformed)
            self.coords[index] = list(transformed[0])
        min_x = min(coord[0] for coord in self.coords)
        max_x = max(coord[0] + self.gap for coord in self.coords)
        if min_x < 0:
            diff = abs(min_x)
            for coord in self.coords:
                coord[0] += diff
        elif max_x > self.width:
            diff = max_x - self.width
            for coord in self.coords:
                coord[0] -= diff


class Orange(Pieces):
    def __init__(self, gap, path, x, y):
        super().__init__(gap, path,  x, y)
        self.surf = pygame.image.load(path + "/orange.png").convert_alpha()
        self.name = "L-Block"
        self.resource_location = path + "/orange_piece.png"
        self.length = 3
        self.thickness = 2
        self.color = "orange"
        self.coords = [[self.x + 2 * self.gap, self.y], [self.x, self.y + self.gap],
                       [self.x + self.gap, self.y + self.gap], [self.x + 2 * self.gap, self.y + self.gap]]
        self.pivot = numpy.array([self.coords[3]])

    def draw(self, surface):
        for coord in self.coords:
            surface.blit(self.surf, coord)

    def rotate(self, anticlockwise_check=True):
        pivot = numpy.array([self.coords[3]])
        clockwise = numpy.array([[math.cos(math.radians(90)), -math.sin(math.radians(90))],
                                 [math.sin(math.radians(90)), math.cos(math.radians(90))]])
        anticlockwise = numpy.array([[math.cos(math.radians(90)), math.sin(math.radians(90))],
                                     [-math.sin(math.radians(90)), math.cos(math.radians(90))]])
        for index, coord in enumerate(self.coords):
            rel = numpy.subtract(numpy.array([coord]), pivot)
            if anticlockwise_check:
                transformed = numpy.dot(anticlockwise, numpy.squeeze(numpy.asarray(rel)))
            else:
                transformed = numpy.dot(clockwise, numpy.squeeze(numpy.asarray(rel)))
            transformed = numpy.add(pivot, transformed)
            self.coords[index] = list(transformed[0])
        min_x = min(coord[0] for coord in self.coords)
        max_x = max(coord[0] + self.gap for coord in self.coords)
        if min_x < 0:
            diff = abs(min_x)
            for coord in self.coords:
                coord[0] += diff
        elif max_x > self.width:
            diff = max_x - self.width
            for coord in self.coords:
                coord[0] -= diff


class Teal(Pieces):
    def __init__(self, gap, path, x, y):
        super().__init__(gap, path,  x, y)
        self.surf = pygame.image.load(path + "/teal.png").convert_alpha()
        self.name = "I-Block"
        self.resource_location = path + "/teal_piece.png"
        self.length = 4
        self.thickness = 1
        self.color = "teal"
        self.coords = [[self.x, self.y], [self.x + self.gap, self.y],
                       [self.x + 2 * self.gap, self.y], [self.x + 3 * self.gap, self.y]]
        self.pivot = numpy.array([self.coords[1]])

    def draw(self, surface):
        for coord in self.coords:
            surface.blit(self.surf, coord)

    def rotate(self, anticlockwise_check=True):
        pivot = numpy.array([self.coords[1]])
        clockwise = numpy.array([[math.cos(math.radians(90)), -math.sin(math.radians(90))],
                                 [math.sin(math.radians(90)), math.cos(math.radians(90))]])
        anticlockwise = numpy.array([[math.cos(math.radians(90)), math.sin(math.radians(90))],
                                     [-math.sin(math.radians(90)), math.cos(math.radians(90))]])
        for index, coord in enumerate(self.coords):
            rel = numpy.subtract(numpy.array([coord]), pivot)
            if anticlockwise_check:
                transformed = numpy.dot(anticlockwise, numpy.squeeze(numpy.asarray(rel)))
            else:
                transformed = numpy.dot(clockwise, numpy.squeeze(numpy.asarray(rel)))
            transformed = numpy.add(pivot, transformed)
            self.coords[index] = list(transformed[0])
        min_x = min(coord[0] for coord in self.coords)
        max_x = max(coord[0] + self.gap for coord in self.coords)
        if min_x < 0:
            diff = abs(min_x)
            for coord in self.coords:
                coord[0] += diff
        elif max_x > self.width:
            diff = max_x - self.width
            for coord in self.coords:
                coord[0] -= diff
