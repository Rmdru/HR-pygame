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