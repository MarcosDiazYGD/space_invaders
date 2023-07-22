import pygame
pygame.mixer.init()

from game.utils.constants import SHOOT_NORMAL, SHOOT_BLASTER, SHIELD_TYPE, DEFAULT_TYPE


class BulletManager:
    def __init__(self):
        self.bullets = []
        self.enemy_bullets = []

    def update(self, game):
        for bullet in self.bullets:
            bullet.update(self.bullets)

            for enemy in game.enemy_manager.enemies:
                if bullet.rect.colliderect(enemy.rect) and bullet.owner == 'player':
                    game.score += 10
                    self.bullets.remove(bullet)
                    game.enemy_manager.enemies.remove(enemy)

        for bullet in self.enemy_bullets:
            bullet.update(self.enemy_bullets)

            if bullet.rect.colliderect(game.player.rect) and bullet.owner == 'enemy':

                if game.player.power_up_type == SHIELD_TYPE:
                    self.enemy_bullets.remove(bullet)

                if game.player.power_up_type == DEFAULT_TYPE:
                    if game.player.lives <= 1:
                        game.higt_score.append(game.score)
                        game.death_count += 1
                        self.enemy_bullets.remove(bullet)
                        game.playing = False
                        break
                    else:
                        game.player.lives -= 1
                        self.enemy_bullets.remove(bullet)


    def draw(self, screen):
        for bullet in self.enemy_bullets:
            bullet.draw(screen)

        for bullet in self.bullets:
            bullet.draw(screen)

    def add_bullet(self, bullet, game):
        if bullet.owner == 'enemy' and len(self.enemy_bullets) < 5:
            current_time = pygame.time.get_ticks()
            time = 3000
            
            if current_time > time: 
                self.enemy_bullets.append(bullet)
                SHOOT_NORMAL.play()
                time += 3000

        if bullet.owner == 'player':
            current_time = pygame.time.get_ticks()
            time = 3000
            if current_time >= time:
                self.bullets.append(bullet)
                game.player.shoot_sound.play()
                time += 3000 

    def reset(self):
        self.bullets = []
        self.enemy_bullets = []
