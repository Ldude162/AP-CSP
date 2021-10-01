'''
Made by Linus Reynolds and Logan King
On 10/1/2021
Advanced spider
'''
import turtle as trtl
# Create a spider body
drawer = trtl.Turtle()
drawer.pensize(40)
drawer.circle(20)



# Configure spider legs
legs = 8
legLen = 70
drawerHeading = 240 / legs
drawer.pensize(5)
increment = 0

# Draw legs
while (increment < legs):
    drawer.penup()
    drawer.goto(0,20)
    if increment < 4:
        drawer.setheading(drawerHeading*increment + 100)
        drawer.pendown()
        drawer.circle(100,100)
        drawer.penup()
    else:
        drawer.setheading(drawerHeading*increment + 40)
        drawer.pendown()
        drawer.circle(100,-100)
        drawer.penup()
    increment = increment + 1

# create h e a d
drawer.goto(0,0)
drawer.pendown()
drawer.pensize(40)
drawer.circle(10)


# Create e y e s
drawer.pensize(10)
drawer.penup()
drawer.pencolor("red")
drawer.goto(10,-10)
drawer.pendown()
drawer.circle(0.1)
drawer.penup()
drawer.goto(-10,-10)
drawer.pendown()
drawer.circle(0.1)
drawer.pencolor("black")

drawer.hideturtle()

wn = trtl.Screen()
wn.mainloop()