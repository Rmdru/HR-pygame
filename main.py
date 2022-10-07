# Import libraries
import random
import pygame
from pygame.locals import *

# initializing pygame
pygame.init()

# vars
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
TARGET_AMOUNT = 5
TARGET_SPEED = [-3, 0]
TARGET_SIZE = 50
TARGET_SPAWN_AREA_WIDTH = 0.6
TARGET_SPAWN_INTERVAL = 5
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
icon = pygame.image.load("nohtyp_logo_simplified.png")
pygame.display.set_icon(icon)

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

# made top left score text size color
def create_font(t, s=32, c=(255, 255, 255), b=False, i=False):
    font = pygame.font.SysFont('Arial', s, bold=b, italic=i)
    text = font.render(t, True, c)
    return text

# game over screen
def game_over_screen():
    # font object..................................
    def create_font(t, s=72, c=(255, 255, 0), b=False, i=False):
        font = pygame.font.SysFont("Arial", s, bold=b, italic=i)
        text = font.render(t, True, c)
        return text

    # Text to be rendered with create_font
    game_over_text = create_font("GAME OVER")
    restart_text = create_font("Press Space to quit", 36, (9, 0, 180))

    # loop to render game over screen
    while True:
        canvas.fill((0, 0, 0))
        game_over_text_rect = game_over_text.get_rect(center=(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2))
        restart_text_rect = restart_text.get_rect(center=(SCREEN_WIDTH / 2, (SCREEN_HEIGHT / 2 + 75)))
        canvas.blit(game_over_text, game_over_text_rect)
        canvas.blit(restart_text, restart_text_rect)
        for event in pygame.event.get():
            if event.key == pygame.K_SPACE or event.type == pygame.QUIT:
                pygame.quit()
                quit() 
        pygame.display.update()
        clock.tick(GAME_SPEED)

