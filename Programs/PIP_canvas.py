import pygame
import sys
from pygame.locals import *
from pygame.compat import unichr_, unicode_

pygame.init()
pygame.display.set_mode((600, 400))
pygame.display.set_caption("A Pygame display")

screen = pygame.display.get_surface()
screen.fill((0,0,0))

def main():
    while True:
        for event in pygame.event.get():
            # IT
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
        pygame.display.update()

main()


