from random import randint

class Cards(object):
    def __init__(self, suit, number):
        self.suit = suit
        self.number = number

    def CardNumber(self):
        return self.suit * self.number

    def CardSuit(self):
        if self.suit == 1:
            out+= "♠"
        if self.suit == 2:
            out+= "♥"
        if self.suit == 3:
            out+= "♦"
        if self.suit == 4:
            out+= "♣"

        

r = Cards(randint(1,4), randint(1,13))
print("Yes %s " %(r.CardNumber()))
