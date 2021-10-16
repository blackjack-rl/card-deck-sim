from abc import ABC, abstractmethod
from enum import Enum, IntEnum, auto
from random import choice
from typing import List, NamedTuple


class Suit(Enum):
    SPADE = auto()
    DIAMOND = auto()
    HEART = auto()
    CLUB = auto()

    def __repr__(self) -> str:
        return self.name


class Face(IntEnum):
    ACE = -1
    TWO = 2
    THREE = 3
    FOUR = 4
    FIVE = 5
    SIX = 6
    SEVEN = 7
    EIGHT = 8
    NINE = 9
    TEN = 10
    JACK = 10
    QUEEN = 10
    KING = 10

    def __repr__(self) -> str:
        return self.name


class Card(NamedTuple):
    suit: Suit
    face: Face


def generate_card_deck() -> List[Card]:
    """Generates a standard 52 card deck"""
    deck = []

    for suit in Suit:
        for face in Face:
            deck.append(Card(suit, face))

    return deck


class Deck(ABC):
    def __init__(self, num_of_decks=1) -> None:
        self.num_of_decks = num_of_decks

    @abstractmethod
    def draw_card(self):
        pass


class ContinuousShuffleMachine(Deck):
    def __init__(self, num_of_decks=1) -> None:
        super().__init__(num_of_decks=num_of_decks)


class StandardDeck(Deck):
    def __init__(self, num_of_decks=1) -> None:
        super().__init__(num_of_decks=num_of_decks)
        self.deck = [1, 2, 3, 4, 5]
        # self.discard_pile = []

    def draw_card(self):
        card = choice(self.deck)
        return card


if __name__ == "__main__":
    from pprint import pprint

    deck = StandardDeck()
    print(deck.draw_card())
    pprint(generate_card_deck())
