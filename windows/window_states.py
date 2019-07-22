""" This module contains `hidden`, `passive` and `active` window states. """


from abc import ABC
from typing import Tuple


# State pattern.
class WindowState(ABC):
    """ Base class of window states. """

    def __init__(self, window):
        self.window = window

    def can_handle(self, mouse_pos: Tuple[int, int]) -> bool:
        """ Return true if window can handle mouse click. """
        return self.window.rect.collidepoint(mouse_pos)

    def handle(self, mouse_pos: Tuple[int, int]):
        """ Action window does when it can handle mouse click. """


class HiddenWindowState(WindowState):
    """ Class represents `hidden` window state. """

    def __init__(self, window):
        super().__init__(window)
        # In hidden state window is invisible.
        self.window.image.set_alpha(0)

    def can_handle(self, mouse_pos: Tuple[int, int]) -> bool:
        return False


class PassiveWindowState(WindowState):
    """ Class represents `passive` window state. """

    def __init__(self, window):
        super().__init__(window)
        self.window.image.set_alpha(self.window._default_alpha)
        # In passive state window doesn't have borders.
        self.window.remove_borders()

    def handle(self, mouse_pos: Tuple[int, int]):
        self.window.active()
        self.window.first_click_action()


class ActiveWindowState(WindowState):
    """ Class represents `active` window state. """

    def __init__(self, window):
        super().__init__(window)
        self.window.image.set_alpha(self.window._default_alpha)
        # In active state window has borders.
        self.window.add_borders()

    def handle(self, mouse_pos: Tuple[int, int]):
        self.window.passive()
        # If window is in active state, then it was clicked once.
        # Thus next click is second, so call second click action while clicked.
        self.window.second_click_action()
