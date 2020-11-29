import turtle
def drawsnake (r,a,l):
    turtle.seth(-40)
    for i in range(l):
        turtle.circle(r,a)
        turtle.circle(-r,a)
    turtle.circle(r,a/2)
    turtle.fd(40)
    turtle.circle(16,180)
    turtle.fd(40*2/3)
turtle.setup(650,350,200,200)
turtle.penup
turtle.fd(-250)
turtle.pendown
turtle.pensize(25)
turtle.pencolor("purple")
drawsnake(45,85,3)
turtle.done()

