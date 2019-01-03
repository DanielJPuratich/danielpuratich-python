import pygame

# Start PyGame system
pygame.init()

# Create a screen with dimensions
screen = pygame.display.set_mode([800, 600])

# Helper variables
is_running = True
GREEN = (0, 255, 0)
radius = 50

while is_running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            is_running = False
    pygame.draw.circle(screen, GREEN, (100, 100), radius)
    pygame.display.update()

pygame.quit()
