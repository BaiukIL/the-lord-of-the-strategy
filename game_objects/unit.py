from game_objects.object_properties import speed as speed_mod, health as health_mod, damage as damage_mod
from game_objects import base_object
from abc import ABC


class Unit(base_object.GameObject, health_mod.Health, speed_mod.Speed, ABC):
    def __init__(self, race, health: int, speed: int, image_file):
        base_object.GameObject.__init__(self, race=race, image_file=image_file)
        health_mod.Health.__init__(self, health=health)
        speed_mod.Speed.__init__(self, speed=speed)

    def info(self):
        print(self.__class__.__name__)


class Warrior(Unit, damage_mod.Damage):
    def __init__(self, race, health: int, speed: int, damage: int, image_file):
        Unit.__init__(self, race=race, health=health, speed=speed, image_file=image_file)
        damage_mod.Damage.__init__(self, damage=damage)


class ElfWarrior(Warrior):
    pass


class OrcWarrior(Warrior):
    pass


class DwarfWarrior(Warrior):
    pass


class Scout(Unit):
    pass


class ElfScout(Scout):
    pass


class OrcScout(Scout):
    pass


class DwarfScout(Scout):
    pass


class Builder(Unit):
    pass


class ElfBuilder(Builder):
    pass


class OrcBuilder(Builder):
    pass


class DwarfBuilder(Builder):
    pass