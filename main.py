# imports
import pygame

# initializing pygame
pygame.init()

# vars
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
BACKGROUND_COLOR = (0, 0, 0)
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

def startbutton(message, x, y, width, height, inactivecolour, activecolour, action=None):
    mouse = pygame.mouse.get_pos()
    mouse_click = pygame.mouse.get_pressed()

    if x + width > mouse[0] > x and y + height > mouse[1] > y:
        pygame.draw.rect(canvas, activecolour, (x, y, width, height))
    else:
        pygame.draw.rect(canvas, inactivecolour, (x, y, width, height))

    text_in_small_letters = pygame.font.Font("freesansbold.ttf", 40)
    text_appearence_outsidelook, textRect = text_settings(message, text_in_small_letters)
    textRect.center = ((x + (width / 2)), (y + (height / 2)))
    canvas.blit(text_appearence_outsidelook, textRect)

while not quit_game_requested():
    canvas.fill(WHITE)
    text_in_capital_letters = pygame.font.Font('freesansbold.ttf', 95)
    text_appearance_outsidelook, TextRect = text_settings("Space Shooter", text_in_capital_letters)
    TextRect.center = ((SCREEN_WIDTH / 2), (SCREEN_HEIGHT / 2))
    canvas.blit(text_appearance_outsidelook, TextRect)

    startbutton("Play!!!", 290, 380, 200, 100, DARK_GREEN, LIGHT_GREEN)

    pygame.display.update()
    clock.tick(GAME_SPEED)