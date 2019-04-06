from units import unit
from object_properties import damage as damage_mod


class Warrior(unit.Unit, damage_mod.Damage):
    def __init__(self, health, speed, damage):
        unit.Unit.__init__(self, health, speed)
        self.set_damage(damage)

    def attack(self, obj):
        print("{} attacks {}".format(self.__class__.__name__, obj.__class__.__name__))


class ElfWarrior(unit.ElfUnit, Warrior):
    pass


class OrcWarrior(unit.OrcUnit, Warrior):
    pass


class DwarfWarrior(unit.DwarfUnit, Warrior):
    pass
