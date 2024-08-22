import pytest

from src.core.board import Board
from src.core.coordinate import Coordinate
from src.core.snake import Snake


def test_board_init(board):
    board = Board.from_dict(board)

    assert board.height == 11
    assert board.width == 11
    assert isinstance(board.food, list)
    assert isinstance(board.hazards, list)
    assert isinstance(board.snakes, list)
    assert all(isinstance(food, Coordinate) for food in board.food)
    assert all(isinstance(hazard, Coordinate) for hazard in board.hazards)
    assert all(isinstance(snake, Snake) for snake in board.snakes)


def test_board_init_with_invalid_data(board):
    board["height"] = "eleven"

    with pytest.raises(ValueError):
        Board.from_dict(board)