import pygame
# project modules #
from interface import button


class SelectedCommand:
    def __init__(self):
        self._command = pygame.sprite.GroupSingle()

    def get(self) -> button.Button or None:
        for command in self._command:
            return command
        return None

    def replace(self, new_command: button.Button):
        for old_command in self._command:
            old_command.passive()
        self._command.add(new_command)
        new_command.active()

    def clear(self):
        self._command.empty()
