""" This module contains different race mines which mine game resources. """


import time
from typing import Tuple
import pygame
# project modules #
import exceptions
from game_objects.buildings import base_building


class Mine(base_building.Building):
    """ Mines resources. """

    def __init__(self, empire, health, cost: int, image: pygame.Surface, size: Tuple[int, int], reload: int):
        base_building.Building.__init__(
            self, empire=empire, health=health, cost=cost, size=size, image=image)
        if reload > 0:
            self.reload = reload
        else:
            raise exceptions.CreationError(
                "Can't create mine with reload <= 0.")
        self.last_call_time = time.time()

    def mine(self):
        """ Increases empire resources. """
        self.empire.resources += 5

    def action_while_update(self):
        if time.time() - self.last_call_time > self.reload:
            self.last_call_time = time.time()
            self.mine()


class ElfMine(Mine):
    pass


class OrcMine(Mine):
    pass


class DwarfMine(Mine):
    pass
