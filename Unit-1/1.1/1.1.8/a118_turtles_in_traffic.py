#   a118_turtles_in_traffic.py
#   Move turtles horizontally and vertically across screen.
#   Stopping turtles when they collide.
import turtle as trtl

# create two empty lists of turtles, adding to them later
horiz_turtles = []
vert_turtles = []

# use interesting shapes and colors
turtle_shapes = ["arrow", "turtle", "circle", "square", "triangle", "classic"]
horiz_colors = ["red", "blue", "green", "orange", "purple", "gold"]
vert_colors = ["darkred", "darkblue", "lime", "salmon", "indigo", "brown"]

tloc = 50
for s in turtle_shapes:
    # Create turtle, put pen up, set the color, move to the right spot.
    ht = trtl.Turtle(shape=s)
    horiz_turtles.append(ht)
    ht.penup()
    new_color = horiz_colors.pop()
    ht.fillcolor(new_color)
    ht.goto(-350, tloc)
    ht.setheading(0)
    # Create another turtle, put pen up, set the color, move to the right spot.
    vt = trtl.Turtle(shape=s)
    vert_turtles.append(vt)
    vt.penup()
    new_color = vert_colors.pop()
    vt.fillcolor(new_color)
    vt.goto( -tloc, 350)
    vt.setheading(270)
    # change the location for the next turtle to go to.
    tloc += 50

# TODO: move turtles across and down screen, stopping for collisions
for ht in horiz_turtles:
    for vt in vert_turtles:
        steps = 0
        while steps < 50:
            vt.forward(1)
            x1 = vt.xcor()
            y1 = vt.ycor()
            steps = steps + 1
    steps = 0
    while steps < 50:
        ht.forward(6)
        x2 = ht.xcor()
        y2 = ht.ycor()
        steps = steps + 1


wn = trtl.Screen()
wn.mainloop()
