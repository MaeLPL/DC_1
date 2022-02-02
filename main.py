# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import pygame
import tcod
import os, sys
import random, time
import tcod.map

### for Imaging
import numpy as np
from PIL import Image

### pygame extras
pygame.mixer.init(22100, -16, 2, 32)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

def draw_game():

    # surface
    SURFACE_MAIN.fill((255,255,255))
    pygame.display.flip()


def game_main_loop():
    events_list = pygame.event.get()
    game_quit = False

    # player_action = "no-action"

    while not game_quit:
        # player action definition

        # handle player input



        ### process INPUT

        draw_game()
        for x in range(5):
            print (x+1)
        for event in events_list:
            if event.type == pygame.KEYDOWN:

                if event.key == pygame.K_c:
                    game_quit = True

    pygame.quit()
    exit()


def game_initialize():
    global SURFACE_MAIN
    pygame.init()

    pygame.key.set_repeat(500,70) # key repeat function (after ms, repeat every ms)

    SURFACE_MAIN = pygame.display.set_mode((800,600))

if __name__ == '__main__':


    game_initialize()

    pygame.display.set_caption('MaeLs dank dung dung')
    game_main_loop()