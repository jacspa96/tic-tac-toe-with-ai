from .base_player import BasePlayer
from utils import find_random_move
import numpy as np


class MediumAiPlayer(BasePlayer):

    def determine_move(self, grid):
        print('Making move level "medium"')
        opposite_symbol = "X" if self.symbol == "O" else "O"
        # First look for possible win
        candidate_coordinates = _find_winning_move_for_symbol(grid, self.symbol, opposite_symbol)
        if candidate_coordinates is not None:
            return candidate_coordinates
        # Then look for blocking the opponent
        candidate_coordinates = _find_winning_move_for_symbol(grid, opposite_symbol, self.symbol)
        if candidate_coordinates is not None:
            return candidate_coordinates
        # Otherwise make a random move
        return find_random_move(grid)


def _find_winning_move_for_symbol(grid, symbol, opposite_symbol):
    grid_size = len(grid)
    for i in range(grid_size):
        if _check_for_winning_condition(grid[i, :], symbol, opposite_symbol):
            return i, np.where(grid[i, :] == " ")[0][0]
        if _check_for_winning_condition(grid[:, i], symbol, opposite_symbol):
            return np.where(grid[:, i] == " ")[0][0], i

    if _check_for_winning_condition(grid.diagonal(), symbol, opposite_symbol):
        coordinate = np.where(grid.diagonal() == " ")[0][0]
        return coordinate, coordinate

    if _check_for_winning_condition(np.fliplr(grid).diagonal(), symbol, opposite_symbol):
        coordinate = np.where(np.fliplr(grid).diagonal() == " ")[0][0]
        # Map coordinate from counter-diagonal to game grid
        return coordinate, abs(coordinate - grid_size + 1)


def _check_for_winning_condition(row, symbol, opposite_symbol):
    return (np.count_nonzero(row == symbol) == len(row) - 1
            and np.count_nonzero(row == opposite_symbol) == 0)
