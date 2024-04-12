from abc import ABC, abstractmethod


class BasePlayer(ABC):

    @abstractmethod
    def determine_move(self, grid):
        pass
        