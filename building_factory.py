import elf_buildings
import orc_buildings
import dwarf_buildings


# abstract factory of races' factories
class RaceBuildingFactory:
    def build_barrack(self, strength):
        raise NotImplementedError

    def build_mine(self, strength):
        raise NotImplementedError

    def build_wall(self, strength):
        raise NotImplementedError


# factory of Elves' buildings
class ElfBuildingFactory(RaceBuildingFactory):
    def build_barrack(self, strength):
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
