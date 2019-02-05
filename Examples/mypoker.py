from random import randint
import random

class Cards(object):
    def __init__(self, suit, number):
        self.suit = suit
        self.number = number

    def __str__(self):
        out = "|"
        if self.number == 1:
            out+= "A"
        elif self.number == 11:
            out+= "J"
        elif self.number == 12:
            out+= "Q"
        elif self.number == 13:
            out+= "K"
        else:
            out += str(self.number)
        if self.suit == 0:                                                      #turns the number representing the suit into the unicode character for the suit
            out += "♠"
        if self.suit == 1:
            out += "♥"
        if self.suit == 2:
            out += "♦"
        if self.suit == 3:
            out += "♣"
        out += "|"
        return out

class Hand(object):
    def __init__(self, cards):
        self.cards = cards


    def __str__(self):
        out = ""
        for x in self.cards:
            out+= x.__str__()
        return out

    def ResetHand(self):
        self.cards = []

class Deck(object):
    def __init__(self, cards):
        self.cards = cards

    def ResetDeck(self):
        self.cards = []
        for e in range(0,52):
            if e <= 12:
                self.cards.append(Cards(1, (e + 1)))
            if e > 13 and e <= 26:
                self.cards.append(Cards(2, (e - 13)))
            if e > 26 and e <= 39:
                self.cards.append(Cards(3, (e - 26)))
            if e > 39:
                self.cards.append(Cards(0, (e - 39)))

    def ShuffleDeck(self):
        random.shuffle(self.cards)

    def Deal(self, targetHand, amountToDraw):
        if len(self.cards)-1 > 0:
            for i in range(amountToDraw):
                try:
                    targetHand.cards.append(self.cards[len(self.cards) - 1])
                    self.cards.pop(len(self.cards) - 1)
                except:
                    print("No cards left.")
                    break


#possible_numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13',]
#notUsedNumbers = []

deck1 = Deck([])
hand1 = Hand([])

while True:
    print("Deal a hand (y/n)?")
    playerIn = input()
    if len(deck1.cards) <= 0:
        deck1.ResetDeck()
        deck1.ShuffleDeck()
    if playerIn == "y":
        hand1.ResetHand()
        deck1.Deal(hand1, 10)
        print(hand1)
    elif playerIn == "n":
        break
    else:
        print("go die")













#r = Cards(randint(1,4), randint(1,13))

#x = Cards(randint(1,4), randint(1,13))

#cards = 52

#print("You want a hand? Yes/No")
#generate = input()
#while cards >= 0:
#    print("You want a hand? Yes/No")
#    generate = input()
#    random.shuffle(
#    if generate == 'yes':
#        print(r.GetNumber(), r.GetSuit())
#        print(x.GetNumber(), x.GetSuit())
#        cards = cards - 2
#        generate = input()
#        print(cards)
