from cell import Cell
from button import Button
import colors
import pygame


def heuristic(point1, point2):
    """
    Returns the distance between two points.
    params:
        point1 (int tuple): first  point
        point2 (int tuple): second point
    return:
        dist (int): Manhattan (aka L) distance between the points
    """
    x1, y1 = point1
    x2, y2 = point2

    dist = abs(x1-x2) + abs(y1-y2)

    return dist


def make_grid(rows, width):
    """
    Return a grid of cells.
    params:
        rows  (int): number of rows in the grid
        width (int): width of the screen
    return:
        grid (list): 2D list of cells
    """
    grid = []
    # calculate the width of each cell based on the number of rows
    cell_width = width // rows

    for i in range(rows):
        grid.append([])
        for j in range(rows):
            cell = Cell(i, j, cell_width, rows)
            grid[i].append(cell)

    return grid


def draw_grid(display, rows, width):
    """ Draws the grid of lines """
    cell_width = width // rows

    for i in range(rows + 1):
        pygame.draw.line(display, colors.GREY,
                         (0, i*cell_width), (width, i*cell_width))
        for j in range(rows):
            pygame.draw.line(display, colors.GREY,
                             (j*cell_width, 0), (j*cell_width, width))


def draw(display, grid, rows, width, buttons=None):
    """ Main draw method which draws each cell and the grid. """
    display.fill(colors.WHITE, ((0, 0), (width, width)))
    display.fill(colors.BLUE, ((0, width), (width, width+50)))

    for row in grid:
        for cell in row:
            cell.draw(display)

    draw_grid(display, rows, width)

    if buttons is not None:
        for button in buttons:
            button.update(display)

    pygame.display.update()


def get_mouse_pos(mouse_pos, rows, width):
    """
    Return the cell that has been clicked on with the mouse.
    params:
        mouse_pos (int, int): position of the cursor
        rows (int): number of rows in the grid
        width (int): width of the scren
    return:
        row, col (int, int): coordinates of clicked cell
    """
    cell_width = width // rows
    y, x = mouse_pos    # get the x, y coordinates of the mouse

    row = y // cell_width
    col = x // cell_width

    return row, col
