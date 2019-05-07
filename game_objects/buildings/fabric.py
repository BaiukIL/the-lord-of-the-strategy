from game_objects.buildings import barrack, mine, wall
from game_objects import races
from abc import ABC, abstractmethod
from images import image


class Manufacture:
    """Abstract Factory"""

    def create_fabric(self, city):
        if city.race == races.ELVES:
            return ElvesFabric(city)
        elif city.race == races.ORCS:
            return OrcsFabric(city)
        elif city.race == races.DWARFS:
            return DwarfsFabric(city)


class Fabric(ABC):
    """Template Method"""

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
        return barrack.ElvesBarrack(health=10, city=self._master_city, image_file=image.ELVES_BARRACK)

    def build_mine(self) -> mine.Mine:
        return mine.Mine(health=5, city=self._master_city, image_file=image.ELVES_MINE)

    def build_wall(self) -> wall.Wall:
        return wall.Wall(health=3, city=self._master_city, image_file=image.ELVES_WALL)


class OrcsFabric(Fabric):
    def build_barrack(self) -> barrack.Barrack:
        return barrack.OrcsBarrack(health=10, city=self._master_city, image_file=image.ORCS_BARRACK)

    def build_mine(self) -> mine.Mine:
        return mine.Mine(health=5, city=self._master_city, image_file=image.ORCS_MINE)

    def build_wall(self) -> wall.Wall:
        return wall.Wall(health=3, city=self._master_city, image_file=image.ORCS_WALL)


class DwarfsFabric(Fabric):
    def build_barrack(self) -> barrack.Barrack:
        return barrack.DwarfsBarrack(health=15, city=self._master_city, image_file=image.DWARFS_BARRACK)

    def build_mine(self) -> mine.Mine:
        return mine.Mine(health=8, city=self._master_city, image_file=image.DWARFS_MINE)

    def build_wall(self) -> wall.Wall:
        return wall.Wall(health=5, city=self._master_city, image_file=image.DWARFS_WALL)
