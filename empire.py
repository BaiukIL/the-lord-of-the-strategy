import races
import army
import city


class EmpireFactory:
    def create_empire(self, race):
        if race is races.elves:
            return ElfEmpire()
        elif race is races.orcs:
            return OrcEmpire()
        elif race is races.dwarfs:
            return DwarfEmpire()
        else:
            raise Exception("Unknown race: {}".format(race))


class Empire:
    def __init__(self):
        self.army = None
        self.cities = dict()
        print("{} has been created".format(self.__class__.__name__))

    def establish_city(self, name):
        raise NotImplementedError

    def get_city(self, name):
        if name in self.cities:
            return self.cities.get(name)
        else:
            raise KeyError("{} city doesn't exist in {}".format(name, self.__class__.__name__))

    def destroy_city(self, name):
        if name in self.cities:
            print("{} has been destroyed".format(name))
            return self.cities.pop(name)
        else:
            raise KeyError("{} city doesn't exist in {}".format(name, self.__class__.__name__))


class ElfEmpire(Empire, races.Elves):
    def __init__(self):
        super().__init__()
        self.army = army.ElfArmy(self)

    def establish_city(self, name):
        if name not in self.cities:
            self.cities[name] = city.ElfCity(name, self)
        else:
            raise KeyError("City {} has already exists in {} cities".format(name, self.__class__.__name__))


class OrcEmpire(Empire, races.Orcs):
    def __init__(self):
        super().__init__()
        self.army = army.OrcArmy(self)

    def establish_city(self, name):
        if name not in self.cities:
            self.cities[name] = city.OrcCity(name, self)
        else:
            raise KeyError("City {} has already exists in {} cities".format(name, self.__class__.__name__))


class DwarfEmpire(Empire, races.Dwarfs):
    def __init__(self):
        super().__init__()
        self.army = army.DwarfArmy(self)

    def establish_city(self, name):
        if name not in self.cities:
            self.cities[name] = city.DwarfCity(name, self)
        else:
            raise KeyError("City {} has already exists in {} cities".format(name, self.__class__.__name__))