def game_loop():
    #var for game loop, if true, game runs
    game_loop = True

    #create game frame variable
    game_frame = 0

    # create background
    background = pygame.Surface(canvas.get_size())
    background = background.convert()

    # The number/amount of stars on the (background) screen
    STARS_AMOUNT = 200

    # create N stars randomly on the background
    stars = [[random.randint(0, SCREEN_WIDTH), random.randint(0, SCREEN_HEIGHT)]
            for x in range(STARS_AMOUNT)]

    #generate target surfaces
    targets_surface = []
    targets_color = []

    #function to spawn targets
    def spawn_targets():
        for i in range(TARGET_AMOUNT):
            target_color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
            spawn_area_width = SCREEN_WIDTH * TARGET_SPAWN_AREA_WIDTH
            target_surface = pygame.Rect(pygame.Rect(random.randint(spawn_area_width, SCREEN_WIDTH - TARGET_SIZE), random.randint(0, SCREEN_HEIGHT - TARGET_SIZE), TARGET_SIZE, TARGET_SIZE))
            targets_surface.append(target_surface)
            targets_color.append(target_color)

    spawn_targets()

    # function to trigger game over screen when target hit leftside of the window
    def target_hit_leftside(target_rect):
        if target_rect.left <= 0:
            game_loop = False
            game_over_screen()

    # Player
    PlayerImg = pygame.image.load("rocket.png")
    PlayerImg_X_size = 64
    PlayerImg_Y_size = 64
    playerX = SCREEN_WIDTH / 10
    playerY = ( SCREEN_HEIGHT // 2 ) - ( PlayerImg_Y_size // 2 )
    playerX_change = 0
    playerY_change = 0
    player_speed = 5

    # Bullet
    # Ready = Cant't see the bullet
    # Fire = Bullet is moving on screen
    BulletImg = pygame.image.load("bullet.png")
    BulletImg_X_size = 32
    BulletImg_Y_size = 32
    bulletX = playerX
    bulletY = playerY + (BulletImg_Y_size // 2)
    bulletX_change = 15
    bullet_state = "ready"

    def player(x, y):
        canvas.blit(PlayerImg, (x, y))

    while game_loop:
        #add time element to the game
        game_frame = game_frame + 1
        game_time = game_frame / GAME_SPEED

        #spawn targets on TARGET_SPAWN_INTERVAL
        if game_time % TARGET_SPAWN_INTERVAL == 0:
            spawn_targets()

        background.fill((0, 0, 0))
        for star in stars:
            pygame.draw.line(background,
                             (255, 255, 255), (star[0], star[1]), (star[0], star[1]))
            star[0] = star[0] - 1
            if star[0] < 0:
                star[0] = SCREEN_WIDTH
                star[1] = random.randint(0, SCREEN_HEIGHT)

        canvas.blit(background, (0, 0))

        # loop through target surfaces to draw them on the canvas
        for index, item in enumerate(targets_surface):
            item.move_ip(TARGET_SPEED)
            pygame.draw.rect(canvas, targets_color[index], item)
            target_hit_leftside(item)


        def fire_bullet(x, y):
            canvas.blit(BulletImg, (x + (BulletImg_X_size // 2 ), y + (BulletImg_Y_size // 2)))

        # Check events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            # If keystroke is Pressed
            if event.type == pygame.KEYDOWN:
                # If a key, X decreases
                if event.key == pygame.K_a:
                    playerX_change = -player_speed
                # If d key, X increases
                if event.key == pygame.K_d:
                    playerX_change = +player_speed
                # If w key, Y decreases
                if event.key == pygame.K_w:
                    playerY_change = -player_speed
                # If s key, Y increases
                if event.key == pygame.K_s:
                    playerY_change = +player_speed
                
                ## Shooting
                if event.key == pygame.K_SPACE and bullet_state == "ready":
                    # To make sure the bullet starts at the front of the player
                    bulletX = playerX + 32
                    # Set bullet Y coordinate to current player Y coordinate
                    bulletY = playerY
                    fire_bullet(bulletX, bulletY)
                    
                    # Change bullet state to "fire" if space is pressed
                    while bullet_state == "ready":
                        bullet_state = "fire"

            # If keystroke is released, change speed to 0
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_a:
                    playerX_change = 0
                if event.key == pygame.K_d:
                    playerX_change = 0
                if event.key == pygame.K_w:
                    playerY_change = 0
                if event.key == pygame.K_s :
                    playerY_change = 0

        playerX += playerX_change
        playerY += playerY_change

        # Stop player if they hit the screen border
        if playerX <= 0:
            playerX = 0
        if playerX >= SCREEN_WIDTH - PlayerImg_X_size:
            playerX = SCREEN_WIDTH - PlayerImg_X_size
        if playerY <= 0:
            playerY = 0
        if playerY >= SCREEN_HEIGHT - PlayerImg_Y_size:
            playerY = SCREEN_HEIGHT - PlayerImg_Y_size

        # Prevent player from going too far right
        if playerX >= SCREEN_WIDTH * 0.60:
            playerX = SCREEN_WIDTH * 0.60

        # Bullet movement
        if bullet_state == "fire":
            fire_bullet(bulletX, bulletY)
            bulletX += bulletX_change

        # Reset bullet if it hits the border
        if bulletX >= SCREEN_WIDTH:
            bulletX = playerX
            bullet_state = "ready"

        player(playerX, playerY)

        score_amount = 1
        # write score on corner of screen
        score_texts = create_font(f'Score:{score_amount}')
        canvas.blit(score_texts, (10, 10))

        pygame.display.update()
        clock.tick(GAME_SPEED)

def startbutton(message, x, y, width, height, inactivecolour, activecolour, action=None):
    mouse = pygame.mouse.get_pos()
    mouse_click = pygame.mouse.get_pressed()

    if x + width > mouse[0] > x and y + height > mouse[1] > y:
        pygame.draw.rect(canvas, activecolour, (x, y, width, height))
        if mouse_click[0] == 1 and action != None:
            if action == "play":
                game_loop()
    else:
        pygame.draw.rect(canvas, inactivecolour, (x, y, width, height))

    text_in_small_letters = pygame.font.Font("freesansbold.ttf", 40)
    text_appearence_outsidelook, textRect = text_settings(message, text_in_small_letters)
    textRect.center = ((x + (width / 2)), (y + (height / 2)))
    canvas.blit(text_appearence_outsidelook, textRect)

while not quit_game_requested():
    #bg color
    canvas.fill(WHITE)

    text_in_capital_letters = pygame.font.Font('freesansbold.ttf', 95)
    text_appearance_outsidelook, TextRect = text_settings("Space Shooter", text_in_capital_letters)
    TextRect.center = ((SCREEN_WIDTH / 2), (SCREEN_HEIGHT / 2))
    canvas.blit(text_appearance_outsidelook, TextRect)

    startbutton("Play!!!", 290, 380, 200, 100, DARK_GREEN, LIGHT_GREEN, "play")

    #update the display
    pygame.display.flip()

    #wait for next clock tick
    clock.tick(GAME_SPEED)