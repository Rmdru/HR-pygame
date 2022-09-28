import pygame

# Initialise pygame
pygame.init()

# Create the screen
screen_width = 1000
screen_height = 500
screen = pygame.display.set_mode((screen_width, screen_height))

# Title an Icon
pygame.display.set_caption("Space Invaders")
icon = pygame.image.load("nohtyp_logo_simplified.png")
pygame.display.set_icon(icon)

# Player
PlayerImg = pygame.image.load("rocket.png")
PlayerImg_X_size = 64
PlayerImg_Y_size = 64
playerX = screen_width / 10
playerY = ( screen_height // 2 ) - ( PlayerImg_Y_size // 2 )
playerX_change = 0
playerY_change = 0

# Bullet
# Ready = Cant't see the bullet
# Fire = Bullet is moving on screen
BulletImg = pygame.image.load("bullet.png")
BulletImg_X_size = 32
BulletImg_Y_size = 32
bulletX = playerX
bulletY = playerY + (BulletImg_Y_size // 2)
bulletX_change = 1
bulletY_change = 0
bullet_state = "ready"

def player(x, y):
    screen.blit(PlayerImg, (x, y))

def bullet(x, y):
    screen.blit(BulletImg, (x, y))

def fire_bullet(x, y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(BulletImg, (x + (BulletImg_X_size // 2 ), y + (BulletImg_Y_size // 2)))

# Game Loop
running = True
while running:

    # RGB - Red/Green/Blue
    screen.fill((255, 255, 255))

    # Check events
    for event in pygame.event.get():
        # Quit
        if event.type == pygame.QUIT:
            running = False
        # If keystroke is Pressed
        if event.type == pygame.KEYDOWN:
            ## Movement
            print("A keystroke is pressed")
            # If a key, X decreases
            if event.key == pygame.K_a:
                playerX_change = -0.4
                print("Key a is pressed")
            # If d key, X increases
            if event.key == pygame.K_d:
                playerX_change = +0.4
                print("Key d is pressed")
            # If w key, Y decreases
            if event.key == pygame.K_w:
                playerY_change = -0.4
                print("Key w is pressed")
            # If s key, Y increases
            if event.key == pygame.K_s:
                playerY_change = +0.4
                print("Key s is pressed")
            
            ## Shooting
            if event.key == pygame.K_SPACE and bullet_state == "ready":
                # To make sure the bullet starts at the front of the player
                bulletX = playerX + 32
                # Set bullet Y coordinate to current player Y coordinate
                bulletY = playerY
                fire_bullet(playerX, bulletY)
                print("Key space is pressed")

        # If keystroke is released, change speed to 0
        if event.type == pygame.KEYUP:
            print("Keystroke has been released")
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
    if playerX >= screen_width - PlayerImg_X_size:
        playerX = screen_width - PlayerImg_X_size
    if playerY <= 0:
        playerY = 0
    if playerY >= screen_height - PlayerImg_Y_size:
        playerY = screen_height - PlayerImg_Y_size

    # Prevent player from going too far right
    if playerX >= screen_width * 0.60:
        playerX = screen_width * 0.60

    # Bullet movement
    if bullet_state == "fire":
        fire_bullet(bulletX, bulletY)
        bulletX += bulletX_change

    # Reset bullet if it hits the border
    if bulletX >= screen_width:
        bulletX = playerX
        bullet_state = "ready"

    player(playerX, playerY)

    pygame.display.update()
