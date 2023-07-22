import random
import pygame
from game.components.power_ups.shield import Shield
from game.components.power_ups.heart import Heart
from game.components.power_ups.rate_of_fire import Rate_Of_Fire
from game.utils.constants import SPACESHIP_SHIELD, SHIELD_TYPE, HEART_TYPE, RATE_OF_FIRE_TYPE, SHOOT_POWER


class PowerUpManager:
    def __init__(self):
        self.power_ups = []
        self.duration = random.randint(3, 5)
        self.when_appears = random.randint(5000, 10000)
        self.power_ups_types = {'shield': Shield(), 'heart': Heart(), 'rate_of_fire': Rate_Of_Fire()}
        self.power_up_list = []

    def update(self, game):
        current_time = pygame.time.get_ticks()

        if len(self.power_ups) == 0 and current_time >= self.when_appears:
            
            self.generate_power_up(game)

        for power_up in self.power_ups:
            power_up.update(game.game_speed, self.power_ups)

            if game.player.rect.colliderect(power_up.rect):
                game.player.power_up_type = power_up.type
                game.player.has_power_up = True

                if game.player.power_up_type == SHIELD_TYPE:
                    power_up.start_time = pygame.time.get_ticks()
                    game.player.power_time_up = power_up.start_time + (self.duration * 1000)
                    game.player.set_image((65, 75), SPACESHIP_SHIELD)
                    self.power_ups.remove(power_up)
                
                if game.player.power_up_type == HEART_TYPE:
                    power_up.start_time = pygame.time.get_ticks()
                    game.player.power_time_up = power_up.start_time + (self.duration * 1000)
                    game.player.lives += 1
                    self.power_ups.remove(power_up)

                if game.player.power_up_type == RATE_OF_FIRE_TYPE:
                    power_up.start_time = pygame.time.get_ticks()
                    game.player.power_time_up = power_up.start_time + (self.duration * 1000)
                    game.player.RATE_OF_FIRE = 300
                    game.player.shoot_sound = SHOOT_POWER
                    self.power_ups.remove(power_up)


    def draw(self, screen):
        for power_up in self.power_ups:
            power_up.draw(screen)

    def generate_power_up(self, game):
        dic_list = self.power_ups_types.keys()
        self.power_up_list = list(dic_list)
        power_up = self.power_ups_types[ self.power_up_list[random.randint(0, len(self.power_up_list) - 1)]]
        self.when_appears += random.randint(5000, 10000)
        self.power_ups.append(power_up)

    def reset(self):
        self.power_ups = []
