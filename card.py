import random

class Card:

    def __init__(self, name, description, flavour_text) -> None:
        self.name = name
        self.description = description
        self.flavour_text = flavour_text

    def card_effect(self) -> None:
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
    

class CelticGuardian(Card):

    def __init__(self) -> None:
        super().__init__("Celtic Guardian", "Can be played immediately from hand when opponent attacks directly.", "Always supposed to be there.")
        self.attack = 1400
        self.defense = 1200


class JacksKnight(Card):

    def __init__(self) -> None:
        super().__init__("Jack's Knight", "", "Belongs to some guy named Jack.")
        self.attack = 1900
        self.defense = 1000


class DarkMagician(Card):

    def __init__(self) -> None:
        super().__init__("Dark Magician", "", "Spooky wizard man.")
        self.attack = 2500
        self.defense = 2100