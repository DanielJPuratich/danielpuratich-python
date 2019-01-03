import pygame, math
from pygame.locals import *
from random import randrange
from base_game import BaseGame


class Stars(BaseGame):

    def __init__(self, num_stars, max_depth, width=800, height=600, fps=60):
        self.num_stars = num_stars
        self.max_depth = max_depth
        super().__init__(width, height, fps)

    # Overrides
    def on_init(self):
        self.init_stars()

    def on_update(self, elapsed_time):
        self.move_stars()

    def on_draw(self):
        self.screen.fill((0, 0, 0))
        self.draw_stars()
        pygame.display.flip()

    def on_event(self, event):
        if event.type == KEYDOWN:
            if (event.key == K_ESCAPE) or (event.key == K_q):
                self.stop()

    def on_exit(self):
        print("On Exit Called...")

    def init_stars(self):
        """ Create the starfield """
        self.stars = []
        for i in range(self.num_stars):
            # A star is represented as a list with this format: [X,Y,Z]
            star = [randrange(-25, 25), randrange(-25, 25), randrange(1, self.max_depth)]
            self.stars.append(star)

    def move_stars(self):
        for star in self.stars:
            # The Z component is decreased on each frame.
            star[2] -= 0.19

            # If the star has past the screen (I mean Z<=0) then we
            # reposition it far away from the screen (Z=max_depth)
            # with random X and Y coordinates.
            if star[2] <= 0:
                star[0] = randrange(-25, 25)
                star[1] = randrange(-25, 25)
                star[2] = self.max_depth

    def draw_stars(self):
        origin_x = self.screen.get_width() / 2
        origin_y = self.screen.get_height() / 2

        for star in self.stars:
            # Convert the 3D coordinates to 2D using perspective projection.
            k = 128.0 / star[2]
            x = int(star[0] * k + origin_x)
            y = int(star[1] * k + origin_y)

            # Draw the star (if it is visible in the screen).
            # We calculate the size such that distant stars are smaller than
            # closer stars. Similarly, we make sure that distant stars are
            # darker than closer stars. This is done using Linear Interpolation.
            if 0 <= x < self.screen.get_width() and 0 <= y < self.screen.get_height():
                size = (1 - float(star[2]) / self.max_depth) * 5
                shade = (1 - float(star[2]) / self.max_depth) * 255
                self.screen.fill((shade, shade, shade), (x, y, size, size))

if __name__ == "__main__":
    Stars(512, 32).start()