import health
import logging
from abc import abstractmethod


class BuildingBuilder:
    # methods for Building creation
    pass


class Building(health.Health):
    def __init__(self, city, strength):
        health.Health.__init__(self, strength)
        self.master_city = city
        logging.info("{} is created".format(self.__class__.__name__))

    def update(self):
        pass
        logging.info("{} has been updated!".format(self.__class__.__name__))

    def _destroy(self):
        self.master_city.remove_building()
        logging.info("{} has been destroyed".format(self.__class__.__name__))


class BarrackBuilder:
    # methods for Barrack creation
    pass


# fabric of units
class Barrack(Building):
    def __init__(self, strength):
        Building.__init__(self, strength)

    def add_unit_to_army(self, unit):
        self.master_city.master_empire.army.recruit(unit)

    @abstractmethod
    def create_scout(self):
        pass

    @abstractmethod
    def create_builder(self):
        pass

    @abstractmethod
    def create_warrior(self):
        pass


class MineBuilder:
    # methods for Mine creation
    pass


class Mine(Building):
    def __init__(self, strength):
        Building.__init__(self, strength)

    def mine(self):
        logging.info("{} is mining".format(self.__class__.__name__))


class WallBuilder:
    # methods for Wall creation
    pass


class WallDirector:
    def build_elf_wall(self):
        pass

    def build_orc_wall(self):
        pass

    def build_dwarf_wall(self):
        pass


class Wall(Building):
    def __init__(self, strength):
        Building.__init__(self, strength)

    def update(self):
        pass
        logging.info("{} is updated".format(self.__class__.__name__))
