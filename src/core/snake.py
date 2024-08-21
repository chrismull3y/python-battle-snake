from .coordinates import Coordinate


class Snake:
    def __init__(self, snake_data: dict) -> None:
        self.id: str = snake_data["id"]
        self.name: str = snake_data["name"]
        self.health: int = snake_data["health"]
        self.head: Coordinate = Coordinate.from_dict(snake_data["head"])
        self.body: list[Coordinate] = [
            Coordinate.from_dict(part) for part in snake_data["body"]
        ]
        self.length: int = snake_data["length"]
