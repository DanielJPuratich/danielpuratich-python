import turtle as t

def main () :
    #t.hideturtle()
    #t.speed(0)
    t.setup(width=800 , height=800)
    t.title("Turtle Graphics - turtleIntro")
    t.bgcolor("#1de047")
    line ()
    square ()
    circle ()
    triangle ()
    t.exitonclick ()

def line () :
    t.pencolor('red')
    moveT(50 , 0)
    t.left(180)
    t.forward(100)

def square () :
    t.pencolor('blue')
    moveT(100, 100)
    t.forward(200)
    t.left(90)
    t.forward(200)
    t.left(90)
    t.forward(200)
    t.left(90)
    t.forward(200)
    t.left(90)

def circle () :
    t.pencolor('purple')
    moveT(0,300)
    t.circle(300)

def triangle () :
    t.pencolor('orange')
    moveT(200,-125)
    t.forward(400)
    t.right(120)
    t.forward(400)
    t.right(120)
    t.forward(400)

def moveT (x , y) :
    t.penup ()
    t.setpos(x , y)
    t.pendown ()

main ()
