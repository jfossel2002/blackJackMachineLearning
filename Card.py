class Card:
    def __init__(self, mySuit, myRank):
        self.suit = mySuit
        self.rank = myRank
    
    def getSuit(self):
        return self.suit

    def getRank(self):
        return self.rank
    
    def equals(self, card):
        if(self.suit == card.suit):
            if(self.rank == card.rank):
                return True
        return False

    def toString(self):
        return self.getRank() + " of " + self.getSuit()
