
# Bibliotheek importeren
import pygame

# Zorgen dat de code bij de items in de Pygame bibliotheek kan
pygame.init()

# Scherminstellingen
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

def startknop(mededeling,x,y,breedte,hoogte,inactivecolor,activecolor,action=None):
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
