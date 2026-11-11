# Academic Integrity Statement 
# filename: coin.py
# Author: Prabhav Bhagat
# student ID: 524555
# email: 524555@learning.eynesbury.edu.au
# date: 14/10/2026
# description: Coin Class 
# This is my work as defined by the Academic Integrity Policy

import random 


class Coin: 
    def __init__(self):
        self.set_value()
        return

    def get_value(self): 
        return self.__value

    def set_value(self):
        self.__value = random.randint(0,1)
        return

    def toss(self): 
        self.set_value()
        return self.get_value()    
    pass 

coin = Coin()
print(coin.toss())
print(coin.toss())
print(coin.toss())