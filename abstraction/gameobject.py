"""Every game object has fields of this class, so every game entity (class) is inherited from this one"""

from abstraction import races
from abc import ABC, abstractmethod
import pygame


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
    def info(self): pass


class RealObject(GameObject, pygame.sprite.Sprite, ABC):
    image: pygame.Surface
    rect: pygame.Rect

    def __init__(self, race, image_file: str):
        pygame.sprite.Sprite.__init__(self)
        GameObject.__init__(self, race)
        self.image = pygame.image.load(image_file)
        self.rect = self.image.get_rect()

    def click_react(self) -> pygame.Surface:
        selected = pygame.Surface((100, 100))
        selected.fill((100, 0, 0))
        return selected
