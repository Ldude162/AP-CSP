import turtle as trtl

painter = trtl.Turtle()
painter.speed(0)
painter.pensize(5)

# starting location of the tower
x = -150
y = -150
newX = -150

# height of tower and a counter for each floor
num_floors = 63
floor = 0
towerReset = 0
# iterate
while floor < num_floors:
  # set placement and color of turtle
  painter.penup()
  # detect if it's time for a new tower
  if towerReset == 21:
    newX = newX + 100
    painter.goto(newX, -150)
    x = newX
    y = -150
    towerReset = 0
  else:
    painter.goto(x, y)
  # Choose color
  if floor % 6 > 2:
    painter.color("gray")
  elif floor % 12 > 2:
    painter.color("red")
  else:
    painter.color("blue")
  y = y + 5 # location of next floor
  # Add onto the floor number
  floor = floor + 1
  towerReset = towerReset + 1
  #draw the floor
  painter.pendown()
  painter.forward(50)

wn = trtl.Screen()
wn.mainloop()