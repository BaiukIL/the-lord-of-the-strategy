"""Every game object has fields of this class, so every game entity is inherited from one of these"""


from entities import races
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
    def info(self):
        pass


class RealObject(GameObject, pygame.sprite.Sprite, ABC):

    image: pygame.Surface
    rect: pygame.Rect

    def __init__(self, race, image_file: str):
        pygame.sprite.Sprite.__init__(self)
        GameObject.__init__(self, race)
        self.image = pygame.transform.scale(pygame.image.load(image_file), (200, 200))
        self.rect = self.image.get_rect()

    @abstractmethod
    def react_click(self) -> (pygame.Surface, list, list):
        """Returns image, info text and list of commands
        player can interact with the object.
        (*) Every text line is a separate element of list because
        pygame.font.Font.render() can't handle with `\n`
        """
        pass
