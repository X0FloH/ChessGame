import pygame

displaySize = (1000, 900)

pygame.init()

pygame.display.set_caption('Chess Networked V0.1')

display = pygame.display.set_mode(displaySize)

running = True

while running:
    display.fill((0, 0, 0))

    pygame.display.update()
