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
        self.dealer = Dealer()

    def newPlayer(self, name):
        newPlayer = Player(name, [], 100, 100)
        return newPlayer

    def deal(self):
        for i in range(0,2):
            for j in range(0,len(self.playerArray)):
                self.playerArray[j].addCard(self.deck.draw())  #Deal cards to players
            self.dealer.addCard(self.deck.draw())
            
    def hit(self, player):
        player.addCard(self.deck.draw())
    
    def dealerPlayOut(self):
        while(self.dealer.getHandValue()<17):
            self.hit(self.dealer)

    def playerPlayOut(self):
        print()

    def toString(self):
        myStr = ""
        myStr += "Dealer: "
        myStr += " (Value "
        myStr += str(self.dealer.getHandValue())
        myStr += ")\n"
        myStr += self.dealer.toString()
        for i in range(0, len(self.playerArray)):
            myStr += "\nPlayer: "
            myStr += str(i)
            myStr += " (Value "
            myStr += str(self.playerArray[i].getHandValue())
            myStr += ")\n"
            myStr += self.playerArray[i].toString()
            myStr += "\n"
        return myStr

        
        