'''
Made by Linus Reynolds and Logan King
On 10/12/21
Turtles in Traffic Revised
'''
import turtle as trtl

# create two empty lists of turtles, adding to them later
horiz_turtles = []
vert_turtles = []

# use interesting shapes and colors
turtle_shapes = ["arrow", "turtle", "circle", "square", "triangle", "classic"]
horiz_colors = ["red", "blue", "green", "orange", "purple", "gold"]
vert_colors = ["darkred", "darkblue", "lime", "salmon", "indigo", "brown"]


# Creates turtles and puts them at the starting points
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

# Defines what to do when a turtle is supposed to be removed.
def removeTurtle():
  ht.forward(350 - steps * 6)
  ht.color("gray")
  horiz_turtles.remove(ht)

# Loops 30 times
steps = 0
while steps < 30:
  htSteps = 0
  # Moves horizontal turtles
  for ht in horiz_turtles:
    htSteps = htSteps + 1
    
    ht.forward(6)

    # If the turtle is about to collide, it will zoom to the end
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


  # Moves vertical turtles until they are at the finish
  for vt in vert_turtles:
    vt.forward(12)
    if vt.ycor() <= -130:
      vt.color("gray")
      vert_turtles.remove(vt)
    
  # Increments the loop
  steps = steps + 1


wn = trtl.Screen()
wn.mainloop()
