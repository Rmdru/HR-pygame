# imports
import pygame

# initializing pygame
pygame.init()

# vars
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
BACKGROUND_COLOR = (0, 0, 0)

# application window name
pygame.display.set_caption("Werkplaats 1: PyGame Nohtyp")

# set application window size
canvas = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# set application window icon
logo = pygame.image.load("RuimteschipLogo.png")
pygame.display.set_icon(logo)

#start pygame clock
clock = pygame.time.Clock()

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
    # Kleuren voor de schermachtergrond (wit) en de teksten (zwart)
    zwart = (0, 0, 0)
    wit = (255, 255, 255)

    # Kleuren van de startknop wanneer je wel/niet met de muis erover gaat
    donker_groen = (0, 200, 0)
    licht_groen = (0, 255, 0)

    # Functies definiëren en uitvoeren

    def tekst_instellingen(tekst, lettertype):
        tekst_weergave = lettertype.render(tekst, True, zwart)
        return tekst_weergave, tekst_weergave.get_rect()

    def startknop(mededeling, x ,y ,breedte, hoogte, inactivecolor, activecolor, action=None):
        muis = pygame.mouse.get_pos()

        if x + breedte > muis[0] > x and y + hoogte > muis[1] > y:
            pygame.draw.rect(canvas, activecolor, (x, y, breedte, hoogte))
        else:
            pygame.draw.rect(canvas, inactivecolor, (x, y, breedte, hoogte))

        tekst_in_kleine_letters = pygame.font.Font("freesansbold.ttf", 40)
        tekst_uiterlijk, textRect = tekst_instellingen(mededeling, tekst_in_kleine_letters)
        textRect.center = ((x + (breedte / 2)), (y + (hoogte / 2)))
        canvas.blit(tekst_uiterlijk, textRect)

    def startscherm_game():
        start = True
        while start:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

            canvas.fill(wit)
            tekst_in_hoofdletters = pygame.font.Font('freesansbold.ttf', 95)
            tekst_uiterlijk, TextRect = tekst_instellingen("Space Shooter", tekst_in_hoofdletters)
            TextRect.center = ((SCREEN_WIDTH / 2), (SCREEN_HEIGHT / 2))
            canvas.blit(tekst_uiterlijk, TextRect)

            startknop("Play!!!", 290, 380, 200, 100, donker_groen, licht_groen)

            pygame.display.update()
            clock.tick(15)

    startscherm_game()