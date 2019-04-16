from abstraction.units import unit as unit_mod
from abstraction.units import scout, warrior
from abstraction.units import builder
from abstraction.buildings import base_building
from abc import ABC, abstractmethod


# Factory & Template Method ???
class Barrack(base_building.Building, ABC):
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
    def _create_builder(self) -> builder.Builder: pass

    @abstractmethod
    def _create_scout(self) -> scout.Scout: pass

    @abstractmethod
    def _create_warrior(self) -> warrior.Warrior: pass

    def _add_to_army(self, unit: unit_mod.Unit):
        self._master_city._master_empire.army.recruit_unit(unit=unit)


class ElvesBarrack(Barrack):
    def _create_builder(self) -> builder.Builder:
        return builder.ElfBuilder(race=self.race, health=4, speed=2)

    def _create_scout(self) -> scout.Scout:
        return scout.ElfScout(race=self.race, health=6, speed=2)

    def _create_warrior(self) -> warrior.Warrior:
        return warrior.ElfWarrior(race=self.race, health=6, speed=1, damage=1)


class OrcsBarrack(Barrack):
    def _create_builder(self) -> builder.Builder:
        return builder.OrcBuilder(race=self.race, health=2, speed=2)

    def _create_scout(self) -> scout.Scout:
        return scout.OrcScout(race=self.race, health=3, speed=2)

    def _create_warrior(self) -> warrior.Warrior:
        return warrior.OrcWarrior(race=self.race, health=3, speed=1, damage=1)


class DwarfsBarrack(Barrack):
    def _create_builder(self) -> builder.Builder:
        return builder.DwarfBuilder(race=self.race, health=2, speed=2)

    def _create_scout(self) -> scout.Scout:
        return scout.DwarfScout(race=self.race, health=3, speed=2)

    def _create_warrior(self) -> warrior.Warrior:
        return warrior.DwarfWarrior(race=self.race, health=3, speed=1, damage=1)
