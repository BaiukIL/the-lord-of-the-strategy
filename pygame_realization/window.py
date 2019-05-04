import pygame
from configs import interface_config


def add_borders(window: 'Window', borders_size: int = interface_config.BORDERS_SIZE) -> 'Window':
    """Decorator"""
    compressed_image = pygame.transform.scale(
        window.image, (window.image.get_width() - borders_size * 2,
                       window.image.get_height() - borders_size * 2)
    )
    window.image.fill(interface_config.BORDERS_COLOR)
    window.image.blit(compressed_image, (borders_size, borders_size))
    return window


class WindowState:
    """State pattern"""
    def __init__(self, window: 'Window'):
        self._window = window


class HiddenWindowState(WindowState):
    def __init__(self, window):
        super().__init__(window)
        self._window.image.set_alpha(0)


class VisibleWindowState(WindowState):
    def __init__(self, window, bright: int):
        super().__init__(window)
        # self._window.image.fill(game_config.BLACK)
        self._window.image.set_alpha(bright)


class Window(pygame.sprite.Sprite):
    """
    Surface superstructure
    """

    _state: WindowState

    image: pygame.Surface
    rect: pygame.Rect

    """
    Message which appears when player points to the window
    """
    _hint_message: str
    _bordered: bool

    def __init__(self, size: tuple, message: str = str()):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface(size)
        self.rect = self.image.get_rect()
        self._hint_message = message
        self.visible()

    def change_state(self, state: WindowState):
        self._state = state

    def hide(self):
        self.change_state(HiddenWindowState(self))

    def visible(self, bright: int = 255):
        self.change_state(VisibleWindowState(self, bright))
