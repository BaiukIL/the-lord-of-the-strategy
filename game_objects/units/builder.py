""" This module contains `Builder` unit. """


from abc import ABC
# project modules #
import image as img
from game_objects import game_objects_configs as configs
from game_objects.units.unit import Unit


class Builder(Unit, ABC):
    """ A unit which can create buildings. """

    def __init__(self,
                 empire,
                 health: int,
                 speed: int):

        Unit.__init__(self,
                      empire=empire,
                      health=health,
                      speed=speed,
                      size=configs.BUILDER_SIZE,
                      image=img.get_image(empire).BUILDER,
                      cost=configs.BUILDER_COST)


class ElfBuilder(Builder):
    def __init__(self, empire):
        Builder.__init__(self, empire=empire,
                         health=2,
                         speed=12)


class OrcBuilder(Builder):
    def __init__(self, empire):
        Builder.__init__(self, empire=empire,
                         health=2,
                         speed=6)


class DwarfBuilder(Builder):
    def __init__(self, empire):
        Builder.__init__(self, empire=empire,
                         health=4,
                         speed=6)
