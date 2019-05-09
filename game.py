import pygame
import templates
from game_objects import empire
from typing import *


class Game(metaclass=templates.Singleton):
    empires: List[empire.Empire]
    objects = pygame.sprite.RenderUpdates()
