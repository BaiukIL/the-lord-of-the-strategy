""" This module contains `Empire`.
One empire represents one player. """


from typing import Text
import pygame
# project modules #
import image as img
from game_objects import army, city


class Empire:
    """ Empires represent players. One empire defines one player. """

    def __init__(self,
                 race,
                 name: str = 'DefaultEmpireName',
                 start_resources: int = 100):
        self.race = race
        self.name = name
        self.resources = start_resources
        self.icon = img.get_image(self).EMPIRE_ICON
        self.army = army.Army(empire=self)
        self.objects = pygame.sprite.Group()
        self.friends = pygame.sprite.Group()
        self.enemies = pygame.sprite.Group()
        self.cities = pygame.sprite.Group()

    def alive(self) -> bool:
        """ Returns true if empire is alive. """
        return len(self.cities) != 0

    def set_city(self, name: str, cost: int = 50):
        for city_ in self.cities:
            if city_.name == name:
                raise EmpireError(f'City {name} has already exists in {self.name} cities')
        # If city is first (default), it is free.
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
        """ Returns city with `name` name. """
        for city_ in self.cities:
            if city_.name == name:
                return city_
        raise EmpireError(f'{name} city does not exist in {self.name}')

    def info(self) -> Text:
        """ Returns string represents object information. """
        result = ''
        result += f'Name: {self.name}\n'
        result += f'Race: {self.race}\n'
        result += 'Cities:\n'
        for _city in self.cities:
            result += f' - {_city.name}'
        return result


class EmpireError(Exception):
    pass
