import pygame
import exceptions
from interface import message
from configs import interface_config
from interface import window
from abc import ABC, abstractmethod
from typing import *


class Button(window.Window, ABC):
    """A window which is located in the middle bottom of the screen.
    Represents commands which selected object has."""

    def __init__(self, image: pygame.Surface, action: Callable, text: Text, interface):
        window.Window.__init__(self, interface_config.COMMAND_SIZE, image)
        self._action = action
        self.activated = False
        self._hint_message = text
        self._interface = interface

    def active(self):
        self.change_state(window.ActiveWindowState(self))
        self.activated = True

    def passive(self):
        self.change_state(window.PassiveWindowState(self))
        self.activated = False

    def click_action(self):
        self._interface.change_selected_command(self)

    def return_click_action(self):
        self._interface.change_selected_command(None)

    def handle_empty_click(self, mouse_pos: Tuple[int, int]):
        pass

    def handle_object_click(self, obj):
        pass

    def execute(self, *args):
        try:
            self._action(*args)
        except exceptions.CreationError as error:
            mes = message.Message(str(error), lifetime=2)
            mes.rect.topleft = self.rect.x, self.rect.y - 70
            self._interface.messages.add(mes)
        finally:
            self.passive()


class NoInteractionButton(Button):
    def click_action(self):
        self._interface.change_selected_command(self)
        self.execute()


class MouseInteractionButton(Button):
    def handle_empty_click(self, mouse_pos: Tuple[int, int]):
        self.execute(mouse_pos)


class ObjectInteractionButton(Button):
    def handle_object_click(self, obj):
        self.execute(obj)
