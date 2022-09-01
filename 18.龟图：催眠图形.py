import turtle
for x in range(50):
    turtle.setheading(90)
    turtle.forward(200-4*x)
    turtle.right(90)
    turtle.forward(200-4*x)
    turtle.penup()
    turtle.hideturtle()
    turtle.goto(4*(x+1),0)
    turtle.showturtle()
    turtle.pendown()
    
    
