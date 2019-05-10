import pygame
from game_objects import unit as unit_mod
from game_objects.buildings import base_building
from abc import ABC, abstractmethod
from images import image as img
from typing import *


class Barrack(base_building.Building, ABC):
    """Factory & Template Method"""

    def create_builder(self):
        unit = self._create_builder()
        self._action_after_unit_creation(unit)
        return unit

    def create_scout(self):
        unit = self._create_scout()
        self._action_after_unit_creation(unit)
        return unit

    def create_warrior(self):
        unit = self._create_warrior()
        self._action_after_unit_creation(unit)
        return unit

    @abstractmethod
    def _create_builder(self) -> unit_mod.Builder: 
        pass

    @abstractmethod
    def _create_scout(self) -> unit_mod.Scout: 
        pass

    @abstractmethod
    def _create_warrior(self) -> unit_mod.Warrior: 
        pass

    def _action_after_unit_creation(self, unit: unit_mod.Unit):
        self.empire.army.recruit_unit(unit=unit)
        unit.rect.topleft = self.rect.bottomleft
        unit.rect.y += 20

    @property
    def no_interaction_commands(self) -> List[Tuple[pygame.Surface, Callable, Text]]:
        return [(img.get_image(self.empire).SCOUT, self.create_scout, 'create scout'),
                (img.get_image(self.empire).BUILDER, self.create_builder, 'create builder'),
                (img.get_image(self.empire).WARRIOR, self.create_warrior, 'create warrior')]


class ElvesBarrack(Barrack):
    def _create_builder(self) -> unit_mod.Builder:
        return unit_mod.ElfBuilder(empire=self.empire, 
                                   health=4, 
                                   speed=2, 
                                   image=img.get_image(self.empire).BUILDER, 
                                   size=(100, 100))

    def _create_scout(self) -> unit_mod.Scout:
        return unit_mod.ElfScout(empire=self.empire, 
                                 health=6, 
                                 speed=2, 
                                 image=img.get_image(self.empire).SCOUT, 
                                 size=(100, 100))

    def _create_warrior(self) -> unit_mod.Warrior:
        return unit_mod.ElfWarrior(empire=self.empire, 
                                   health=6, 
                                   speed=1, 
                                   damage=1, 
                                   image=img.get_image(self.empire).WARRIOR, 
                                   size=(100, 100))


class OrcsBarrack(Barrack):
    def _create_builder(self) -> unit_mod.Builder:
        return unit_mod.OrcBuilder(empire=self.empire, 
                                   health=2, 
                                   speed=2, 
                                   image=img.get_image(self.empire).BUILDER, 
                                   size=(100, 100))

    def _create_scout(self) -> unit_mod.Scout:
        return unit_mod.OrcScout(empire=self.empire, 
                                 health=3, 
                                 speed=2, 
                                 image=img.get_image(self.empire).SCOUT, 
                                 size=(100, 100))

    def _create_warrior(self) -> unit_mod.Warrior:
        return unit_mod.OrcWarrior(empire=self.empire, 
                                   health=3, 
                                   speed=1, 
                                   damage=1, 
                                   image=img.get_image(self.empire).WARRIOR, 
                                   size=(100, 100))


class DwarfsBarrack(Barrack):
    def _create_builder(self) -> unit_mod.Builder:
        return unit_mod.DwarfBuilder(empire=self.empire,
                                     health=2,
                                     speed=2,
                                     image=img.get_image(self.empire).BUILDER,
                                     size=(100, 100))

    def _create_scout(self) -> unit_mod.Scout:
        return unit_mod.DwarfScout(empire=self.empire,
                                   health=3,
                                   speed=2,
                                   image=img.get_image(self.empire).SCOUT,
                                   size=(100, 100))

    def _create_warrior(self) -> unit_mod.Warrior:
        return unit_mod.DwarfWarrior(empire=self.empire,
                                     health=3,
                                     speed=1,
                                     damage=1,
                                     image=img.get_image(self.empire).WARRIOR,
                                     size=(100, 100))
