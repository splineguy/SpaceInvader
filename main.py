import pygame

# Initialize the pygame
pygame.init()  # ALWAYS INCLUDE IN PYGAME

# Create the screen
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Space Invaders")
icon = pygame.image.load("ufo.png")
pygame.display.set_icon(icon)


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # RGB - Red, Green Blue
    screen.fill((255, 0, 0))
    pygame.display.update()  # ALWAYS INCLUDE IN PYGAME
