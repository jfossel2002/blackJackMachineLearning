from Card import *
import random
class Deck:
    allCards = []
    allSuits = ["Clubs", "Diamonds", "Spades", "Hearts"]
    allRanks = ["Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", "Jack", "Queen", "King", "Ace"]

    def __init__(self, numberDecks):
        for i in range(0, numberDecks):
            for suit in self.allSuits:
                for rank in self.allRanks:
                    self.allCards.append(Card(suit, rank))
    
    def getDeck(self):
        return self.allCards

    def shuffle(self):
        self.allCards = random.sample(self.allCards, len(self.allCards))

    def draw(self):
        drawnCard = self.allCards.pop()
        return drawnCard

    def toString(self):
        myStr = "["
        for card in self.allCards:
            myStr += card.toString()
            myStr += ", "
        myStr += "]"
        return myStr