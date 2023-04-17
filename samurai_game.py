import pygame
from pygame import *
pygame.init()

window = pygame.display.set_mode((800, 500))
pygame.display.set_caption("Last Samurai")
window.fill((0, 0, 0))
clock = time.Clock()

class GameSprites():
    pass

some_value = True
while some_value == True:
    window.fill((0, 0, 0))

    for e in event.get():
        if e.type == QUIT:
            some_value = False

    display.update()
    clock.tick(60)