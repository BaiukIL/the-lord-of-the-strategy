from abstraction.buildings import barrack, mine, wall
from abstraction import races
from abc import ABC, abstractmethod


# Abstract Factory
class Manufacture:
    def create_fabric(self, city):
        if city.race == races.elves:
            return ElvesFabric(city)
        elif city.race == races.orcs:
            return OrcsFabric(city)
        elif city.race == races.dwarfs:
            return DwarfsFabric(city)


# Template Method ???
class Fabric(ABC):
    def __init__(self, city):
        self._master_city = city

    @abstractmethod
    def build_barrack(self) -> barrack.Barrack: pass

    @abstractmethod
    def build_mine(self) -> mine.Mine: pass

    @abstractmethod
    def build_wall(self) -> wall.Wall: pass


class ElvesFabric(Fabric):
    def build_barrack(self) -> barrack.Barrack:
        return barrack.ElvesBarrack(health=10, city=self._master_city)

    def build_mine(self) -> mine.Mine:
        return mine.Mine(health=5, city=self._master_city)

    def build_wall(self) -> wall.Wall:
        return wall.Wall(health=3, city=self._master_city)


class OrcsFabric(Fabric):
    def build_barrack(self) -> barrack.Barrack:
        return barrack.OrcsBarrack(health=10, city=self._master_city)

    def build_mine(self) -> mine.Mine:
        return mine.Mine(health=5, city=self._master_city)

    def build_wall(self) -> wall.Wall:
        return wall.Wall(health=3, city=self._master_city)


class DwarfsFabric(Fabric):
    def build_barrack(self) -> barrack.Barrack:
        return barrack.DwarfsBarrack(health=15, city=self._master_city)

    def build_mine(self) -> mine.Mine:
        return mine.Mine(health=8, city=self._master_city)

    def build_wall(self) -> wall.Wall:
        return wall.Wall(health=5, city=self._master_city)
