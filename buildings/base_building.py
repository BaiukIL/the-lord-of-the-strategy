from object_properties import health as health_mod
import races


class Building(health_mod.Health):
    def _set_health(self, health):
        self.set_health(health)

    def _set_city(self, city):
        self.master_city = city

    def _destroy(self):
        self.master_city.remove_building()
        print("{} has been destroyed".format(self.__class__.__name__))


# building BUILDER
class BaseBuilder:
    obj: Building

    def reset(self, building_type: Building):
        self.obj = building_type

    def set_city(self, city):
        self.obj._set_city(city)

    def set_health(self, health):
        self.obj._set_health(health)

    def get(self):
        return self.obj


class ElfBuilding(Building, races.Elves):
    # some unique race methods
    pass


class OrcBuilding(Building, races.Orcs):
    # some unique race methods
    pass


class DwarfBuilding(Building, races.Dwarfs):
    # some unique race methods
    pass
