import pygame
import sys
from pygame.locals import *
from pygame.compat import unichr_, unicode_

WIDTH = 1000
HEIGHT = 800

pygame.init()
pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Showing pictures")

SURF = pygame.display.get_surface()
SURF.fill((0,0,0))

def main():
    while True:
        SURF.fill((0,0,0))
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
        
        draw_picture(x = WIDTH/2, y = HEIGHT/2, file = "Beach.png", 
                     center = True,
                     scale = 0.5)

        pygame.display.update()


def draw_picture(x, y, file, center = False, scale = 1):
    picture = pygame.image.load(file)
    # retrieving the box
    box = picture.get_rect()
    # transformation
    if scale != 1:
        new_width = int(box.width * scale)
        new_height = int(box.height * scale)
        picture = pygame.transform.smoothscale(picture, 
                                               (new_width, new_height))
    # getting the new box
    box = picture.get_rect()
    if center:
        box.center = (x,y)
    else:
        box.topleft = (x,y)
    SURF.blit(picture, box)

main()


