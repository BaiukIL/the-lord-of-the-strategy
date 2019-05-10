import pygame
from configs import game_config
import templates


class Map(pygame.sprite.Sprite, metaclass=templates.Singleton):

    image: pygame.Surface
    rect: pygame.Rect
    color = game_config.MAP_COLOR

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface(game_config.MAP_SIZE)
        self.image.fill(self.color)
        self.rect = self.image.get_rect()

    def clear(self):
        self.image.fill(self.color)
