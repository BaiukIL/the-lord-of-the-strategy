"""Every game object has fields of this class,
so every game entity is inherited from one of these"""


import pygame
import game
from abc import ABC, abstractmethod
from interface import window, interface, command
from images import image
from typing import *


class GameObject(window.Window, ABC):
    """"""

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
        game.Game().objects.add(self)

    @abstractmethod
    def info(self) -> Text:
        pass

    def upgrade(self):
        pass

    def handle(self, mouse_pos: Tuple[int, int]):
        interface.Interface().handle_object_click(self)
        self.active()

    def destroy(self):
        """This method is called when object is out of health"""
        interface.Interface().handle_object_deletion()
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