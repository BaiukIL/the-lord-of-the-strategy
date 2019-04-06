import races


class Army:
    def __init__(self, empire):
        self.master_empire = empire
        self.units = list()

    def info(self):
        print("Army's race: {}".format(self.what_race()))
        print("Army consists of:")
        for unit in self.units:
            print(' - {}'.format(unit.__class__.__name__))

    def recruit_unit(self, unit):
        if unit not in self.units:
            self.units.append(unit)
        else:
            raise KeyError("Unit: {} has already exists in the army {}".format(unit, self.__class__.__name__))

    def remove_unit(self, unit):
        if unit in self.units:
            self.units.remove(unit)
        else:
            raise KeyError("No such unit: {} in the army {}".format(unit, self.__class__.__name__))


class ElfArmy(Army, races.Elves):
    pass


class OrcArmy(Army, races.Orcs):
    pass


class DwarfArmy(Army, races.Dwarfs):
    pass
