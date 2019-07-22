""" This module contains different race walls which protects empires. """


from game_objects.buildings import base_building


class Wall(base_building.Building):
    """ Cheap builing which is out of methods. Used to protect an empire. """


class ElfWall(Wall):
    pass


class OrcWall(Wall):
    pass


class DwarfWall(Wall):
    pass
