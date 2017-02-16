class FlashcardRepository(object):

    def __init__(self, category):
        self.category = category

    def CreateCards():
        lCards = []
        print("Creating cards...")

        print("Done")
        return lCards

    def GetCards(category):
        lCards = []
        print("Getting {} cards...")

        print("Done")
        return lCards

    def SaveCards(lCards):
        result = True
        print("Saving cards...")

        print("Done")
        return result

    def DeleteCardsByCategory(category):
        result = True
        print("Deleting {} cards...".format(category))

        print("Done")
        return result

    def DeleteCardsByList(lCards):
        result = True
        for card in lCards:
            print("Deleting card {}...".format(card))

        print("Done")
        return result

    def DeleteCard(card):
        result = True
        print("Deleting card {}...".format(card))

        print("Done")
        return result
