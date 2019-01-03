import pygame as pg
from base_game import BaseGame

class Shapes(BaseGame):

    # Properties
    speed = 0 # px per second
    back_color = (0, 0, 0)
    line_color = (255, 255, 255)
    size = 100
    the_surface = pg.image.load("square.png")

    # make transparent
    # color_key = the_surface.get_at((0,0))
    # the_surface.set_colorkey(color_key)

    # draw rect into surface
    the_rect = the_surface.get_rect()
    the_rect.left = 0
    the_rect.top = 0

    def on_init(self):
        self.speed = 5.0 / self.fps

    def on_update(self, elapsed_time):

        delta_pos = self.speed * elapsed_time
        self.the_rect.left += delta_pos
        self.the_rect.top += delta_pos

        if self.the_rect.right > self.screen_rect.right:
            self.the_rect.right = 0
        if self.the_rect.top > self.screen_rect.bottom:
            self.the_rect.top = 0

    def on_draw(self):
        self.screen.fill((0, 0, 0))
        self.screen.blit(self.the_surface, self.the_rect)
        pg.display.flip()

if __name__ == "__main__":
    Shapes().start()
