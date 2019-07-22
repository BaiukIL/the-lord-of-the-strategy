""" This module contains `GameObject` which is a class
all visible game objects (buildings and units) are based on (i.e. inherited). """


from abc import ABC
from typing import Tuple, Text, List, Callable
import pygame
# project modules #
import exceptions
import image as img
import game
from game_objects import game_objects_configs as configs
from interface import click_handler
from windows import window


class GameObject(window.Window, ABC):
    """ Base class of all visible objects (buildings, units, etc. ). """

    def __init__(self,
                 empire,
                 health: int,
                 cost: int,
                 image: pygame.Surface,
                 size: Tuple[int, int]):

        self._assert_creation_is_possible(empire, cost)

        window.Window.__init__(self, image, size=size)

        self.empire = empire
        self.cost = cost
        self.health = health
        self.icon_image = image
        self.minimap_image = pygame.transform.scale(self.icon_image, tuple(
            [int(i * configs.MINIMAP_ICONS_SIZE_NORMALIZATION_FACTOR) for i in size]))
        self._all_objects = game.Game().objects

        game.Game().objects.add(self)
        self.empire.objects.add(self)

    def increase_health(self, value: int):
        """ Increases health by positive `value` value. """
        self.health += value

    def decrease_health(self, value: int):
        """ Decreases health by positive `value` value. """

        self.health -= value
        if self.health <= 0:
            self.die()

        tmp_image = pygame.Surface(self.rect.size)
        tmp_image.fill(pygame.Color('red'))
        self.set_tmp_image(tmp_image, delay=0.06)

    def info(self) -> Text:
        """ Returns string represents object information. """
        result = ''
        result += f'Race: {self.empire.race}\n'
        result += f'Empire: {self.empire.name}\n'
        result += f'Health: {self.health}\n'
        return result

    def upgrade(self):
        """ Upgrades the object. """

    def delete(self):
        """ Deletes the object and gets half of its cost back. """
        self.empire.resources += self.cost // 2
        self.die()

    def die(self):
        """ Is called when object is out of health. """
        click_handler.ClickHandler().handle_object_kill(self)
        self.kill()

    # Window methods.
    def first_click_action(self):
        click_handler.ClickHandler().handle_object_first_click(self)

    def second_click_action(self):
        click_handler.ClickHandler().handle_object_second_click(self)

    def handle_empty_click(self, mouse_pos: Tuple[int, int]):
        """ Reaction to mouse click with `mouse_pos`. """

    def interact_with(self, obj: 'GameObject'):
        """ Reaction to other object (`obj`) click. """

    @property
    def default_commands(self) -> List[Tuple[pygame.Surface, Callable, Text]]:
        """ Returns list of default commands.
        Every game object has default commands: `remove` and `upgrade`. """
        return [(img.get_image().UPGRADE, self.upgrade, 'Upgrade'),
                (img.get_image().REMOVE, self.delete, 'Remove')]

    @property
    def no_interaction_commands(self) -> List[Tuple[pygame.Surface, Callable, Text]]:
        """ Returns list of commands which can be executed with single click. """
        return self.default_commands

    @property
    def mouse_interaction_commands(self) -> List[Tuple[pygame.Surface, Callable, Text]]:
        """ Returns list of commands responsible for click interaction. It means that
        while clicked, these commands wait for next click to interact with one. """
        return []

    @property
    def object_interaction_commands(self) -> List[Tuple[pygame.Surface, Callable, Text]]:
        """ Returns list of commands responsible for objects interaction. It means that
        while clicked, these commands wait for another object click to interact with one. """
        return []

    def _assert_creation_is_possible(self, empire, cost: int):
        if empire.resources - cost < 0:
            raise exceptions.CreationResourcesLimitError(f"Can't create object - lack of resources")
        empire.resources -= cost
