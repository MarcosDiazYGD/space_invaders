import pygame
pygame.mixer.init()
import os

# Global Constants
TITLE = "Spaceships Game"
SCREEN_HEIGHT = 600
SCREEN_WIDTH = 1100
FPS = 30
IMG_DIR = os.path.join(os.path.dirname(__file__), "..", "assets")


# WALLPAPERS
BG = pygame.image.load(os.path.join(IMG_DIR, 'Other/Track.png'))
TABLE = pygame.image.load(os.path.join(IMG_DIR, 'Other/table_points.png'))


# ICONS
SHIELD = pygame.image.load(os.path.join(IMG_DIR, 'Other/shield.png'))
RATE_OF_FIRE = pygame.image.load(os.path.join(IMG_DIR, 'Bullet/bullet_1.png'))
HEART = pygame.image.load(os.path.join(IMG_DIR, 'Other/heart.png'))
ICON = pygame.image.load(os.path.join(IMG_DIR, "Spaceship/spaceship.png"))
REPLAY = pygame.image.load(os.path.join(IMG_DIR, "Other/Reset.png"))
GAME_OVER = pygame.image.load(os.path.join(IMG_DIR, "Other/GameOver.png"))
GAME_TITLE = pygame.image.load(os.path.join(IMG_DIR, "Other/game_title.png"))
EXPLOSION = pygame.image.load(os.path.join(IMG_DIR, "Sprites/fireball.gif"))


# POWER TYPES 
DEFAULT_TYPE = "default"
SHIELD_TYPE = 'shield'
HEART_TYPE = 'heart'
RATE_OF_FIRE_TYPE = 'rate of fire'

FIRE_RATE = 1000

# SPRITES
SPACESHIP_SPRITE = pygame.image.load(os.path.join(IMG_DIR, "Other/ships_sprite.png"))
SPACESHIP = pygame.image.load(os.path.join(IMG_DIR, "Spaceship/spaceship.png"))
SPACESHIP_SHIELD = pygame.image.load(os.path.join(IMG_DIR, "Spaceship/spaceship_shield.png"))

BULLET_1 = pygame.image.load(os.path.join(IMG_DIR, "Bullet/laser-yellow-01.png"))
BULLET_2 = pygame.image.load(os.path.join(IMG_DIR, "Bullet/laser-yellow-02.png"))
BULLET_3 = pygame.image.load(os.path.join(IMG_DIR, "Bullet/laser-yellow-03.png"))
BULLET_4 = pygame.image.load(os.path.join(IMG_DIR, "Bullet/laser-yellow-04.png"))

ENEMY_1 = pygame.image.load(os.path.join(IMG_DIR, "Enemy/enemy_1.png"))
ENEMY_2 = pygame.image.load(os.path.join(IMG_DIR, "Enemy/enemy_2.png"))

BULLET_ENEMY_1 = pygame.image.load(os.path.join(IMG_DIR, "Bullet/laser-red-01.png"))
BULLET_ENEMY_2 = pygame.image.load(os.path.join(IMG_DIR, "Bullet/laser-red-02.png"))
BULLET_ENEMY_3 = pygame.image.load(os.path.join(IMG_DIR, "Bullet/laser-red-03.png"))
BULLET_ENEMY_4 = pygame.image.load(os.path.join(IMG_DIR, "Bullet/laser-red-04.png"))


# FONTS

FONT_STYLE = 'freesansbold.ttf'

# SOUNDS
MUSIC =  pygame.mixer.Sound(os.path.join(IMG_DIR, 'Sounds/drunkle.mp3'))
SHOOT_NORMAL = pygame.mixer.Sound(os.path.join(IMG_DIR, "Sounds/shoot_normal.wav"))
SHOOT_POWER = pygame.mixer.Sound(os.path.join(IMG_DIR, "Sounds/shoot_power.wav"))
SHOOT_BLASTER = pygame.mixer.Sound(os.path.join(IMG_DIR, "Sounds/blaster.wav"))
EXPLOSION_SOUND = pygame.mixer.Sound(os.path.join(IMG_DIR, "Sounds/explosion.wav"))
