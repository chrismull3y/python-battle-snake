from .board import Board
from .snake import Snake
from .coordinate import Coordinate


HEALTH_LIMIT = 90


class Battlesnake:
    def __init__(self, game_state):
        self.board: Board = Board.from_dict(game_state["board"])
        self.you: Snake = Snake.from_dict(game_state["you"])
        self.needs_food: bool = self.you.health < HEALTH_LIMIT

    def calculate_best_move(self):
        possible_moves = ["up", "down", "left", "right"]
        safe_moves = self.filter_safe_moves(possible_moves)
        if not safe_moves:
            return "up"

        food_targeted_move = (
            self.move_towards_food(safe_moves) if self.needs_food else None
        )
        if food_targeted_move:
            return food_targeted_move

        hazard_avoiding_move = self.avoid_hazards(safe_moves)
        if hazard_avoiding_move:
            return hazard_avoiding_move

        return self.maximize_space(safe_moves)

    def filter_safe_moves(self, moves):
        head = self.you.head
        board_limits = Coordinate(x=self.board.width - 1, y=self.board.height - 1)

        all_snake_bodies = {
            (part.x, part.y) for snake in self.board.snakes for part in snake.body
        }

        safe_moves = []
        for move in moves:
            new_position = self.next_position(head, move)
            if (
                (new_position.x, new_position.y) not in all_snake_bodies
                and 0 <= new_position.x <= board_limits.x
                and 0 <= new_position.y <= board_limits.y
            ):
                safe_moves.append(move)

        return safe_moves

    def move_towards_food(self, safe_moves):
        food_positions = [food for food in self.board.food]
        if not food_positions:
            return None

        closest_food = min(
            food_positions,
            key=lambda pos: abs(pos.x - self.you.head.x) + abs(pos.y - self.you.head.y),
        )
        return self.find_best_move_to_target(safe_moves, closest_food)

    def find_best_move_to_target(self, safe_moves: dict, target: Coordinate):
        head = self.you.head
        best_move = None
        min_distance = float("inf")
        for move in safe_moves:
            new_position = self.next_position(head, move)
            distance = abs(new_position.x - target.x) + abs(new_position.y - target.y)
            if distance < min_distance:
                min_distance = distance
                best_move = move

        return best_move

    def avoid_hazards(self, safe_moves):
        if not self.board.hazards:
            return None

        hazard_positions = {hazard for hazard in self.board.hazards}
        head = self.you.head
        safe_from_hazards = [
            move
            for move in safe_moves
            if self.next_position(head, move) not in hazard_positions
        ]
        return safe_from_hazards[0] if safe_from_hazards else None

    def next_position(self, head: Coordinate, direction: str) -> Coordinate:
        moves = {
            "up": Coordinate(0, 1),
            "down": Coordinate(0, -1),
            "left": Coordinate(-1, 0),
            "right": Coordinate(1, 0),
        }
        return Coordinate(head.x + moves[direction].x, head.y + moves[direction].y)

    def maximize_space(self, safe_moves):
        # TODO: Create a algorithim to maximize board space. Maybe flood fill?
        # https://docs.battlesnake.com/guides/useful-algorithms
        return safe_moves[0]
