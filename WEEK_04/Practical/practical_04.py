# Academic Integrity Statement
# filename: "practical_04.py"
# author: Prabhav BHAGAT
# student id: 5245555
# email: 524555@learning.eynesbury.edu.au
# date: 11/11/2026
#
# This is all my own work as per the Eynesbury College Academic Integrity Policy


#TASK 01

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
        if amount <= self.__money:  #corrected a typo
            self.__money -= amount  #corrected a typo 
        else: 
            print("Cannot spend that much money")
            print("Insufficient Funds !")

    def die(self): 
        self.__alive = False

# #testing the code above
# girl = Person('Tiffany', 22, 5000.50)
# # Testing getters
# print(girl.getName())
# print(girl.getAge())
# print(girl.isAlive())
# print(girl.getMoney())

# # Testing mutator
# girl.setName('Tiffany Smith')
# girl.haveBirthday()
# girl.spendMoney(500.50)
# girl.die()

# # Print again
# print(girl.getName())
# print(girl.getAge())
# print(girl.isAlive())
# print(girl.getMoney())

class Employee(Person):
    def __init__(self, name, age, money, jobTitle, wage):
        super().__init__(name, age, money)
        self.__wage = wage
        self.__jobTitle.__ = jobTitle
        self.hours = 0 


    def getJobTitle(self): 
        return self.__jobTitle
    
    def setWage(self, wage): 
        if wage>0: 
            self.__wage = wage
            
    def work(self, numHours):
        self.__hours += numHours
    
    def receivePay(self): 
        self.__money += (self.__hours)*(self.__wage)
        self.__hours = 0

