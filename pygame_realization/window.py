import pygame
from configs import game_config


def border(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return result
    return wrapper


# State
class WindowState:
    def __init__(self, window):
        self._window = window


class HiddenWindowState(WindowState):
    def __init__(self, window):
        super().__init__(window)
        self._window.set_alpha(0)


class VisibleWindowState(WindowState):
    def __init__(self, window):
        super().__init__(window)
        self._window.fill(game_config.BLACK)
        self._window.set_alpha(150)


class Window(pygame.Surface):
    """
    Surface superstructure
    """
    _state: WindowState

    rect = pygame.Rect(0, 0, 0, 0)

    """
    Message which appears while player points to the window
    """
    _hint_message: str

    def __init__(self, size: int, message: str = str(), visible: bool = False):
        super().__init__(size)
        self._hint_message = message
        if visible:
            self._state = VisibleWindowState(self)
        else:
            self._state = HiddenWindowState(self)

    def change_state(self, state: WindowState):
        self._state = state

    def hide(self):
        self.change_state(HiddenWindowState(self))

    def visible(self):
        self.change_state(VisibleWindowState(self))


class Ability(Window):
    def _handle_click(self, *args):
        pass
