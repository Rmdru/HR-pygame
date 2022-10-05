import pygame
from pygame.locals import *

pygame.init()
pygame.font.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# font object..................................
def create_font(t, s=72, c=(255, 255, 0), b=False, i=False):
    font = pygame.font.SysFont("Arial", s, bold=b, italic=i)
    text = font.render(t, True, c)
    return text


# Text to be rendered with create_font
game_over_text = create_font("GAME OVER")
restart_text = create_font("Press Space to restart", 36, (9, 0, 180))

canvas = pygame.display.set_mode((800, 600))
loop = True
clock = pygame.time.Clock()
while loop == True:
    canvas.fill((0, 0, 0))

    game_over_text_rect = game_over_text.get_rect(center=(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2))
    restart_text_rect = restart_text.get_rect(center=(SCREEN_WIDTH / 2, (SCREEN_HEIGHT / 2 + 75)))
    canvas.blit(game_over_text, game_over_text_rect)
    canvas.blit(restart_text, restart_text_rect)
    for e in pygame.event.get():
        if e.type == QUIT:
            loop = 0
    pygame.display.update()
    clock.tick(60)


