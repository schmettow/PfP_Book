import pygame
import sys
from time import time
from pygame.locals import *
import random
from pygame.compat import unichr_, unicode_

##### VARIABLES #####
# Colors

col_black = (0, 0, 0)
col_green = (0, 255, 0)
col_green_dim = (0, 60, 0)
BACKGR_COL = col_black

SURF_SIZE = (500, 500)

pygame.init()
pygame.display.set_mode(SURF_SIZE)
pygame.display.set_caption("Mouse events")

surf = pygame.display.get_surface()
surf.fill(BACKGR_COL)
font = pygame.font.Font(None, 160)

# STATE == "move"

def main():
    while True:
        #surf.fill(BACKGR_COL)        
 
#        for event in pygame.event.get():
#            if event.type == MOUSEMOTION:
#                pass
#            if event.type == MOUSEBUTTONDOWN:
#                STATE = "paint"
#            if event.type == MOUSEBUTTONUP:
#                STATE = "move"
#            if event.type == QUIT:
#                STATE = "quit"
#                pygame.quit()
#                sys.exit()

        #  Presentitionals
        #if STATE == paint:
        if pygame.mouse.get_pressed()[0]:
            position = pygame.mouse.get_pos()
            pygame.draw.circle(surf, (255, 255, 255), 
                               (position[0],position[1]), 
                               8, 2)

        pygame.display.update()
 
main()


