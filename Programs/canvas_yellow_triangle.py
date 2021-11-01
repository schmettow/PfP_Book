import pygame
import sys
from time import time
from pygame.locals import *
import random
from pygame.compat import unichr_, unicode_

##### VARIABLES #####
# Colors

col_black = (0, 0, 0)
col_gray = (120, 120, 120)
col_red = (250, 0, 0)
col_green = (0, 255, 0)
col_yellow = (250, 250, 0)

col_red_dim = (120, 0, 0)
col_green_dim = (0, 60, 0)
col_yellow_dim = (120,120,0)

BACKGR_COL = col_red
SCREEN_SIZE = (500, 500)

pygame.init()
pygame.display.set_mode(SCREEN_SIZE)
pygame.display.set_caption("Yellow triangle")

screen = pygame.display.get_surface()
screen.fill(BACKGR_COL)

font = pygame.font.Font(None, 160)

def main():
    print("Canvas size is (" + str(SCREEN_SIZE[0]) + "," + str(SCREEN_SIZE[1]) + ")")
    print("(0,0) is the upper left corner")    
    while True:
        pygame.display.get_surface().fill(BACKGR_COL)
        for event in pygame.event.get():
            # Interactive transition conditionals (ITC)

            # always include transition for quit events
            if event.type == QUIT:
                pygame.quit()
                sys.exit()        
        ## here you can draw

        # define what your triangle will look like
        myPointlist = ((200, 275), (300, 275), (250, 175)) # the three points of the triangle that will be connected
        myThickness = 0  # the thickness of the outer edges. If set to 0, the triangle will be filled. 

        # draw your triangle. Give four arguments (Surface, color, pointlist, width)
        pygame.draw.polygon(screen, col_yellow, myPointlist, myThickness)

        # update the screen to display the changes you made
        pygame.display.update()

        

main()


