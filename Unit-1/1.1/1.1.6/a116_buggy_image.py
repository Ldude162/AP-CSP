'''
Made by Linus Reynolds and Logan King
On 10/1/2021
Buggy Image Fixed Variables
'''
import turtle as trtl

drawer = trtl.Turtle()
drawer.pensize(40)
drawer.circle(20)

legs = 6
legLen = 70
drawerHeading = 380 / legs
drawer.pensize(5)
increment = 0
while (increment < legs):
  drawer.goto(0,0)
  drawer.setheading(drawerHeading*increment)
  drawer.forward(legLen)
  increment = increment + 1
drawer.hideturtle()

wn = trtl.Screen()
wn.mainloop()