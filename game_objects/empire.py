from game_objects import army, city
from typing import *


class Empire:
    """"""

    race: str
    name: str
    resources: int = 500
    _cities: Dict[str, city.City] = dict()
    army: army.Army
    friends: List['Empire']
    enemies: List['Empire']

    def __init__(self, race, name: str = 'DefaultEmpireName'):
        self.race = race
        self.name = name
        self.army = army.Army(empire=self)

    def set_city(self, name: str):
        if name not in self._cities:
            self._cities[name] = city.City(empire=self, name=name)
        else:
            raise EmpireError("City {} has already exists in {} cities".format(name, self.name))

    def get_city(self, name: str) -> city.City:
        if name in self._cities:
            return self._cities.get(name)
        else:
            raise EmpireError("{} city does not exist in {}".format(name, self.name))

    def info(self) -> Text:
        result = str()
        result += "Name: {}\n".format(self.name)
        result += "Race: {}\n".format(self.race)
        if len(self._cities) == 0:
            result += "No cities\n"
        else:
            result += "Cities:\n"
            for _city in self._cities.values():
                result += " - {}".format(_city.name)
        return result


class EmpireError(Exception):
    pass
