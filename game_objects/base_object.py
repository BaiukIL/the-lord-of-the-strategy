import pygame
import game
from interface.interface import Interface
from abc import ABC, abstractmethod
from interface import window
from images import image
import templates
from typing import *


class GameObject(window.Window, templates.Publisher, ABC):
    """Base class for all objects, belonging to any empire"""

    cost: int

    """Image which is drawn on Selected interface window"""
    icon_image: pygame.Surface

    def __init__(self, empire, image_file: str, size: Tuple[int, int], icon_file: str = None):
        self.empire = empire
        window.Window.__init__(self, size=size, image=pygame.image.load(image_file))
        if icon_file is None:
            self.icon_image = pygame.image.load(image_file)
        else:
            self.icon_image = pygame.image.load(icon_file)
        game.Game.objects.add(self)

    @abstractmethod
    def info(self) -> Text:
        pass

    def upgrade(self):
        pass

    def click_action(self):
        Interface().handle_object_click(self)

    def return_click_action(self):
        Interface().handle_empty_click()

    def destroy(self):
        """This method is called when object is out of health"""
        Interface().handle_object_deletion()
        self.kill()

    @property
    def no_interaction_commands(self) -> List[Tuple[str, Callable, Text]]:
        return [(image.UPGRADE, self.upgrade, 'Upgrade'),
                (image.REMOVE, self.destroy, 'Remove')]

    @property
    def mouse_interaction_commands(self) -> List[Tuple[str, Callable, Text]]:
        return []

    @property
    def object_interaction_commands(self) -> List[Tuple[str, Callable, Text]]:
        return []
