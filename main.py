import pygame
import os

current_path = os.path.dirname(__file__)
resource_path = os.path.join(current_path, 'resources')

pygame.init()

screen = pygame.display.set_mode((800, 600))

# Title and Icon
pygame.display.set_caption("Space Invadors")
icon = pygame.image.load(os.path.join(resource_path, 'ufo.png'))
pygame.display.set_icon(icon)

playerImg = pygame.image.load(os.path.join(resource_path, 'space-invaders.png'))
playerX = 370
playerY = 480
playerX_change = 0.0
playerY_change = 0.0


def player(x, y):
    screen.blit(playerImg, (x, y))


running = True

while running:

    screen.fill((0, 0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_change = -0.3
            if event.key == pygame.K_RIGHT:
                playerX_change = 0.3
            if event.key == pygame.K_UP:
                playerY_change = -0.3
            if event.key == pygame.K_DOWN:
                playerY_change = 0.3
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP or event.key == pygame.K_DOWN or pygame.K_LEFT or pygame.K_RIGHT:
                playerY_change = 0.0
                playerX_change = 0.0

    playerX += playerX_change
    playerY += playerY_change

    player(playerX, playerY)

    pygame.display.update()
