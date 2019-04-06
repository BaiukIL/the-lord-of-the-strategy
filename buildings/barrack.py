from buildings import base_building
from units import scout
from units import builder
from units import warrior


class BarrackBuilder(base_building.BaseBuilder):
    # some barrack building methods
    pass


class BarrackDirector:
    def build_elf_barrack(self, building_builder: BarrackBuilder, city):
        building_builder.reset(ElfBarrack())
        building_builder.set_health(10)
        building_builder.set_city(city)
        return building_builder.get()

    def build_orc_barrack(self, building_builder, city):
        building_builder.reset(OrcBarrack())
        building_builder.set_health(10)
        building_builder.set_city(city)
        return building_builder.get()

    def build_dwarf_barrack(self, building_builder, city):
        building_builder.reset(DwarfBarrack())
        building_builder.set_health(10)
        building_builder.set_city(city)
        return building_builder.get()


# fabric of units
class Barrack(base_building.Building):
    # def _add_unit_to_army(self, unit):
    #     self.master_city.master_empire.army.recruit(unit)

    def create_scout(self):
        raise NotImplementedError

    def create_builder(self):
        raise NotImplementedError

    def create_warrior(self):
        raise NotImplementedError


class ElfBarrack(Barrack, base_building.ElfBuilding):
    def create_scout(self):
        return scout.ElfScout(health=3, speed=2)

    def create_builder(self):
        return builder.ElfBuilder(health=3, speed=2)

    def create_warrior(self):
        return warrior.ElfWarrior(health=3, speed=1, damage=1)


class OrcBarrack(Barrack, base_building.OrcBuilding):
    def create_scout(self):
        return scout.OrcScout(health=3, speed=2)

    def create_builder(self):
        return builder.OrcBuilder(health=3, speed=2)

    def create_warrior(self):
        return warrior.OrcWarrior(health=3, speed=1, damage=1)


class DwarfBarrack(Barrack, base_building.DwarfBuilding):
    def create_scout(self):
        return scout.DwarfScout(health=3, speed=2)

    def create_builder(self):
        return builder.DwarfBuilder(health=3, speed=2)

    def create_warrior(self):
        return warrior.DwarfWarrior(health=3, speed=1, damage=1)
