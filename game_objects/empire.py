import pygame
from game_objects import army, city
from images import image as img
from typing import *


class Empire:
    """"""

    def __init__(self, race, name: str = 'DefaultEmpireName'):
        self.race = race
        self.name = name
        self.resources = 100
        self.army = army.Army(empire=self)
        self.objects = pygame.sprite.Group()
        self.cities = pygame.sprite.Group()
        self.icon = img.get_image(self).EMPIRE_ICON

    def alive(self) -> bool:
        return len(self.cities) != 0

    def set_city(self, name: str):
        for _city in self.cities:
            if _city.name == name:
                raise EmpireError("City {} has already exists in {} cities".format(name, self.name))
        cost = 50
        # if it is default city, it doesn't cost anything
        if len(self.cities) == 0:
            cost = 0
        self.cities.add(city.City(empire=self,
                                  name=name,
                                  cost=cost,
                                  image=img.get_image(self).CITY,
                                  size=(200, 200),
                                  health=30))

    def get_city(self, name: str) -> city.City:
        for _city in self.cities:
            if _city.name == name:
                return _city
        raise EmpireError("{} city does not exist in {}".format(name, self.name))

    def info(self) -> Text:
        result = str()
        result += "Name: {}\n".format(self.name)
        result += "Race: {}\n".format(self.race)
        result += "Cities:\n"
        for _city in self.cities:
            result += " - {}".format(_city.name)
        return result


class EmpireError(Exception):
    pass
