# Academic Integrity Statement
# filename: "practical_04.py"
# author: Prabhav BHAGAT
# student id: 5245555
# email: 524555@learning.eynesbury.edu.au
# date: 11/11/2026
#
# This is all my own work as per the Eynesbury College Academic Integrity Policy


class Person: 
    def __init__(self,name,age,money):
        self.__name = name
        self.__age = age 
        self.__money = money 
        self.__alive = True


    def getName(self): 
        return self.__name

    def getAge(self): 
        return self.__age

    def isAlive(self): 
        return self.__alive

    def getMoney(self): 
        return self.__money

    def setName(self,name): 
        self.__name = name

    def haveBirthday(self): 
        self.__age += 1 

    def spendMoney(self, amount): 
        if amount <= self._money: 
            self._money -= amount
        else: 
            print("Cannot spend that much money")
            print("Insufficient Funds !")

    def die(self): 
        self.__alive = False    