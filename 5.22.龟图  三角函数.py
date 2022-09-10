import turtle
def main():
    x1=int(input('请输入第一个点的横坐标： '))
    y1=int(input('请输入第一个点的纵坐标： '))
    x2=int(input('请输入第二个点的横坐标： '))
    y2=int(input('请输入第二个点的纵坐标： '))
    x3=int(input('请输入第三个点的横坐标： '))
    y3=int(input('请输入第三个点的纵坐标： '))
    color=input('请输入填充的颜色：')
    san_jiao_xing(x1,y1,x2,y2,x3,y3,color)

def san_jiao_xing(num1,num2,num3,num4,num5,num6,color):
    turtle.penup()
    turtle.fillcolor(color)
    turtle.begin_fill()
    turtle.goto(num1,num2)
    turtle.pendown()
    turtle.goto(num3,num4)
    turtle.goto(num5,num6)
    turtle.end_fill()

if __name__=='__main__':
    main()
    
