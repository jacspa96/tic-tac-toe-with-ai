from abc import ABC, abstractmethod


class BasePlayer(ABC):

    def __init__(self, symbol):
        self.symbol = symbol

    @abstractmethod
    def determine_move(self, grid):
        pass
        