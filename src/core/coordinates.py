from dataclasses import dataclass


@dataclass
class Coordinate:
    x: int
    y: int

    @classmethod
    def from_dict(cls, data):
        return cls(x=data["x"], y=data["y"])
