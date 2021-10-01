'''
Made by Linus Reynolds and Logan King
On 10/1/2021
Buggy Image Fixed Spider
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
  drawer.goto(0,20)
  if increment < 4:
      drawer.setheading(drawerHeading*increment + 140)
  else:
      drawer.setheading(drawerHeading*increment + 180)
  drawer.forward(legLen)
  increment = increment + 1

# Create e y e s
drawer.pensize(20)
drawer.penup()
drawer.pencolor("red")
drawer.goto(20,0)
drawer.pendown()
drawer.circle(0.1)
drawer.penup()
drawer.goto(-20,0)
drawer.pendown()
drawer.circle(0.1)
drawer.pencolor("black")

drawer.hideturtle()

wn = trtl.Screen()
wn.mainloop()