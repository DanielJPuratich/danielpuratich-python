import pygame, math
from pygame.locals import *
import random
from base_game import BaseGame

class Bouncy(BaseGame):

    COLOR_KEY = "color"
    POSITION_KEY = "position"
    VELOCITY_KEY = "velocity"
    RADIUS_KEY = "radius"
    X_KEY = "x"
    Y_KEY = "y"
    VX_KEY = "vx"
    VY_KEY = "vy"

    def __init__(self, ball_count=1, collisions=False, width=800, height=600, fps=60):
        self.ball_count = ball_count
        self.balls = []
        self.collisions = collisions
        super().__init__(width, height, fps)

    # Overrides
    def on_init(self):
        for index in range(0, self.ball_count):
            ball = self.random_ball()
            self.balls.append(ball)

    def on_update(self, elapsed_time):
        for ball in self.balls:
            x = ball[Bouncy.POSITION_KEY][Bouncy.X_KEY]
            y = ball[Bouncy.POSITION_KEY][Bouncy.Y_KEY]
            radius = ball[Bouncy.POSITION_KEY][Bouncy.RADIUS_KEY]
            vx = ball[Bouncy.VELOCITY_KEY][Bouncy.VX_KEY]
            vy = ball[Bouncy.VELOCITY_KEY][Bouncy.VY_KEY]

            # flip x
            if x <= radius or x >= (self.width - radius):
                vx *= -1
                ball[Bouncy.VELOCITY_KEY][Bouncy.VX_KEY] = vx

            # flip y
            if y <= radius or y >= (self.height - radius):
                vy *= -1
                ball[Bouncy.VELOCITY_KEY][Bouncy.VY_KEY] = vy

            # update position
            ball[Bouncy.POSITION_KEY][Bouncy.X_KEY] += vx
            ball[Bouncy.POSITION_KEY][Bouncy.Y_KEY] += vy

    def on_draw(self):
        self.screen.fill((0, 0, 0))

        for ball in self.balls:
            x = ball[Bouncy.POSITION_KEY][Bouncy.X_KEY]
            y = ball[Bouncy.POSITION_KEY][Bouncy.Y_KEY]
            radius = ball[Bouncy.POSITION_KEY][Bouncy.RADIUS_KEY]
            color = ball[Bouncy.COLOR_KEY]
            pygame.draw.circle(self.screen, color, (x, y), radius)

        pygame.display.flip()

    def on_event(self, event):
        if event.type == KEYDOWN:
            if (event.key == K_ESCAPE) or (event.key == K_q):
                self.stop()

    def on_exit(self):
        print("On Exit Called...")

    def random_velocity(self):
        vx = (1 if ((random.randint(0, 100) % 2) == 0) else -1) * random.randint(2, 10)
        vy = (1 if ((random.randint(0, 100) % 2) == 0) else -1) * random.randint(2, 10)
        return {Bouncy.VX_KEY: vx, Bouncy.VY_KEY: vy}

    def random_radius(self):
        return random.randint(2, 20)

    def random_ball(self):
        return {
            Bouncy.COLOR_KEY: self.random_color(),
            Bouncy.POSITION_KEY: self.random_position(),
            Bouncy.VELOCITY_KEY: self.random_velocity()
        }

    def random_position(self):

        radius = self.random_radius()
        x = random.randint(radius, self.width - radius)
        y = random.randint(radius, self.height - radius)

        return {Bouncy.X_KEY: x, Bouncy.Y_KEY: y, Bouncy.RADIUS_KEY: radius}

    def random_color(self):
        max_color = 255
        red = random.randint(0, max_color)
        green = random.randint(0, max_color)
        blue = random.randint(0, max_color)

        return pygame.Color(red, green, blue, 128)

if __name__ == "__main__":
    Bouncy(100).start()