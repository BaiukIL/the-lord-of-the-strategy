""" This module contains `Scout` unit. """


from abc import ABC
# project modules #
import image as img
from game_objects import game_objects_configs as configs
from game_objects.units.attack_unit import AttackUnit


class Scout(AttackUnit, ABC):
    """ A simple attack unit which has medium attack distance and low damage. """

    def __init__(self,
                 empire,
                 health: int,
                 speed: int,
                 damage: int):

        AttackUnit.__init__(self,
                            empire=empire,
                            health=health,
                            speed=speed,
                            damage=damage,
                            fight_distance=400,
                            size=configs.SCOUT_SIZE,
                            image=img.get_image(empire).SCOUT,
                            cost=configs.SCOUT_COST)


class ElfScout(Scout):
    def __init__(self, empire):
        Scout.__init__(self, empire=empire,
                       health=3,
                       speed=12,
                       damage=1)


class OrcScout(Scout):
    def __init__(self, empire):
        Scout.__init__(self, empire=empire,
                       health=3,
                       speed=6,
                       damage=2)


class DwarfScout(Scout):
    def __init__(self, empire):
        Scout.__init__(self, empire=empire,
                       health=6,
                       speed=6,
                       damage=1)
