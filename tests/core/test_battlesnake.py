import pytest

from src.core.battlesnake import Battlesnake


def test_safe_moves(game_state):
    snake = Battlesnake(game_state)
    safe_moves = snake.filter_safe_moves(["up", "down", "left", "right"])

    assert "up" not in safe_moves


def test_food_targeting(game_state):
    snake = Battlesnake(game_state)
    move = snake.move_towards_food(["up", "right"])

    assert move == "up"


def test_hazard_avoidance(game_state):
    game_state["board"]["hazards"].append({"x" :2, "y": 1})
    snake = Battlesnake(game_state)
    move = snake.avoid_hazards(["up", "right", "down"])
    
    assert move == "up"


def test_best_move_decision(game_state):
    snake = Battlesnake(game_state)
    best_move = snake.calculate_best_move()

    assert best_move in ["up", "right", "down"]


@pytest.mark.parametrize("health, expected", [(95, False), (85, True)])
def test_needs_food(game_state, health, expected):
    game_state["you"]["health"] = health
    snake = Battlesnake(game_state)

    assert snake.needs_food == expected