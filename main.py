# Import the Pygame library
import pygame

# Ensure that the code can use the items in the Pygame library
pygame.init()

# Screen settings
screen_width = 800
screen_height = 600

# Colours for the screenbackground (white) and for the texts (black)
black = (0, 0, 0)
white = (255, 255, 255)

# Colours for the startbutton when you do and don't move over the button with a mouse
dark_green = (0, 200, 0)
light_green = (0, 255, 0)

# Title bar above the screen - added title and logo
startscreen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Team: nohtyp')
clock = pygame.time.Clock()
logo = pygame.image.load("RuimteschipLogo.png")
pygame.display.set_icon(logo)

# Determine functions and execute them

def text_settings(text, lettertype_font):
    text_display = lettertype_font.render(text, True, black)
    return text_display, text_display.get_rect()


def startbutton(message, x, y, width, height, inactivecolour, activecolour, action=None):
    muis = pygame.mouse.get_pos()
    muisklik = pygame.mouse.get_pressed()

    if x + width > muis[0] > x and y + height > muis[1] > y:
        pygame.draw.rect(startscreen, activecolour, (x, y, width, height))
    else:
        pygame.draw.rect(startscreen, inactivecolour, (x, y, width, height))

    text_in_small_letters = pygame.font.Font("freesansbold.ttf", 40)
    text_appearence_outsidelook, textRect = text_settings(message, text_in_small_letters)
    textRect.center = ((x + (width / 2)), (y + (height / 2)))
    startscreen.blit(text_appearence_outsidelook, textRect)


def startscreen_game():
    start = True
    while start:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        startscreen.fill(white)
        text_in_capital_letters = pygame.font.Font('freesansbold.ttf', 95)
        text_appearance_outsidelook, TextRect = text_settings("Space Shooter", text_in_capital_letters)
        TextRect.center = ((screen_width / 2), (screen_height / 2))
        startscreen.blit(text_appearance_outsidelook, TextRect)

        startbutton("Play!!!", 290, 380, 200, 100, dark_green, light_green)

        pygame.display.update()
        clock.tick(15)


startscreen_game()