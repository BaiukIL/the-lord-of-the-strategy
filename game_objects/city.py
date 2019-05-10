import pygame
from game_objects import base_object
from game_objects.buildings import fabric
from images import image as img
from configs import game_config
from typing import *


class CityError(Exception):
    pass


class City(base_object.GameObject):

    name: str
    _buildings = pygame.sprite.Group()

    def __init__(self, name: str, empire):
        base_object.GameObject.__init__(self,
                                        empire=empire,
                                        image=img.get_image(empire).CITY,
                                        size=game_config.CITY_SIZE)
        self.name = name
        self._fabric = fabric.Manufacture().create_fabric(self.empire)

    def build_barrack(self, mouse_pos: Tuple[int, int]):
        building = self._fabric.build_barrack()
        self._buildings.add(building)
        building.rect.center = mouse_pos
        return building

    def build_mine(self, mouse_pos: Tuple[int, int]):
        building = self._fabric.build_mine()
        self._buildings.add(building)
        building.rect.center = mouse_pos
        return building

    def build_wall(self, mouse_pos: Tuple[int, int]):
        building = self._fabric.build_wall()
        self._buildings.add(building)
        building.rect.center = mouse_pos
        return building

    def info(self) -> Text:
        result = str()
        result += "Name: {}\n".format(self.name)
        result += "Race: {}\n".format(self.empire.race)
        result += "Empire: {}\n".format(self.empire.name)
        return result

    @property
    def mouse_interaction_commands(self) -> List[Tuple[pygame.Surface, Callable, Text]]:
        return [(img.get_image(self.empire).BARRACK, self.build_barrack, 'build barrack'),
                (img.get_image(self.empire).WALL, self.build_wall, 'build wall'),
                (img.get_image(self.empire).MINE, self.build_mine, 'build mine')]
