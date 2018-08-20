import pygame
import sys
from time import time
import random
from pygame.locals import *
from pygame.compat import unichr_, unicode_

##### VARIABLES #####
# Colors
col_white = (250, 250, 250)
col_black = (0, 0, 0)
col_gray = (220, 220, 220)
col_red = (250, 0, 0)
col_green = (0, 200, 0)
col_blue = (0, 0, 250)
col_yellow = (250,250,0)

WORDS    = ("red", "green", "blue")

COLORS   = {"red": col_red,
            "green": col_green,
            "blue": col_blue}

KEYS     = {"red": K_b,
            "green": K_n,
            "blue": K_m}


BACKGR_COL = col_gray
SCREEN_SIZE = (700, 500)

pygame.init()
pygame.display.set_mode(SCREEN_SIZE) 
pygame.display.set_caption("Stroop Test")

screen = pygame.display.get_surface()
screen.fill(BACKGR_COL)

font = pygame.font.Font(None, 80)
font_small = pygame.font.Font(None, 40) 


def main():
    """ Start the Stroop task.
    """
    STATE = "welcome"    
    
    #size = font.size(text)
    
    trial_number = 0    
    
    while True:
        pygame.display.get_surface().fill(BACKGR_COL)        

        # Changing states
        for event in pygame.event.get():                        
            if STATE == "welcome":
                if event.type == KEYDOWN and event.key == K_SPACE:
                    STATE = "prepare_next_trial"
                    print(STATE)
                    
            if STATE == "prepare_next_trial":
                trial_number = trial_number + 1
                this_word  = pick_color()
                this_color = pick_color()
                time_when_presented = time()
                STATE = "wait_for_response"
                print(STATE)
                    
            if STATE == "wait_for_response":
                if event.type == KEYDOWN and event.key in KEYS.values():
                    time_when_reacted = time()
                    this_reaction_time = time_when_reacted - time_when_presented
                    this_correctness = (event.key == KEYS[this_color])
                    STATE = "feedback"
                    print(STATE)

                
            if STATE == "feedback":
                if event.type == KEYDOWN and event.key == K_SPACE:
                    if trial_number < 20:
                        STATE = "prepare_next_trial"
                    else:
                        STATE = "goodbye"
                    print(STATE)
            
            if event.type == QUIT:
                STATE = "quit"

        # Drawing to the screen
        if STATE == "welcome":
            draw_welcome()
            draw_button(SCREEN_SIZE[0]*1/5, 450, "Red: X", col_red)
            draw_button(SCREEN_SIZE[0]*3/5, 450, "Green: N", col_green)
            draw_button(SCREEN_SIZE[0]*4/5, 450, "Blue: M", col_blue)
        
        if STATE == "wait_for_response":
            draw_stimulus(this_color, this_word)
            draw_button(SCREEN_SIZE[0]*1/5, 450, "Red: X", col_red)
            draw_button(SCREEN_SIZE[0]*3/5, 450, "Green: N", col_green)
            draw_button(SCREEN_SIZE[0]*4/5, 450, "Blue: M", col_blue)
        
        if STATE == "feedback":
            draw_feedback(this_correctness, this_reaction_time)
        
        if STATE == "goodbye":
            draw_goodbye()
        
        if STATE == "quit":
            pygame.quit()
            sys.exit()

        pygame.display.update()
        
def pick_color():
    """ Return a random word.
    """
    random_number = random.randint(0,2)
    return WORDS[random_number]

def draw_button(xpos, ypos, label, color):
    text = font_small.render(label, True, color, BACKGR_COL)
    text_rectangle = text.get_rect()
    text_rectangle.center = (xpos, ypos)
    screen.blit(text, text_rectangle)

def draw_welcome():
    text_surface = font.render("STROOP Experiment", True, col_black, BACKGR_COL)
    text_rectangle = text_surface.get_rect()
    text_rectangle.center = (SCREEN_SIZE[0]/2.0,150)
    screen.blit(text_surface, text_rectangle)
    
    '''Ch1, Exercise 3'''
    #text_surface = font.render(msgText,True,msgColor,BACKGR_COL)
    #text_rectangle = text_surface.get_rect()
    #text_rectangle.center = (SCREEN_SIZE[0]/2.0,225)
    #screen.blit(text_surface,text_rectangle)
    
    text_surface = font_small.render("Press Spacebar to continue", True, col_black, BACKGR_COL)
    text_rectangle = text_surface.get_rect()
    text_rectangle.center = (SCREEN_SIZE[0]/2.0,300)
    screen.blit(text_surface, text_rectangle)

def draw_stimulus(color, word):
    text_surface = font.render(word, True, COLORS[color], col_gray)
    text_rectangle = text_surface.get_rect()
    text_rectangle.center = (SCREEN_SIZE[0]/2.0,150)
    screen.blit(text_surface, text_rectangle)

def draw_feedback(correct, reaction_time):
    if correct:
        text_surface = font_small.render("correct", True, col_black, BACKGR_COL)
        text_rectangle = text_surface.get_rect()
        text_rectangle.center = (SCREEN_SIZE[0]/2.0,150)
        screen.blit(text_surface, text_rectangle)
        text_surface = font_small.render(str(int(reaction_time * 1000)) + "ms", True, col_black, BACKGR_COL)
        text_rectangle = text_surface.get_rect()
        text_rectangle.center = (SCREEN_SIZE[0]/2.0,200)
        screen.blit(text_surface, text_rectangle)
    else:
        text_surface = font_small.render("Wrong key!", True, col_red, BACKGR_COL)
        text_rectangle = text_surface.get_rect()
        text_rectangle.center = (SCREEN_SIZE[0]/2.0,150)
        screen.blit(text_surface, text_rectangle)
    text_surface = font_small.render("Press Spacebar to continue", True, col_black, BACKGR_COL)
    text_rectangle = text_surface.get_rect()
    text_rectangle.center = (SCREEN_SIZE[0]/2.0,300)
    screen.blit(text_surface, text_rectangle)

def draw_goodbye():
    text_surface = font_small.render("END OF THE EXPERIMENT", True, col_black, BACKGR_COL)
    text_rectangle = text_surface.get_rect()
    text_rectangle.center = (SCREEN_SIZE[0]/2.0,150)
    screen.blit(text_surface, text_rectangle)
    text_surface = font_small.render("Close the application.", True, col_black, BACKGR_COL)
    text_rectangle = text_surface.get_rect()
    text_rectangle.center = (SCREEN_SIZE[0]/2.0,200)
    screen.blit(text_surface, text_rectangle)
    
main()



