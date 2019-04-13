from buildings import barrack, mine, wall
import races
import abc


# Abstract Factory
class Manufacture:
    def create_fabric(self, city):
        if city.race == races.elves:
            return ElvesFabric(city)
        elif city.race == races.orcs:
            return OrcsFabric(city)
        elif city.race == races.dwarfs:
            return DwarfsFabric(city)


# Template Method
class Fabric(abc.ABC):
    def __init__(self, city):
        self._master_city = city

    def build_barrack(self) -> barrack.Barrack:
        building = self._build_barrack()
        self._add_to_city_buildings(building)
        return building

    def build_mine(self) -> mine.Mine:
        building = self._build_mine()
        self._add_to_city_buildings(building)
        return building

    def build_wall(self) -> wall.Wall:
        building = self._build_wall()
        self._add_to_city_buildings(building)
        return building

    def _build_barrack(self) -> barrack.Barrack:
        raise NotImplementedError

    def _build_mine(self) -> mine.Mine:
        raise NotImplementedError

    def _build_wall(self) -> wall.Wall:
        raise NotImplementedError

    def _add_to_city_buildings(self, building):
        self._master_city._buildings.append(building)


class ElvesFabric(Fabric):
    def _build_barrack(self) -> barrack.Barrack:
        return barrack.Barrack(health=10, city=self._master_city)

    def _build_mine(self) -> mine.Mine:
        return mine.Mine(health=5, city=self._master_city)

    def _build_wall(self) -> wall.Wall:
        return wall.Wall(health=3, city=self._master_city)


class OrcsFabric(Fabric):
    def _build_barrack(self) -> barrack.Barrack:
        return barrack.Barrack(health=10, city=self._master_city)

    def _build_mine(self) -> mine.Mine:
        return mine.Mine(health=5, city=self._master_city)

    def _build_wall(self) -> wall.Wall:
        return wall.Wall(health=3, city=self._master_city)


class DwarfsFabric(Fabric):
    def _build_barrack(self) -> barrack.Barrack:
        return barrack.Barrack(health=15, city=self._master_city)

    def _build_mine(self) -> mine.Mine:
        return mine.Mine(health=8, city=self._master_city)

    def _build_wall(self) -> wall.Wall:
        return wall.Wall(health=5, city=self._master_city)
