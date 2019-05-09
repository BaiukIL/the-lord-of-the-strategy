import pygame
from configs import interface_config
import templates
from abc import ABC
from typing import *


class WindowException(Exception):
    pass


class WindowState(ABC):
    """State pattern"""

    _window: 'Window'

    def __init__(self, window: 'Window'):
        self._window = window

    def can_handle(self, mouse_pos: Tuple[int, int]) -> bool:
        if self._window.rect.collidepoint(mouse_pos):
            return True
        return False

    def handle(self, mouse_pos: Tuple[int, int]):
        pass


class HiddenWindowState(WindowState):
    def __init__(self, window: 'Window'):
        super().__init__(window)
        self._window._image.set_alpha(0)

    def can_handle(self, mouse_pos: Tuple[int, int]) -> bool:
        return False


class PassiveWindowState(WindowState):
    def __init__(self, window: 'Window'):
        super().__init__(window)
        self._window._image.set_alpha(self._window._default_alpha)
        self._window.remove_borders()

    def handle(self, mouse_pos: Tuple[int, int]):
        self._window.active()
        self._window.click_action()


class ActiveWindowState(WindowState):
    def __init__(self, window: 'Window'):
        super().__init__(window)
        self._window._image.set_alpha(self._window._default_alpha)
        self._window.add_borders()

    def handle(self, mouse_pos: Tuple[int, int]):
        self._window.passive()
        self._window.return_click_action()


class Window(pygame.sprite.Sprite, templates.Handler):
    """Surface extension"""

    _state: WindowState

    _image: pygame.Surface
    rect: pygame.Rect

    """Message which appears when player points to the window"""
    _hint_message: str = None

    _default_alpha: int = 255

    """Indicator: shows if window has borders or not"""
    _bordered: bool = False

    """If True, borders will never disappear"""
    _constant_bordered: bool = False

    """If False, borders will never appear"""
    _never_bordered: bool = False

    _borders_size: int = interface_config.BORDERS_SIZE
    _borders_color = interface_config.BORDERS_COLOR

    def __init__(self, size: Tuple[int, int], image: pygame.Surface = None):
        pygame.sprite.Sprite.__init__(self)
        if image is not None:
            self._image = pygame.transform.scale(image, size)
        else:
            self._image = pygame.Surface(size, pygame.SRCALPHA)
        self.rect = self._image.get_rect()
        self.passive()

    def set_default_alpha(self, alpha: int):
        self._default_alpha = alpha
        self._image.set_alpha(alpha)

    def set_constant_bordered(self):
        if self._constant_bordered:
            raise WindowException("Contradictory borders settings")
        self._constant_bordered = True
        self.add_borders()

    def set_never_bordered(self):
        if self._constant_bordered:
            raise WindowException("Contradictory borders settings")
        self._never_bordered = True
        self.remove_borders()

    @property
    def image(self):
        """Used by Groups"""
        if self._bordered:
            image = pygame.Surface(self.rect.size, pygame.SRCALPHA)
            image.set_alpha(self._image.get_alpha())
            compressed_image = pygame.transform.scale(self._image, (self.rect.width - self._borders_size,
                                                                    self.rect.height - self._borders_size))
            pygame.draw.rect(image, self._borders_color, [0, 0, self.rect.width, self.rect.height], self._borders_size)
            # // 2 because borders_size = left_border + right_border
            image.blit(compressed_image, (self._borders_size // 2, self._borders_size // 2))
        else:
            image = self._image
        return image

    def change_state(self, state: WindowState):
        self._state = state

    def hide(self):
        self.change_state(HiddenWindowState(self))

    def passive(self):
        self.change_state(PassiveWindowState(self))

    def active(self):
        self.change_state(ActiveWindowState(self))

    def clear(self):
        self._image.fill((0, 0, 0, 0))

    def add_borders(self):
        if not self._never_bordered:
            self._bordered = True

    def remove_borders(self):
        if not self._constant_bordered:
            self._bordered = False

    def can_handle(self, mouse_pos: Tuple[int, int]) -> bool:
        return self._state.can_handle(mouse_pos)

    def handle(self, mouse_pos: Tuple[int, int]):
        self._state.handle(mouse_pos)

    def click_action(self):
        """Empty method which can be overridden.
        It's called when window is clicked in passive state"""
        pass

    def return_click_action(self):
        """Empty method which can be overridden.
        It's called when window is clicked in active state"""
        pass
