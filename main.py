# imports
import pygame

# initializing pygame
pygame.init()

# vars
SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720
BACKGROUND_COLOR = (0, 0, 0)

# application window name
pygame.display.set_caption("Werkplaats 1: PyGame Nohtyp")

# set application window size
canvas = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# application window icon
logo = pygame.image.load("img/RuimteschipLogo.png").convert_alpha()
logo_rect = logo.get_rect()

# function to check if user has requested to quit game
def quit_game_requested():
    halting = False
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            halting = True
            break
    return halting

# loop that runs every frame
while not quit_game_requested():
    # bg color
    canvas.fill(BACKGROUND_COLOR)

    canvas.blit(logo, logo_rect)

    pygame.display.flip()


# Hier staat de code voor de score board
def message_to_screen(message, color, font_size, x, y):
    '''display messages to screen.'''
    font = pygame.font.Sysfont(font_name, font_size)
    text = font.render(message, True, color)
    text_rect = text.get_rect()
    text_rect = (x, y)
    screen.blit(text_rect)

    message_to_screen("score:) " + str(score), WHITE, 24, SCREEN_WIDTH/2, 10)

    bullet_collision = pygame.sprite.groupcollide(all_meteors, all_bullets, True, True)
    for collision in bullet_collision:
        spawn_new_meteor()
        score += 150 - self.radius

# FIXME: Maak keuze qua taal (.EN), statische variabelen in HEADERS. Maak een keuze qua breedte. DdV

scherm_breedte = 800
scherm_hoogte = 600

# Kleuren voor de schermachtergrond (wit) en de teksten (zwart)
zwart = (0, 0, 0)
wit = (255, 255, 255)

# Kleuren van de startknop wanneer je wel/niet met de muis erover gaat
donker_groen = (0, 200, 0)
licht_groen = (0, 255, 0)

# Balk boven het scherm - toegevoegde naam en logo
startscherm = pygame.display.set_mode((scherm_breedte, scherm_hoogte))
pygame.display.set_caption('Team: nohtyp')
clock = pygame.time.Clock()

logo = pygame.image.load("RuimteschipLogo.png")
pygame.display.set_icon(logo)

# Functies definiëren en uitvoeren

def tekst_instellingen(tekst, lettertype):
    tekst_weergave = lettertype.render(tekst, True, zwart)
    return tekst_weergave, tekst_weergave.get_rect()

def startknop(mededeling, x ,y ,breedte, hoogte, inactivecolor, activecolor, action=None):
    muis = pygame.mouse.get_pos()
    muisklik = pygame.mouse.get_pressed()

    if x + breedte > muis[0] > x and y + hoogte > muis[1] > y:
        pygame.draw.rect(startscherm, activecolor, (x, y, breedte, hoogte))
    else:
        pygame.draw.rect(startscherm, inactivecolor, (x, y, breedte, hoogte))

    tekst_in_kleine_letters = pygame.font.Font("freesansbold.ttf", 40)
    tekst_uiterlijk, textRect = tekst_instellingen(mededeling, tekst_in_kleine_letters)
    textRect.center = ((x + (breedte / 2)), (y + (hoogte / 2)))
    startscherm.blit(tekst_uiterlijk, textRect)

def startscherm_game():
    start = True
    while start:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        startscherm.fill(wit)
        tekst_in_hoofdletters = pygame.font.Font('freesansbold.ttf', 95)
        tekst_uiterlijk, TextRect = tekst_instellingen("Space Shooter", tekst_in_hoofdletters)
        TextRect.center = ((scherm_breedte / 2), (scherm_hoogte / 2))
        startscherm.blit(tekst_uiterlijk, TextRect)

        startknop("Play!!!", 290, 380, 200, 100, donker_groen, licht_groen)

        pygame.display.update()
        clock.tick(15)

startscherm_game()