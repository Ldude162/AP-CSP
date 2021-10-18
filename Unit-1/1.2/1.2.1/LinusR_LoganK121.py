# a121_catch_a_turtle.py
#-----import statements-----
import turtle
import random

#-----game configuration----
spot_color = "cyan"
spot_size = 2
spot_shape = "circle"
score = 0
font_setup = ("Arial", 20, "normal")

#-----countdown variables-----
timer = 30
counter_interval = 1000   #1000 represents 1 second
timer_up = False

#-----countdown writer-----
counter =  turtle.Turtle()
counter.penup()
counter.goto(-200, -150)

#-----initialize turtle-----
jeff = turtle.Turtle()
jeff.shape(spot_shape)
jeff.shapesize(spot_size)
jeff.fillcolor(spot_color)
jeff.penup()
score_writer = turtle.Turtle()
score_writer.penup()
score_writer.goto(0, 150)

#-----game functions--------
def spot_clicked(x, y):
    change_position()
    update_score()

def change_position():
    x = random.randint(-200, 200)
    y = random.randint(-150, 150)
    jeff.goto(x, y)

def update_score():
    global score
    score += 1
    score_writer.clear()
    score_writer.write(score, font=font_setup)

#-----events----------------
wn = turtle.Screen()
jeff.onclick(spot_clicked)
wn.mainloop()