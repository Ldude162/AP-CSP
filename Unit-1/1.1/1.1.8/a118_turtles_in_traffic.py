#   a118_turtles_in_traffic.py
#   Move turtles horizontally and vertically across screen.
#   Stopping turtles when they collide.
import turtle as trtl

# create two empty lists of turtles, adding to them later
horiz_turtles = []
vert_turtles = []
collided_turtles = []

# use interesting shapes and colors
turtle_shapes = ["arrow", "turtle", "circle", "square", "triangle", "classic"]
horiz_colors = ["red", "blue", "green", "orange", "purple", "gold"]
vert_colors = ["darkred", "darkblue", "lime", "salmon", "indigo", "brown"]

tloc = -60
for s in turtle_shapes:
    # Create turtle, put pen up, set the color, move to the right spot.
    ht = trtl.Turtle(shape=s)
    horiz_turtles.append(ht)
    ht.penup()
    new_color = horiz_colors.pop()
    ht.fillcolor(new_color)
    ht.goto(-150, tloc)
    ht.setheading(0)
    # Create another turtle, put pen up, set the color, move to the right spot.
    vt = trtl.Turtle(shape=s)
    vert_turtles.append(vt)
    vt.penup()
    new_color = vert_colors.pop()
    vt.fillcolor(new_color)
    vt.goto(tloc - 10, 130)
    vt.setheading(270)
    # change the location for the next turtle to go to.
    tloc += 50

# Sets variables so it doesn't have an error in the first loop.
x2 = 0
y2 = 0
x1 = 30
y1 = 30
for ht in horiz_turtles:
    for vt in vert_turtles:
        steps = 0
        # moves turtle
        while steps < 50:
            
            if abs(x2 -x1) > 20 or abs(y2 - y1) > 20:
              vt.forward(1)
              x1 = vt.xcor()
              y1 = vt.ycor()
              steps = steps + 1
            else:
              vt.left(90)
              vt.forward(70)
              vt.right(90)
              
              x2 = 0
              y2 = 0
    steps = 0
    while steps < 50:
        ht.forward(6)
        x2 = ht.xcor()
        y2 = ht.ycor()
        steps = steps + 1
    ht.color("gray")
for vt in vert_turtles:
  vt.color("gray")

wn = trtl.Screen()
wn.mainloop()
