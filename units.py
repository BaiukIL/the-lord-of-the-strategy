import health
import speed
import prototype
import logging
import race


class Unit(health.Health, speed.Speed, prototype.Prototype):
    def __init__(self, _health, _speed):
        health.Health.__init__(self, _health)
        speed.Speed.__init__(self, _speed)
        logging.info("{} unit has created".format(self.__class__.__name__))

    def _destroy(self):
        pass
        logging.info("{} is killed".format(self.__name__))

    # it can have more difficult logic in future
    def clone(self):
        pass


class Scout(Unit):
    pass


class Warrior(Unit):
    pass


class Miner(Unit):
    pass


class ElfUnit(Unit, race.Elf):
    def __init__(self, _health, _speed):
        Unit.__init__(self, _health, _speed)

    def skill(self):
        self.health *= 2


class OrcUnit(Unit, race.Orc):
    def __init__(self, _health, _speed):
        Unit.__init__(self, _health, _speed)

    def skill(self):
        self.speed *= 2


class DwarfUnit(Unit, race.Dwarf):
    def __init__(self, _health, _speed):
        Unit.__init__(self, _health, _speed)

    def skill(self):
        self.damage *= 2
