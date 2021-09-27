'''
Made by Linus Reynolds
On 9/23/2021
1.1.4 nested loop
'''

import turtle as trtl

# Sets up turtle
painter = trtl.Turtle()
painter.shape("circle")
painter.hideturtle()
painter.penup()
painter.speed(100)

# Makes drawing
x = -200
y = -200
while (y < 200): 
    y = y + 50
    painter.goto(x,y)
    painter.color("red")
    painter.stamp()
    while (x < 0):
        x = x + 50
        painter.goto(x,y)
        painter.color("blue")
        painter.stamp()
    x = -200



wn = trtl.Screen()
wn.mainloop()