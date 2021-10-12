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

  ht = trtl.Turtle(shape=s)
  horiz_turtles.append(ht)
  ht.penup()
  new_color = horiz_colors.pop()
  ht.fillcolor(new_color)
  ht.goto(-200, tloc - 150)
  ht.setheading(0)

  vt = trtl.Turtle(shape=s)
  vert_turtles.append(vt)
  vt.penup()
  new_color = vert_colors.pop()
  vt.fillcolor(new_color)
  vt.goto(-tloc + 150, 200)
  vt.setheading(270)
  
  tloc += 50



# TODO: move turtles across and down screen, stopping for collisions

def removeTurtle():
  ht.forward(350 - steps * 6)
  ht.color("gray")
  print("ht", ht.xcor(), ht.ycor())
  horiz_turtles.remove(ht)



steps = 0
while steps < 30:
  htSteps = 0
  for ht in horiz_turtles:
    htSteps = htSteps + 1
    
    ht.forward(6)
    if steps == 2 and htSteps == 6:
      removeTurtle()
    elif steps == 6 and htSteps == 5:
      removeTurtle()
    elif steps == 9 and htSteps == 4:
      removeTurtle()
    elif steps == 12 and htSteps == 3:
      removeTurtle()
    elif steps == 15 and htSteps == 2:
      removeTurtle()
    elif steps == 18 and htSteps == 1:
      removeTurtle()

  for vt in vert_turtles:
    vt.forward(12)
    print("vt", vt.xcor(), vt.ycor())
    if vt.ycor() <= -130:
      vt.color("gray")
      vert_turtles.remove(vt)
    
  steps = steps + 1


wn = trtl.Screen()
wn.mainloop()
