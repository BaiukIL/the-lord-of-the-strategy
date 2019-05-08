import pygame
from images import image
from configs import game_config
import templates


class Map(pygame.sprite.Sprite, metaclass=templates.Singleton):

    default_image: pygame.Surface = pygame.transform.scale(pygame.image.load(image.MAP), game_config.MAP_SIZE)
    image: pygame.Surface
    rect: pygame.Rect

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = self.default_image.copy()
        self.rect = self.image.get_rect()

    def clear(self):
        self.image.blit(self.default_image, (0, 0))
