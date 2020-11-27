import pygame

temp = pygame.display.set_mode((1, 1))


class Grid:
    def __init__(self, gap, path):
        self.surf = pygame.Surface((gap, gap))
        self.color = "white"
        self.path_img = path
        self.path = path

    def is_white(self):
        return self.color == "white"

    def set_color(self, color):
        self.color = color
        self.path = self.path_img + f"/{color}.png"


class Board:
    def __init__(self, gap, path, row, col):
        self.gap = gap
        self.path = path
        self.row = row
        self.col = col
        self.board = [[Grid(self.gap, self.path) for j in range(col)] for i in range(row)]
        self.board_send = [[self.board[i][j].color for j in range(col)] for i in range(row)]
        self.pos = []

    def covert_coordinates_to_array_pos(self, coords):
        self.pos.clear()
        for coord in coords:
            self.pos.append([int((coord[1] // 40)) - 1, int((coord[0] // 40))])
        return self.pos

    def draw_board(self, surface):
        for i in range(self.row):
            for j in range(self.col):
                if not self.board[i][j].is_white():
                    surface.blit(pygame.image.load(self.board[i][j].path), (j * 40, i * 40))

    def change_spot_color(self, piece):
        pos = self.covert_coordinates_to_array_pos(piece.coords)
        for i in pos:
            self.board[int(i[0])][int(i[1])].set_color(piece.color)
            self.board_send = [[self.board[i][j].color for j in range(self.col)] for i in range(self.row)]
        """for lin in self.board:
            for grid in lin:
                print(grid.color, end=" ")
            print()"""

    def check_spot_free_y(self, piece):
        pos = self.covert_coordinates_to_array_pos(piece.coords)
        for i in pos:
            if not self.board[int(i[0]) + 1][int(i[1])].is_white():
                return True

    def check_spot_free_y_key(self, piece):
        pos = self.covert_coordinates_to_array_pos(piece.coords)
        for i in pos:
            if not self.board[int(i[0]) + 2][int(i[1])].is_white():
                return True

    def check_line(self):
        count = 0
        for i in range(self.row):
            if all(not self.board[i][j].is_white() for j in range(0, self.col)):
                count += 1
                self.move_down(i)
        return count

    def check_spot_free_x(self, piece, direction):
        pos = self.covert_coordinates_to_array_pos(piece.coords)
        if direction == "left":
            if all(self.board[int(i[0]) + 1][int(i[1]) - 1].is_white() for i in pos):
                return True
        if direction == "right":
            if all(self.board[int(i[0]) + 1][int(i[1]) + 1].is_white() for i in pos):
                return True

        return False

    def move_down(self, row):
        for i in range(row, 0, -1):
            for j in range(self.col):
                self.board[i][j].set_color(self.board[i - 1][j].color)

    def is_game_over(self):
        for j in range(0, self.col):
            if not self.board[0][j].is_white():
                return True
