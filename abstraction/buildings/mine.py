from abstraction.buildings import base_building


class Mine(base_building.Building):
    def mine(self):
        print("{} is mining".format(self.__class__.__name__))


class ElfMine(Mine):
    pass


class OrcMine(Mine):
    pass


class DwarfMine(Mine):
    pass
