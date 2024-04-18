#Mia Douglas
#04/06/2024
#P4LAB1b
#Draw my initials

import turtle  

# Function to draw the letter M
def draw_M():
    turtle.pendown()  
    turtle.left(90)   
    turtle.forward(100) 
    turtle.right(135)  
    turtle.forward(70) 
    turtle.left(90)   
    turtle.forward(70)  
    turtle.right(135)  
    turtle.forward(100)  
    turtle.penup()    

# Function to draw the letter D
def draw_D():
    turtle.pendown() 
    turtle.left(180)   
    turtle.forward(100)  
    turtle.right(90)  
    turtle.circle(-50, 180)  
    turtle.penup()    
    turtle.left(90)  
    turtle.forward(100)  
    turtle.left(90)  

# Main function to draw initials
def draw_initials():
    turtle.speed(1)   
    turtle.color("blue")  
    turtle.pensize(5)
    
# Drawing the letter M
    draw_M()

    # Moving to the right to draw the next letter
    turtle.penup()   
    turtle.goto(150, 0)  
    turtle.pendown()  

    # Drawing the letter D
    draw_D()

    turtle.done()
       


draw_initials()
