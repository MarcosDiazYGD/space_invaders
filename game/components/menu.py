import pygame
from game.utils.constants import SCREEN_HEIGHT, SCREEN_WIDTH, FONT_STYLE, GAME_OVER, HEART, TABLE

class Menu:
  HALF_SCREEN_HEIGHT = SCREEN_HEIGHT // 2
  HALF_SCREEN_WIDTH = SCREEN_WIDTH // 2

  def __init__(self, screen, message):
    screen.fill((255,255,255))
    self.font = pygame.font.Font(FONT_STYLE)
    self.text = self.font.render(message, True, (0,0,0))
    self.text_rect = self.text.get_rect()
    self.text_rect.center = (self.HALF_SCREEN_WIDTH, self.HALF_SCREEN_HEIGHT)
    self.messages = []

  def update(self, game):
    pygame.display.update()
    self.handle_events_on_menu(game)
    self.draw_lives(game)

  def draw(self, screen):
    for text in self.messages:
      screen.blit(self.text, self.text_rect)

  def handle_events_on_menu(self, game):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game.playing = False
                game.running = False
            elif event.type == pygame.KEYDOWN:
                game.run()

  def reset_screen_color(self, screen):
    screen.fill((255,255,255))

  def add_message(self, message, coord_x = HALF_SCREEN_WIDTH , coord_y = HALF_SCREEN_HEIGHT, color = (0,0,0)):
    self.text = self.font.render(message, True, color)
    self.text_rect = self.text.get_rect()
    self.text_rect.center = (coord_x, coord_y)
    self.messages.append(self.text)

  def draw_higth_score(self, game, size = 16, coord_x = SCREEN_WIDTH - 50, coord_y = 25, color = (255,255,255), text = ''):
    hight_score = max(game.higt_score)
    font = pygame.font.Font(FONT_STYLE, size)
    text = font.render(f'{text}{hight_score}', True, color)
    text_rect = text.get_rect()
    text_rect.center = ((coord_x, coord_y))
    game.screen.blit(text, text_rect)

  def draw_score(self, game, size = 16, coord_x = SCREEN_WIDTH - 50, coord_y = 25, color = (255, 255, 255), text = ''):
    font = pygame.font.Font(FONT_STYLE, size)
    text = font.render(f'{text}{game.score}', True, color)
    text_rect = text.get_rect()
    text_rect.center = ((coord_x, coord_y))
    game.screen.blit(text, text_rect)

  def draw_deaths(self, game, size = 16, coord_x = SCREEN_WIDTH - 50, coord_y = 25, color = (255,255,255), text = ''):
    font = pygame.font.Font(FONT_STYLE, size)
    text = font.render(f'{text}{game.death_count}', True, color)
    text_rect = text.get_rect()
    text_rect.center = ((coord_x, coord_y))
    game.screen.blit(text, text_rect)

  def draw_game_over(self, game, coord_x = SCREEN_WIDTH//2, coord_y = SCREEN_HEIGHT//5):
    sprite = pygame.transform.scale(GAME_OVER, (300, 80))
    sprite_rect = sprite.get_rect()
    sprite_rect.center = (coord_x, coord_y)
    game.screen.blit(sprite, sprite_rect)

  def draw_table(self, game):
    table = pygame.transform.scale(TABLE, (600, 300))
    table_rect = table.get_rect()
    table_rect.center = ( SCREEN_WIDTH // 2,SCREEN_HEIGHT // 2)
    game.screen.blit(table, table_rect)

  def draw_lives(self, game):
    heart = pygame.transform.scale(HEART, (25, 25))
    heart_number = game.player.lives
    heart_spacing = 30
    margin = 25

    for i in range(heart_number):
        heart_rect = heart.get_rect()
        heart_rect.topleft = (margin + heart_spacing * i, 25)
        game.screen.blit(heart, heart_rect)