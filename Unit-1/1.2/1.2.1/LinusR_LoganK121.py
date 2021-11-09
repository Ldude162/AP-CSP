'''
Made by Linus Reynolds and Logan King
On 10/22/2021
Dot game thing 1.2.1
'''
#-----import statements-----
import turtle
import random

#-----game configuration----
spot_color = "black"
spot_size = 2
spot_shape = "circle"
score = 0
font_setup = ("Arial", 20, "normal")
colors = ["cyan", "blue", "green", "yellow", "pink", "purple"]
sizes = [0.5, 1, 1.5, 2, 2.5, 3]

#-----countdown variables-----
timer = 5
counter_interval = 1000   #1000 represents 1 second
timer_up = False

#-----countdown writer-----
counter =  turtle.Turtle()
counter.penup()
counter.ht()
counter.goto(-200, -150)

#-----initialize turtle-----
jeff = turtle.Turtle()
jeff.shape(spot_shape)
jeff.shapesize(spot_size)
jeff.fillcolor(spot_color)
jeff.ht()
jeff.penup()
score_writer = turtle.Turtle()
score_writer.penup()
score_writer.ht()
score_writer.goto(0, 150)
start_button = turtle.Turtle()
start_button.penup()
start_button.color("lime")
start_button.shape("square")
start_button.shapesize(10)
start_button.goto(10,20)
text_writer = turtle.Turtle()
text_writer.penup()
text_writer.ht()
text_writer.goto(-70,0)
text_writer.write("Click to start", font = font_setup)

#-----game functions--------
def spot_clicked(x, y):
    if timer >0:
      add_color()
      change_position()
      change_size()
      update_score()
    else:
      jeff.ht()

def change_position():
    x = random.randint(-200, 200)
    y = random.randint(-150, 150)
    jeff.goto(x, y)

def update_score():
    global score
    score += 1
    score_writer.clear()
    score_writer.write(score, font=font_setup)

def countdown():
  global timer, timer_up
  counter.clear()
  if timer <= 0:
    counter.write("Time's Up", font=font_setup)
    timer_up = True
  else:
    counter.write("Timer: " + str(timer), font=font_setup)
    timer -= 1
    counter.getscreen().ontimer(countdown, counter_interval)

def add_color():
  color = random.choice(colors)
  jeff.color(color)
  jeff.stamp()
  jeff.color(spot_color)

def change_size():
  size = random.choice(sizes)
  jeff.shapesize(size)

def start_game(x, y):
  jeff.st()
  jeff.onclick(spot_clicked)
  wn.ontimer(countdown, counter_interval)
  start_button.ht()
  text_writer.clear()
  wn.mainloop()


#-----events----------------
wn = turtle.Screen()
wn.bgcolor("red")
start_button.onclick(start_game)
text_writer.clear()
text_writer.write("Click to start", font = font_setup)

wn.mainloop()