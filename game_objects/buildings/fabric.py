from game_objects.buildings import barrack, mine, wall
from game_objects import races
from abc import ABC, abstractmethod
from images import image


class Manufacture:
    """Abstract Factory"""

    def create_fabric(self, city):
        if city.empire.race == races.ELVES:
            return ElvesFabric(city)
        elif city.empire.race == races.ORCS:
            return OrcsFabric(city)
        elif city.empire.race == races.DWARFS:
            return DwarfsFabric(city)


class Fabric(ABC):
    """Template Method"""

    def __init__(self, city):
        self.city = city

    @abstractmethod
    def build_barrack(self) -> barrack.Barrack:
        pass

    @abstractmethod
    def build_mine(self) -> mine.Mine:
        pass

    @abstractmethod
    def build_wall(self) -> wall.Wall:
        pass


class ElvesFabric(Fabric):
    def build_barrack(self) -> barrack.Barrack:
        return barrack.ElvesBarrack(health=10, empire=self.city, image_file=image.ELVES_BARRACK, size=(200, 200))

    def build_mine(self) -> mine.Mine:
        return mine.Mine(health=5, empire=self.city, image_file=image.ELVES_MINE, size=(200, 200))

    def build_wall(self) -> wall.Wall:
        return wall.Wall(health=3, empire=self.city, image_file=image.ELVES_WALL, size=(10, 50))


class OrcsFabric(Fabric):
    def build_barrack(self) -> barrack.Barrack:
        return barrack.OrcsBarrack(health=10, empire=self.city, image_file=image.ORCS_BARRACK, size=(200, 200))

    def build_mine(self) -> mine.Mine:
        return mine.Mine(health=5, empire=self.city, image_file=image.ORCS_MINE, size=(200, 200))

    def build_wall(self) -> wall.Wall:
        return wall.Wall(health=3, empire=self.city, image_file=image.ORCS_WALL, size=(10, 50))


class DwarfsFabric(Fabric):
    def build_barrack(self) -> barrack.Barrack:
        return barrack.DwarfsBarrack(health=15, empire=self.city, image_file=image.DWARFS_BARRACK, size=(200, 200))

    def build_mine(self) -> mine.Mine:
        return mine.Mine(health=8, empire=self.city, image_file=image.DWARFS_MINE, size=(200, 200))

    def build_wall(self) -> wall.Wall:
        return wall.Wall(health=5, empire=self.city, image_file=image.DWARFS_WALL, size=(10, 50))
