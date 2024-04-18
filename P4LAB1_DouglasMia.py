#Mia Douglas
#04/04/2024
#P4LAB1
#Write a turtle graphics programs that draws a triangle and a square using loops

import turtle
t = turtle.Turtle()

#SQUARE
side = int(input("Length of side: "))
#side=100
for i in range(4):
   t.forward(side)
   t.left(90)

#TRIANGLE
for i in range(3):
    t.forward(side)
    t.left(120)

