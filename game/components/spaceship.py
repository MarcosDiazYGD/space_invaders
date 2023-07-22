from game.components.bullets.bullet import Bullet
from game.utils.constants import SCREEN_HEIGHT, SCREEN_WIDTH, SPACESHIP, SHOOT_BLASTER, DEFAULT_TYPE, BULLET_1
from pygame.sprite import Sprite
import pygame


class Spaceship(Sprite):
    SHIP_WIDTH = 40
    SHIP_HEIGHT = 60
    X_POS = (SCREEN_WIDTH // 2) - SHIP_WIDTH
    Y_POS = 500
    SHIP_SPEED = 20
    RATE_OF_FIRE = 1000

    def __init__(self):
        self.image = SPACESHIP
        self.image = pygame.transform.scale(self.image, (self.SHIP_WIDTH, self.SHIP_HEIGHT))
        self.rect = self.image.get_rect()
        self.rect.x = self.X_POS
        self.rect.y = self.Y_POS
        self.type = 'player'
        self.power_up_type = DEFAULT_TYPE
        self.has_power_up = False
        self.power_time_up = 0
        self.shoot_timer = pygame.time.get_ticks() + self.RATE_OF_FIRE
        self.shoot_sound = SHOOT_BLASTER
        self.bullet_type = BULLET_1
        self.lives = 3

    def update(self, user_input, game):
        if user_input[pygame.K_LEFT]:
            self.move_left()
        if user_input[pygame.K_RIGHT]:
            self.move_right()
        if user_input[pygame.K_UP]:
            self.move_up()
        if user_input[pygame.K_DOWN]:
            self.move_down()
        if user_input[pygame.K_SPACE]:
            current_time = pygame.time.get_ticks()
            if current_time >= self.shoot_timer:
                self.shoot(game)
                self.shoot_timer = current_time + self.RATE_OF_FIRE  
        if user_input[pygame.K_F11]:
            pygame.display.toggle_fullscreen()
        
        
    def move_left(self):
        self.rect.x -= self.SHIP_SPEED
        if self.rect.left < 0:
            self.rect.x = SCREEN_WIDTH - self.SHIP_WIDTH

    def move_right(self):
        self.rect.x += self.SHIP_SPEED
        if self.rect.right >= SCREEN_WIDTH - self.SHIP_WIDTH:
            self.rect.x = 0

    def move_up(self):
        if self.rect.y > SCREEN_HEIGHT // 2:
            self.rect.y -= self.SHIP_SPEED

    def move_down(self):
        if self.rect.y < SCREEN_HEIGHT - 70:
            self.rect.y += self.SHIP_SPEED

    def shoot(self, game):
        bullet = Bullet(self)
        game.bullet_manager.add_bullet(bullet, game)

    def set_image(self, size = (SHIP_WIDTH, SHIP_HEIGHT), image = SPACESHIP):
        self.image = image
        self.image = pygame.transform.scale(self.image, size)

    def draw(self, screen):
        screen.blit(self.image, (self.rect.x, self.rect.y))
