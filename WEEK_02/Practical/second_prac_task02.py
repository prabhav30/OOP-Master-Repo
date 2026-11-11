# Academic Integrity Statement
# filename: "second_prac_task02.py"
# author: Prabhav BHAGAT
# student id: 524555
# email: 524555@learning.eynesbury.edu.au
# date: 28/10/2026
#
# This is all my own work as per the Eynesbury College Academic Integrity Policy 

import turtle
import random

#TASK 2.1
class TurtleCluster: 
    def __init__(self): 
        self.cluster = []

    def addturtle(self,turtle):
        self.cluster.append(turtle)

#TASK_2.2
    def goTolocation(self,x,y):
        for t in self.cluster:
            t.goto(x,y)

#Task 2.3
    def spreadOut(self): 
        for t in self.cluster: 
            t.right(random.randint(1,360))
            t.forward(random.randint(1,100))

#TASK 2.4
myGroup = TurtleCluster()

for i in range(5): 
    t=turtle.Turtle()
    myGroup.addturtle(t)

myGroup.spreadout()
myGroup.goTolocation(100,100)
myGroup.spreadOut()

turtle.exitonclick()
