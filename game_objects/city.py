from game_objects import base_object
from game_objects.buildings import fabric
from images import image
from configs import game_config
from typing import *


class CityError(Exception):
    pass


class City(base_object.GameObject):
    def __init__(self, name, empire):
        base_object.GameObject.__init__(self, race=empire.race, image_file=image.CITY, size=game_config.CITY_SIZE)
        self.name = name
        self._master_empire = empire
        self._fabric = fabric.Manufacture().create_fabric(self)
        self._buildings = list()

    def build_barrack(self):
        building = self._fabric.build_barrack()
        self._buildings.append(building)
        return building

    def build_mine(self):
        building = self._fabric.build_mine()
        self._buildings.append(building)
        return building

    def build_wall(self):
        building = self._fabric.build_wall()
        self._buildings.append(building)
        return building

    def info(self) -> Text:
        result = str()
        result += "Name: {}\n".format(self.name)
        result += "Race: {}\n".format(self.race)
        if len(self._buildings) == 0:
            result += "No buildings\n"
        else:
            result += "Buildings:\n"
            for building in self._buildings:
                result += " - {}".format(building.__class__.__name__)
        return result

    def remove_building(self, building):
        if building in self._buildings:
            self._buildings.remove(building)
        else:
            raise CityError("No such building: {} in {}".format(building.__class__.__name__, self.name))

    @property
    def commands(self):
        return ((image.BUILD, self.build_wall, 'build wall'),
                (image.REMOVE, self.build_mine, 'build mine'),
                (image.ICON, self.build_barrack, 'build barrack'),
                (image.ICON, self.remove_building, 'remove building'))
