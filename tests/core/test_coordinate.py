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


def test_coordinate_from_dict_invalid_value():
    data = {"x": "a", "y": 7}
    with pytest.raises(ValueError):
        Coordinate.from_dict(data)
