""" This module contains `SelectedInfo` which shows selected object information. """


from typing import Text
import pygame
# project modules #
from windows import window
from interface import interface_configs as configs


class SelectedInfo(window.Window):
    """ A window which is responsible for showing selected object information.
    Located in the left bottom corner of the screen. """

    def __init__(self):
        window.Window.__init__(self, pygame.Surface(
            configs.SELECTED_SIZE, pygame.SRCALPHA))

        self.selected_object = pygame.sprite.GroupSingle()
        self._font = pygame.font.SysFont(
            name=configs.FONT_STYLE, size=configs.FONT_SIZE)

        self.background_color = (200, 200, 100)
        self.rect.bottomleft = (0, configs.SCR_HEIGHT)
        self.borders_size = 3
        self.set_constant_bordered()
        self.hide()

    def replace(self, obj):
        """ Replaces old object info with new one. """
        self.selected_object.add(obj)
        self.active()

    def action_after_hide(self):
        self.clear()

    def action_after_active(self):
        self._place_object_info()

    def _place_object_info(self):
        background = pygame.Surface(self.rect.size)
        background.fill(self.background_color)
        self.reset_image(background)
        self._place_image(self.selected_object.sprite._default_image)
        self._place_text(self.selected_object.sprite.info())

    def _place_image(self, image: pygame.Surface):
        selected_img_side_size = min(self.rect.width // 2, self.rect.height // 2)
        self.image.blit(
            pygame.transform.scale(
                image, (selected_img_side_size, selected_img_side_size)),
            (self.rect.width // 2 - 5, self.rect.height // 2 - 5))

    def _place_text(self, text: Text):
        line_pos = [5, 5]
        for line in text.split('\n'):
            self.image.blit(self._font.render(line, True, pygame.Color('black')), line_pos)
            line_pos[1] += configs.VERTICAL_LINES_INDENT

    def action_while_update(self):
        if self.is_active():
            self._place_object_info()
