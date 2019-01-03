import pygame, sys, math


class BaseGame:
    def __init__(self, width=800, height=600, fps=60):

        self.width = width
        self.height = height
        self.fps = fps
        self.running = False
        self.screen_rect = pygame.Rect(0, 0, self.width, self.height)

        pygame.init()
        self.screen = pygame.display.set_mode((self.width, self.height), pygame.DOUBLEBUF)
        self.clock = pygame.time.Clock()
        self.on_init()

    # Update Methods
    def on_init(self):
        pass

    # Update game/app logic
    def on_update(self, elapsed_time):
        pass

    # Draw to screen
    def on_draw(self):
        pass

    # Handle event
    def on_event(self, event):
        pass

    # About to exit
    def on_exit(self):
        pass

    # Lifecycle
    def start(self):
        self.running = True
        self.run()

    def stop(self):
        self.running = False

    def exit_game(self):
        self.on_exit()
        pygame.quit()
        sys.exit()

    def run(self):
        while self.running:
            # Handle events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.exit_game()
                    return
                else:
                    self.on_event(event)

            # Update clock
            elapsed_time = self.clock.get_time()

            # Update Logic
            self.on_update(elapsed_time)

            # Draw
            self.on_draw()

            # Update clock
            self.clock.tick(self.fps)

            # Update display
            pygame.display.update()

        # Running set off
        self.exit_game()