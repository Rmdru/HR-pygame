#import pygame
import pygame
#import random
import random

#initializing pygame
pygame.init()

#vars
GAME_SPEED = 60
SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720
BACKGROUND_COLOR = (0, 0, 0)
TARGET_AMOUNT = 5
TARGET_SPEED = [-5, 0]
TARGET_SIZE = 50
TARGET_SPAWN_AREA_WIDTH = 0.5

#application window name
pygame.display.set_caption("Werkplaats 1: PyGame Nohtyp")

#start pygame clock
clock = pygame.time.Clock()

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

#generate target surfaces
targets_surface = []
targets_color = []
for i in range(TARGET_AMOUNT):
    target_color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    spawn_area_width = SCREEN_WIDTH * TARGET_SPAWN_AREA_WIDTH
    target_surface = pygame.Rect(pygame.Rect(random.randint(spawn_area_width, SCREEN_WIDTH - TARGET_SIZE), random.randint(0, SCREEN_HEIGHT - TARGET_SIZE), TARGET_SIZE, TARGET_SIZE))
    targets_surface.append(target_surface)
    targets_color.append(target_color)

#loop that runs every frame
while not quit_game_requested():
    #bg color
    canvas.fill(BACKGROUND_COLOR)

    #loop through target surfaces to draw them on the canvas
    for index, item in enumerate(targets_surface):
        item.move_ip(TARGET_SPEED)
        pygame.draw.rect(canvas, targets_color[index], item)

    #update the display
    pygame.display.flip()

    #wait for next clock tick
    clock.tick(GAME_SPEED)