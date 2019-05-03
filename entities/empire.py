from entities import gameobject, army, city


class EmpireError(Exception):
    pass


class Empire(gameobject.GameObject):
    def __init__(self, race, name: str = 'DefaultEmpireName'):
        gameobject.GameObject.__init__(self, race=race)
        self.army = army.Army(empire=self)
        self._name = name
        self._cities = dict()

    @property
    def name(self):
        return self._name

    def set_city(self, name: str):
        if name not in self._cities:
            self._cities[name] = city.City(empire=self, name=name)
        else:
            raise EmpireError("City {} has already exists in {} cities".format(name, self._name))

    def get_city(self, name: str) -> city.City:
        if name in self._cities:
            return self._cities.get(name)
        else:
            raise EmpireError("{} city does not exist in {}".format(name, self._name))

    def destroy_city(self, name: str):
        if name in self._cities:
            return self._cities.pop(name)
        else:
            raise EmpireError("{} city doesn't exist in {}".format(name, self._name))

    def info(self):
        print("Empire name: {}".format(self._name))
        print("Empire race: {}".format(self._race))
        if len(self._cities) == 0:
            print("There are no cities")
        else:
            print("Empire cities:")
            for _city in self._cities.values():
                print(" - {}".format(_city.name))
