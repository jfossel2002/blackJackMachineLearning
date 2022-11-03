from Deck import *
from Player import *
from Dealer import *
class BlackJack:
    numberPlayers = 0
    numberDecks = 0
    deck = None
    playerArray = []
    def __init__(self, numPlayers = 3, numDecks = 1):
        self.numberPlayers = numPlayers
        self.numberDecks = numDecks
        self.deck = Deck(4)
        for i in range(0,self.numberPlayers):
            self.playerArray.append(self.newPlayer(str(i)))
        self.deck.shuffle()

    def newPlayer(self, name):
        newPlayer = Player(name, [], 100, 100)
        return newPlayer

    def deal(self):
        for i in range(0,2):
            for j in range(0,len(self.playerArray)):
                self.playerArray[j].addCard(self.deck.draw())

    def toString(self):
        myStr = ""
        for i in range(0, len(self.playerArray)):
            myStr += "Player: "
            myStr += str(i)
            myStr += "\n"
            myStr += self.playerArray[i].toString()
            myStr += "\n"
        return myStr
        