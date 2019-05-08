import pygame
from game_objects import base_object
from game_objects.buildings import fabric
from images import image
from configs import game_config
from typing import *


class CityError(Exception):
    pass


class City(base_object.GameObject):
    _buildings = pygame.sprite.Group()

    def __init__(self, name: str, empire):
        base_object.GameObject.__init__(self, empire=empire, image_file=image.CITY, size=game_config.CITY_SIZE)
        self.name = name
        self._fabric = fabric.Manufacture().create_fabric(self)

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
        return result

    @property
    def mouse_interaction_commands(self) -> List[Tuple[str, Callable, Text]]:
        return [(image.BUILD, self.build_barrack, 'build barrack'),
                (image.BUILD, self.build_wall, 'build wall'),
                (image.BUILD, self.build_mine, 'build mine')]
