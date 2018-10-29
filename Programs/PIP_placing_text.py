import pygame
import sys
from pygame.locals import *
from pygame.compat import unichr_, unicode_

WIDTH = 1000
HEIGHT = 800

pygame.init()
pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Drawing figures")

FONT = pygame.font.Font('freesansbold.ttf',40)

SURF = pygame.display.get_surface()
SURF.fill((0,0,0))

def main():
    while True:
        SURF.fill((0,0,0))
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
        
        draw_text(x = 0, y = 0, text = "Pygame says:")
        draw_textbox(x = WIDTH/2, y = HEIGHT/2,
                     width = WIDTH/2, height = HEIGHT/2,
                     text = "Hi there!", 
                  center = True)
        
        pygame.display.update()


def draw_text(x, y, text,
              color = (255, 255, 255),
              center = False):
    rendered_text = FONT.render(text, True, color)
    # retrieving teh abstract rectangle of the text box
    box = rendered_text.get_rect()
    # this sets the x and why coordinates
    if center:
        box.center = (x,y)
    else:
        box.topleft = (x,y)
    # This puts a pre-rendered object to the screen
    SURF.blit(rendered_text, box)
    
def draw_textbox(x, y, width, height, text,
              color = (255, 255, 255),
              center = False):
    rendered_text = FONT.render(text, True, color)
    rendered_text = pygame.transform.smoothscale(rendered_text, (width, height))
    # retrieving teh abstract rectangle of the text box
    box = rendered_text.get_rect()
    # this sets the x and why coordinates
    if center:
        box.center = (x,y)
    else:
        box.topleft = (x,y)
    # This puts a pre-rendered object to the screen
    SURF.blit(rendered_text, box)
 
main()


