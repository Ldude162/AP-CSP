'''
Made by Linus Reynolds
On 9/23/2021
1.1.4 #9b
'''
import turtle as trtl

# Sets up the turtle
painter = trtl.Turtle()
painter.speed(0)
painter.penup()
painter.color("salmon")
circleColor = "salmon"
painter.pensize(2)

# Sets the circle number
spiral_space = 0

# Loops until there are 80 circles
while (spiral_space < 80): 
    # Makes circle
    painter.goto(0,0)
    painter.right(20)
    painter.forward(50+(spiral_space*1.5))
    painter.pendown()
    painter.circle(10)
    painter.penup()
    spiral_space = spiral_space + 1
    # Decides color of circle
    painter.color(circleColor)
    if (spiral_space % 18 == 0):
        painter.color("navy")
        circleColor = "navy"
    if (spiral_space % 36 == 0):
        painter.color("salmon")
        circleColor = "salmon"
    if spiral_space % 5 == 0:
        painter.color("green")
    if spiral_space % 10 == 0:
        painter.color("red")

wn = trtl.Screen()
wn.mainloop()
