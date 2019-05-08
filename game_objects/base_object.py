"""Every game object has fields of this class,
so every game entity is inherited from one of these"""


import pygame
import game
from game_objects import races
from abc import ABC, abstractmethod
from interface import window, interface
from images import image
from typing import *


class GameEntity(ABC):
    def __init__(self, race):
        if race in races.races:
            self.race = race
        else:
            races.RaceError("Unknown race: {}".format(race))

    @abstractmethod
    def info(self) -> Text:
        pass


class GameObject(GameEntity, window.Window, ABC):
    """"""

    """Reference to mater empire"""
    empire: object
    cost: int

    """Image which is drawn on Selected interface window"""
    icon_image: pygame.Surface

    def __init__(self, race, image_file: str, size: Tuple[int, int], icon_file: str = None):
        GameEntity.__init__(self, race)
        window.Window.__init__(self, size, image=pygame.image.load(image_file))
        game.Game().objects.add(self)
        if icon_file is None:
            self.icon_image = pygame.image.load(image_file)
        else:
            self.icon_image = pygame.image.load(icon_file)

    def handle(self, mouse_pos: Tuple[int, int]):
        self.active()
        interface.Interface().handle_object_click(self)

    @property
    def commands(self) -> List[Tuple]:
        commands = [(image.REMOVE, self.destroy, 'destroy')]
        print(self.unique_commands)
        commands.extend(self.unique_commands)
        return commands

    @property
    @abstractmethod
    def unique_commands(self) -> List[Tuple]:
        pass

    def destroy(self):
        """This method is called when object is out of health"""
        self.kill()
