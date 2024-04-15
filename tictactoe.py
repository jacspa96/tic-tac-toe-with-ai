import numpy as np
from utils import GameState, print_game_grid, check_game_state
from players.human_player import HumanPlayer
from players.easy_ai_player import EasyAiPlayer
from players.medium_ai_player import MediumAiPlayer
from players.hard_ai_player import HardAiPlayer

GRID_SIZE = 3


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
                x_player = _determine_player(commands[1], "X")
                o_player = _determine_player(commands[2], "O")
                return False, x_player, o_player
            except ValueError:
                print("Bad parameters!")
                continue

        else:
            print("Bad parameters!")


def _determine_player(player_type, symbol):
    if player_type == "user":
        return HumanPlayer()
    elif player_type == "easy":
        return EasyAiPlayer()
    elif player_type == "medium":
        return MediumAiPlayer()
    elif player_type == "hard":
        return HardAiPlayer(symbol)
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

        symbol = "X" if x_turn else "O"
        if x_turn:
            coordinates = x_player.determine_move(game_grid, symbol)
        else:
            coordinates = o_player.determine_move(game_grid, symbol)

        game_grid[coordinates[0]][coordinates[1]] = "X" if x_turn else "O"
        x_turn = not x_turn

        print_game_grid(game_grid)
        game_state = check_game_state(game_grid)

    print(game_state.value)


if __name__ == '__main__':
    play_game()
