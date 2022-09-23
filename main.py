#imports
import pygame
#import random
import random

#initializing pygame
pygame.init()

#vars
SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720
BACKGROUND_COLOR = (0, 0, 0)
TARGET_AMOUNT = 5
TARGET_SPEED = 10
TARGET_SPAWN_INTERVAL = 1000

#application window name
pygame.display.set_caption("Werkplaats 1: PyGame Nohtyp")

#set application window size
canvas = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

#function to check if user has requested to quit game
def quit_game_requested():
    halting = False
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            halting = True
            break
    return halting

#spawn targets
for i in range(TARGET_AMOUNT):
    color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    spawn_area_width = SCREEN_WIDTH / 2
    pygame.draw.rect(canvas, color, pygame.Rect(random.randint(spawn_area_width, SCREEN_WIDTH - 50), random.randint(0, SCREEN_HEIGHT - 50), 50, 50))
    pygame.display.flip()

#loop that runs every frame
while not quit_game_requested():
    #bg color
    canvas.fill(BACKGROUND_COLOR)

    #update the display
    # pygame.display.flip()