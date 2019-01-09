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
        for event in p.event.get():
            if event.type == p.QUIT:
                t = 'False'


def randLvl () :
    p.display.update()






Menu()
#baseLoop()
p.quit()
