#   a123_apple_1.py
import turtle as trtl
import random as rand

#-----setup-----
apple_image = "apple.gif" # Store the file name of your shape

wn = trtl.Screen()
wn.setup(width=1.0, height=1.0)
wn.addshape(apple_image) # Make the screen aware of the new file

letters = ['a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l']
appls = []
treeAppls = []
treeLetters = []

for i in letters:
  appl = trtl.Turtle()
  appl.shape(apple_image)
  appl.penup()
  appl.hideturtle()
  appls.append(appl)
  

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



for i in range(3):
  appl = rand.choice(appls)
  appl.showturtle()
  appl.goto(rand.randrange(-150, 150), rand.randrange(0, 150))
  for a in treeAppls:
    while abs(a.xcor() - appl.xcor()) < 20 and abs(a.ycor() - appl.ycor()) < 20:
      appl.goto(rand.randrange(-150, 150), rand.randrange(0, 150))
  randomLetter = rand.choice(letters)
  index = letters.index(randomLetter)
  letters.pop(index)
  treeAppls.append(appl)
  treeLetters.append(randomLetter)



wn.tracer(False)
xcor = appl.xcor()
ycor = appl.ycor()
appl.goto(xcor - 20, ycor - 50)
appl.write(randomLetter.upper(), font=("Arial", 50, "normal"))
appl.goto(xcor,ycor)
wn.tracer(True)

wn.onkeypress(byeByeAppl, randomLetter)
wn.listen()
wn.mainloop()