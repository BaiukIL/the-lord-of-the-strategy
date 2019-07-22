""" This module contains `Message` - game info-window. """


import time
from typing import Text
import pygame
# project modules #
from windows.window import Window
from interface import interface_configs as configs


class Message(Window):
    """ A window which represents info and error messages. """

    def __init__(self, text: Text, lifetime: int):
        pixels_per_letter = 9
        pixels_per_line = configs.FONT_SIZE
        gap = 5
        # `gap * 2` means left and right gaps. 
        Window.__init__(self, pygame.Surface(
            (_max_line_length(text) * pixels_per_letter + gap * 2,
             _lines_number(text) * pixels_per_line + gap * 2)))
        self._borders_color = pygame.Color('red')
        self._borders_size = 1
        self.set_constant_bordered()

        font = pygame.font.SysFont(name=configs.FONT_STYLE, size=configs.FONT_SIZE)
        line_pos = [gap, gap]
        for line in text.split('\n'):
            line_surface = font.render(line, True, pygame.Color('red'))
            self.image.blit(line_surface, line_pos)
            line_pos[1] += configs.VERTICAL_LINES_INDENT

        self._creation_time = time.time()
        self.lifetime = lifetime

    def update(self, *args):
        if time.time() - self._creation_time > self.lifetime:
            self.kill()


def _max_line_length(text: Text):
    max_line_length = 0
    for line in text.split('\n'):
        if max_line_length < len(line):
            max_line_length = len(line)
    return max_line_length


def _lines_number(text: Text):
    return len(text.split('\n'))
