# -*- coding: utf-8 -*-
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
col_pink = (250,0,127)

NTRIALS = 5

WORDS    = ("red", "green", "blue", "yellow", "pink")

COLORS   = {"red": col_red,
            "green": col_green,
            "blue": col_blue,
            "yellow": col_yellow,
            "pink": col_pink}

KEYS     = {"red": K_b,
            "green": K_n,
            "blue": K_m,
            "yellow":K_v,
            "pink":K_c}


BACKGR_COL = col_gray
SCREEN_SIZE = (700, 500)

pygame.init()
pygame.display.set_mode(SCREEN_SIZE) 
pygame.display.set_caption("Stroop Test")

screen = pygame.display.get_surface()
screen.fill(BACKGR_COL)

font = pygame.font.Font(None, 80)
font_small = pygame.font.Font(None, 40)

p_numbers = range(1,11)

conditions = {"Stroop_3":[1,2,4,8,10],
              "Stroop_5":[3,5,6,7,9]}

def main():
    """ Start the Stroop task.
    """
    ## Variables
    STATE = "welcome"
    trial_number = 0
    # initialize participant number
    p_number = 0

    # for gathering the response times
    RT = []

    while True:
        pygame.display.get_surface().fill(BACKGR_COL)        

        # Changing states by user input
        for event in pygame.event.get():
            # welcome screen --> prepare next trial (space bar)
            if STATE == "welcome":
                if event.type == KEYDOWN and event.key == K_SPACE:
                    STATE = "enter_participant_number"
                    print(STATE)

            # wait for response --> feedback (b, n, m)
            elif STATE == "wait_for_response":
                if event.type == KEYDOWN and event.key in KEYS.values():
                    # remember when the user has reacted
                    time_when_reacted = time()
                    # calculate the response time
                    this_reaction_time = time_when_reacted - time_when_presented
                    RT.append(this_reaction_time)
                    # was the response correct?
                    this_correctness = (event.key == KEYS[this_color])
                    STATE = "feedback"
                    print(STATE)
            
            elif STATE == "enter_participant_number":
                p_number = prompt()
                STATE = "transition_experiment"
                print(STATE + "\nThank you, you entered number " + str(p_number) + 
                      "\nPLEASE RETURN TO THE PYGAME WINDOW")
                
            elif STATE == "transition_experiment":
                if event.type == KEYDOWN and event.key == K_SPACE:
                    STATE = "prepare_next_trial"

            if event.type == QUIT:
                STATE = "quit"


        # automatic state transitions
        # prepare next trial --> wait for response (immediatly)
        if STATE == "prepare_next_trial":
            trial_number = trial_number + 1
            # randomly pick word and color
            # depending on condition
            if p_number in conditions["Stroop_3"]:
                this_word  = pick_color()
                this_color = pick_color()
            else:
                this_word = pick_color5()
                this_color = pick_color5()
            # remember when stimulus was presented
            time_when_presented = time()
            STATE = "wait_for_response"
            print(STATE)

        # show feedback, then advance to next trial or goodbye  (for 1s)
        if STATE == "feedback" and (time() - time_when_reacted) > 1:
            if trial_number < NTRIALS:
                STATE = "prepare_next_trial"
            else:
                STATE = "goodbye"
            print(STATE)


        # Drawing to the screen
        if STATE == "welcome":
            draw_welcome()
            draw_button(SCREEN_SIZE[0]*1/6, 450, "Pink: C", col_pink)
            draw_button(SCREEN_SIZE[0]*2/6, 450, "Yellow: V", col_yellow)
            draw_button(SCREEN_SIZE[0]*3/6, 450, "Red: B", col_red)
            draw_button(SCREEN_SIZE[0]*4/6, 450, "Green: N", col_green)
            draw_button(SCREEN_SIZE[0]*5/6, 450, "Blue: M", col_blue)
        
        if STATE == "enter_participant_number":
            draw_enter()
        
        if STATE == "transition_experiment":
            draw_transition()
            if p_number in conditions["Stroop_3"]:
                draw_button(SCREEN_SIZE[0]*1/4, 450, "Red: B", col_red)
                draw_button(SCREEN_SIZE[0]*2/4, 450, "Green: N", col_green)
                draw_button(SCREEN_SIZE[0]*3/4, 450, "Blue: M", col_blue)
            else:
                draw_button(SCREEN_SIZE[0]*1/6, 450, "Pink: C", col_pink)
                draw_button(SCREEN_SIZE[0]*2/6, 450, "Yellow: V", col_yellow)
                draw_button(SCREEN_SIZE[0]*3/6, 450, "Red: B", col_red)
                draw_button(SCREEN_SIZE[0]*4/6, 450, "Green: N", col_green)
                draw_button(SCREEN_SIZE[0]*5/6, 450, "Blue: M", col_blue)
        
        if STATE == "wait_for_response":
            draw_stimulus(this_color, this_word)
            if p_number in conditions["Stroop_3"]:
                draw_button(SCREEN_SIZE[0]*1/4, 450, "Red: B", col_red)
                draw_button(SCREEN_SIZE[0]*2/4, 450, "Green: N", col_green)
                draw_button(SCREEN_SIZE[0]*3/4, 450, "Blue: M", col_blue)
            else:
                draw_button(SCREEN_SIZE[0]*1/6, 450, "Pink: C", col_pink)
                draw_button(SCREEN_SIZE[0]*2/6, 450, "Yellow: V", col_yellow)
                draw_button(SCREEN_SIZE[0]*3/6, 450, "Red: B", col_red)
                draw_button(SCREEN_SIZE[0]*4/6, 450, "Green: N", col_green)
                draw_button(SCREEN_SIZE[0]*5/6, 450, "Blue: M", col_blue)
        
        if STATE == "feedback":
            draw_feedback(this_correctness, this_reaction_time)
        
        if STATE == "goodbye":
            draw_goodbye()
        
        if STATE == "quit":
            pygame.quit()
            sys.exit()

        pygame.display.update()

def prompt():
    p_number = 0
    while p_number == 0:
        p_number = int(raw_input("Please enter participant number here:"))
    if p_number in range(1, len(p_numbers) + 1):
        return p_number
    else:
        print "Unknown participant number, valid participant numbers are 1 to 10"
        prompt()
                    
def pick_color():
    """ Return a random word.
    """
    random_number = random.randint(0,2)
    return WORDS[random_number]

def pick_color5():
    """ Return a random word,
    5 color Stroop version
    """
    random_number = random.randint(0,4)
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
    text_surface = font_small.render("Press Spacebar to continue", True, col_black, BACKGR_COL)
    text_rectangle = text_surface.get_rect()
    text_rectangle.center = (SCREEN_SIZE[0]/2.0,300)
    screen.blit(text_surface, text_rectangle)

def draw_enter():
    text_surface = font_small.render("Please enter participant number in console", True, col_black, BACKGR_COL)
    text_rectangle = text_surface.get_rect()
    text_rectangle.center = (SCREEN_SIZE[0]/2.0,250)
    screen.blit(text_surface, text_rectangle)

def draw_transition():
    text_surface = font_small.render("Press Spacebar to start the experiment", True, col_black, BACKGR_COL)
    text_rectangle = text_surface.get_rect()
    text_rectangle.center = (SCREEN_SIZE[0]/2.0,250)
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
        #text_surface = font_small.render("Press Spacebar to continue", True, col_black, BACKGR_COL)


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



