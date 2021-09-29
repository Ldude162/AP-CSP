'''
Made by Linus Reynolds and Logan King
On 9/29/2021
Robot Maze 1
'''
import turtle as trtl

#----- maze and turtle config variables
screen_h = 400
screen_w = 420
startx = -100
starty = -100
turtle_scale = 1.5

#------ robot commands
def move():
  robot.dot(10)
  robot.fd(50)

def turn_left():
  robot.speed(0)
  robot.lt(90)
  robot.speed(2)


#----- init screen
wn = trtl.Screen()
wn.setup(width=screen_w, height=screen_h)
robot_image = "robot.gif"
wn.addshape(robot_image)

#----- init robot
robot = trtl.Turtle(shape=robot_image)
robot.hideturtle()
robot.color("darkorchid")
robot.pencolor("darkorchid")
robot.penup()
robot.setheading(90)
robot.turtlesize(turtle_scale, turtle_scale)
robot.goto(startx, starty)
robot.speed(2)
robot.showturtle()

#---- TODO: change maze here
wn.bgpic("maze2.png") # other file names should be maze2.png, maze3.png

#---- TODO: begin robot movement here
# move robot forward with move()
# turn robot left with turn_left()
# sample while loop:

#Moves up 3
i = 0
while (i < 3): # forward 3
  move()
  print("forward")
  i = i + 1 

# turns right
i = 0
while i < 3:
    turn_left()
    print("left")
    i = i + 1

# goes to the square
i = 0
while i < 2:
    move()
    print("forward")
    i = i + 1

# Goes back to start
robot.goto(startx, starty)

#Runs algorithm to go to 1 square off
i = 0
while i < 2:
    a = 0
    while a < 3:
        move()
        a = a + 1
    turn_left()
    i = i + 1

# Moves to gray square
move()

#---- end robot movement 

wn.mainloop()
