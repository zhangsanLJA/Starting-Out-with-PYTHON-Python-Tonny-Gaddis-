import math
import turtle
turtle.penup()
turtle.goto(50/math.sqrt(2)+25,25)
turtle.setheading(135)
turtle.down()
for x in range(8):
    turtle.forward(50)
    turtle.left(45)
turtle.penup()
turtle.goto(0,0)
turtle.write('STOP')
