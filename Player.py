class Player:
    def __init__(self, name = "None", myHand = [], myTotalMoney = 100, myStartingMoney = 100):
        self.allHands = []
        self.hand = myHand
        self.totalMoney = myTotalMoney
        self.startingMoney = myStartingMoney
        self.name = name
        self.aceValue = 11
        self.cardValues = {"Two": 2, "Three": 3, "Four": 4, "Five": 5, "Six": 6, "Seven": 7, "Eight": 8, "Nine": 9, "Ten": 10, "Jack": 10, "Queen": 10, "King": 10, "Ace": self.aceValue}
        self.allHands.append(self.hand)

    def addCard(self, card, handIndex):
        self.allHands[handIndex].append(card)
    
    def getHand(self):
        return self.hand
    
    def addHand(self, newHand):
        self.allHands.append(newHand)

    def splitHand(self, handIndex):
        newHand = []
        newHand.append(self.allHands[handIndex][0])
        self.allHands[handIndex].remove(self.allHands[handIndex][1])
        self.addHand(newHand)
    
    def toString(self):
        myStr = ""
        for j in range(0, len(self.allHands)):
            myStr += "Hand "
            myStr += str(j)
            myStr += ": Value: "
            myStr += str(self.getHandValue(self.allHands[j], 0))
            myStr += "\n"
            for i in range(0,len(self.allHands[j])):
                myStr += self.allHands[j][i].toString()
                myStr += "\n"
        return myStr
    
    def getAceValue(self):
        return self.aceValue
    
    def setAceValue(self, value):
        self.cardValues = {"Two": 2, "Three": 3, "Four": 4, "Five": 5, "Six": 6, "Seven": 7, "Eight": 8, "Nine": 9, "Ten": 10, "Jack": 10, "Queen": 10, "King": 10, "Ace": value}

    def getHandValue(self, myHand, iterations = 0):
        self.setAceValue(11)
        sumValue = 0
        for i in range(0, len(myHand)):
            sumValue += self.cardValues[myHand[i].getRank()]
            if(sumValue > 21):
                for j in range(0, len(myHand)):
                    if(myHand[j].getRank() == "Ace"):
                        self.setAceValue(1)
                        i = 0
                        if(iterations < 1):
                            sumValue = self.getHandValue(myHand, iterations=iterations+1)
        return sumValue
    

