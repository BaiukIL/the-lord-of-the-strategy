import pygame
import exceptions
from game_objects import base_object
from game_objects.buildings import fabric
from images import image as img
from typing import *


class CityError(Exception):
    pass


class City(base_object.GameObject):
    def __init__(self, name: str, health: int, cost: int, image: pygame.Surface, size: Tuple[int, int], empire):
        base_object.GameObject.__init__(self,
                                        empire=empire,
                                        health=health,
                                        cost=cost,
                                        image=image,
                                        size=size)
        self.name = name
        self.buildings = pygame.sprite.Group()
        self.empire.cities.add(self)
        self._fabric = fabric.Manufacture().create_fabric(self.empire)

    def build_barrack(self, mouse_pos: Tuple[int, int]):
        size = 170, 170
        rect = self._get_building_rect(size, mouse_pos)
        self._assert_creation_place_is_free(rect)
        building = self._fabric.build_barrack(size)
        self._action_after_building_creation(building, rect)
        return building

    def build_mine(self, mouse_pos: Tuple[int, int]):
        size = 150, 150
        rect = self._get_building_rect(size, mouse_pos)
        self._assert_creation_place_is_free(rect)
        building = self._fabric.build_mine(size)
        self._action_after_building_creation(building, rect)
        return building

    def build_wall(self, mouse_pos: Tuple[int, int]):
        size = 50, 200
        rect = self._get_building_rect(size, mouse_pos)
        self._assert_creation_place_is_free(rect)
        building = self._fabric.build_wall(size)
        self._action_after_building_creation(building, rect)
        return building

    def _get_building_rect(self, size: Tuple[int, int], mouse_pos: Tuple[int, int]) -> pygame.Rect:
        rect = pygame.Rect(mouse_pos, size)
        rect.center = mouse_pos
        return rect

    def _assert_creation_place_is_free(self, rect: pygame.Rect):
        sprite = pygame.sprite.Sprite()
        sprite.rect = rect
        if pygame.sprite.spritecollideany(sprite, self._all_objects):
            raise exceptions.CreationPlaceError("Can't create building here - place is occupied")

    def _action_after_building_creation(self, building, rect: pygame.Rect):
        self.buildings.add(building)
        building.rect = rect

    def info(self) -> Text:
        result = str()
        result += "Race: {}\n".format(self.empire.race)
        result += "Empire: {}\n".format(self.empire.name)
        result += "Name: {}\n".format(self.name)
        result += "Health: {}\n".format(self.health)
        return result

    @property
    def mouse_interaction_commands(self) -> List[Tuple[pygame.Surface, Callable, Text]]:
        return [(img.get_image(self.empire).BARRACK, self.build_barrack, 'build barrack'),
                (img.get_image(self.empire).WALL, self.build_wall, 'build wall'),
                (img.get_image(self.empire).MINE, self.build_mine, 'build mine')]
