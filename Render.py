import pygame

def renderText(color, font, pos, fontSize, text, display):
    newFont = pygame.font.SysFont(font, fontSize)
    textSurface = newFont.render(text, True, color)
    display.blit(textSurface, pos)

def renderCircle(color, pos, radius, display):
    pygame.draw.circle(display, color, (int(pos[0]), int(pos[1])), radius)

def renderRect(color, pos, size, display):
    pygame.draw.rect(display, color, pygame.Rect(int(pos[0]), int(pos[1]), int(size[0]), int(size[1])))
