""" This module contains `Building` which is base class for game buildings. """


from abc import ABC
from game_objects import base_object


class Building(base_object.GameObject, ABC):
    """ Currently, it is empty class, but in the future
    there are might be some methods common for all buildings. """
