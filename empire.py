import logging
import races
import army
import city
from collections import defaultdict


class EmpireFactory:
    def create_empire(self, race):
        if race is races.Elf:
            return ElfEmpire()
        elif race is races.Orc:
            return OrcEmpire()
        elif race is races.Dwarf:
            return DwarfEmpire()
        else:
            raise Exception("Unknown race: {}".format(race))


class Empire:
    def __init__(self):
        self.army = army.Army()
        self.cities = defaultdict(city.City)
        logging.info("{}Empire has created".format(self.race.__name__))

    def establish_city(self, name):
        if name not in self.cities:
            self.cities[name] = city.City(self.race, name, empire=self)
            logging.info("{}Empire has established city: {}".format(self.race.__name__, name))
        else:
            raise KeyError("City {} has already exists in {} cities".format(name, self.race.__name__))

    def get_city(self, name):
        if name in self.cities:
            return self.cities.get(name)
        else:
            raise KeyError("{} city doesn't exist in {}Empire".format(name, self.race.__name__))

    def what_race(self):
        return self.__name__


class ElfEmpire(Empire):
    def __init__(self):
        pass


class OrcEmpire(Empire):
    def __init__(self):
        pass

    def

class DwarfEmpire(Empire):
    def __init__(self):
        pass