'''
Made by Linus Reynolds
On 11/9/21
1.2.3 Appls Falling
'''
import turtle as trtl
import random as rand

#-----setup-----
apple_image = "apple.gif" # Store the file name of your shape

wn = trtl.Screen()
wn.setup(width=1.0, height=1.0)
wn.addshape(apple_image) # Make the screen aware of the new file

letters = ['a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l']
treeAppls = []
treeLetters = []
activeLetters= []
applsLeft = 3

#-----functions-----
# given a turtle, set that turtle to be shaped by the image file
def draw_apple(active_apple):
  active_apple.shape(apple_image)
  wn.update()

def byeByeAppl(letter):
  if letter in treeLetters:
    letterIndex = treeLetters.index(letter)
    appl = treeAppls[letterIndex]
    appl.right(90)
    ycor = appl.ycor()
    appl.clear()
    while ycor > -120:
      appl.forward(2)
      ycor = appl.ycor()
    appl.hideturtle()
    newTurtle(letter)

def firstTurtles():
  appl = trtl.Turtle()
  appl.shape(apple_image)
  appl.penup()
  appl.goto(rand.randrange(-150, 150), rand.randrange(0, 150))
  for a in treeAppls:
    while abs(a.xcor() - appl.xcor()) < 20 and abs(a.ycor() - appl.ycor()) < 20:
      appl.goto(rand.randrange(-150, 150), rand.randrange(0, 150))
  randomLetter = rand.choice(letters)
  i = letters.index(randomLetter)
  letters.pop(i)
  treeAppls.append(appl)
  treeLetters.append(randomLetter)
  wn.tracer(False)
  xcor = appl.xcor()
  ycor = appl.ycor()
  appl.goto(xcor - 20, ycor - 50)
  appl.color('white')
  appl.write(randomLetter.upper(), font=("Arial", 50, "normal"))
  appl.goto(xcor,ycor)
  wn.tracer(True)

def newTurtle(letter):
  global applsLeft
  if letters:
    appl = trtl.Turtle()
    appl.shape(apple_image)
    appl.penup()
    appl.goto(rand.randrange(-150, 150), rand.randrange(0,  150))
    
    for a in treeAppls:
      while abs(a.xcor() - appl.xcor()) < 50 and abs(a.ycor()   - appl.ycor()) < 50:
        appl.goto(rand.randrange(-150, 150), rand.randrange(0, 150))
    randomLetter = rand.choice(letters)
    i = letters.index(randomLetter)
    letters.pop(i)
    letterIndex = treeLetters.index(letter)
    treeAppls[letterIndex] = appl
    treeLetters[letterIndex] = randomLetter
    wn.tracer(False)
    xcor = appl.xcor()
    ycor = appl.ycor()
    appl.goto(xcor - 20, ycor - 50)
    appl.color('white')
    appl.write(randomLetter.upper(), font=("Arial", 50,   "normal"))
    appl.goto(xcor,ycor)
    wn.tracer(True)
    for i in treeLetters:
      wn.onkeypress(lambda i=i: byeByeAppl(i), i)
    wn.listen()
    wn.mainloop()
  else:
    applsLeft -= 1
    if applsLeft < 1:
      print('Thank you for playing!')
      wn.bye()

#-----function calls-----
wn.bgpic("background.gif")



for i in range(3):
  firstTurtles()


for i in treeLetters:
  wn.onkeypress(lambda i=i: byeByeAppl(i), i)
wn.listen()
wn.mainloop()