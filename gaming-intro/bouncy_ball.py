import pygame, random

# Start PyGame system
pygame.init()

# Create a screen with dimensions
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode([screen_width, screen_height])

# Helper variables
is_running = True
GREEN = (0, 255, 0)
radius = 50

# Pick random position
position_x = random.randint(0, screen_width)
position_y = random.randint(0, screen_height)
v_x = 10
v_y = 10

while is_running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            is_running = False

    # Check position
    if ((position_x + radius) > screen_width) or ((position_x - radius) < 0):
        v_x = v_x * -1

    if ((position_y + radius) > screen_height) or ((position_y - radius) < 0):
        v_y = v_y * -1

    position_x = position_x + v_x
    position_y = position_y + v_y

    screen.fill((0,0,0))
    pygame.draw.circle(screen, GREEN, (position_x, position_y), radius)
    pygame.display.update()

pygame.quit()
