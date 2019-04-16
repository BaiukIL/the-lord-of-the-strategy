from abstraction.object_properties import health as health_mod
from abstraction import gameobject
from abc import ABC


class Building(gameobject.RealObject, health_mod.Health, ABC):
    def __init__(self, health, city):
        gameobject.RealObject.__init__(self, race=city.race)
        health_mod.Health.__init__(self, health=health)
        self._master_city = city
        # bridge from building to race
        # self.race_property = building_unique.ElfBuildingUnique()

    def info(self):
        pass

    def _destroy(self):
        self._master_city.remove_building()
        del self
