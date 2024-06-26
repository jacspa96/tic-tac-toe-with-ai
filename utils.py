from enum import Enum
import numpy as np
import random


class GameState(Enum):
    CONTINUE = "Game not finished"
    DRAW = "Draw"
    X_WIN = "X wins"
    O_WIN = "O wins"


def print_game_grid(game_grid):
    height, width = game_grid.shape
    print("---------")
    for i in range(height):
        print("|", end=" ")
        for j in range(width):
            print(game_grid[i][j], end=" ")
        print("|")
    print("---------")


def validate_coordinates(grid, coordinates):
    if len(coordinates) != 2:
        print("Coordinates should contain exactly 2 numbers")
        return False
    height_index = coordinates[0]
    width_index = coordinates[1]
    if height_index not in range(1, 4) or width_index not in range(1, 4):
        print("Coordinates should be from 1 to 3!")
        return False
    if grid[height_index-1][width_index-1] != " ":
        print("This cell is occupied! Choose another one!")
        return False
    return True


def find_random_move(grid):
    available_cells = find_available_cells(grid)
    return random.choice(available_cells)


def find_available_cells(grid):
    available_cells = []
    (height, width) = grid.shape
    for i in range(height):
        for j in range(width):
            if grid[i, j] == " ":
                available_cells.append((i, j))
    assert available_cells, "No available moves for AI player"
    return available_cells


def check_game_state(grid):
    grid_size = len(grid)
    for i in range(grid_size):
        if np.all(grid[i, :] == "X") or np.all(grid[:, i] == "X"):
            return GameState.X_WIN
        elif np.all(grid[i, :] == "O") or np.all(grid[:, i] == "O"):
            return GameState.O_WIN

    if np.all(grid.diagonal() == "X") or np.all(np.fliplr(grid).diagonal() == "X"):
        return GameState.X_WIN
    elif np.all(grid.diagonal() == "O") or np.all(np.fliplr(grid).diagonal() == "O"):
        return GameState.O_WIN

    if np.any(grid == " "):
        return GameState.CONTINUE
    else:
        return GameState.DRAW
