# font object..................................
def create_font(t, s=72, c=(255, 255, 0), b=False, i=False):
    font = pygame.font.SysFont("Arial", s, bold=b, italic=i)
    text = font.render(t, True, c)
    return text


# Text to be rendered with create_font
game_over = create_font("GAME OVER")
restart = create_font("Press Space to restart", 36, (9, 0, 180))

canvas = pygame.display.set_mode((600, 400))
loop = True
clock = pygame.time.Clock()
while loop == True:
    canvas.fill((0, 0, 0))
    x, y = pygame.mouse.get_pos()
    canvas.blit(game_over, (100, 150))
    canvas.blit(restart, (x, y))
    for e in pygame.event.get():
        if e.type == QUIT:
            loop = 0
    pygame.display.update()
    clock.tick(60)


