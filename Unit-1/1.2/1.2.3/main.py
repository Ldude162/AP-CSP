#   a123_apple_1.py
import turtle as trtl
import random as rand

#-----setup-----
apple_image = "pear.gif" # Store the file name of your shape

wn = trtl.Screen()
wn.setup(width=1.0, height=1.0)
wn.addshape(apple_image) # Make the screen aware of the new file

appl = trtl.Turtle()
appl.penup()

letters = ['a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l']

#-----functions-----
# given a turtle, set that turtle to be shaped by the image file
def draw_apple(active_apple):
  active_apple.shape(apple_image)
  wn.update()

def byeByeAppl():
  appl.right(90)
  ycor = appl.ycor()
  appl.clear()
  while ycor > -120:
    appl.forward(1)
    ycor = appl.ycor()
  appl.hideturtle()


#-----function calls-----
draw_apple(appl)
wn.bgpic("background.gif")

randomLetter = rand.choice(letters)

wn.tracer(False)
xcor = appl.xcor()
ycor = appl.ycor()
appl.goto(xcor - 20, ycor - 50)
appl.write(randomLetter.upper(), color=("white"), font=("Arial", 50, "normal"))
appl.goto(xcor,ycor)
wn.tracer(True)

wn.onkeypress(byeByeAppl, randomLetter)
wn.listen()
wn.mainloop()