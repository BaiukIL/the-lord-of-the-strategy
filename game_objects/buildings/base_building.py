from game_objects.object_properties import health as hl
from game_objects import base_object
from abc import ABC


class Building(base_object.GameObject, hl.Health, ABC):
    def __init__(self, health, city, image_file, size):
        base_object.GameObject.__init__(self, race=city.race, size=size, image_file=image_file)
        hl.Health.__init__(self, health=health)
        self._master_city = city
