from .base_player import BasePlayer
from utils import GameState, check_game_state, find_available_cells


class HardAiPlayer(BasePlayer):

    def determine_move(self, grid):
        print('Making move level "hard"')
        return self._find_best_move(grid, self.symbol, True)[0]

    def _evaluate_value_of_game_state(self, state):
        if state == GameState.X_WIN:
            return 10 if self.symbol == "X" else -10
        if state == GameState.O_WIN:
            return 10 if self.symbol == "O" else -10
        if state == GameState.DRAW:
            return 0
        return None

    def _find_best_move(self, grid, symbol, ai_turn):
        game_state = check_game_state(grid)
        score = self._evaluate_value_of_game_state(game_state)
        if score is not None:
            return None, score

        available_cells = find_available_cells(grid)
        opposite_symbol = "X" if symbol == "O" else "O"
        moves = []
        scores = []
        for move in available_cells:
            grid[move] = symbol
            moves.append(move)
            # Ignore returned move, as we are only interested with the score.
            # We need move only for the final return to 'determine_move' function,
            # but this is the current move.
            score = self._find_best_move(grid, opposite_symbol, not ai_turn)[1]
            grid[move] = " "
            # Tweak to speed up early minimax:
            # If we find value that we know to be max/min, no need to look further
            if (ai_turn and score == 10) or (not ai_turn and score == -10):
                return move, score
            scores.append(score)
        if ai_turn:
            move_index = scores.index(max(scores))
        else:
            move_index = scores.index(min(scores))
        return moves[move_index], scores[move_index]
