from queue import PriorityQueue
from helpers import heuristic
import pygame
import colors
import random

path = 0

# func to construct the path from goal to start


def construct_path(came_from, current, draw):
    global path
    """ Used to construct the shortest path after the algorithm has worked it out. """
    while current in came_from:
        path += 1
        current = came_from[current]
        current.set_color(colors.YELLOW)
        draw()

# A* algorithm (if you don't know how it works, go online and look it up :) )


def a_star(draw, grid, start, end):
    count = 0
    open_set = PriorityQueue()
    open_set.put((0, count, start))
    came_from = {}
    g_score = {cell: float("inf") for row in grid for cell in row}
    g_score[start] = 0
    f_score = {cell: float("inf") for row in grid for cell in row}
    f_score[start] = heuristic(start.get_pos(), end.get_pos())

    open_set_hash = {start}

    while not open_set.empty():
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

        curr = open_set.get()[2]
        open_set_hash.remove(curr)

        if curr == end:
            construct_path(came_from, end, draw)
            end.set_end()
            start.set_start()
            return True

        for node in curr.neighbors:
            if node == end:
                construct_path(came_from, end, draw)
                end.set_end()
                start.set_start()
                print(path)
                return True
            temp_g = g_score[curr] + 1

            if temp_g < g_score[node]:
                came_from[node] = curr
                g_score[node] = temp_g
                f_score[node] = temp_g + \
                    heuristic(node.get_pos(), end.get_pos())
                if node not in open_set_hash:
                    count += 1
                    open_set.put((f_score[node], count, node))
                    open_set_hash.add(node)
                    node.set_available()
        draw()

        if curr != start:
            curr.set_visited()

    return False

# Dijkstra's algorithm


def dijkstra(draw, grid, start, end):
    graph = {}
    distances = {}
    for row in grid:
        for cell in row:
            cell.update_neighbors(grid)
            graph[cell] = {
                neighbor: neighbor.weight for neighbor in cell.neighbors}
            distances[cell] = cell.weight

    path = []
    current_node = start
    available_nodes = {current_node: current_node.weight}
    came_from = {}
    while available_nodes and current_node != end:
        min_value = current_node.weight
        current_node.update_neighbors(grid)
        current_node.set_visited()
        for node in current_node.neighbors:
            if not node.is_visited():
                node.set_weight(current_node.weight + 1)
                available_nodes[node] = node.weight
                came_from[node] = current_node
                node.set_available()
        available_nodes.pop(current_node)

        sorted_nodes = {key: value for key, value in sorted(
            available_nodes.items(), key=lambda item: item[1])}
        if sorted_nodes:
            current_node = (list(sorted_nodes)[0])
            start.set_start()
            end.set_end()
        else:
            break

        draw()

    if current_node == end:
        while came_from[current_node] != start:
            # while current_node != start:
            try:
                path.insert(0, current_node)
                current_node = came_from[current_node]
                current_node.set_path()
            except KeyError:
                break
            draw()
        path.insert(0, start)

    # start.set_start()
    # end.set_end()

    # shortest_distance = {}
    # grid_copy = grid
    # unseen_nodes = grid_copy

# draw the borders on the edge of the screen


def draw_borders(draw, grid, start, end):
    # draw the border around the edges
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            if col == 0 or col == len(grid)-1:
                grid[row][col].set_barrier()
                draw()
            if row == 0 or row == len(grid)-1:
                grid[row][col].set_barrier()
                draw()

# randomly generate walls based on some stupid mathematics


def generate_walls(draw, grid, start, end):
    x = random.randint(2, len(grid)-2)
    y = random.randint(2, len(grid)-2)
    current_cell = grid[x][y]
    visited = []
    available_cells = (len(grid) - 2)**2
    visited_cells = 1

    while visited_cells < available_cells // 2:
        current_cell.update_neighbors(grid)
        neighbors = current_cell.neighbors

        if not neighbors:
            current_cell = visited.pop()
            continue

        if len(neighbors) > 3:
            next_cell = random.choice(neighbors)
        else:
            x = random.randint(2, len(grid)-2)
            y = random.randint(2, len(grid)-2)
            next_cell = grid[x][y]
        if next_cell == start or next_cell == end:
            continue
        visited.append(current_cell)
        current_cell = next_cell
        current_cell.set_barrier()
        draw()
        visited_cells += 1
