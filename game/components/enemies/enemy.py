import random
import pygame
from pygame.sprite import Sprite
pygame.mixer.init()

from game.components.bullets.bullet import Bullet
from game.utils.constants import ENEMY_1, ENEMY_2, SCREEN_HEIGHT, SCREEN_WIDTH, SHOOT_NORMAL

class Enemy(Sprite):
    SHOOT_SOUND = pygame.mixer.Sound(SHOOT_NORMAL)
    SHIP_WIDTH = 40
    SHIP_HEIGHT = 60
    Y_POS = 20
    X_POS_LIST = [50, 100, 150, 200, 250, 300, 350, 400, 450, 500, 550]
    SPEED_Y = 1
    SPEED_X = 5
    MOV_X = {0: 'left', 1: 'right'}
    IMAGE = {1: ENEMY_1, 2: ENEMY_2}

    def __init__(self, image=1, speed_x=SPEED_X, speed_y=SPEED_Y, move_x_for=[30, 100]):
        self.image = self.IMAGE[image]
        self.image = pygame.transform.scale(self.image,(self.SHIP_WIDTH, self.SHIP_HEIGHT))
        self.rect = self.image.get_rect()
        self.rect.y = self.Y_POS
        self.rect.x = self.X_POS_LIST[random.randint(0, 10)]
        self.speed_x = speed_x
        self.speed_y = speed_y 
        self.movement_x = self.MOV_X[random.randint(0, 1)]
        self.move_x_for = random.randint(move_x_for[0], move_x_for[1])
        self.index = 0
        self.type = 'enemy'
        self.shoot_timer = pygame.time.get_ticks() + 300 

    def update(self, ships, game):
        self.rect.y += self.speed_y
        current_time = pygame.time.get_ticks()
        if current_time >= self.shoot_timer:
            self.shoot(game)
            self.shoot_timer = current_time + 1000  

        if self.movement_x == 'left':
            self.rect.x -= self.speed_x
        else:
            self.rect.x += self.speed_x
        
        self.change_movement_x()

        if self.rect.y >= SCREEN_HEIGHT:
            ships.remove(self)
        
        if self.rect.colliderect(game.player.rect):
            if game.player.lives == 0:
                game.higt_score.append(game.score)
                print(game.higt_score)
                game.death_count += 1
                game.enemy_manager.enemies.remove(self)
                game.playing = False
            else: 
                game.player.lives -= 1


    def draw(self, screen):
        screen.blit(self.image, (self.rect.x, self.rect.y))

    def change_movement_x(self):
        self.index += 1
        if (self.index >= self.move_x_for and self.movement_x == 'right') or (self.rect.x >= SCREEN_WIDTH - self.SHIP_WIDTH):
            self.movement_x = 'left'
            self.index = 0
        elif (self.index >= self.move_x_for and self.movement_x == 'left') or (self.rect.x <= 10):
            self.movement_x = 'right'
            self.index = 0
    
    def shoot(self, game):
        bullet = Bullet(self)
        game.bullet_manager.add_bullet(bullet, game)
