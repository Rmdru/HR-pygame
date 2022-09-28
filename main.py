#imports
import pygame

#initializing pygame
pygame.init()

#vars
SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720
BACKGROUND_COLOR = (0, 0, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)

#application window name
pygame.display.set_caption("Werkplaats 1: PyGame Nohtyp")

#set application window size
canvas = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

#application window icon
logo = pygame.image.load("img/RuimteschipLogo.png").convert_alpha()
logo_rect = logo.get_rect()

pygame.display.set_caption ("Game Over")

#Loop until the user clicks on the close button
done = False

# Used to set how fast the screen refreshes
clock = pygame.time.Clock()


game_over = False
if self._is_collision():
    game_over = True
    return game_over, self.score




