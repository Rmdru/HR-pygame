# Import libraries
import random
import pygame
from pygame.locals import *

# Ensure that the code can use the items in the Pygame library
pygame.init()

# Screen settings
screen_width = 1120
screen_height = 800

# Title bar above the screen - added title and logo
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Team nohtyp: Side scrolling shoot 'm up")
logo = pygame.image.load("RuimteschipLogo.png")
pygame.display.set_icon(logo)
