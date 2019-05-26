import pygame
import time
from typing import Tuple
# project modules #
import configs
from windows import window_states


class Window(pygame.sprite.Sprite):
    """Surface extension"""

    _state: window_states.WindowState

    # Message which appears when player points to the window
    _hint_message = None

    _default_alpha = 255

    # Indicator: shows if window has borders or not
    _bordered = False

    # If True, borders will never disappear
    _constant_bordered = False

    # If False, borders will never appear
    _never_bordered = False

    _borders_size = configs.BORDERS_SIZE
    _borders_color = configs.BORDERS_COLOR

    def __init__(self, size: Tuple[int, int], image: pygame.Surface = None):
        pygame.sprite.Sprite.__init__(self)
        if image is not None:
            self.real_image = pygame.transform.scale(image, size)
        else:
            self.real_image = pygame.Surface(size, pygame.SRCALPHA)
        self.rect = self.real_image.get_rect()
        self._draw_image = self.real_image
        self.passive()
        self._tmp_delay = 0
        self._last_tmp_time = 0

    def set_default_alpha(self, alpha: int):
        self._default_alpha = alpha
        self.real_image.set_alpha(alpha)

    def set_constant_bordered(self):
        if self._constant_bordered:
            raise WindowError("Contradictory borders settings")
        self._constant_bordered = True
        self.add_borders()

    def set_never_bordered(self):
        if self._constant_bordered:
            raise WindowError("Contradictory borders settings")
        self._never_bordered = True
        self.remove_borders()

    def set_temporary_image(self, image: pygame.Surface, delay: float):
        self._draw_image = image
        self._tmp_delay = delay
        self._last_tmp_time = time.time()

    @property
    def image(self):
        """Used by Groups"""
        if self._bordered:
            image = pygame.Surface(self.rect.size, pygame.SRCALPHA)
            image.set_alpha(self._draw_image.get_alpha())
            compressed_draw_image = pygame.transform.scale(self._draw_image, (self.rect.width - self._borders_size,
                                                                              self.rect.height - self._borders_size))
            pygame.draw.rect(image, self._borders_color, [0, 0, self.rect.width, self.rect.height], self._borders_size)
            # // 2 because borders_size = left_border + right_border
            image.blit(compressed_draw_image, (self._borders_size // 2, self._borders_size // 2))
        else:
            image = self._draw_image
        return image

    def change_state(self, state: window_states.WindowState):
        self._state = state

    def hide(self):
        self.change_state(window_states.HiddenWindowState(self))
        self.action_while_hide()

    def action_while_hide(self):
        pass

    def passive(self):
        self.change_state(window_states.PassiveWindowState(self))
        self.action_while_passive()

    def action_while_passive(self):
        pass

    def active(self):
        self.change_state(window_states.ActiveWindowState(self))
        self.action_while_active()

    def action_while_active(self):
        pass

    def clear(self):
        self.real_image.fill((0, 0, 0, 0))

    def add_borders(self):
        if not self._never_bordered:
            self._bordered = True

    def remove_borders(self):
        if not self._constant_bordered:
            self._bordered = False

    def handle_click(self, mouse_pos: Tuple[int, int]) -> bool:
        if self.can_handle_click(mouse_pos):
            self.handle(mouse_pos)
            return True
        return False

    def can_handle_click(self, mouse_pos: Tuple[int, int]) -> bool:
        return self._state.can_handle(mouse_pos)

    def handle(self, mouse_pos: Tuple[int, int]):
        self._state.handle(mouse_pos)

    def first_click_action(self):
        """Empty method which can be overridden.
        It's called when window is clicked in passive state"""
        pass

    def second_click_action(self):
        """Empty method which can be overridden.
        It's called when window is clicked in active state"""
        pass

    def action_while_update(self):
        """Empty method"""
        pass

    def update(self, *args):
        self.action_while_update()
        if self.real_image is not self._draw_image:
            if time.time() - self._last_tmp_time > self._tmp_delay:
                self._draw_image = self.real_image


class WindowError(Exception):
    pass
