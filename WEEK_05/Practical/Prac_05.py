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

    def getNameHarvardFormat(self):
        surname = self.__names[-1]
        initials = ""

        for names in range(len(self.__names) - 1):
            initials += self.__names[names][0]

        return surname + " " + initials

# Task 1 & 1.2 testing

programmer = Person(['Augusta', 'Ada', 'King'], 36)
print(programmer.getFullName(), 'is', programmer.getAge())
programmer.birthday()
print(programmer.getFullName(), 'is', programmer.getAge())
print(programmer.getNameHarvardFormat())
print(programmer)


#TASK 02

class Book:

    def __init__(self, authors, title, publisher, publishYear, publishPlace):
        if len(authors) >= 1:
            self.__authors = authors

        self.__title = title
        self.__publisher = publisher
        self.__publishYear = publishYear
        self.__publishPlace = publishPlace

    def displayAuthors(self):
        print(self.__authors)

    def getHavardReference(self):
        r = ""
        for author in self.__authors:
            r += author.getNameHarvardFormat() + ', '

        r += self.__title + ', ' + self.__publisher + ', ' + str(self.__publishYear) \
             + ', ' + self.__publishPlace

        return r 
    