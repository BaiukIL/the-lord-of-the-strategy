from buildings import barrack
from buildings import mine
from buildings import wall
import races


class City:
    def __init__(self, name, empire):
        self.name = name
        self.master_empire = empire
        self.buildings = list()

    def build_barrack(self):
        raise NotImplementedError

    def build_mine(self):
        raise NotImplementedError

    def build_wall(self):
        raise NotImplementedError

    def info(self):
        print("City name: {}".format(self.name))
        print("City race: {}".format(self.what_race()))
        if len(self.buildings) == 0:
            print("There're no buildings in this city")
        else:
            print("City buildings:")
            for building in self.buildings:
                print(" - {}".format(building.__class__.__name__))

    def remove_building(self, building):
        if building in self.buildings:
            self.buildings.remove(building)
        else:
            raise KeyError("No such building: {} in {}".format(building, self.name))


class ElfCity(City, races.Elves):
    def build_barrack(self):
        director = barrack.BarrackDirector()
        builder = barrack.BarrackBuilder()
        self.buildings.append(director.build_elf_barrack(builder, self))

    def build_mine(self):
        director = mine.MineDirector()
        builder = mine.MineBuilder()
        self.buildings.append(director.build_elf_mine(builder, self))

    def build_wall(self):
        director = wall.WallDirector()
        builder = wall.WallBuilder()
        self.buildings.append(director.build_elf_wall(builder, self))


class OrcCity(City, races.Orcs):
    def build_barrack(self):
        director = barrack.BarrackDirector()
        builder = barrack.BarrackBuilder()
        self.buildings.append(director.build_orc_barrack(builder, self))

    def build_mine(self):
        director = mine.MineDirector()
        builder = mine.MineBuilder()
        self.buildings.append(director.build_orc_mine(builder, self))

    def build_wall(self):
        director = wall.WallDirector()
        builder = wall.WallBuilder()
        self.buildings.append(director.build_orc_wall(builder, self))


class DwarfCity(City, races.Dwarfs):
    def build_barrack(self):
        director = barrack.BarrackDirector()
        builder = barrack.BarrackBuilder()
        self.buildings.append(director.build_dwarf_barrack(builder, self))

    def build_mine(self):
        director = mine.MineDirector()
        builder = mine.MineBuilder()
        self.buildings.append(director.build_dwarf_mine(builder, self))

    def build_wall(self):
        director = wall.WallDirector()
        builder = wall.WallBuilder()
        self.buildings.append(director.build_dwarf_wall(builder, self))
