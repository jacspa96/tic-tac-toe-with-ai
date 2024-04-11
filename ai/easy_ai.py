from .base_ai import BaseAi
import random


class EasyAi(BaseAi):

    def determine_move(self, grid):
        print('Making move level "easy"')
        available_cells = []
        (height, width) = grid.shape
        for i in range(height):
            for j in range(width):
                if grid[i, j] == " ":
                    available_cells.append((i+1, j+1))
        assert available_cells, "No available moves for AI player"
        return random.choice(available_cells)
