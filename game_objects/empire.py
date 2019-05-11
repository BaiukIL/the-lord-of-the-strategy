import pygame
from game_objects import army, city
from typing import *


class Empire:
    """"""

    def __init__(self, race, name: str = 'DefaultEmpireName'):
        self.race = race
        self.name = name
        self.resources = 500
        self.army = army.Army(empire=self)
        self._cities = pygame.sprite.Group()

    def alive(self) -> bool:
        return len(self._cities) != 0

    def set_city(self, name: str):
        for _city in self._cities:
            if _city.name == name:
                raise EmpireError("City {} has already exists in {} cities".format(name, self.name))
        self._cities.add(city.City(empire=self, name=name))

    def get_city(self, name: str) -> city.City:
        for _city in self._cities:
            if _city.name == name:
                return _city
        raise EmpireError("{} city does not exist in {}".format(name, self.name))

    def info(self) -> Text:
        result = str()
        result += "Name: {}\n".format(self.name)
        result += "Race: {}\n".format(self.race)
        result += "Cities:\n"
        for _city in self._cities:
            result += " - {}".format(_city.name)
        return result


class EmpireError(Exception):
    pass
