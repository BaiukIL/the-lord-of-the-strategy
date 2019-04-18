from abstraction.units import unit
from abstraction.object_properties import damage as damage_mod


class Warrior(unit.Unit, damage_mod.Damage):
    def __init__(self, race, health: int, speed: int, damage: int, image_file):
        unit.Unit.__init__(self, race=race, health=health, speed=speed, image_file=image_file)
        damage_mod.Damage.__init__(self, damage=damage)


class ElfWarrior(Warrior):
    pass


class OrcWarrior(Warrior):
    pass


class DwarfWarrior(Warrior):
    pass
