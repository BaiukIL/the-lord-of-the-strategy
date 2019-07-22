""" This module contains `Game` singleton which links game entities and represents game states. """


import pygame
# project modules #
import singleton


class Game(metaclass=singleton.Singleton):
    """ A mediator which links game entities and represents game states (play, menu, etc.). """

    objects = pygame.sprite.RenderUpdates()

    def __init__(self, player_empire, enemy_empire):
        self.player_emp = player_empire
        self.enemy_emp = enemy_empire
