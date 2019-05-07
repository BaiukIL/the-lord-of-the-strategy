import pygame
from configs import interface_config
import templates
from typing import *


class WindowState:
    """State pattern"""

    def __init__(self, window: 'Window'):
        self._window = window

    def can_handle(self, mouse_pos: Tuple[int, int]) -> bool:
        return False


class HiddenWindowState(WindowState):
    def __init__(self, window: 'Window'):
        super().__init__(window)
        self._window.image.set_alpha(0)


class ActiveWindowState(WindowState):
    def __init__(self, window: 'Window', bright: int):
        super().__init__(window)
        self._window.image.set_alpha(bright)

    def can_handle(self, mouse_pos: Tuple[int, int]) -> bool:
        if self._window.rect.collidepoint(mouse_pos):
            return True
        return False


class SelectedWindowState(ActiveWindowState):
    def __init__(self, window: 'Window', bright: int = 255):
        super().__init__(window, bright)
        self._window.add_borders()


class Window(pygame.sprite.Sprite, templates.Handler):
    """Surface extension"""

    _state: WindowState

    """Full image and its rectangle. Used by Group to draw.
    Important: this field is used by Groups.
    Use inner_image.blit() to draw something on Window"""
    image: pygame.Surface
    rect: pygame.Rect

    """Pure image, i.e. without borders and other stuff"""
    inner_image: pygame.Surface

    """Default image"""
    _reset_image: pygame.Surface

    """Message which appears when player points to the window"""
    _hint_message: str = None

    """Indicator: shows if window has borders or not"""
    bordered: bool = False
    borders_size: int = interface_config.BORDERS_SIZE
    borders_color: pygame.Color = interface_config.BORDERS_COLOR

    def __init__(self, size: Tuple[int, int], image: pygame.Surface = None):
        pygame.sprite.Sprite.__init__(self)
        if image is not None:
            self.image = pygame.transform.scale(image, size)
        else:
            self.image = pygame.Surface(size)
        self.inner_image = self.image.copy()
        self._reset_image = self.image.copy()
        self.rect = self.image.get_rect()
        self.active()

    def change_state(self, state: WindowState):
        self._state = state

    def hide(self):
        self.change_state(HiddenWindowState(self))

    def reset(self):
        self.image = self._reset_image.copy()

    def active(self, bright: int = 255):
        self.change_state(ActiveWindowState(self, bright))

    def add_borders(self):
        if not self.bordered:
            self.bordered = True
            self.inner_image = self.image.copy()
            self.image.fill((0, 0, 0, 0))
            pygame.draw.rect(self.image, self.borders_color, ((0, 0), self.rect.size), self.borders_size)
            # self.inner_image = self.image.subsurface(
            #     ((self.borders_size // 2, self.borders_size // 2),
            #      (self.rect.width - self.borders_size, self.rect.height - self.borders_size)))

            # // 2 because borders_size = left_border + right_border
            self.image.blit(self.inner_image, (self.borders_size // 2, self.borders_size // 2))

    def remove_borders(self):
        if self.bordered:
            self.bordered = False
            self.image.blit(self.inner_image, (0, 0))

    def can_handle(self, mouse_pos: Tuple[int, int]) -> bool:
        return self._state.can_handle(mouse_pos)
