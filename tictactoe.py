import numpy as np
from enum import Enum
from ai.easy_ai import EasyAi

GRID_SIZE = 3


class GameState(Enum):
    CONTINUE = "Game not finished"
    DRAW = "Draw"
    X_WIN = "X wins"
    O_WIN = "O wins"


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


def play_game():
    game_grid = np.full((GRID_SIZE, GRID_SIZE), " ")
    x_turn = True
    print_game_grid(game_grid)
    game_state = GameState.CONTINUE

    ai_player = EasyAi()

    while game_state == GameState.CONTINUE:

        if x_turn:
            coordinates = input("Enter the coordinates: ")
            try:
                coordinates = [int(coordinate) for coordinate in coordinates.split(" ")]
            except ValueError:
                print("You should enter numbers!")
                continue

            if not validate_coordinates(game_grid, coordinates):
                continue
        else:
            coordinates = ai_player.determine_move(game_grid)

        game_grid[coordinates[0]-1][coordinates[1]-1] = "X" if x_turn else "O"
        x_turn = not x_turn

        print_game_grid(game_grid)
        game_state = check_game_state(game_grid)

    print(game_state.value)


if __name__ == '__main__':
    play_game()
