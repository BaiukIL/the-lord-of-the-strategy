from abstraction.object_properties import speed as speed_mod
from abstraction.object_properties import health as health_mod
from abstraction import gameobject


class Unit(gameobject.RealObject, health_mod.Health, speed_mod.Speed):
    def __init__(self, race, health: int, speed: int, image_file):
        gameobject.RealObject.__init__(self, race=race, image_file=image_file)
        health_mod.Health.__init__(self, health=health)
        speed_mod.Speed.__init__(self, speed=speed)

    def info(self):
        print(self.__class__.__name__)

    def _destroy(self):
        print("{} is killed".format(self.__class__.__name__))
