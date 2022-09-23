#imports
import pygame

#initializing pygame
pygame.init()

#vars
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 400
BACKGROUND_COLOR = (0, 0, 0)

#application window name
pygame.display.set_caption("Werkplaats 1: PyGame Nohtyp")

#set application window size
canvas = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

logo = pygame.image.load("images/RuimteschipLogo.png").convert_alpha()
logo_rect = logo.get_rect()

#function to check if user has requested to quit game
def quit_game_requested():
    halting = False
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            halting = True
            break
    return halting

#loop that runs every frame
while not quit_game_requested():
    #bg color
    canvas.fill(BACKGROUND_COLOR)