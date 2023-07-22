import pygame
import time
pygame.mixer.init()
from game.components.menu import Menu
from game.components.bullets.bullet_manager import BulletManager
from game.components.enemies.enemy_manager import EnemyManager
from game.components.power_ups.power_up_manager import PowerUpManager

from game.utils.constants import BG, ICON, SCREEN_HEIGHT, SCREEN_WIDTH, TITLE, FPS, DEFAULT_TYPE, FONT_STYLE, GAME_TITLE, SHOOT_BLASTER, MUSIC, BULLET_1
from game.components.spaceship import Spaceship


class Game:
    SUM_SCORE_EVENT = pygame.USEREVENT + 1

    def __init__(self):
        pygame.init()
        pygame.display.set_caption(TITLE)
        pygame.display.set_icon(ICON)
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()
        self.playing = False
        self.running = False
        self.game_speed = 10
        self.x_pos_bg = 0
        self.y_pos_bg = 0
        self.player = Spaceship()
        self.enemy_manager = EnemyManager()
        self.bullet_manager = BulletManager()
        self.power_up_manager = PowerUpManager()
        self.pause = False
        self.death_count = 0
        self.higt_score = []
        self.score = 0
        self.menu = Menu(self.screen, 'press any key')

    def execute(self):
        MUSIC.play()
        self.running = True
        while self.running:
            if not self.playing:
                self.show_menu()
        pygame.display.quit()
        pygame.quit()

    def run(self):
        self.score = 0
        self.player.lives = 3
        pygame.time.set_timer(self.SUM_SCORE_EVENT, 100)

        self.bullet_manager.reset()
        self.enemy_manager.reset()
        self.power_up_manager.reset()

        self.playing = True
        while self.playing:
            self.events()
            self.update()
            self.draw()

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False
                pygame.QUIT()
            if event.type == self.SUM_SCORE_EVENT:
                self.score += 1

    def update(self):
        user_input = pygame.key.get_pressed()
        self.player.update(user_input, self)
        self.enemy_manager.update(self)
        self.bullet_manager.update(self)
        self.power_up_manager.update(self)

    def draw(self):
        self.clock.tick(FPS)
        self.screen.fill((255, 255, 255))
        self.draw_background()
        self.player.draw(self.screen)
        self.enemy_manager.draw(self.screen)
        self.bullet_manager.draw(self.screen)
        self.menu.draw_score(self)
        self.menu.draw_lives(self)
        self.power_up_manager.draw(self.screen)
        self.draw_power_up_time()
        pygame.display.update()

    def draw_background(self):
        image = pygame.transform.scale(BG, (SCREEN_WIDTH, SCREEN_HEIGHT))
        image_height = image.get_height()
        self.screen.blit(image, (self.x_pos_bg, self.y_pos_bg))
        self.screen.blit(image, (self.x_pos_bg, self.y_pos_bg - image_height))
        if self.y_pos_bg >= SCREEN_HEIGHT:
            self.screen.blit(
                image, (self.x_pos_bg, self.y_pos_bg - image_height))
            self.y_pos_bg = 0

        self.y_pos_bg += self.game_speed

    def show_menu(self):
        half_screen_width = SCREEN_WIDTH // 2
        half_screen_height = SCREEN_HEIGHT // 2

        self.menu.reset_screen_color(self.screen)
        self.draw_background()

        if self.player.lives <= 1:
            self.menu.draw_game_over(self)
            self.menu.draw_table(self)
            self.menu.draw_higth_score(self, 20, SCREEN_WIDTH // 3 * 2 - 50, SCREEN_HEIGHT // 2 - 55, (255, 255, 255))
            self.menu.draw_score(self, 20, SCREEN_WIDTH // 3 * 2 - 50, SCREEN_HEIGHT // 2, (255, 255, 255))
            self.menu.draw_deaths(self, 20, SCREEN_WIDTH // 3 * 2 - 50, SCREEN_HEIGHT // 2 + 55, (255, 255, 255))
            current_time = pygame.time.get_ticks()
            if current_time >= 1000:
                self.menu.add_message("PRESS ANY KEY", SCREEN_WIDTH // 2,(SCREEN_HEIGHT // 2 + SCREEN_HEIGHT // 3), (255, 255, 255))

        else:
            title = pygame.transform.scale(GAME_TITLE, (600, 400))
            title_rect = title.get_rect()
            title_rect.center = (half_screen_width, SCREEN_HEIGHT // 3)
            self.screen.blit(title, title_rect)
            self.menu.add_message("PRESS ANY KEY", half_screen_width,
                                  (SCREEN_HEIGHT - SCREEN_HEIGHT // 10), (255, 255, 255))
            icon = pygame.transform.scale(ICON, (80, 120))
            icon_rect = icon.get_rect()
            icon_rect.center = (half_screen_width, half_screen_height + 100)
            self.screen.blit(icon, icon_rect)

        self.menu.draw(self.screen)
        self.menu.update(self)

    def draw_power_up_time(self):
        if self.player.has_power_up:
            time_to_show = round((self.player.power_time_up - pygame.time.get_ticks())/1000, 2)

            if time_to_show >= 0:
                font = pygame.font.Font(FONT_STYLE, 15)
                text = font.render(
                    f'{self.player.power_up_type.capitalize()} is enable for {time_to_show} seconds', True, (255, 255, 255))
                text_rect = text.get_rect()
                self.screen.blit(text, (540, 50))
            else:
                self.player_has_power_up = False
                self.player.power_up_type = DEFAULT_TYPE
                self.player.set_image()
                self.player.RATE_OF_FIRE = 1000
                self.player.shoot_sound = SHOOT_BLASTER

    def countdown(self):  # IMPLEMENTAR CUENTA REGRESIVA ANTES DE EMPEZAR LA RONDA
        current_time = pygame.time.get_ticks()
        seconds = 3
