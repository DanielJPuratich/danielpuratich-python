import pygame as p
from random import randint
import time as t

clock = p.time.Clock()
p.init()
screen = p.display.set_mode([800, 600])

def baseLoop () :
    t = 'True'
    white = (255,255,255)
    black = (0,0,0)
    x = 350
    y = 578
    w = 100
    h = 20

    while t=='True':
            ms = clock.tick(100)
            screen.fill(black)
            p.draw.rect(screen, white, (x,y,w,h), 0)
            p.display.update()
            for event in p.event.get():
                if event.type == p.QUIT:
                    t = 'False'
            if event.type == p.KEYDOWN:
                    if event.key == p.K_LEFT:
                        if x>=2 :
                            x -= ms / 2
                    if event.key == p.K_RIGHT:
                        if x<=698 :
                            x += ms / 2
            #Add system to detect hitting a brick, and when brick hit, downgrading it to "lower" color
            #Add win factor, when all bricks gone, a couple second break, then back to randLvl to generate another one

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
    y = 0
    red5 = (221, 11, 56)
    purple4 = (168, 11, 221)
    blue3 = (11, 53, 221)
    green2 = (11, 221, 144)
    yellow1 = (193, 221, 11)

    for row in List :
        x = 0
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
            p.draw.rect(screen, color, (x*50.5,y*26,50,25), 0 )
            x = x + 1
        y = y + 1
    p.display.update()





Menu()
p.quit()