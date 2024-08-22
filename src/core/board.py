from dataclasses import dataclass

from .snake import Snake
from .coordinate import Coordinate


@dataclass
class Board:
    height: int
    width: int
    food: list[Coordinate]
    hazards: list[Coordinate]
    snakes: list[Snake]

    @classmethod
    def from_dict(cls, board_data: dict):
        food = [Coordinate.from_dict(item) for item in board_data["food"]]
        hazards = [Coordinate.from_dict(item) for item in board_data["hazards"]]
        snakes = [Snake.from_dict(snake_data) for snake_data in board_data["snakes"]]
        return cls(
            height=int(board_data["height"]),
            width=int(board_data["width"]),
            food=food,
            hazards=hazards,
            snakes=snakes,
        )
