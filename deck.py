from abc import ABC


class Deck(ABC):
    def __init__(self, num_of_decks=1) -> None:
        self.num_of_decks = num_of_decks


class ContinuousShuffleMachine(Deck):
    def __init__(self, num_of_decks=1) -> None:
        super().__init__(num_of_decks=num_of_decks)


class StandardDeck(Deck):
    def __init__(self, num_of_decks=1) -> None:
        super().__init__(num_of_decks=num_of_decks)


if __name__ == "__main__":
    pass
