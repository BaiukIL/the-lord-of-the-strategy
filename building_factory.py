import elf_buildings
import orc_buildings
import dwarf_buildings
from abc import abstractmethod


class ElfDirector:
    def create_barrack(self):
        pass

    def create_


class ElfBuilder:
    def


# abstract factory of races' factories
class RaceBuildingFactory:
    @abstractmethod
    def build_barrack(self, strength):
        pass

    @abstractmethod
    def build_mine(self, strength):
        pass

    @abstractmethod
    def build_wall(self, strength):
        pass


# factory of Elves' buildings
class ElfBuildingFactory(RaceBuildingFactory):
    def build_barrack(self, strength):
        elf_builder = ElfBuilder()
        director = ElfDirector(elf_builder)
        return elf_buildings.ElfBarrack(strength)

    def build_mine(self, strength):
        return elf_buildings.ElfMine(strength)

    def build_wall(self, strength):
        return elf_buildings.ElfWall(strength)


# factory of Orcs' buildings
class OrcBuildingFactory(RaceBuildingFactory):
    def build_barrack(self, strength):
        return orc_buildings.OrcBarrack(strength)

    def build_mine(self, strength):
        return orc_buildings.OrcMine(strength)

    def build_wall(self, strength):
        return orc_buildings.OrcWall(strength)


# factory of Dwarfs' buildings
class DwarfBuildingFactory(RaceBuildingFactory):
    def build_barrack(self, strength):
        return dwarf_buildings.DwarfBarrack(strength)

    def build_mine(self, strength):
        return dwarf_buildings.DwarfMine(strength)

    def build_wall(self, strength):
        return dwarf_buildings.DwarfWall(strength)
