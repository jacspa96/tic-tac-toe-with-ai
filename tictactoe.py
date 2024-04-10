import numpy as np
from enum import Enum

GRID_SIZE = 3


class GameState(Enum):
    CONTINUE = "Game not finished"
    DRAW = "Draw"
    X_WIN = "X wins"
    O_WIN = "O wins"


def get_initial_state():
    cells = input("Enter the cells: ")
    cells = cells.replace("_", " ")
    cells = np.array(list(cells))
    assert len(cells) == 9, "Input must contain exactly 9 elements"

    x_count = 0
    o_count = 0
    for cell in cells:
        assert cell in ["X", "O", " "], "Input must contain only symbols 'X', 'O' and '_'"
        if cell == "X":
            x_count += 1
        elif cell == "O":
            o_count += 1
    x_o_difference = x_count - o_count
    assert 0 <= x_o_difference <= 1, "Difference between 'X' and 'O' symbols cannot be larger than 1"

    return cells.reshape(GRID_SIZE, GRID_SIZE), x_o_difference


def validate_coordinates(grid, coordinates):
    height_index = coordinates[0]
    width_index = coordinates[1]
    if height_index not in range(1, 4) or width_index not in range(1, 4):
        print("Coordinates should be from 1 to 3!")
        return False
    if grid[height_index-1][width_index-1] != " ":
        print("This cell is occupied! Choose another one!")
        return False
    return True


def print_game_grid(game_grid):
    print("---------")
    for i in range(GRID_SIZE):
        print("|", end=" ")
        for j in range(GRID_SIZE):
            print(game_grid[i][j], end=" ")
        print("|")
    print("---------")


def check_game_state(grid):
    for i in range(GRID_SIZE):
        if np.all(grid[i, :] == "X"):
            return GameState.X_WIN
        elif np.all(grid[i, :] == "O"):
            return GameState.O_WIN

    if np.all(grid.diagonal() == "X") or np.all(np.fliplr(grid).diagonal() == "X"):
        return GameState.X_WIN
    elif np.all(grid.diagonal() == "O") or np.all(np.fliplr(grid).diagonal() == "O"):
        return GameState.O_WIN

    if np.any(grid == " "):
        return GameState.CONTINUE
    else:
        return GameState.DRAW


def play_game():
    game_grid, o_turn = get_initial_state()
    print_game_grid(game_grid)
    game_state = check_game_state(game_grid)

    while game_state == GameState.CONTINUE:

        coordinates = input("Enter the coordinates: ")
        try:
            coordinates = [int(coordinate) for coordinate in coordinates.split(" ")]
        except ValueError:
            print("You should enter numbers!")
            continue

        if not validate_coordinates(game_grid, coordinates):
            continue

        game_grid[coordinates[0]-1][coordinates[1]-1] = "O" if o_turn else "X"
        o_turn = not o_turn

        print_game_grid(game_grid)
        game_state = check_game_state(game_grid)

    print(game_state.value)


play_game()
