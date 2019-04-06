from object_properties import speed as speed_mod, health as health_mod
import races


class Unit(health_mod.Health, speed_mod.Speed):
    def __init__(self, health, speed):
        self.set_health(health)
        self.set_speed(speed)

    def _destroy(self):
        print("{} is killed".format(self.__class__.__name__))


class ElfUnit(Unit, races.Elves):
    pass


class OrcUnit(Unit, races.Orcs):
    pass


class DwarfUnit(Unit, races.Dwarfs):
    pass
