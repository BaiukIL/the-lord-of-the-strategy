""" This module contains `Camera` - an actual game display. """


from typing import Tuple
import pygame
# project modules #
from interface import interface_configs as configs
from world_map import Map


class Camera(pygame.Rect):
    """ A frame within which player can see game changes. """

    def __init__(self):
        super().__init__(configs.CAMERA_START_POS, configs.SCR_SIZE)
        self._speed = configs.CAMERA_SPEED

    def move_view(self, key, mouse_pos: Tuple[int, int]):
        """ Moves camera if mouse is close to screen borders, 
        or if appropriate keyboard buttons are pressed. """

        if key[pygame.K_w] or mouse_pos[1] == 0:
            self.y -= self._speed
        if key[pygame.K_s] or mouse_pos[1] == configs.SCR_HEIGHT - 1:
            self.y += self._speed
        if key[pygame.K_a] or mouse_pos[0] == 0:
            self.x -= self._speed
        if key[pygame.K_d] or mouse_pos[0] == configs.SCR_WIDTH - 1:
            self.x += self._speed
        self._fix_collision_with_map()

    def _fix_collision_with_map(self):
        """ Checks map borders collision. """
        if self.left < 0:
            self.left = 0
        elif self.right > Map().rect.right:
            self.right = Map().rect.right
        if self.bottom > Map().rect.bottom:
            self.bottom = Map().rect.bottom
        elif self.top < 0:
            self.top = 0
