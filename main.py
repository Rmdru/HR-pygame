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

# create background
background = pygame.Surface(screen.get_size())
background = background.convert()

# The number/amount of stars on the (background) screen
N = 200

# create N stars randomly on the background
stars = [[random.randint(0, screen_width), random.randint(0, screen_height)]
        for x in range(N)]

def main():
    # main loop
    clock = pygame.time.Clock()
    while 1:
        clock.tick(22)
        for event in pygame.event.get():
            if event.type == QUIT:
                return
            elif event.type == KEYDOWN and event.key == K_ESCAPE:
                return
        background.fill((0, 0, 0))
        for star in stars:
            pygame.draw.line(background,
                             (255, 255, 255), (star[0], star[1]), (star[0], star[1]))
            star[0] = star[0] - 1
            if star[0] < 0:
                star[0] = screen_width
                star[1] = random.randint(0, screen_height)
        screen.blit(background, (0, 0))
        pygame.display.flip()