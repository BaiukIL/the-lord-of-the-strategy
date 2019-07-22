""" This module contains `Minimap` - window which is a brief version of the map. """


from typing import Tuple
import pygame
# project modules #
from interface import interface_configs as configs
from windows.window import Window
from world_map import Map
import game


class Minimap(Window):
    """ A window which is a brief version of the map.
    Located in the right bottom of the screen. """

    def __init__(self):
        Window.__init__(self, Map().image, configs.MINIMAP_SIZE)

        self.borders_size = 3
        self.rect.bottomright = configs.SCR_SIZE
        self.set_constant_bordered()
        # `frame` on the minimap is a camera position on the map.
        self._frame = pygame.Rect(
            (0, 0), self._convert_to_minimap_coordinates(configs.SCR_SIZE))

    def move_frame(self, pos: Tuple[int, int]):
        """ Moves frame at `pos` position.
        `pos` must be real map position i.e. position with a glance to current camera offset. """
        self._frame.topleft = self._convert_to_minimap_coordinates(pos)

    def action_while_update(self):
        """ Blits all game objects' minimap icons onto minimap. """
        self.reset_image(self._default_image.copy())
        for obj in game.Game().objects:
            self.image.blit(
                obj.minimap_image, self._convert_to_minimap_coordinates(obj.rect.topleft))
        # Draw frame.
        pygame.draw.rect(self.image, self.borders_color, self._frame, 1)

    def _convert_to_minimap_coordinates(self, pos: Tuple[int, int]) -> Tuple[int, int]:
        """ Converts global map position (`pos`) to minimap position. """
        x = pos[0] * self.rect.width // Map().rect.width
        y = pos[1] * self.rect.height // Map().rect.height
        return (x, y)

    def _convert_to_minimap_size(self, size: Tuple[int, int]) -> Tuple[int, int]:
        """ Converts real object size to its minimap size. """
        width = size[0] * self.rect.width // Map().rect.width
        height = size[1] * self.rect.height // Map().rect.height
        return (width, height)
