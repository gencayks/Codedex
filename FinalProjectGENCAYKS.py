import pygame
import sys

# Game settings
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
PLAYER_SPEED = 5
BULLET_SPEED = 5
ALIEN_SPEED = 3
FONT_NAME = 'freesansbold.ttf'
FONT_SIZE = 32

# Initialize Pygame
pygame.init()

# Set up display
WINDOW = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption('Space Invaders')

# Set up assets
player = pygame.image.load('player.png')
alien = pygame.image.load('alien.png')
bullet = pygame.image.load('bullet.png')

# Set up game variables
player_pos = [WINDOW_WIDTH / 2, WINDOW_HEIGHT - player.get_height()]
bullets = []
alien_pos = [WINDOW_WIDTH / 2, 50]
alien_dir = 1
score = 0

# Set up font
font = pygame.font.Font(FONT_NAME, FONT_SIZE)

# Game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                bullets.append([player_pos[0], player_pos[1]])

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player_pos[0] -= PLAYER_SPEED
    if keys[pygame.K_RIGHT]:
        player_pos[0] += PLAYER_SPEED

    for b in bullets:
        b[1] -= BULLET_SPEED
        if b[1] < 0:
            bullets.remove(b)
        elif b[0] >= alien_pos[0] and b[0] <= alien_pos[0] + alien.get_width() and b[1] <= alien_pos[1] + alien.get_height():
            bullets.remove(b)
            score += 1
            alien_pos = [WINDOW_WIDTH / 2, 50]

    alien_pos[0] += ALIEN_SPEED * alien_dir
    if alien_pos[0] <= 0 or alien_pos[0] >= WINDOW_WIDTH - alien.get_width():
        alien_dir *= -1

    WINDOW.fill((0, 0, 0))
    WINDOW.blit(player, player_pos)
    WINDOW.blit(alien, alien_pos)
    for b in bullets:
        WINDOW.blit(bullet, b)
    score_text = font.render('Score: ' + str(score), True, (255, 255, 255))
    WINDOW.blit(score_text, (10, 10))
    pygame.display.update()