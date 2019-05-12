import pygame
import templates


class Game(metaclass=templates.Singleton):
    """Mediator which links empires and interface"""
    objects = pygame.sprite.RenderUpdates()
