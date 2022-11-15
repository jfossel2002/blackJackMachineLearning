from Deck import *
from BlackJack import *
from Card import *
myBlackJack = BlackJack()
myBlackJack.deal()
myBlackJack.dealerPlayOut()
for player in myBlackJack.playerArray:
    myBlackJack.playerPlayOut(player)
print(myBlackJack.toString())