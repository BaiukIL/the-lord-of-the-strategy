import pygame
import templates
from game_objects import empire
from interface.interface import Interface
from typing import *


def add_to_game(obj: templates.Publisher):
    Game().objects.add(obj)
    obj.subscribe('click', Interface())


class Game(metaclass=templates.Singleton):
    """Mediator which links empires and interface"""
    empires: List[empire.Empire]
    objects = pygame.sprite.RenderUpdates()
