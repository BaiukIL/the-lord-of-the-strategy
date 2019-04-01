import building_factory
import races


class City:
    def __init__(self, _race, name, empire):
        self.race = _race
        self.name = name
        self.master_empire = empire
        self.buildings = list()


    def info(self):
        print("City race: {}".format(self.race.__name__))
        print("City name: {}".format(self.name))
        if len(self.buildings) == 0:
            print("There're no buildings in this city")
        else:
            print("City buildings:")
            for building in self.buildings:
                print(" - {}".format(building.__class__.__name__))

    def build_barrack(self):
        self.buildings.append(self.factory.build_barrack())

    def build_mine(self, strength):
        self.buildings.append(self.factory.build_mine(strength))

    def build_wall(self, strength):
        self.buildings.append(self.factory.build_wall(strength))

    def remove_building(self, building):
        self.buildings.remove(building)
