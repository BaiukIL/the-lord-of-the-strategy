import pygame
import game
from interface.interface import Interface
from abc import ABC
from interface import window
from images import image as img
from typing import *


class GameObject(window.Window, ABC):
    """Base class for all objects, belonging to any empire"""

    def __init__(self, empire, health, cost: int, image: pygame.Surface, size: Tuple[int, int]):
        self.empire = empire
        self.health = health
        self.cost = cost
        window.Window.__init__(self, size=size, image=image)
        game.Game().objects.add(self)
        self.icon_image = image

    def increase_health(self, value: int):
        if value >= 0:
            self.health += value
        else:
            raise GameObjectError("Can't increase negative health: {}. Use decrease_health for this".format(value))

    def decrease_health(self, value: int):
        if value >= 0:
            self.health -= value
        else:
            raise GameObjectError("Can't decrease negative health: {}. Use increase_health for this".format(value))
        if self.health <= 0:
            self.destroy()

    def info(self) -> Text:
        result = str()
        result += "Race: {}\n".format(self.empire.race)
        result += "Empire: {}\n".format(self.empire.name)
        result += "Health: {}\n".format(self.health)
        return result

    def upgrade(self):
        pass

    def destroy(self):
        """This method is called when object is out of health"""
        Interface().hide_all()
        self.kill()

    # Window methods
    def click_action(self):
        Interface().handle_object_click(self)

    def return_click_action(self):
        Interface().hide_all()
        pass

    def handle_empty_click(self, mouse_pos: Tuple[int, int]):
        """Empty method. Here object can handle mouse click."""
        pass

    def handle_object_click(self, obj: 'GameObject'):
        """Empty method. Here object can handle other (obj) object click."""
        pass

    @property
    def default_commands(self) -> List[Tuple[pygame.Surface, Callable, Text]]:
        return [(img.get_image().UPGRADE, self.upgrade, 'Upgrade'),
                (img.get_image().REMOVE, self.destroy, 'Remove')]

    @property
    def no_interaction_commands(self) -> List[Tuple[pygame.Surface, Callable, Text]]:
        return self.default_commands

    @property
    def mouse_interaction_commands(self) -> List[Tuple[pygame.Surface, Callable, Text]]:
        return []

    @property
    def object_interaction_commands(self) -> List[Tuple[pygame.Surface, Callable, Text]]:
        return []


class GameObjectError(Exception):
    pass
