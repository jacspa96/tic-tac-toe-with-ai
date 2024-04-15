from .base_player import BasePlayer
from utils import find_random_move


class EasyAiPlayer(BasePlayer):

    def determine_move(self, grid, symbol=None):
        print('Making move level "easy"')
        return find_random_move(grid)
