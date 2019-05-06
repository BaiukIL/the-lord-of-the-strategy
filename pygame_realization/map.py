import pygame
from images import image
from pygame_realization import singleton
from configs import game_config


class Map(pygame.sprite.Sprite, metaclass=singleton.Singleton):

    image: pygame.Surface
    rect: pygame.Rect

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(pygame.image.load(image.MAP), game_config.MAP_SIZE)
        self.rect = self.image.get_rect()
