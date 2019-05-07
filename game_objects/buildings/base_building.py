from game_objects.object_properties import health as health_mod
from game_objects import base_object
from abc import ABC


class Building(base_object.GameObject, health_mod.Health, ABC):
    def __init__(self, health, city, image_file):
        base_object.GameObject.__init__(self, race=city.race, image_file=image_file)
        health_mod.Health.__init__(self, health=health)
        self._master_city = city
        # bridge from building to race
        # self.race_property = building_unique.ElfBuildingUnique()

    def info(self):
        pass

    def _destroy(self):
        self._master_city.remove_building()
        del self
