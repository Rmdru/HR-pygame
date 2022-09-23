#imports
import pygame

#initializing pygame
pygame.init()

#vars
SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720
BACKGROUND_COLOR = (0, 0, 0)

#application window name
pygame.display.set_caption("Werkplaats 1: PyGame Nohtyp")

#set application window size
canvas = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

#application window icon
logo = pygame.image.load("img/RuimteschipLogo.png").convert_alpha()
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

    canvas.blit(logo, logo_rect)

    pygame.display.flip()