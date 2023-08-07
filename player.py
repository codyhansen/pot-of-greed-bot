from card import *

class Player:

    def __init__(self, name, hand, field, points) -> None:
        self.name = name
        self.hand = hand
        self.field = field
        self.points = points


    def draw(self) -> Card:
        card = random.choice(Card.__subclasses__())
        return card()