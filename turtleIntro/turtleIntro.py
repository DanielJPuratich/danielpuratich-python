import turtle as t

def mainDrawing () :
    t.hideturtle ()
    t.speed(0)
    t.setup(width=800 , height=800)
    p = t.Pen()
    c = '#268dd6'
    t.title("Turtle Graphics - turtleIntro")
    p.pencolor(c)
    drawing1 (p)
    drawing2 (p)
    drawing3 (p)
    drawing4 (p)
    drawing5 (p)
    t.exitonclick ()


def drawing1 (p) :
    #set background, drawing square in bottom right
    t.bgcolor("#1de047")
    t.pencolor('#268dd6')
    moveT(100, -100)
    t.right(90)
    for x in range(0,4) :
        t.forward(100)
        t.left(90)
    moveT (0 , 0)


def drawing2 (p) :
    #draw cirle bottom left
    moveT (-150 , -150)
    t.pencolor('#e05d1c')
    for x in range(75) :
        t.forward(5)
        t.right(5)
    moveT (0 , 0)

def drawing3 (p) :
    #make circle in top right with a fill color
    moveT(-150 , 150)
    t.pencolor("#ce06ba")
    for x in range(0,75) :
        t.forward(5)
        t.right(5)
    moveT(-210,165)
    t.pensize(125)
    t.forward(1)
    t.pensize(1)
    moveT(0,0)

def drawing4 (p) :
    #make square in top right with line color
    moveT(150,150)
    t.pencolor("#e2df0d")
    t.right(75)
    t.pensize(5)
    for x in range(150) :
        t.forward(x)
        t.left(90)
    t.pensize(1)
    moveT(0,0)

def drawing5 (p) :
    moveT(0,0)

def moveT (x , y) :
    #made this function to move the pen to cordinates without drawing
    t.penup()
    t.setpos(x , y)
    t.pendown ()

mainDrawing ()
