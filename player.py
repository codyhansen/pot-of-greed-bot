from dataclasses import dataclass

@dataclass
class Player:
    name: str
    hand: []
    points: int