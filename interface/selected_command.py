""" This module contains `SelectedCommand` which keeps track of last choosen selected command. """


import pygame
# project modules #
from interface import button


class SelectedCommand:
    """ Keeps track of last choosen (selected) command. """

    def __init__(self):
        self._command = pygame.sprite.GroupSingle()

    def get(self) -> button.Button or None:
        """ Returns selected command if it exists or `None` otherwise. """
        for command in self._command:
            return command
        return None

    def replace(self, new_command: button.Button):
        """ Replace current command with `new_command`. """
        for old_command in self._command:
            old_command.passive()
        self._command.add(new_command)
        new_command.active()

    def clear(self):
        """ Clear selected command (i.e. there is no selected command after this action). """
        for old_command in self._command:
            old_command.passive()
        self._command.empty()
