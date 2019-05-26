import pygame
from abc import ABC
from typing import Tuple, Text, List, Callable
# project modules #
import game
from interface import click_handler
import exceptions
from windows import window
import image as img


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
        self.icon_image = image
        game.Game().objects.add(self)
        self.empire.objects.add(self)
        self._all_objects = game.Game().objects

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

    def delete(self):
        """Player can delete object using this method
        and get half of its cost back"""
        self.empire.resources += self.cost // 2
        self.die()

    def die(self):
        """This method is called when object is out of health"""
        click_handler.ClickHandler().handle_object_kill(self)
        self.kill()

    # Window methods
    def first_click_action(self):
        click_handler.ClickHandler().handle_object_first_click(self)

    def second_click_action(self):
        click_handler.ClickHandler().handle_object_second_click(self)

    def handle_empty_click(self, mouse_pos: Tuple[int, int]):
        """Empty method. Here object can handle mouse click."""
        pass

    def interact_with(self, obj: 'GameObject'):
        """Empty method. Here object can handle other object click."""
        pass

    @property
    def default_commands(self) -> List[Tuple[pygame.Surface, Callable, Text]]:
        return [(img.get_image().UPGRADE, self.upgrade, 'Upgrade'),
                (img.get_image().REMOVE, self.delete, 'Remove')]

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
