# Academic Integrity Statement
# filename: "prac.py"
# author: Prabhav BHAGAT
# student id: 524555
# email: 524555@learning.eynesbury.edu.au
# date: 04/11/2026
#
# This is all my own work as per the Eynesbury College Academic Integrity Policy 


# Task1

import random 

class Card: 

    def __init__(self,suit,value_str):
        self.__suit = suit
        self.__value_str = value_str

    def getSuit(self):
        return self.__suit
    
    def getValueStr(self): 
        return self.__value_str
    
    def getValue(self): 
        if self.__value_str == "ace": 
            return 1
        elif self.__value_str in ("jack", "king", "queen"):
            return 10
        else:
            return int(self.__value_str)

    def toString(self): 
        return self.__value_str + "of" + self.__suit



import random 

class Card: 

    def __init__(self,suit,value_str):
        self.__suit = suit
        self.__value_str = value_str

    def getSuit(self):
        return self.__suit
    
    def getValueStr(self): 
        return self.__value_str
    
    def getValue(self): 
        if self.__value_str == "ace": 
            return 1
        elif self.__value_str in ("jack", "king", "queen"):
            return 10
        else:
            return int(self.__value_str)

    def toString(self): 
        return self.__value_str + "of" + self.__suit

c1 = Card('hearts', 'ace')
print(c1.toString(), 'is worth', c1.getValue())
c2 = Card('spades', 'jack')
print(c2.toString(), 'is worth', c2.getValue())



#TASK 02 

class Deck: 
    def __init__(self): 
        self.cards = []
        self.reset()
    def reset(self): 
        self.cards=[]
        for suit in ['Hearts', 'Spades', 'Diamonds', 'Clubs']:
            for value in ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King']:
                card = Card(suit,value)
                self.card.append(card)
    def shuffle(self): 
        random.shuffle(self.card)
    def drawCard(self):
        return self.cards.pop()
    
    
 #TASK 03 

class Hand: 
    def __init__(self): 
        sellf.cards =[]

    def addToHand(self,card): 
        if len(self.__card)<5: 
            self.__cards.append(card)
        else: 
            print("Limit reached")

    def getHandValue(self): 
        total=0
        for card in self.__cards: 
            total += card.getValue()
        return total

    def emptyHand(self): 
        self.__cards = []

    def showCards(self): 
        self.desc = []

        for card in self.__cards: 
            self.desc.append(card.toString())
        print(",".join(self,desc))


#finishing task 03 
