import pygame
import sys
from pygame.locals import *
from pygame.compat import unichr_, unicode_

pygame.init()
width = 1000
height = 800

pygame.display.set_mode((width, height))
pygame.display.set_caption("Drawing figures")

screen = pygame.display.get_surface()
screen.fill((0,0,0))

def main():
    while True:
        screen.fill((0,0,0))
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
        
        draw_circ(250, 200, 200, (255, 255, 255), 5)
        draw_circ(250, 200, 150, (255, 255, 255), 20)
        draw_circ(250, 650, 100, (255, 0, 0), 0)
        
        draw_rect(500, 50, 400, 600, (0, 0, 255), 0)
        draw_rect(500, 50, 200, 200, (0, 255, 0), 10)
        
        draw_tria(250, 200, 250, 650, 500, 50)
        
        pygame.display.update()


def draw_circ(x, y, radius, 
                color = (255,255,255), 
                stroke_size = 1):
    pygame.draw.circle(screen, color, 
                       (x,y), radius, stroke_size)

def draw_rect(x, y, 
              width, height, 
              color = (255,255,255), 
              stroke_size = 1):
    pygame.draw.rect(screen, color, (x, y, width, height), stroke_size)
    pass

def draw_tria(x_1, y_1, 
                  x_2, y_2,
                  x_3, y_3, color = (255,255,255), 
                  stroke_size = 1):
    points = ((x_1, y_1), (x_2, y_2), (x_3, y_3))
    pygame.draw.polygon(screen, color, points, stroke_size)
    pass


main()


