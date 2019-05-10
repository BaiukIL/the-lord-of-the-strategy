from game_objects.object_properties import health as hl
from game_objects import base_object
from abc import ABC
import templates
from typing import *


class BuildingBuilder(templates.Builder):

    building: 'Building'
    _health: int

    def set_health(self, health: int):
        self._health = health

    def get_result(self):
        return self.building


class Building(base_object.GameObject, hl.Health, ABC):
    def __init__(self, health: int, empire, image, size: Tuple[int, int]):
        base_object.GameObject.__init__(self, empire=empire, size=size, image=image)
        hl.Health.__init__(self, health=health)

    def info(self) -> Text:
        result = str()
        result += "Race: {}\n".format(self.empire.race)
        result += "Empire: {}\n".format(self.empire.name)
        result += "Health: {}\n".format(self.health)
        return result
