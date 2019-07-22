""" This module contains `Map` singleton. """


import pygame
# project modules #
import singleton
import game_configs as configs


class Map(pygame.sprite.Sprite, metaclass=singleton.Singleton):
    """ Map is a surface all game objects are located on. """

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(pygame.Surface(configs.MAP_SIZE), configs.MAP_SIZE)
        self.image.fill((0, 255, 0))
        self.rect = self.image.get_rect()
