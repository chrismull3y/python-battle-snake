import pytest
from src.core.coordinate import Coordinate 


def test_coordinate_creation():
    coord = Coordinate(x=5, y=10)
    assert coord.x == 5
    assert coord.y == 10


def test_coordinate_from_dict():
    data = {"x": 3, "y": 7}
    coord = Coordinate.from_dict(data)
    assert coord.x == 3
    assert coord.y == 7


def test_coordinate_from_dict_missing_key():
    data = {"x": 3}
    with pytest.raises(KeyError):
        Coordinate.from_dict(data)


def test_coordinate_from_dict_invalid_type():
    data = {"x": "a", "y": 7}
    with pytest.raises(TypeError):
        Coordinate.from_dict(data)


def test_coordinate_equality():
    coord1 = Coordinate(x=1, y=2)
    coord2 = Coordinate(x=1, y=2)
    assert coord1 == coord2


def test_coordinate_inequality():
    coord1 = Coordinate(x=1, y=2)
    coord2 = Coordinate(x=2, y=1)
    assert coord1 != coord2
