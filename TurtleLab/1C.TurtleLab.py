import turtle as t

def main () :
    t.setup(width=800 , height=800)
    t.title("Turtle Graphics - turtleIntro")
    t.bgcolor("#1de047")
    t.hideturtle()
    t.speed(0)
    posPos ()
    #posNeg ()
    #negNeg()
    #posNeg ()
    t.exitonclick ()

def posPos () :
    #square
    moveT(150,250)
    t.pencolor('red')
    for x in range(0,4) :
        t.forward(90)
        t.right(90)


def moveT (x , y) :
    t.penup ()
    t.setpos(x , y)
    t.pendown ()



main ()
