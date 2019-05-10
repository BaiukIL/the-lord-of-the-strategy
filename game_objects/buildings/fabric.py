from game_objects.buildings import barrack, mine, wall
from game_objects import races
from abc import ABC, abstractmethod
from images import image as img


class Manufacture:
    """Abstract Factory"""

    def create_fabric(self, empire):
        if empire.race == races.ELVES:
            return ElvesFabric(empire)
        elif empire.race == races.ORCS:
            return OrcsFabric(empire)
        elif empire.race == races.DWARFS:
            return DwarfsFabric(empire)


class Fabric(ABC):
    """Template Method"""

    def __init__(self, empire):
        self.empire = empire

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
        return barrack.ElvesBarrack(health=10, 
                                    empire=self.empire, 
                                    image=img.get_image(self.empire).BARRACK,
                                    size=(200, 200))

    def build_mine(self) -> mine.Mine:
        return mine.Mine(health=5,
                         empire=self.empire,
                         image=img.get_image(self.empire).MINE,
                         size=(200, 200))

    def build_wall(self) -> wall.Wall:
        return wall.Wall(health=3, 
                         empire=self.empire, 
                         image=img.get_image(self.empire).WALL,
                         size=(50, 200))


class OrcsFabric(Fabric):
    def build_barrack(self) -> barrack.Barrack:
        return barrack.OrcsBarrack(health=10, 
                                   empire=self.empire, 
                                   image=img.get_image(self.empire).BARRACK,
                                   size=(200, 200))

    def build_mine(self) -> mine.Mine:
        return mine.Mine(health=5, 
                         empire=self.empire, 
                         image=img.get_image(self.empire).MINE,
                         size=(200, 200))

    def build_wall(self) -> wall.Wall:
        return wall.Wall(health=3, 
                         empire=self.empire, 
                         image=img.get_image(self.empire).WALL,
                         size=(10, 50))


class DwarfsFabric(Fabric):
    def build_barrack(self) -> barrack.Barrack:
        return barrack.DwarfsBarrack(health=15, 
                                     empire=self.empire, 
                                     image=img.get_image(self.empire).BARRACK,
                                     size=(200, 200))

    def build_mine(self) -> mine.Mine:
        return mine.Mine(health=8, 
                         empire=self.empire, 
                         image=img.get_image(self.empire).MINE,
                         size=(200, 200))

    def build_wall(self) -> wall.Wall:
        return wall.Wall(health=5, 
                         empire=self.empire, 
                         image=img.get_image(self.empire).WALL,
                         size=(10, 50))
