import pygame
from abc import ABC
# project modules #
import game
import exceptions
from interface.interface import Interface
from interface import window
import image as img
from typing import Tuple, Text, List, Callable


class GameObject(window.Window, ABC):
    """Base class for all objects, belonging to any empire"""

    def __init__(self, empire, health: int, cost: int, image: pygame.Surface, size: Tuple[int, int]):
        assert health > 0
        assert cost >= 0
        self.empire = empire
        self.cost = cost
        self.health = health
        if empire.resources - cost >= 0:
            empire.resources -= cost
        else:
            raise exceptions.CreationResourcesLimitError(f"Can't create object - lack of resources")
        window.Window.__init__(self, size=size, image=image)
        game.Game().objects.add(self)
        self.empire.objects.add(self)
        self._all_objects = game.Game().objects
        self._interface = Interface()
        self.icon_image = image

    def increase_health(self, value: int):
        assert value >= 0
        self.health += value

    def decrease_health(self, value: int):
        if value >= 0:
            self.health -= value
            tmp_image = pygame.Surface(self.rect.size)
            tmp_image.fill((150, 0, 0))
            self.set_temporary_image(tmp_image, delay=0.06)
        else:
            raise GameObjectError(f"Can't decrease negative health: {value}. Use increase_health for this")
        if self.health <= 0:
            self.die()

    def info(self) -> Text:
        result = str()
        result += f"Race: {self.empire.race}\n"
        result += f"Empire: {self.empire.name}\n"
        result += f"Health: {self.health}\n"
        return result

    def upgrade(self):
        pass

    def destroy(self):
        """Player can ruin this object using this method
        and get half of its cost back"""
        self.empire.resources += self.cost // 2
        self.die()

    def die(self):
        """This method is called when object is out of health"""
        if self._interface.buffer.sprite is self:
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


class GameObjectError(Exception):
    pass
