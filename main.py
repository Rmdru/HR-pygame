# Import libraries
import random
import pygame
from pygame.locals import *

# initializing pygame
pygame.init()

# vars
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
TARGET_AMOUNT = 5
TARGET_SPEED = [-5, 0]
TARGET_SIZE = 50
TARGET_SPAWN_AREA_WIDTH = 0.5
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
DARK_GREEN = (0, 200, 0)
LIGHT_GREEN = (0, 255, 0)
GAME_SPEED = 60

# application window name
pygame.display.set_caption("Werkplaats 1: PyGame Nohtyp")

# set application window size
canvas = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# set application window icon
logo = pygame.image.load("RuimteschipLogo.png")
pygame.display.set_icon(logo)

# start pygame clock
clock = pygame.time.Clock()

# function to check if user has requested to quit game
def quit_game_requested():
    halting = False
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            halting = True
            break
    return halting

# Determine functions and execute them
def text_settings(text, lettertype_font):
    text_display = lettertype_font.render(text, True, BLACK)
    return text_display, text_display.get_rect()

def game_loop():
    # create background
    background = pygame.Surface(canvas.get_size())
    background = background.convert()

    # The number/amount of stars on the (background) screen
    STARS_AMOUNT = 200

    # create N stars randomly on the background
    stars = [[random.randint(0, SCREEN_WIDTH), random.randint(0, SCREEN_HEIGHT)]
            for x in range(STARS_AMOUNT)]

    #generate target surfaces
    targets_surface = []
    targets_color = []
    for i in range(TARGET_AMOUNT):
        target_color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        spawn_area_width = SCREEN_WIDTH * TARGET_SPAWN_AREA_WIDTH
        target_surface = pygame.Rect(pygame.Rect(random.randint(spawn_area_width, SCREEN_WIDTH - TARGET_SIZE), random.randint(0, SCREEN_HEIGHT - TARGET_SIZE), TARGET_SIZE, TARGET_SIZE))
        targets_surface.append(target_surface)
        targets_color.append(target_color)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        background.fill((0, 0, 0))
        for star in stars:
            pygame.draw.line(background,
                             (255, 255, 255), (star[0], star[1]), (star[0], star[1]))
            star[0] = star[0] - 1
            if star[0] < 0:
                star[0] = SCREEN_WIDTH
                star[1] = random.randint(0, SCREEN_HEIGHT)

        canvas.blit(background, (0, 0))

        #loop through target surfaces to draw them on the canvas
        for index, item in enumerate(targets_surface):
            item.move_ip(TARGET_SPEED)
            pygame.draw.rect(canvas, targets_color[index], item)

        pygame.display.update()
        clock.tick(GAME_SPEED)

def startbutton(message, x, y, width, height, inactivecolour, activecolour, action=None):
    mouse = pygame.mouse.get_pos()
    mouse_click = pygame.mouse.get_pressed()

    if x + width > mouse[0] > x and y + height > mouse[1] > y:
        pygame.draw.rect(canvas, activecolour, (x, y, width, height))
        if mouse_click[0] == 1 and action != None:
            if action == "play":
                game_loop()
    else:
        pygame.draw.rect(canvas, inactivecolour, (x, y, width, height))

    text_in_small_letters = pygame.font.Font("freesansbold.ttf", 40)
    text_appearence_outsidelook, textRect = text_settings(message, text_in_small_letters)
    textRect.center = ((x + (width / 2)), (y + (height / 2)))
    canvas.blit(text_appearence_outsidelook, textRect)

while not quit_game_requested():
    #bg color
    canvas.fill(WHITE)

    text_in_capital_letters = pygame.font.Font('freesansbold.ttf', 95)
    text_appearance_outsidelook, TextRect = text_settings("Space Shooter", text_in_capital_letters)
    TextRect.center = ((SCREEN_WIDTH / 2), (SCREEN_HEIGHT / 2))
    canvas.blit(text_appearance_outsidelook, TextRect)

    startbutton("Play!!!", 290, 380, 200, 100, DARK_GREEN, LIGHT_GREEN, "play")

    #update the display
    pygame.display.flip()

    #wait for next clock tick
    clock.tick(GAME_SPEED)