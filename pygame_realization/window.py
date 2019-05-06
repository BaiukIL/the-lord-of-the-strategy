import pygame
from configs import interface_config
from pygame_realization import base_handler


class WindowState:
    """State pattern"""

    def __init__(self, window: 'Window'):
        self._window = window

    def can_handle(self, mouse_pos: tuple) -> bool:
        return False


class HiddenWindowState(WindowState):
    def __init__(self, window):
        super().__init__(window)
        self._window.image.set_alpha(0)


class ActiveWindowState(WindowState):
    def __init__(self, window, bright: int):
        super().__init__(window)
        self._window.image.set_alpha(bright)

    def can_handle(self, mouse_pos: tuple) -> bool:
        return self._window.rect.collidepoint(mouse_pos)


class SelectedWindowState(ActiveWindowState):
    def __init__(self, window):
        super().__init__(window)
        self._window.add_borders()


class Window(pygame.sprite.Sprite, base_handler.BaseHandler):
    """
    Surface extension
    """

    _state: WindowState

    _image: pygame.Surface
    _reset_image: pygame.Surface

    rect: pygame.Rect

    """
    Message which appears when player points to the window
    """
    _hint_message: str = str()

    """
    Indicator: shows if window has borders or not
    """
    _bordered: bool = False
    _borders_size: int = interface_config.BORDERS_SIZE
    _borders_color: pygame.Color = interface_config.BORDERS_COLOR

    def __init__(self, size: tuple):
        pygame.sprite.Sprite.__init__(self)
        self._image = self._reset_image = pygame.Surface(size)
        self.rect = self.image.get_rect()

    def change_state(self, state: WindowState):
        self._state = state

    def hide(self):
        self.change_state(HiddenWindowState(self))

    def active(self, bright: int = 255):
        self.change_state(ActiveWindowState(self, bright))

    def reset(self):
        self.image = self._reset_image

    def set_borders_size(self, size: int):
        self._borders_size = size

    def set_borders_color(self, color: pygame.Color):
        self._borders_color = color

    @property
    def image(self):
        return self._image

    @image.setter
    def image(self, surface: pygame.Surface):
        self._image = surface
        if self._bordered:
            self.add_borders()

    def add_borders(self):
        self._bordered = True
        pygame.draw.rect(self._image, self._borders_color, ((0, 0), self.rect.size), interface_config.BORDERS_SIZE)

    def remove_borders(self):
        self._bordered = False
        # // 2 because borders_size = left_border + right_border
        self._image = self._image.subsurface(
            ((self._borders_size // 2, self._borders_size // 2),
             (self.rect.width - self._borders_size, self.rect.height - self._borders_size)))
        self._image = pygame.transform.scale(self._image, self.rect.size)

    def can_handle(self, mouse_pos: tuple) -> bool:
        return self._state.can_handle(mouse_pos)
