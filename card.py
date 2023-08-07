import random

class Card:

    def __init__(self, name, description, flavour_text) -> None:
        self.name = name
        self.description = description
        self.flavour_text = flavour_text

    def card_effect() -> None:
        pass


class PotOfGreed(Card):

    def __init__(self) -> None:
        super().__init__("Pot of Greed", "Draw 3 cards from the top of your deck.", "That's what it do, Yugi.")

    def card_effect(self) -> []:
        cards = []
        for x in range(3):
            card = random.choice(Card.__subclasses__())
            cards.append(card())
        
        return cards
    

pig = PotOfGreed()

draw = pig.card_effect()

print(draw[1].name)