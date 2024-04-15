from .base_player import BasePlayer
from utils import validate_coordinates


class HumanPlayer(BasePlayer):

    def determine_move(self, grid, symbol=None):
        while True:
            coordinates = input("Enter the coordinates: ")
            try:
                coordinates = [int(coordinate) for coordinate in coordinates.split(" ")]
            except ValueError:
                print("You should enter numbers!")
                continue

            if validate_coordinates(grid, coordinates):
                return coordinates[0] - 1, coordinates[1] - 1
