import turtle as t
from random import randint

def main () :
    t.setup(width=800 , height=800)
    t.title("Turtle Graphics - turtleIntro")
    t.bgcolor("black")
    t.hideturtle()
    t.speed(0)
    background()
    midground()
    #foreground()
    t.exitonclick()

def background () :
    t.pencolor("green")
    moveT(0,-350)
    t.pensize(0.1)
    for x in range(0,500) :
        f = x / 5
        print("\r Background - " + str(f) + "%", end='')
        y = x%2
        if y==1 :
            randcolor()
        t.circle(x)

def midground () :
    moveT(0,0)
    t.pencolor('black')
    for x in range(0,1000) :
        t.forward(x)
        t.right(90.1)


def foreground () :
    ewfi = 5


def randcolor () :
    b = randint(1,245)
    c = randint(1,245)
    d = randint(1,245)
    tup = (b, c, d)
    t.colormode(255)
    t.pencolor(tup)

def moveT(x,y) :
    t.penup()
    t.setpos(x,y)
    t.pendown()


main ()
