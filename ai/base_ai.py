from abc import ABC, abstractmethod


class BaseAi(ABC):

    @abstractmethod
    def determine_move(self, grid):
        pass
        