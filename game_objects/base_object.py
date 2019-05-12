import pygame
import game
import exceptions
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
        if empire.resources - cost >= 0:
            empire.resources -= cost
        else:
            raise exceptions.CreationResourcesLimitError("Can't create object - lack of resources")
        window.Window.__init__(self, size=size, image=image)
        game.Game().objects.add(self)
        self.empire.objects.add(self)
        self._all_objects = game.Game().objects
        self._interface = Interface()
        self.icon_image = image

    def increase_health(self, value: int):
        if value >= 0:
            self.health += value
        else:
            raise GameObjectError("Can't increase negative health: {}. Use decrease_health for this".format(value))

    def decrease_health(self, value: int):
        if value >= 0:
            self.health -= value
            self._image.fill()
        else:
            raise GameObjectError("Can't decrease negative health: {}. Use increase_health for this".format(value))
        if self.health <= 0:
            self.die()

    def info(self) -> Text:
        result = str()
        result += "Race: {}\n".format(self.empire.race)
        result += "Empire: {}\n".format(self.empire.name)
        result += "Health: {}\n".format(self.health)
        return result

    def upgrade(self):
        pass

    def destroy(self):
        """Player can ruin this object using this method
        and get half of its cost back"""
        self._interface.hide_all()
        self.empire.resources += self.cost // 2
        self.kill()

    def die(self):
        """This method is called when object is out of health"""
        self._interface.hide_all()
        self.kill()

    # Window methods
    def click_action(self):
        self._interface.handle_object_click(self)

    def return_click_action(self):
        self._interface.hide_all()
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

    def update(self, *args):
        """There might be animation update (i.e. effect of object moving)"""
        pass


class GameObjectError(Exception):
    pass
