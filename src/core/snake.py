from dataclasses import dataclass
from .coordinate import Coordinate


@dataclass
class Snake:
    id: str
    name: str
    health: int
    head: Coordinate
    body: list[Coordinate]
    length: int

    @classmethod
    def from_dict(cls, snake_data: dict):
        head = Coordinate.from_dict(snake_data["head"])
        body = [Coordinate.from_dict(part) for part in snake_data["body"]]
        return cls(
            id=snake_data["id"],
            name=snake_data["name"],
            health=int(snake_data["health"]),
            head=head,
            body=body,
            length=int(snake_data["length"]),
        )
