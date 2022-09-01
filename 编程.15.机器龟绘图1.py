import turtle


def main():
    tu1()
    turtle.penup()
    turtle.goto(-50,0)
    turtle.pendown()
    tu2()

def tu1():
    turtle.showturtle()
    turtle.fillcolor('black')
    turtle.begin_fill()
    turtle.goto(25,25)
    turtle.goto(50,0)
    turtle.goto(25,-25)
    turtle.end_fill()
    turtle.hideturtle()

def tu2():
    turtle.showturtle()
    turtle.fillcolor('black')
    turtle.begin_fill()
    turtle.goto(-25,25)
    turtle.goto(0,0)
    turtle.goto(-25,-25)
    turtle.end_fill()
    turtle.hideturtle()

if __name__=='__main__':
    main()
