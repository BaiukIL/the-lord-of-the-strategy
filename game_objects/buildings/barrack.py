from game_objects import unit as unit_mod
from game_objects.buildings import base_building
from abc import ABC, abstractmethod
from images import image


class Barrack(base_building.Building, ABC):
    """Factory & Template Method"""

    def create_builder(self):
        unit = self._create_builder()
        self.empire.army.recruit_unit(unit=unit)
        return unit

    def create_scout(self):
        unit = self._create_scout()
        self.empire.army.recruit_unit(unit=unit)
        return unit

    def create_warrior(self):
        unit = self._create_warrior()
        self.empire.army.recruit_unit(unit=unit)
        return unit

    @abstractmethod
    def _create_builder(self) -> unit_mod.Builder: pass

    @abstractmethod
    def _create_scout(self) -> unit_mod.Scout: pass

    @abstractmethod
    def _create_warrior(self) -> unit_mod.Warrior: pass


class ElvesBarrack(Barrack):
    def _create_builder(self) -> unit_mod.Builder:
        return unit_mod.ElfBuilder(empire=self.empire, health=4, speed=2, image_file=image.ELVES_BUILDER, size=(50, 50))

    def _create_scout(self) -> unit_mod.Scout:
        return unit_mod.ElfScout(empire=self.empire, health=6, speed=2, image_file=image.ELVES_SCOUT, size=(50, 50))

    def _create_warrior(self) -> unit_mod.Warrior:
        return unit_mod.ElfWarrior(empire=self.empire, health=6, speed=1, damage=1, image_file=image.ELVES_WARRIOR, size=(50, 50))


class OrcsBarrack(Barrack):
    def _create_builder(self) -> unit_mod.Builder:
        return unit_mod.OrcBuilder(empire=self.empire, health=2, speed=2, image_file=image.ORCS_BUILDER, size=(50, 50))

    def _create_scout(self) -> unit_mod.Scout:
        return unit_mod.OrcScout(empire=self.empire, health=3, speed=2, image_file=image.ORCS_SCOUT, size=(50, 50))

    def _create_warrior(self) -> unit_mod.Warrior:
        return unit_mod.OrcWarrior(empire=self.empire, health=3, speed=1, damage=1, image_file=image.ORCS_WARRIOR, size=(50, 50))


class DwarfsBarrack(Barrack):
    def _create_builder(self) -> unit_mod.Builder:
        return unit_mod.DwarfBuilder(empire=self.empire, health=2, speed=2, image_file=image.DWARFS_BUILDER, size=(50, 50))

    def _create_scout(self) -> unit_mod.Scout:
        return unit_mod.DwarfScout(empire=self.empire, health=3, speed=2, image_file=image.DWARFS_SCOUT, size=(50, 50))

    def _create_warrior(self) -> unit_mod.Warrior:
        return unit_mod.DwarfWarrior(empire=self.empire, health=3, speed=1, damage=1, image_file=image.DWARFS_WARRIOR, size=(50, 50))
