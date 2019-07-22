""" This module contains `Warrior` unit. """


from abc import ABC
# project modules #
import image as img
from game_objects import game_objects_configs as configs
from game_objects.units.attack_unit import AttackUnit


class Warrior(AttackUnit, ABC):
    """ A simple attack unit which has a little attack distance and medium damage. """

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
                            fight_distance=180,
                            size=configs.WARRIOR_SIZE,
                            image=img.get_image(empire).WARRIOR,
                            cost=configs.WARRIOR_COST)


class ElfWarrior(Warrior):
    """ Elf warrior. """

    def __init__(self, empire):
        Warrior.__init__(self, empire=empire,
                         health=5,
                         speed=6,
                         damage=2)


class OrcWarrior(Warrior):
    """ Orc warrior. """

    def __init__(self, empire):
        Warrior.__init__(self, empire=empire,
                         health=5,
                         speed=3,
                         damage=4)


class DwarfWarrior(Warrior):
    """ Dwarf warrior. """

    def __init__(self, empire):
        Warrior.__init__(self, empire=empire,
                         health=10,
                         speed=3,
                         damage=2)
