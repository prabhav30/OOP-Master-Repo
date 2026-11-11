# Academic Integrity Statement
# filename: "second_prac_task01.py"
# author: Prabhav BHAGAT
# student id: 524555
# email: 524555@learning.eynesbury.edu.au
# date: 28/10/2026
#
# This is all my own work as per the Eynesbury College Academic Integrity Policy 


import turtle

#TASK_01

myturtle = turtle.Turtle()
myWindow = turtle.Screen()

myWindow.setup(width=600, height=500)
myWindow.bgcolor("blue")

myturtle.pensize(3)
myturtle.shape("turtle")
myturtle.color("white")

myturtle.penup()
myturtle.goto(50,100)
myturtle.pendown()

myturtle.forward(100)
myturtle.right(90)
myturtle.forward(50)
myturtle.right(90)
myturtle.forward(100)
myturtle.right(90)
myturtle.forward(50)

terry = turtle.Turtle()
terry.color("yellow")
terry.shape("turtle")
terry.pensize(3)
terry.forward(100)
terry.right(120)
terry.forward(100)
terry.right(120)
terry.forward(100)
terry.right(120)

myWindow.exitonclick()

