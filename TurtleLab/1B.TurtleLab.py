import turtle as t


def main () :
    t.setup(width=800 , height=800)
    t.title("Turtle Graphics - turtleIntro")
    t.bgcolor("#1de047")
    t.hideturtle()
    t.speed(0)
    inputinfo ()
    circle ()
    t.exitonclick ()

def inputinfo () :
    c = input ('Input a color to draw with - ')
    l = int(input('Input the length in pixels of each side - '))
    n = int(input('Input the nunmber of sides for your polygon - '))
    if n<=2 :
        error()
    something (c , l , n)


def something (c , l , n) :
    t.pencolor(c)
    t.penup()
    b = (l / -2)
    c = (l / 2)
    t.setpos(b , c)
    t.pendown ()
    a = 360 / n
    for x in range(0,n) :
        t.forward(l)
        t. right(a)

def circle () :
    t.penup()
    t.setpos(-300,-300)
    t.pendown()
    t.circle(50)

def error () :
    p = input('You cant have polygon with 2 or less sides')

main ()
