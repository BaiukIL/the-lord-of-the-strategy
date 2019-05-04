from entities import gameobject
from entities.buildings import fabric
from images import image


class CityError(Exception):
    pass


class City(gameobject.RealObject):
    def __init__(self, name, empire):
        gameobject.RealObject.__init__(self, race=empire.race, image_file=image.CITY)
        self._name = name
        self._master_empire = empire
        self._fabric = fabric.Manufacture().create_fabric(self)
        self._buildings = list()

    @property
    def name(self):
        return self._name

    def build_barrack(self):
        building = self._fabric.build_barrack()
        self._buildings.append(building)
        return building

    def build_mine(self):
        building = self._fabric.build_mine()
        self._buildings.append(building)
        return building

    def build_wall(self):
        building = self._fabric.build_wall()
        self._buildings.append(building)
        return building

    def info(self):
        print("City name: {}".format(self._name))
        print("City race: {}".format(self._race))
        if len(self._buildings) == 0:
            print("There're no buildings in this city")
        else:
            print("City buildings:")
            for building in self._buildings:
                print(" - {}".format(building.__class__.__name__))

    def remove_building(self, building):
        if building in self._buildings:
            self._buildings.remove(building)
        else:
            raise CityError("No such building: {} in {}".format(building.__class__.__name__, self._name))

    def react_click(self):
        img = self.image.copy()
        text = ['name: {}'.format(self.name)]
        commands = [['build wall', self.build_wall, image.BUILD],
                    ['build mine', self.build_mine, image.REMOVE],
                    ['build barrack', self.build_barrack, image.ICON],
                    ['remove building', self.remove_building, image.ICON]]
        return img, text, commands
