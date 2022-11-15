from Deck import *
from Player import *
from Dealer import *
class BlackJack:
    numberPlayers = 0
    numberDecks = 0
    deck = None
    playerArray = []
    def __init__(self, numPlayers = 3, numDecks = 100):
        self.numberPlayers = numPlayers
        self.numberDecks = numDecks
        self.deck = Deck(numDecks)
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
                self.playerArray[j].addCard(self.deck.draw(),0)  #Deal cards to players
            self.dealer.addCard(self.deck.draw(), 0)
            
    def hit(self, player, handIndex):
        newCard = self.deck.draw()
        player.addCard(newCard,handIndex)
    
    def dealerPlayOut(self):
        while(self.dealer.getHandValue()<17):
            self.hit(self.dealer,0)

    def shouldISplit(self, player, i):
        split = False
        if(player.allHands[i][0].equals(player.allHands[i][1])):
            split = True
        return split

    def playerPlayOut(self, player):
        i = 0
        length = 1
        while i < length: #Each iteratrion handles hand i for player
            if(len(player.allHands[i])==2): 
                if(self.shouldISplit(player, i)): #Place splitting logic here in the if statement to split and restart looking through decks
                    player.splitHand(i)
                    self.hit(player, i)
                    self.hit(player, length)
                    length += 1
                    i = 0
                else:
                    i+=1

    

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
            myStr += "\n"
            myStr += self.playerArray[i].toString()
            myStr += "\n"
        return myStr

        
        