import turtle as t
from random import randint

def main () :
    t.setup(width=800 , height=800)
    t.title("Python Turtle Graphics - Introduction")
    randback ()
    t.hideturtle()
    t.speed(0)
    t.tracer(0,0)
    print("Program has four parts to complete. By Daniel P")
    background()
    midground()
    foreground()
    someground ()
    ros()
    tros()
    t.update
    t.exitonclick()


#=================================================================================================================

def background () :
    t.pencolor("green")
    moveT(0,-400)
    t.pensize(0.1)
    for x in range(0,500) :
        f = x / 5
        print("\rBackground - " + str(f) + "%", end='')
        y = x%2
        if y==1 :
            randcolor()
        t.circle(x)
    print("\rBackground - " + '100' + "%")
    t.update()

def midground () :
    moveT(0,-390)
    t.pencolor('black')
    xcord = 0
    ycord = -390
    b = 0
    g = 800
    for x in range(0,g) :
        t.forward(x)
        t.right(90)
        f = x / 8
        print("\rMidground - " + str(f) + "%", end='')
        b = b +1
        if b==4 :
            xcord = xcord -2
            ycord = ycord +4
            moveT(xcord,ycord)
            b = 0
    print("\rMidground - " + '100' + "%")
    t.update()


def foreground () :
    xcord = 0
    ycord = -390
    moveT(0,-390)
    t.pencolor("white")
    h = 0
    for x in range(0,41) :
        t.forward(x*20)
        xcord = xcord -10
        ycord = ycord +3
        moveT(xcord,ycord)
        h = h+1
        f = h/2.68
        print("\rForeground - " + str(f) + "%", end='')
    for x in range(41,0,-1) :
        t.forward(x*20)
        xcord = xcord +10
        ycord = ycord +3
        moveT(xcord,ycord)
        h=h+1
        f = h/2.68
        print("\rForeground - " + str(f) + "%", end='')
    for x in range(0,41) :
        t.forward(x*20)
        xcord = xcord -10
        ycord = ycord +3
        moveT(xcord,ycord)
        h=h+1
        f = h/2.68
        print("\rForeground - " + str(f) + "%", end='')
    for x in range(41,0,-1) :
        t.forward(x*20)
        xcord = xcord +10
        ycord = ycord +3
        moveT(xcord,ycord)
        h=h+1
        f = h/2.68
        print("\rForeground - " + str(f) + "%", end='')
    for x in range(0,41) :
        t.forward(x*20)
        xcord = xcord -10
        ycord = ycord +3
        moveT(xcord,ycord)
        h=h+1
        f = h/2.68
        print("\rForeground - " + str(f) + "%", end='')
    for x in range(41,0,-1) :
        t.forward(x*20)
        xcord = xcord +10
        ycord = ycord +3
        moveT(xcord,ycord)
        h=h+1
        f = h/2.68
        print("\rForeground - " + str(f) + "%", end='')
    for x in range(0,22) :
        t.forward(x*20)
        xcord = xcord -10
        ycord = ycord +3
        moveT(xcord,ycord)
        h=h+1
        f = h/2.68
        print("\rForeground - " + str(f) + "%", end='')
    print("\rForeground - " + '100' + "%")
    t.update()

def someground () :
    moveT(0,-425)
    t.pensize(50)
    t.left(90)
    t.color("black")
    for x in range(0,1740) :
        d = x / 17.4
        print("\rSomeground - " + str(d) + "%", end='')
        t.forward(1)
        if x==870 :
            t.right(90)
            moveT(-425,0)
        g = x%3
        if g==1 :
            t.color("black")
        elif g==2 :
            t.color("white")
        else :
            randcolor ()
    moveT(0,0)
    t.color("black")
    t.forward(0.1)
    print("\rSomeground - " + '100' + "%")
    t.update()

def ros () :
    moveT(0,0)
    t.pensize(1)
    t.pencolor("black")
    for x in range(0,(360)) :
        moveT(0,0)
        randcolor ()
        t.circle(randint(25,300))
        t.right(3)
    print("Trippy part - 100%")
    t.update()

def tros () :
    moveT(0,0)
    t.pencolor("black")
    for x in range(0,360) :
        moveT(0,0)
        t.circle(300)
        t.right(3)
    print("Other part - 100%")
    t.update()


#=================================================================================================================

def randback () :
    b = randint(1,245)
    c = randint(1,245)
    d = randint(1,245)
    tup = (b, c, d)
    t.colormode(255)
    t.bgcolor(tup)

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

#=================================================================================================================

main ()
