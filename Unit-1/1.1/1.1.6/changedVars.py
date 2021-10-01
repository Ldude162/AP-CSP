'''
Made by Linus Reynolds and Logan King
On 10/1/2021
Buggy Image Changed Values
'''
import turtle as trtl
# Create a spider body
drawer = trtl.Turtle()
drawer.pensize(40)
drawer.circle(20)

# Configure spider legs
legs = 8
legLen = 70
drawerHeading = 360 / legs
drawer.pensize(5)
increment = 0

# Draw legs
while (increment < legs):
  drawer.goto(0,20)
  drawer.setheading(drawerHeading*increment)
  drawer.forward(legLen)
  increment = increment + 1
drawer.hideturtle()

wn = trtl.Screen()
wn.mainloop()