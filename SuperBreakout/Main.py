
import pygame as p
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
            p.display.update()
            screen.fill(black)
            p.draw.rect(screen, white, (x,y,w,h), 0)
            for event in p.event.get():
                if event.type == p.QUIT:
                    t = 'False'
            if event.type == p.KEYDOWN:
                    if event.key == p.K_LEFT:
                        if x!=2 :
                            x -= 1
                    if event.key == p.K_RIGHT:
                        if x!=698 :
                            x += 1


baseLoop()
p.quit()
