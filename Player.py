class Player:
    def __init__(self, name = "None", myHand = [], myTotalMoney = 100, myStartingMoney = 100):
        self.hand = myHand
        self.totalMoney = myTotalMoney
        self.startingMoney = myStartingMoney
        self.name = name
    
    def addCard(self, card):
        self.hand.append(card)
    
    def getHand(self):
        return self.hand
    
    def toString(self):
        myStr = ""
        for i in range(0,len(self.hand)):
            myStr += self.hand[i].toString()
            myStr += "\n"
        return myStr
