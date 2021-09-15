'''
Made by Linus Reynolds
On 9/15/2021
1.1.2 turtle project
'''
 
#Imports Turtle module
import turtle as trtl
 
#Makes a turtle object
painter = trtl.Turtle()
 
#User input decides the scale of the drawing
scale = float(input("What scale would you like the drawing to be? For example, 2 would make the drawing twice as big. Please note that the maximum scale is 4.")) 

#Checks if the scale is too big
if scale > 4:
	print("Scale too big! Please try a smaller number!")
else:
	#Teleports the turtle to the correct starting position
	painter.penup()
	painter.goto(-50 * scale, 20 * scale)
	painter.pendown()
	#Makes rectangle
	for i in range(2):
		painter.forward(100 * scale)
		painter.right(90)
		painter.forward(50 *scale)
		painter.right(90)
	#Makes the vertical line
	painter.penup()
	painter.forward(50 * scale)
	painter.right(90)
	painter.pendown()
	painter.forward(50 * scale)
	painter.penup()
	#Makes the horizontal line
	painter.right(90)
	painter.forward(50 * scale)
	painter.right(90)
	painter.forward(25 *scale)
	painter.right(90)
	painter.pendown()
	painter.forward(100 * scale)
	painter.penup()
	#Makes the diagonal lines
	painter.left(90)
	painter.forward(25 * scale)
	painter.left(116)
	painter.pendown()
	painter.forward(111 * scale)
	painter.penup()
	painter.right(116)
	painter.forward(49 * scale)
	painter.right(117)
	painter.pendown()
	painter.forward(112 * scale)
	#Moves the turtle out of the way
	painter.penup()
	painter.forward(20 * scale)
	#Keeps the screen from closing right after the program finishes
	wn = trtl.Screen()
	wn.mainloop()
