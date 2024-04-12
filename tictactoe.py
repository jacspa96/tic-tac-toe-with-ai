import numpy as np
from enum import Enum
from utils import GameState, print_game_grid
from players.human_player import HumanPlayer
from players.easy_ai_player import EasyAiPlayer

GRID_SIZE = 3
AVAILABLE_COMMANDS = {"start", "easy "}


class PlayerType(Enum):
    HUMAN = "human",
    EASY_AI = "easy"


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


def game_setup():
    while True:
        commands = input("Input command: ")
        if commands == "exit":
            return True, None, None

        commands = commands.split(" ")
        if len(commands) != 3:
            print("Bad parameters!")
            continue

        if commands[0] == "start":
            try:
                x_player = _determine_player(commands[1])
                o_player = _determine_player(commands[2])
                return False, x_player, o_player
            except ValueError:
                print("Bad parameters!")
                continue

        else:
            print("Bad parameters!")


def _determine_player(player_type):
    if player_type == "user":
        return HumanPlayer()
    elif player_type == "easy":
        return EasyAiPlayer()
    raise ValueError(f"Unrecognized player type {player_type}")


def play_game():
    game_grid = np.full((GRID_SIZE, GRID_SIZE), " ")
    x_turn = True
    should_exit, x_player, o_player = game_setup()
    if should_exit:
        return
    print_game_grid(game_grid)
    game_state = GameState.CONTINUE

    while game_state == GameState.CONTINUE:

        if x_turn:
            coordinates = x_player.determine_move(game_grid)
        else:
            coordinates = o_player.determine_move(game_grid)

        game_grid[coordinates[0]-1][coordinates[1]-1] = "X" if x_turn else "O"
        x_turn = not x_turn

        print_game_grid(game_grid)
        game_state = check_game_state(game_grid)

    print(game_state.value)


if __name__ == '__main__':
    play_game()
