from .base_player import BasePlayer
from utils import find_random_move


class EasyAiPlayer(BasePlayer):

    def __init__(self, symbol=None):
        super().__init__(symbol)

    def determine_move(self, grid):
        print('Making move level "easy"')
        return find_random_move(grid)
