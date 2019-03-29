import building_factory
import race


class City:
    def __init__(self, _race, name):
        self.race = _race
        self.name = name
        self.buildings = list()
        if self.race is race.Elf:
            self.factory = building_factory.ElfBuildingFactory()
        elif self.race is race.Orc:
            self.factory = building_factory.OrcBuildingFactory()
        elif self.race is race.Dwarf:
            self.factory = building_factory.DwarfBuildingFactory()
        else:
            raise Exception("Unknown race: {}".format(race))

    def info(self):
        print("City race: {}".format(self.race.__name__))
        print("City name: {}".format(self.name))
        if len(self.buildings) == 0:
            print("There're no buildings in this city")
        else:
            print("City buildings:")
            for building in self.buildings:
                print(" - {}".format(building.__class__.__name__))

    def build_barrack(self, strength):
        self.buildings.append(self.factory.build_barrack(strength))

    def build_mine(self, strength):
        self.buildings.append(self.factory.build_mine(strength))

    def build_wall(self, strength):
        self.buildings.append(self.factory.build_wall(strength))
