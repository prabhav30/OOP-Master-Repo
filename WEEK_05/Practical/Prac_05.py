# Academic Integrity Statement
# filename: "prac_05.py"
# author: Prabhav BHAGAT
# student id: 5245555
# email: 524555@learning.eynesbury.edu.au
# date: 18/11/2026
#
# This is all my own work as per the Eynesbury College Academic Integrity Policy

# Task 1
class Person:

    def __init__(self, names, age):
        if len(names) >= 1:
            self.__names = names
        else:
            print("Error: Names must contain at least 1 name. Setting default.")
            self.__names = ["Unknown"]

        if age > 0:
            self.__age = age
        else:
            print("Error: Age must be more then zero")
            self.__age = 0


    # Task 1.2
    def __str__(self):
        return 'Person:' + ' ' + 'Name=' + self.getFullName() + ' ' + 'Age=' + str(self.getAge())

    def getFullName(self):
        return " ".join(self.__names)

    def birthday(self):
        self.__age += 1

    def getAge(self):
        return self.__age