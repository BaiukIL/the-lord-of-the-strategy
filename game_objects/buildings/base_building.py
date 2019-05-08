from game_objects.object_properties import health as hl
from game_objects import base_object
from abc import ABC
from typing import *


class Building(base_object.GameObject, hl.Health, ABC):
    def __init__(self, health, empire, image_file, size):
        base_object.GameObject.__init__(self, empire=empire, size=size, image_file=image_file)
        hl.Health.__init__(self, health=health)

    def info(self) -> Text:
        result = str()
        result += "Empire: {}\n".format(self.empire.name)
        result += "Health: {}\n".format(self.health)
        return result
