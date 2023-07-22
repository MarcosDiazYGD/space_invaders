
import pygame
from pygame.sprite import Sprite

from game.utils.constants import BULLET_1, BULLET_ENEMY_1, SCREEN_HEIGHT
pygame.mixer.init()



class Bullet(Sprite):
    BULLET_SIZE = pygame.transform.scale(BULLET_1, (10,20))
    BULLET_ENEMY_SIZE = pygame.transform.scale(BULLET_ENEMY_1, (10,20))
    BULLETS = {'player': BULLET_SIZE, 'enemy': BULLET_ENEMY_SIZE}
    SPEED = 20

    def __init__(self, spaceshift):
        self.image = self.BULLETS[spaceshift.type]
        self.rect = self.image.get_rect()
        self.rect.center = spaceshift.rect.center
        self.owner = spaceshift.type

    def update(self, bullets):
        # enemy
        if self.owner == 'enemy':
            self.rect.y += self.SPEED - 5
            if self.rect.y >= SCREEN_HEIGHT:
                bullets.remove(self)

        # player
        if self.owner == 'player':
            self.rect.y -= self.SPEED
            if self.rect.y <= 0:
                bullets.remove(self)


    def draw (self, screen):
        screen.blit(self.image,(self.rect.x, self.rect.y))