from game_objects import unit as unit_mod
from game_objects.buildings import base_building
from abc import ABC, abstractmethod
from images import image
from typing import *


class Barrack(base_building.Building, ABC):
    """Factory & Template Method"""

    def create_builder(self):
        unit = self._create_builder()
        self._add_to_army(unit)
        return unit

    def create_scout(self):
        unit = self._create_scout()
        self._add_to_army(unit)
        return unit

    def create_warrior(self):
        unit = self._create_warrior()
        self._add_to_army(unit)
        return unit

    @abstractmethod
    def _create_builder(self) -> unit_mod.Builder: pass

    @abstractmethod
    def _create_scout(self) -> unit_mod.Scout: pass

    @abstractmethod
    def _create_warrior(self) -> unit_mod.Warrior: pass

    def _add_to_army(self, unit: unit_mod.Unit):
        self._master_city._master_empire.army.recruit_unit(unit=unit)


class ElvesBarrack(Barrack):
    def _create_builder(self) -> unit_mod.Builder:
        return unit_mod.ElfBuilder(race=self.race, health=4, speed=2, image_file=image.ELVES_BUILDER)

    def _create_scout(self) -> unit_mod.Scout:
        return unit_mod.ElfScout(race=self.race, health=6, speed=2, image_file=image.ELVES_SCOUT)

    def _create_warrior(self) -> unit_mod.Warrior:
        return unit_mod.ElfWarrior(race=self.race, health=6, speed=1, damage=1, image_file=image.ELVES_WARRIOR)

    def unique_commands(self) -> List[Tuple]:
        return [()]


class OrcsBarrack(Barrack):
    def _create_builder(self) -> unit_mod.Builder:
        return unit_mod.OrcBuilder(race=self.race, health=2, speed=2, image_file=image.ORCS_BUILDER)

    def _create_scout(self) -> unit_mod.Scout:
        return unit_mod.OrcScout(race=self.race, health=3, speed=2, image_file=image.ORCS_SCOUT)

    def _create_warrior(self) -> unit_mod.Warrior:
        return unit_mod.OrcWarrior(race=self.race, health=3, speed=1, damage=1, image_file=image.ORCS_WARRIOR)


class DwarfsBarrack(Barrack):
    def _create_builder(self) -> unit_mod.Builder:
        return unit_mod.DwarfBuilder(race=self.race, health=2, speed=2, image_file=image.DWARFS_BUILDER)

    def _create_scout(self) -> unit_mod.Scout:
        return unit_mod.DwarfScout(race=self.race, health=3, speed=2, image_file=image.DWARFS_SCOUT)

    def _create_warrior(self) -> unit_mod.Warrior:
        return unit_mod.DwarfWarrior(race=self.race, health=3, speed=1, damage=1, image_file=image.DWARFS_WARRIOR)
