import colors
import pygame as pygame
""" Main task of this class is basically keeping track of the color of the cell. """


class Cell:
    def __init__(self, row, col, width, total_rows):
        self.row = row
        self.col = col
        self.x = row * width
        self.y = col * width
        self.color = colors.WHITE
        self.neighbors = []
        self.width = width
        self.total_rows = total_rows
        self.weight = float("inf")  # used in Dijkstra's algorithm

    def draw(self, display):
        pygame.draw.rect(display, self.color,
                         (self.x, self.y, self.width, self.width))

    def update_neighbors(self, grid):
        """ Check up,down,left and right neighbors to see if they're barriers. If they are, don't look at them at all. """
        self.neighbors = []
        # check the down neighbor
        if self.row < self.total_rows - 1 and not grid[self.row+1][self.col].is_barrier():
            self.neighbors.append(grid[self.row+1][self.col])
        # check the up neighbor
        if self.row > 0 and not grid[self.row-1][self.col].is_barrier():
            self.neighbors.append(grid[self.row-1][self.col])
        # check the left neighbor
        if self.col > 0 and not grid[self.row][self.col-1].is_barrier():
            self.neighbors.append(grid[self.row][self.col-1])
        # check the right neighbor
        if self.col < self.total_rows - 1 and not grid[self.row][self.col+1].is_barrier():
            self.neighbors.append(grid[self.row][self.col+1])

    def __lt__(self, other):
        return False

    def get_pos(self):
        return self.row, self.col

    def is_visited(self):
        return self.color == colors.LIGHT_BLUE

    def is_available(self):
        return self.color == colors.PURPLE

    def is_barrier(self):
        return self.color == colors.BLACK

    def is_start(self):
        return self.color == colors.RED

    def is_end(self):
        return self.color == colors.GREEN

    def is_path(self):
        return self.color == colors.YELLOW

    def reset(self):
        self.color = colors.WHITE

    def set_color(self, color):
        self.color = color

    def set_start(self):
        self.weight = 0
        self.color = colors.RED

    def set_end(self):
        self.color = colors.GREEN

    def set_barrier(self):
        self.color = colors.BLACK

    def set_visited(self):
        self.color = colors.LIGHT_BLUE

    def set_available(self):
        self.color = colors.PURPLE

    def set_path(self):
        self.color = colors.YELLOW

    def set_weight(self, weight):
        self.weight = weight
