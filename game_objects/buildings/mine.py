import pygame
import exceptions
import time
from game_objects.buildings import base_building
from typing import *


class Mine(base_building.Building):
    def __init__(self, empire, health, cost: int, image: pygame.Surface, size: Tuple[int, int], reload: int):
        base_building.Building.__init__(self, empire=empire, health=health, cost=cost, size=size, image=image)
        if reload > 0:
            self.reload = reload
        else:
            raise exceptions.CreationError("Can't create mine with reload <= 0")
        self.last_call_time = time.time()

    def mine(self):
        self.empire.resources += 20

    def update(self, *args):
        if time.time() - self.last_call_time > self.reload:
            self.last_call_time = time.time()
            self.mine()


class ElfMine(Mine):
    pass


class OrcMine(Mine):
    pass


class DwarfMine(Mine):
    pass
