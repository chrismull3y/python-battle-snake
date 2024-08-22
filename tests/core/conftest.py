import pytest
import json

@pytest.fixture()
def game_state():
    json_path = "tests/core/example_game_state.json"
    with open(json_path, "r") as file:
        data = json.load(file)
    return data


@pytest.fixture()
def snake(game_state):
    return game_state["you"]


@pytest.fixture()
def board(game_state):
    return game_state["board"]