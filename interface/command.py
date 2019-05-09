import pygame
from configs import interface_config
from interface import window
from abc import ABC, abstractmethod
from typing import *


class Command(window.Window, ABC):
    """A window which is located in the middle bottom of the screen.
    Represents commands which selected object has."""

    _action: Callable
    activated: bool = False

    def __init__(self, action: Callable, message: Text, icon_file: str):
        window.Window.__init__(self, interface_config.COMMAND_SIZE, pygame.image.load(icon_file))
        self.set_constant_bordered()
        self._action = action
        self._hint_message = message

    def handle(self, mouse_pos: Tuple[int, int]):
        Interface().selected.handle_command_click(self)
        self.activated = True

    def handle_object_click(self, obj):
        pass

    def handle_empty_click(self, mouse_pos: Tuple[int, int]):
        pass

    def execute(self, *args):
        self._action(*args)
        self.activated = False


class UpgradeCommand(Command):
    def handle(self, mouse_pos: Tuple[int, int]):
        self.execute()


class DeleteCommand(Command):
    def handle(self, mouse_pos: Tuple[int, int]):
        self.execute()


class BuildCommand(Command):
    def execute(self, *args):
        self._action(*args)
        self.activated = False


class ObjectInteractionCommand(Command):
    pass
