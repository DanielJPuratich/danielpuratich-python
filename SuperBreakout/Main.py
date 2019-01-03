import pygame as p
p.init()
screen = p.display.set_mode([800, 600])

t = 'True'
white = (255,255,255)
black = (0,0,0)
x = 350
y = 578
w = 100
h = 20

while t=='True':
        p.display.update()
        p.draw.rect(screen, white, (x,y,w,h), 0)
        for event in p.event.get():
            if event.type == p.QUIT:
                t = 'False'
        if event.type == p.KEYDOWN:
                if event.key == p.K_LEFT:

                    x -= 1
                if event.key == p.K_RIGHT:
                    x += 1


p.quit()
