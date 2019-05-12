import pygame
from typing import Text
# project modules #
from game_objects import army, city
import image as img


class Empire:
    def __init__(self, race, name: str = 'DefaultEmpireName', start_resources: int = 100):
        self.race = race
        self.name = name
        self.resources = start_resources
        self.army = army.Army(empire=self)
        self.objects = pygame.sprite.Group()
        self.cities = pygame.sprite.Group()
        self.icon = img.get_image(self).EMPIRE_ICON

    def alive(self) -> bool:
        return len(self.cities) != 0

    def set_city(self, name: str, cost: int = 50):
        for city_ in self.cities:
            if city_.name == name:
                raise EmpireError(f"City {name} has already exists in {self.name} cities")
        # if it is default city, it doesn't cost anything
        if len(self.cities) == 0:
            cost = 0
        city_ = city.City(empire=self,
                          name=name,
                          cost=cost,
                          image=img.get_image(self).CITY,
                          size=(200, 200),
                          health=30)
        self.cities.add(city_)
        return city_

    def get_city(self, name: str) -> city.City:
        for city_ in self.cities:
            if city_.name == name:
                return city_
        raise EmpireError(f"{name} city does not exist in {self.name}")

    def info(self) -> Text:
        result = str()
        result += f"Name: {self.name}\n"
        result += f"Race: {self.race}\n"
        result += "Cities:\n"
        for _city in self.cities:
            result += f" - {_city.name}"
        return result


class EmpireError(Exception):
    pass
