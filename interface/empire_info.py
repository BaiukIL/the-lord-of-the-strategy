""" This module contains `EmpireInfo` - a window that shows empire info. """


import pygame
# project modules #
from windows import window
from interface import interface_configs as configs


class EmpireInfo:
    """ A window which shows empire information in upper corner. """

    def __init__(self, empire, enemy: bool):
        self.empire = empire
        self.empire_icon = window.Window(empire.icon)
        self.empire_icon.set_default_alpha(170)
        self.resources = window.Window(pygame.Surface((220, 50), pygame.SRCALPHA))
        self.resources.set_default_alpha(170)
        if enemy:
            self.empire_icon.rect.topright = configs.SCR_WIDTH, 0
            self.resources.rect.topright = configs.SCR_WIDTH, 120
        else:
            self.empire_icon.rect.topleft = 0, 0
            self.resources.rect.topleft = 0, 120

    def update(self):
        font = pygame.font.SysFont(name='Ani', size=30)
        self.resources.clear()
        self.resources.image.blit(
            font.render(f'Resources: {self.empire.resources}', True, pygame.Color('black')), (0, 0))

    def draw(self, screen: pygame.Surface):
        """ Draws empire info-window onto the screen. """
        screen.blit(self.empire_icon.image, self.empire_icon.rect)
        screen.blit(self.resources.image, self.resources.rect)
