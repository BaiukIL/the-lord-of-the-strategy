"""Every game object has fields of this class, so every game entity is inherited from one of these"""


from entities import races
from abc import ABC, abstractmethod
import pygame
from pygame_realization import window


class RaceError(Exception):
    pass


class GameObject(ABC):
    def __init__(self, race):
        if race in races.races:
            self._race = race
        else:
            RaceError("Unknown race: {}".format(race))

    @property
    def race(self):
        return self._race

    @abstractmethod
    def info(self):
        pass


class RealObject(GameObject, window.Window, ABC):
    def __init__(self, race, image_file: str, size: tuple):
        window.Window.__init__(self, size)
        GameObject.__init__(self, race)
        self.image = pygame.transform.scale(pygame.image.load(image_file), size)
