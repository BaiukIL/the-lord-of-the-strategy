import logging
import race
import army
import city
from collections import defaultdict


races = {race.Elf, race.Orc, race.Dwarf}


class Empire:
    def __init__(self, _race):
        if _race in races:
            self.race = _race
        else:
            raise KeyError("Unknown race: {}".format(race))
        self.army = army.Army(self.race)
        self.cities = defaultdict(city.City)
        logging.info("{}Empire has created".format(self.race.__name__))

    def get_city(self, name):
        if name in self.cities:
            return self.cities.get(name)
        else:
            raise KeyError("{} city doesn't exist in {}Empire".format(name, self.race.__name__))

    def get_army(self):
        return self.army

    def what_race(self):
        return self.race.__name__

    def establish_city(self, name):
        if name not in self.cities:
            self.cities[name] = city.City(self.race, name)
            logging.info("{}Empire has established city: {}".format(self.race.__name__, name))
        else:
            raise KeyError("City {} has already exists in {} cities".format(name, self.race.__name__))
