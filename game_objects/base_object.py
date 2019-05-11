import pygame
import game
from interface.interface import Interface
from abc import ABC, abstractmethod
from interface import window
from game_objects.object_properties import health as hl
from images import image as img
import templates
from typing import *


class GameObject(window.Window, hl.Health, templates.Publisher, ABC):
    """Base class for all objects, belonging to any empire"""

    cost: int

    """Image which is drawn on Selected interface window"""
    icon_image: pygame.Surface

    def __init__(self, empire, health, image: pygame.Surface, size: Tuple[int, int]):
        self.empire = empire
        window.Window.__init__(self, size=size, image=image)
        hl.Health.__init__(self, health=health)
        game.Game().objects.add(self)

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
        Interface().handle_object_deletion()
        self.kill()

    # Window methods
    def click_action(self):
        Interface().handle_object_click(self)

    def return_click_action(self):
        Interface().hide()
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
