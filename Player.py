class Player:
    def __init__(self, name = "None", myHand = [], myTotalMoney = 100, myStartingMoney = 100):
        self.hand = myHand
        self.totalMoney = myTotalMoney
        self.startingMoney = myStartingMoney
        self.name = name
        self.aceValue = 11
        self.cardValues = {"Two": 2, "Three": 3, "Four": 4, "Five": 5, "Six": 6, "Seven": 7, "Eight": 8, "Nine": 9, "Ten": 10, "Jack": 10, "Queen": 10, "King": 10, "Ace": self.aceValue}

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
    
    def getAceValue(self):
        return self.aceValue
    
    def setAceValue(self):
        self.cardValues = {"Two": 2, "Three": 3, "Four": 4, "Five": 5, "Six": 6, "Seven": 7, "Eight": 8, "Nine": 9, "Ten": 10, "Jack": 10, "Queen": 10, "King": 10, "Ace": 1}

    def getHandValue(self, iterations = 0):
        sumValue = 0
        for i in range(0, len(self.hand)):
            sumValue += self.cardValues[self.hand[i].getRank()]
            if(sumValue > 21):
                for j in range(0, len(self.hand)):
                    if(self.hand[j].getRank() == "Ace"):
                        self.setAceValue()
                        i = 0
                        if(iterations < 1):
                            sumValue = self.getHandValue(iterations=iterations+1)
        return sumValue
    

