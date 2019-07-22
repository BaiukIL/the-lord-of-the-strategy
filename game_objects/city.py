""" This module contains `City` - game object which represents city on the map.  """


from typing import Tuple, List, Callable, Text
import pygame
# project modules #
import exceptions
import image as img
from game_objects import game_objects_configs as configs
from game_objects import base_object
from game_objects.buildings import fabric


class City(base_object.GameObject):
    """ A game object which represents city on the map. """

    def __init__(self,
                 name: str,
                 health: int,
                 cost: int,
                 image: pygame.Surface,
                 size: Tuple[int, int],
                 empire):

        base_object.GameObject.__init__(self,
                                        empire=empire,
                                        health=health,
                                        cost=cost,
                                        image=image,
                                        size=size)

        self.name = name
        self.empire.cities.add(self)
        self.buildings = pygame.sprite.Group()
        self._fabric = fabric.create_fabric(self.empire)

    def build_barrack(self, mouse_pos: Tuple[int, int]):
        """ Builds barrack on `mouse_pos` position. """

        rect = _get_building_rect(configs.BARRACK_SIZE, mouse_pos)
        self._assert_creation_place_is_free(rect)
        building = self._fabric.build_barrack()
        self._action_after_building_creation(building, rect)
        return building

    def build_mine(self, mouse_pos: Tuple[int, int]):
        """ Builds mine on `mouse_pos` position. """

        rect = _get_building_rect(configs.MINE_SIZE, mouse_pos)
        self._assert_creation_place_is_free(rect)
        building = self._fabric.build_mine()
        self._action_after_building_creation(building, rect)
        return building

    def build_wall(self, mouse_pos: Tuple[int, int]):
        """ Builds wall on `mouse_pos` position. """

        rect = _get_building_rect(configs.WALL_SIZE, mouse_pos)
        self._assert_creation_place_is_free(rect)
        building = self._fabric.build_wall()
        self._action_after_building_creation(building, rect)
        return building

    def info(self) -> Text:
        result = ''
        result += f'Race: {self.empire.race}\n'
        result += f'Empire: {self.empire.name}\n'
        result += f'Name: {self.name}\n'
        result += f'Health: {self.health}\n'
        return result

    @property
    def mouse_interaction_commands(self) -> List[Tuple[pygame.Surface, Callable, Text]]:
        return [(img.get_image(self.empire).BARRACK, self.build_barrack, 'build barrack'),
                (img.get_image(self.empire).WALL, self.build_wall, 'build wall'),
                (img.get_image(self.empire).MINE, self.build_mine, 'build mine')]

    def _assert_creation_place_is_free(self, rect: pygame.Rect):
        sprite = pygame.sprite.Sprite()
        sprite.rect = rect
        if pygame.sprite.spritecollideany(sprite, self._all_objects):
            raise exceptions.CreationPlaceError(f"Can't create building here - place is occupied.")

    def _action_after_building_creation(self, building, rect: pygame.Rect):
        self.buildings.add(building)
        building.rect = rect


def _get_building_rect(size: Tuple[int, int], mouse_pos: Tuple[int, int]) -> pygame.Rect:
    rect = pygame.Rect(mouse_pos, size)
    rect.center = mouse_pos
    return rect
