#This doesn't work - Has the basis for a game - collision checks between shapes - level generation - main menu (Idea was for super breakout, this code could be useful in numerous different projects)
import pygame as p
from random import randint
import math
import time as t

clock = p.time.Clock()
p.init()
screen = p.display.set_mode([800, 600])
#====================================================================================================================================
def baseLoop (List,count) :
    t = 'True'
    white = (255,255,255)
    black = (0,0,0)
    x1 = 350
    y1 = 578
    w = 100
    h = 20
    move_right = False
    move_left = False
    red5 = (221, 11, 56)
    purple4 = (168, 11, 221)
    blue3 = (11, 53, 221)
    green2 = (11, 221, 144)
    yellow1 = (193, 221, 11)

    while t=='True':
            ms = clock.tick(60)
            mouse = p.mouse.get_pos()
            screen.fill(black)
            drawBlocks(List)
            p.draw.circle(screen, red5, mouse, 20)  #temporary to check if my collision code works
            p.draw.rect(screen, white, (x1,y1,w,h), 0)
            p.display.update()
            for event in p.event.get():
                if event.type == p.QUIT:
                    t = 'False'
                if event.type == p.KEYDOWN:
                    if event.key == p.K_RIGHT:
                        move_right = True
                    if event.key == p.K_LEFT:
                        move_left = True
                if event.type == p.KEYUP:
                    if event.key == p.K_RIGHT:
                        move_right = False
                    if event.key == p.K_LEFT:
                        move_left = False
            if move_right==True :
                if x1<=698 :
                    x1 = x1 + (ms/2)
            if move_left==True :
                if x1>=2 :
                    x1 = x1 - (ms/2)
            cx = mouse[0]
            cy = mouse[1]
            cr = 20
            rx = x1
            ry = y1
            rw = w
            rh = h
            isCircleRectangleCollision(cx,cy,cr, rx,ry,rw,rh)    #This code works till angle is zero between circle and rectangle - causes code to break
            #Add ball that bounces, and does damage
            #Add system to detect hitting a brick, and when brick hit, downgrading it to "lower" color
            #Add win factor, when all bricks gone, a couple second break, then back to randLvl to generate another one
#====================================================================================================================================
def Menu () :
    black = (0,0,0)
    t = 'True'
    start = p.image.load('menu.jpg')
    button = p.image.load('star.jpg')
    screen.blit(start,(200,75))
    screen.blit(button,(75,385))
    p.display.update()
    while t=='True' :
        mousex, mousey = p.mouse.get_pos()
        #print (str(mousex) + '  ' + str(mousey))       #un comment this to check x and y values of button if asst is changed
        pressed1, pressed2, pressed3 = p.mouse.get_pressed()
        if mousex >= 135 and mousex <= 615 and mousey >= 435 and mousey <= 595 and pressed1:
            screen.fill(black)
            p.display.update()
            randLvl()
            for x in range(0,100000) :
                p.display.update()
        for event in p.event.get():
            if event.type == p.QUIT:
                t = 'False'
#==================================================================================================================================================================================
def randLvl () :
    black = (0,0,0)
    screen.fill(black)
    p.display.update()

    count = randint(1,5)
    if count >= 1 :
        Row1 = [randint(1,5),randint(1,5),randint(1,5),randint(1,5),randint(1,5),randint(1,5),randint(1,5),randint(1,5),randint(1,5),randint(1,5)]
        List = [Row1]
        if count >= 2 :
            Row2 = [randint(1,5),randint(1,5),randint(1,5),randint(1,5),randint(1,5),randint(1,5),randint(1,5),randint(1,5),randint(1,5),randint(1,5)]
            List = [Row1,Row2]
            if count >= 3 :
                Row3 = [randint(1,5),randint(1,5),randint(1,5),randint(1,5),randint(1,5),randint(1,5),randint(1,5),randint(1,5),randint(1,5),randint(1,5)]
                List = [Row1,Row2,Row3]
                if count >= 4 :
                    Row4 = [randint(1,5),randint(1,5),randint(1,5),randint(1,5),randint(1,5),randint(1,5),randint(1,5),randint(1,5),randint(1,5),randint(1,5)]
                    List = [Row1,Row2,Row3,Row4]
                    if count >= 5 :
                        Row5 = [randint(1,5),randint(1,5),randint(1,5),randint(1,5),randint(1,5),randint(1,5),randint(1,5),randint(1,5),randint(1,5),randint(1,5)]
                        List = [Row1,Row2,Row3,Row4,Row5]
    drawBlocks(List)
    p.display.update()
    baseLoop(List,count)
