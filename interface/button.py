import pygame
from abc import ABC
from typing import Tuple, Callable, Text
# project modules #
import exceptions
from interface import message
from interface import click_handler
import configs
from windows import window


class Button(window.Window, ABC):
    """A window which is located in the middle bottom of the screen.
    Represents one of the commands selected object has."""

    def __init__(self, image: pygame.Surface, action: Callable, text: Text):
        window.Window.__init__(self, configs.COMMAND_SIZE, image)
        self._action: Callable = action
        # shows if command is ready to react impact
        self._activated = False
        self._hint_message = text

    def action_while_active(self):
        self._activated = True

    def action_while_passive(self):
        self._activated = False

    def first_click_action(self):
        click_handler.ClickHandler().handle_command_first_click(self)

    def second_click_action(self):
        click_handler.ClickHandler().handle_command_second_click(self)

    def handle_empty_click(self, mouse_pos: Tuple[int, int]):
        pass

    def handle_object_click(self, obj):
        pass

    def execute(self, *args):
        if not self._activated:
            return
        try:
            self._action(*args)
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
