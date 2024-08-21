from .snake import Snake
from .coordinate import Coordinate


class Board:
    def __init__(self, board_data: dict):
        self.height: int = board_data["height"]
        self.width: int = board_data["width"]
        self.food: Coordinate = [
            Coordinate.from_dict(food) for food in board_data["food"]
        ]
        self.hazards: Coordinate = [
            Coordinate.from_dict(hazard) for hazard in board_data["hazards"]
        ]
        self.snakes: list[Snake] = [
            Snake(snake_data) for snake_data in board_data["snakes"]
        ]
