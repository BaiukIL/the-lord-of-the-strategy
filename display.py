""" This module contains `Display` - a sprite which represents game display. """


import pygame
# project modules #
import singleton
from interface.interface_class import Interface


class Display(pygame.sprite.Sprite, metaclass=singleton.Singleton):
    """ A sprite which represents game display with `Interface.camera` rect. """

    def __init__(self, screen: pygame.Surface):
        pygame.sprite.Sprite.__init__(self)
        self.image = screen
        self.rect = Interface().camera
