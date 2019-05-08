import pygame
from configs import interface_config
import templates
from abc import ABC
from typing import *


class WindowState(ABC):
    """State pattern"""

    def __init__(self, window: 'Window'):
        self._window = window

    def can_handle(self, mouse_pos: Tuple[int, int]) -> bool:
        if self._window.rect.collidepoint(mouse_pos):
            return True
        return False


class HiddenWindowState(WindowState):
    def __init__(self, window: 'Window'):
        super().__init__(window)
        self._window._image.set_alpha(0)
        self._window.remove_borders()

    def can_handle(self, mouse_pos: Tuple[int, int]) -> bool:
        return False


class PassiveWindowState(WindowState):
    def __init__(self, window: 'Window'):
        super().__init__(window)
        self._window._image.set_alpha(self._window._default_alpha)
        self._window.remove_borders()


class ActiveWindowState(WindowState):
    def __init__(self, window: 'Window'):
        super().__init__(window)
        self._window._image.set_alpha(self._window._default_alpha)
        self._window.add_borders()


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
    _borders_size: int = interface_config.BORDERS_SIZE
    _borders_color: pygame.Color = interface_config.BORDERS_COLOR

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

    @property
    def image(self):
        """Used by Groups"""
        if self._bordered:
            image = pygame.Surface(self.rect.size, pygame.SRCALPHA)
            compressed_image = pygame.transform.scale(self._image, (self.rect.width - self._borders_size,
                                                                    self.rect.height - self._borders_size))
            pygame.draw.rect(image, self._borders_color, [0, 0, self.rect.width, self.rect.height], self._borders_size)
            # // 2 because borders_size = left_border + right_border
            image.blit(compressed_image, (self._borders_size // 2, self._borders_size // 2))
        else:
            image = self._image
        return image

    @image.setter
    def image(self, surface: pygame.Surface):
        self._image = surface.copy()

    def change_state(self, state: WindowState):
        self._state = state

    def hide(self):
        self.change_state(HiddenWindowState(self))

    def passive(self):
        self.change_state(PassiveWindowState(self))

    def active(self):
        self.change_state(ActiveWindowState(self))

    def clear(self):
        # self._image = pygame.Surface(self.rect.size, pygame.SRCALPHA)
        self._image.fill((0, 0, 0, 0))

    def add_borders(self):
        self._bordered = True

    def remove_borders(self):
        self._bordered = False

    def can_handle(self, mouse_pos: Tuple[int, int]) -> bool:
        return self._state.can_handle(mouse_pos)
