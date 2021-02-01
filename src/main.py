import pygame as pygame
import math
import colors   # custom file that contains constants for colors
import helpers  # custom helper functions
from algorithms import a_star, dijkstra, generate_walls, draw_borders
from button import Button
from tkinter import messagebox, Tk

WIDTH = 800

# set up all buttons with my custom class
a_star_button = Button(WIDTH * 0.05, WIDTH + 10,
                       colors.TEAL, "A* Algorithm", "A*")
dijkstra_button = Button(WIDTH * 0.2, WIDTH + 10,
                         colors.TEAL, "Dijkstra's Algorithm", "Dijkstra")
clear_board_button = Button(WIDTH * 0.85, WIDTH + 10,
                            colors.TEAL, "Clear board", "Clear")
generate_walls_button = Button(WIDTH * 0.45, WIDTH + 10,
                               colors.TEAL, "Generate walls", "Walls")
clear_visited_button = Button(WIDTH * 0.70, WIDTH + 10,
                              colors.TEAL, "Clear visited", "Visited")
buttons = []

# append the buttons to a list which is used later to check for clicks
buttons.append(a_star_button)
buttons.append(dijkstra_button)
buttons.append(clear_board_button)
buttons.append(generate_walls_button)
buttons.append(clear_visited_button)


def main(display, width, rows):
    grid = helpers.make_grid(rows, WIDTH)

    start_pos = None
    end_pos = None
    running = True
    already_executed = False
    generated_walls = False

    # game loop
    while running:
        helpers.draw(display, grid, rows, width, buttons)

        # event loop
        for event in pygame.event.get():
            pos = pygame.mouse.get_pos()
            if event.type == pygame.QUIT:
                running = False

            # process mouse input
            if pygame.mouse.get_pressed()[0]:   # left mouseclick
                # if click is in the bottom of the game screen (buttons)
                if pos[1] > WIDTH:
                    # check each button for a click (needs refactoring)
                    for button in buttons:
                        if button.is_clicked(pos):
                            print("Clicked the button " + button.label)
                            if button.label == "A*":
                                if start_pos and end_pos and already_executed is False:
                                    for row in grid:
                                        for cell in row:
                                            cell.update_neighbors(grid)
                                    a_star(lambda: helpers.draw(display, grid,
                                                                rows, width), grid, start_pos, end_pos)
                                    already_executed = True
                                elif already_executed is True:
                                    Tk().wm_withdraw()
                                    messagebox.showwarning(
                                        "Invalid state", "You must clear the board first")
                                else:
                                    Tk().wm_withdraw()
                                    messagebox.showwarning(
                                        "Invalid state", "You must set start and end positions")
                            if button.label == "Clear":
                                start_pos = None
                                end_pos = None
                                already_executed = False
                                generated_walls = False
                                grid = helpers.make_grid(rows, WIDTH)
                            if button.label == "Visited":
                                for row in grid:
                                    for cell in row:
                                        if cell.is_visited() or cell.is_available() or cell.is_path():
                                            cell.reset()
                                already_executed = False
                            if button.label == "Dijkstra":
                                if start_pos and end_pos and already_executed is False:
                                    for row in grid:
                                        for cell in row:
                                            cell.update_neighbors(grid)
                                    # dijkstra(lambda: helpers.draw(display, grid,
                                            # rows, width), grid, start_pos, end_pos)
                                    dijkstra(lambda: helpers.draw(display, grid,
                                                                  rows, width), grid, start_pos, end_pos)
                                    already_executed = True
                                elif already_executed is True:
                                    Tk().wm_withdraw()
                                    messagebox.showwarning(
                                        "Invalid state", "You must clear the board first")
                                else:
                                    Tk().wm_withdraw()
                                    messagebox.showwarning(
                                        "Invalid state", "You must set start and end positions")
                            if button.label == "Walls" and generated_walls is False:
                                draw_borders(lambda: helpers.draw(display, grid,
                                                                  rows, width), grid, start_pos, end_pos)
                                generate_walls(lambda: helpers.draw(display, grid,
                                                                    rows, width), grid, start_pos, end_pos)
                                generated_walls = True
                            button.clicked = False
                else:
                    row, col = helpers.get_mouse_pos(pos, rows, WIDTH)
                    cell = grid[row][col]
                    if not start_pos and cell != end_pos:
                        start_pos = cell
                        start_pos.set_start()
                    elif not end_pos and cell != start_pos:
                        end_pos = cell
                        end_pos.set_end()
                    elif cell != end_pos and cell != start_pos:
                        cell.set_barrier()

            elif pygame.mouse.get_pressed()[2]:  # right mouseclick
                row, col = helpers.get_mouse_pos(pos, rows, WIDTH)
                cell = grid[row][col]
                cell.reset()

                if cell == start_pos:
                    start_pos = None
                if cell == end_pos:
                    end_pos = None

    pygame.quit()


if __name__ == "__main__":
    rows = 25
    WINDOW = pygame.display.set_mode((WIDTH, WIDTH + 50))
    pygame.display.set_caption("A* Pathfinding Visualization")
    main(WINDOW, WIDTH, rows)
