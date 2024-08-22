import pytest

from src.core.coordinate import Coordinate
from src.core.snake import Snake


def test_snake_initialization(snake):
    snake = Snake.from_dict(snake)

    assert snake.id == "bef1a0dd-b2f6-45b8-abef-37723b3887ba"
    assert snake.name == "Python Snake"
    assert snake.health == 87
    assert isinstance(snake.head, Coordinate)
    assert all(isinstance(part, Coordinate) for part in snake.body)
    assert snake.length == 5


def test_snake_init_raises_key_error(snake):
    missing_key_snake = snake.pop("head")

    with pytest.raises(KeyError):
        Snake.from_dict(missing_key_snake)


def test_snake_attribute_types(snake):
    snake = Snake.from_dict(snake)

    assert isinstance(snake.id, str)
    assert isinstance(snake.name, str)
    assert isinstance(snake.health, int)
    assert isinstance(snake.head, Coordinate)
    assert isinstance(snake.body, list)
    assert all(isinstance(part, Coordinate) for part in snake.body) 
    assert isinstance(snake.length, int)