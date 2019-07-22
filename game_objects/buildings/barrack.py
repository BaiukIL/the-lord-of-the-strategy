""" This module contains `Barrack` - a units factory. """


import time
from abc import ABC, abstractmethod
from typing import Tuple, List, Callable, Text
import pygame
# project modules #
import exceptions
import image as img
from game_objects import game_objects_configs as configs
from game_objects.buildings import base_building
from game_objects.units import builder, warrior, scout


# Factory & Template Method.
class Barrack(base_building.Building, ABC):
    """ Factory of units in the game. """

    # These methods are public and call more specific hidden methods.
    def create_builder(self):
        """ Creates and returns builder. """

        rect = self._get_unit_rect(configs.BUILDER_SIZE)
        self._assert_creation_place_is_free(rect)
        unit = self._create_builder(size=configs.BUILDER_SIZE)
        self._action_after_unit_creation(unit, rect)
        return unit

    def create_scout(self):
        """ Creates and returns scout. """

        rect = self._get_unit_rect(configs.SCOUT_SIZE)
        self._assert_creation_place_is_free(rect)
        unit = self._create_scout(size=configs.SCOUT_SIZE)
        self._action_after_unit_creation(unit, rect)
        return unit

    def create_warrior(self):
        """ Creates and returns warrior. """

        rect = self._get_unit_rect(configs.WARRIOR_SIZE)
        self._assert_creation_place_is_free(rect)
        unit = self._create_warrior(size=configs.WARRIOR_SIZE)
        self._action_after_unit_creation(unit, rect)
        return unit

    # These methods are hidden and overridden in inheritors.
    # They take `size` as argument to avoid unnecessary copies.
    # (Builders of any race, for example, have identical size, so
    # it is a good idea to set size in more general `create_builder` method)
    @abstractmethod
    def _create_builder(self, size: Tuple[int, int]) -> builder.Builder:
        pass

    @abstractmethod
    def _create_scout(self, size: Tuple[int, int]) -> scout.Scout:
        pass

    @abstractmethod
    def _create_warrior(self, size: Tuple[int, int]) -> warrior.Warrior:
        pass

    def _get_unit_rect(self, size: Tuple[int, int]) -> pygame.Rect:
        rect = pygame.Rect(self.rect.topleft, size)
        rect.centerx = self.rect.centerx
        rect.top = self.rect.bottom + 20
        return rect

    def _assert_creation_place_is_free(self, rect: pygame.Rect):
        sprite = pygame.sprite.Sprite()
        sprite.rect = rect
        if pygame.sprite.spritecollideany(sprite, self._all_objects):
            raise exceptions.CreationPlaceError(
                "Can't create unit - place is occupied")

    def _action_after_unit_creation(self, unit, rect: pygame.Rect):
        self.empire.army.recruit_unit(unit=unit)
        unit.rect = rect
        unit.update_position()

    @property
    def no_interaction_commands(self) -> List[Tuple[pygame.Surface, Callable, Text]]:
        return [(img.get_image(self.empire).SCOUT, self.create_scout, 'create scout'),
                (img.get_image(self.empire).BUILDER, self.create_builder, 'create builder'),
                (img.get_image(self.empire).WARRIOR, self.create_warrior, 'create warrior'),
                (img.get_image().UPGRADE, self.upgrade, 'Upgrade'),
                (img.get_image().REMOVE, self.delete, 'Remove')]


class ElvesBarrack(Barrack):
    def _create_builder(self, size: Tuple[int, int]) -> builder.Builder:
        return builder.ElfBuilder(empire=self.empire)

    def _create_scout(self, size: Tuple[int, int]) -> scout.Scout:
        return scout.ElfScout(empire=self.empire)

    def _create_warrior(self, size: Tuple[int, int]) -> warrior.Warrior:
        return warrior.ElfWarrior(empire=self.empire)


class OrcsBarrack(Barrack):
    def _create_builder(self, size: Tuple[int, int]) -> builder.Builder:
        return builder.OrcBuilder(empire=self.empire)

    def _create_scout(self, size: Tuple[int, int]) -> scout.Scout:
        return scout.OrcScout(empire=self.empire)

    def _create_warrior(self, size: Tuple[int, int]) -> warrior.Warrior:
        return warrior.OrcWarrior(empire=self.empire)


class DwarfsBarrack(Barrack):
    def _create_builder(self, size: Tuple[int, int]) -> builder.Builder:
        return builder.DwarfBuilder(empire=self.empire)

    def _create_scout(self, size: Tuple[int, int]) -> scout.Scout:
        return scout.DwarfScout(empire=self.empire)

    def _create_warrior(self, size: Tuple[int, int]) -> warrior.Warrior:
        return warrior.DwarfWarrior(empire=self.empire)


def _assert_delay_is_over(delay: float, last_call_time: float):
    difference = time.time() - last_call_time
    if difference < delay:
        raise exceptions.CreationTimeError(
            f"Can't create unit - not enough time's passed since previous call. \
            \nTime remained: {difference}")
