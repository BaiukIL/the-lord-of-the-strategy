""" This module contains different race fabrics which are responsible for buildings creation. """


from abc import ABC, abstractmethod
# project modules #
import image as img
from game_objects import game_objects_configs as configs
from game_objects.buildings import barrack, mine, wall
from game_objects import races


# Abstract Factory.
def create_fabric(empire):
    """ An abstract factory of `fabric` objects. """
    if empire.race == races.ELVES:
        return ElvesFabric(empire)
    if empire.race == races.ORCS:
        return OrcsFabric(empire)
    if empire.race == races.DWARFS:
        return DwarfsFabric(empire)
    raise FabricError(f'{empire} object is not empire instance.')


# Template Method
class Fabric(ABC):
    """ Factory template. Every race fabric creates buildings of appropriate race. """

    def __init__(self, empire):
        self.empire = empire

    @abstractmethod
    def build_barrack(self) -> barrack.Barrack:
        """ Creates and returns barrack. """

    @abstractmethod
    def build_mine(self) -> mine.Mine:
        """ Creates and returns mine. """

    @abstractmethod
    def build_wall(self) -> wall.Wall:
        """ Creates and returns wall. """


class ElvesFabric(Fabric):
    """ Creates elves buildings. """

    def build_barrack(self) -> barrack.Barrack:
        return barrack.ElvesBarrack(health=15,
                                    cost=configs.BARRACK_COST,
                                    empire=self.empire,
                                    image=img.get_image(self.empire).BARRACK,
                                    size=configs.BARRACK_SIZE)

    def build_mine(self) -> mine.Mine:
        return mine.Mine(health=10,
                         reload=60,
                         cost=configs.MINE_COST,
                         empire=self.empire,
                         image=img.get_image(self.empire).MINE,
                         size=configs.MINE_SIZE)

    def build_wall(self) -> wall.Wall:
        return wall.Wall(health=10,
                         cost=configs.WALL_COST,
                         empire=self.empire,
                         image=img.get_image(self.empire).WALL,
                         size=configs.WALL_SIZE)


class OrcsFabric(Fabric):
    """ Creates orcs buildings. """

    def build_barrack(self) -> barrack.Barrack:
        return barrack.OrcsBarrack(health=15,
                                   cost=configs.BARRACK_COST,
                                   empire=self.empire,
                                   image=img.get_image(self.empire).BARRACK,
                                   size=configs.BARRACK_SIZE)

    def build_mine(self) -> mine.Mine:
        return mine.Mine(health=10,
                         reload=60,
                         cost=configs.MINE_COST,
                         empire=self.empire,
                         image=img.get_image(self.empire).MINE,
                         size=configs.MINE_SIZE)

    def build_wall(self) -> wall.Wall:
        return wall.Wall(health=10,
                         cost=configs.WALL_COST,
                         empire=self.empire,
                         image=img.get_image(self.empire).WALL,
                         size=configs.WALL_SIZE)


class DwarfsFabric(Fabric):
    """ Creates dwarfs buildings. """

    def build_barrack(self) -> barrack.Barrack:
        return barrack.DwarfsBarrack(health=30,
                                     cost=configs.BARRACK_COST,
                                     empire=self.empire,
                                     image=img.get_image(self.empire).BARRACK,
                                     size=configs.BARRACK_SIZE)

    def build_mine(self) -> mine.Mine:
        return mine.Mine(health=20,
                         reload=60,
                         cost=configs.MINE_COST,
                         empire=self.empire,
                         image=img.get_image(self.empire).MINE,
                         size=configs.MINE_SIZE)

    def build_wall(self) -> wall.Wall:
        return wall.Wall(health=20,
                         cost=configs.WALL_COST,
                         empire=self.empire,
                         image=img.get_image(self.empire).WALL,
                         size=configs.WALL_SIZE)


class FabricError(Exception):
    pass