#=================================================================================================================================================================================
def drawBlocks (List) :
        y = 0
        red5 = (221, 11, 56)
        purple4 = (168, 11, 221)
        blue3 = (11, 53, 221)
        green2 = (11, 221, 144)
        yellow1 = (193, 221, 11)
        for row in List :
            x = 0.3
            for value in row :
                if value==1 :
                    color = yellow1
                elif value==2 :
                    color = green2
                elif value==3 :
                    color = blue3
                elif value==4 :
                    color = purple4
                elif value==5 :
                    color = red5
                p.draw.rect(screen, color, ((x*75),(y*25),69,20), 0 )
                x = x + 1
            y = y + 1
#====================================================================================================================================
def isCollision(x1,y1,w1,h1, x2,y2,w2,h2) :   #between 2 rects
    top1x = x1
    top1y = y1
    bot1x = x1 + w1
    bot1y = y1 + h1

    top2x = x2
    top2y = y2
    bot2x = x2 + w2
    bot2y = y2 + h2

    if top1x==top2x or top1x==bot2x or bot1x==top2x or bot1x==bot2x :
        print('Xs equal')
        if top1y==top2y or top1y==bot2y or bot1y==top2y or bot1y==bot2y :
            print('Xs and Ys equal')
            return True
    return False
#=======================================================================================
def isCircleCollision(x1,y1,r1, x2,y2,r2) :   #between 2 circles
    rt = r1 + r2
    xc = abs(x1 - x2)
    yc = abs(y1 - y2)
    ch = math.sqrt(math.pow(xc, 2) + math.pow(yc,2))
    if rt<=ch :
        return True
    else :
        return False
#======================================================================================
def isCircleRectangleCollision(cx,cy,cr, rx,ry,rw,rh) :      #between 1 rect and 1 circle
    RectCenterX = rx + (rw / 2)
    RectCenterY = ry + (rh / 2)
    changeX = abs(cx - RectCenterX)
    changeY = abs(cy - RectCenterY)
    changex = (cx - RectCenterX)
    changey = (cy - RectCenterY)
    dirX = cx - RectCenterX
    dirY = cy - RectCenterY
    xpos = False
    ypos = False
    if dirX>=0 :
        xpos = True
    if dirY>=0 :
        ypos = True
    majorHypot = math.sqrt(math.pow(changeX , 2) + math.pow(changeY ,2))
    neededInRect = majorHypot - cr
    theta = math.degrees(math.acos( (math.pow(changeX,2) + math.pow(majorHypot,2) - math.pow(changeY,2)) / ( 2 * changeX * majorHypot)))      #A = changeY  B = changeX   C = majorHypot - law of cosines
    print(theta)
    if changeY <= changeX :
        smallX = rw / 2
        insideRect = (smallX) /  (math.degrees(math.cos(theta)))
    elif changeY >= changeX :
        smallY = rh / 2
        insideRect = (smallY) / (math.degrees(math.sin(theta)))
    elif changeY == changeX :
        if rw >= rh :
            smallY = rh / 2
            insideRect = (smallY) / (math.degrees(math.sin(theta)))
        elif rw <= rh :
            smallX = rw / 2
            insideRect = (smallX) /  (math.degrees(math.cos(theta)))
        elif rw == rh :
            smallX = rw/2
            #both ways, small x small y and sin or cosine is functional here
            insideRect = (smallX) /  (math.degrees(math.cos(theta)))
    else :
        print('error in calc collision')
    if neededInRect<=insideRect :
        return True
    else :
        return False
#================================================================================================================================
Menu()
p.quit()
