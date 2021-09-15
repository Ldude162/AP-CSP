'''
Made by Linus Reynolds
On 9/15/2021
1.1.1 turtle project
'''

#Imports Turtle module
import turtle as trtl

#Makes a turtle object
painter = trtl.Turtle()

#Makes rectangle
for i in range(2):
    painter.forward(100)
    painter.right(90)
    painter.forward(50)
    painter.right(90)

#Makes the vertical line
painter.penup()
painter.forward(50)
painter.right(90)
painter.pendown()
painter.forward(50)
painter.penup()

#Makes the horizontal line
painter.right(90)
painter.forward(50)
painter.right(90)
painter.forward(25)
painter.right(90)
painter.pendown()
painter.forward(100)
painter.penup()

#Makes the diagonal lines
painter.left(90)
painter.forward(25)
painter.left(116)
painter.pendown()
painter.forward(111)
painter.penup()
painter.right(116)
painter.forward(49)
painter.right(117)
painter.pendown()
painter.forward(112)

#Moves the turtle out of the way
painter.penup()
painter.forward(20)

#Keeps the screen from closing right after the program finishes
wn = trtl.Screen()
wn.mainloop()