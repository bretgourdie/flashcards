from enum import Enum, auto

class FlashcardDispenser(object):

    class Order(Enum):
        SHUFFLED = auto()
        ID_ASC = auto()
        ID_DESC = auto()

    def __init__(self, CardList, CardOrder=Order.SHUFFLED):
        self.CardList = CardList
        self.CardOrder = CardOrder

    def ReviewCardsByTerm(untilPerfect=True):
        print("Reviewing cards by term...")

        print("Done")

    def ReviewCardsByDefinition(untilPerfect=True):
        print("Reviewing cards by definition...")

        print("Done")

