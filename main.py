import pygame

# Initialize the pygame
pygame.init()  # ALWAYS INCLUDE IN PYGAME

# Create the screen
screen = pygame.display.set_mode((800, 600))

# Window Title and Icon
pygame.display.set_caption("Space Invaders")
icon = pygame.image.load("ufo.png")
pygame.display.set_icon(icon)

# Player
playerImg = pygame.image.load('player.png')
playerX = 370
playerY = 480

def player():
    screen.blit(playerImg, (playerX, playerY))

running = True
while running:
    # RGB - Red, Green, Blue
    screen.fill((0, 0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    player()

    pygame.display.update()  # ALWAYS INCLUDE IN PYGAME
