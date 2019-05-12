import pygame
import singleton


class Game(metaclass=singleton.Singleton):
    """Mediator which links empires and interface"""
    objects = pygame.sprite.RenderUpdates()

    def __init__(self, player_empire, enemy_empire):
        self.player_emp = player_empire
        self.enemy_emp = enemy_empire
