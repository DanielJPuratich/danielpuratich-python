
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
            ms = clock.tick(60)
            p.display.update()
            screen.fill(black)
            p.draw.rect(screen, white, (x,y,w,h), 0)
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

#def Menu () :
    #black = (0,0,0)
    #t = 'True'
    #Add some sort of "Super breakout logo and some sot of "start" button
    #while t=='True' :
        #add system to detect click of start button, and if its detected go to rand lvl func

#def randLvl () :
    #In here generate random placement for bricks, random brick levels aka colors





#Menu()
baseLoop()
p.quit()
