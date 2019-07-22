""" This module contains buttons which represent commands in the game. """


from abc import ABC
from typing import Tuple, Callable, Text
import pygame
# project modules #
import exceptions
from interface import message
from interface import click_handler
from interface import interface_configs as configs
from windows import window


class Button(window.Window, ABC):
    """ A window which represents one of the commands selected object has.
    Located in the middle bottom of the screen. """

    def __init__(self, image: pygame.Surface, action: Callable, text: Text):
        window.Window.__init__(self, image, size=configs.COMMAND_SIZE)
        self._action: Callable = action
        # Shows if command is ready to react impact (i.e. if command is selected).
        self._activated = False
        self._hint_message = text

    def action_after_active(self):
        self._activated = True

    def action_after_passive(self):
        self._activated = False

    def first_click_action(self):
        click_handler.ClickHandler().handle_command_first_click(self)

    def second_click_action(self):
        click_handler.ClickHandler().handle_command_second_click(self)

    def handle_empty_click(self, mouse_pos: Tuple[int, int]):
        """ Reaction to empty click (i.e. click no object handled). """

    def handle_object_click(self, obj):
        """ Reaction to object click (i.e. click any of objects handled). """

    def execute(self, *args):
        """ Executes command button contains. """
        if not self._activated:
            return
        try:
            self._action(*args)
        # If command cannot be executed, shows error message.
        except exceptions.CreationError as error:
            msg = message.Message(str(error), lifetime=2)
            msg.rect.topleft = self.rect.x, self.rect.y - 70
            click_handler.ClickHandler().handle_command_bad_execution(msg)
        finally:
            self.passive()


class NoInteractionButton(Button):
    def first_click_action(self):
        click_handler.ClickHandler().handle_command_first_click(self)
        self.execute()


class MouseInteractionButton(Button):
    def handle_empty_click(self, mouse_pos: Tuple[int, int]):
        self.execute(mouse_pos)


class ObjectInteractionButton(Button):
    def handle_object_click(self, obj):
        self.execute(obj)
