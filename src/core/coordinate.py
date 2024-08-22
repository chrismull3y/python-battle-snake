from dataclasses import dataclass


@dataclass
class Coordinate:
    x: int
    y: int

    @classmethod
    def from_dict(cls, data):
        return cls(x=int(data["x"]), y=int(data["y"]))
