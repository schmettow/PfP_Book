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

BACKGR_COL = col_black
SCREEN_SIZE = (500, 500)

pygame.init()
pygame.display.set_mode(SCREEN_SIZE)
pygame.display.set_caption("Mouse events")

screen = pygame.display.get_surface()
screen.fill(BACKGR_COL)

font = pygame.font.Font(None, 60)

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

        # define what the rectangle will look like
        myRect = pygame.Rect(150, 200, 200, 100) # define the location and size of your rectangle (left, top, width, height)
        myThickness = 5 # the thickness of the outer edges. If set to 0, the rectangle will be filled.         
               
        # draw the rectangle. Give four arguments (Surface, color, Rect, width)
        pygame.draw.rect(screen, col_red, myRect, myThickness)

        # draw text inside of the rectangle
        text = font.render("Hi there!", True, col_yellow)
        text_rectangle = pygame.Rect(165, 230, 200, 100)
        screen.blit(text, text_rectangle)

        # update the screen to display the changes you made
        pygame.display.update()

        

main()


