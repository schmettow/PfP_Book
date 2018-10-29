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

SCREEN_SIZE = (500, 500)

pygame.init()
pygame.display.set_mode(SCREEN_SIZE)
pygame.display.set_caption("Mouse events")

screen = pygame.display.get_surface()
screen.fill(BACKGR_COL)
font = pygame.font.Font(None, 160)


def main():
    STATE = "move"
    mousex = 0
    mousey = 0

    while True:
        screen.fill(BACKGR_COL)        
        for event in pygame.event.get():                        
            # IT
            if event.type == QUIT:
                STATE = "quit"
                break
            if STATE == "move":
                if event.type == MOUSEMOTION: # mouse moved, new pointer position is stored
                    mousex = event.pos[0]
                    mousey = event.pos[1]
                if event.type == MOUSEBUTTONDOWN: # left mouse button clicked
                    STATE = "hold"
                    time_when_clicked = time() # we want to "unclick" after some time
                continue
            if STATE == "hold":
                if event.type == MOUSEBUTTONUP: # left mouse button released
                    STATE = "move"
                continue

        #  Presentitionals
        if STATE == "hold":
            draw(mousex, mousey, True)
        
        if STATE == "move":
           draw(mousex, mousey, False)
            
        if STATE == "quit":
            print("Bye bye")
            pygame.quit()
            sys.exit() 
        
        pygame.display.update()

def draw(posx, posy, clicked):
    if clicked:
        color = col_green
    else:
        color = col_green_dim
    text_surface = font.render(str(int(posx)) + ':' + str(int(posy)), True, color, BACKGR_COL)
    text_rectangle = text_surface.get_rect()
    text_rectangle.center = (SCREEN_SIZE[0]/2.0,SCREEN_SIZE[1]/2.0)
    screen.blit(text_surface, text_rectangle)

main()


