import time
from typing import Tuple

import pygame

# project modules #
import configs
from windows import window_states


class Window(pygame.sprite.Sprite):
    """ Surface extension. """

    _state: window_states.WindowState
    _default_image: pygame.Surface

    # Message which appears when player points to the window.
    _hint_message = None

    _default_alpha = 255
    # Indicator: shows if window has borders or not.
    _bordered = False
    # If True, borders will never disappear.
    _constant_bordered = False
    # If False, borders will never appear.
    _never_bordered = False

    _borders_size = configs.BORDERS_SIZE
    _borders_color = configs.BORDERS_COLOR

    def __init__(self, size: Tuple[int, int] = None, image: pygame.Surface = None):
        pygame.sprite.Sprite.__init__(self)
        if image is not None:
            self.image = image
        else:
            if size is None:
                raise WindowError(
                    'Window without default image must have a size')
            self.image = pygame.Surface(size, pygame.SRCALPHA)
        self.rect = self.image.get_rect()
        self._default_image = self.image.copy()
        self._has_tmp_image = False
        self._tmp_image_delay = 0
        self._tmp_image_set_time = 0
        # Initialize window with passive state.
        self.passive()

    def set_default_alpha(self, alpha: int):
        """ `alpha` shows how bright window is.
        255 is very bright, 0 is transparrent. """

        self._default_alpha = alpha
        self.image.set_alpha(alpha)

    def set_constant_bordered(self):
        """ Makes window constant bordered. """
        if self._constant_bordered:
            raise WindowError("Contradictory borders settings")
        self._constant_bordered = True
        self.add_borders()

    def set_never_bordered(self):
        """ Remove window borders forever. """
        if self._constant_bordered:
            raise WindowError("Contradictory borders settings")
        self._never_bordered = True
        self.remove_borders()

    def set_tmp_image(self, image: pygame.Surface, delay: float):
        self.image = image
        self._has_tmp_image = True
        self._tmp_image_delay = delay
        self._tmp_image_set_time = time.time()

    def hide(self):
        """ Switchs window to hidden state. """
        self._change_state(window_states.HiddenWindowState(self))
        self.action_after_hide()

    def action_after_hide(self):
        """ Action window will does when it switchs to hidden state. """

    def passive(self):
        """ Switchs window to passive state. """
        self._change_state(window_states.PassiveWindowState(self))
        self.action_after_passive()

    def action_after_passive(self):
        """ Action window will does when it switchs to hidden state. """

    def active(self):
        """ Switchs window to active state. """
        self._change_state(window_states.ActiveWindowState(self))
        self.action_after_active()

    def action_after_active(self):
        """ Action window will does when it switchs to active state. """

    def clear(self):
        """ Removes window image and makes it transparrent. """
        self.image.fill((0, 0, 0, 0))

    def add_borders(self):
        if self._never_bordered:
            return
        if not self._bordered:
            self._bordered = True
            self._draw_borders()

    def remove_borders(self):
        if self._constant_bordered:
            return
        if self._bordered:
            self._bordered = False
            self._clear_borders()

    def handle_click(self, mouse_pos: Tuple[int, int]) -> bool:
        """ Action window does when it can handle mouse click. """
        if self.can_handle_click(mouse_pos):
            self._handle(mouse_pos)
            return True
        return False

    def can_handle_click(self, mouse_pos: Tuple[int, int]) -> bool:
        """ Return true if window can handle mouse click. """
        return self._state.can_handle(mouse_pos)

    def first_click_action(self):
        """ Empty method which can be overridden.
        It's called when window is clicked in passive state. """

    def second_click_action(self):
        """Empty method which can be overridden.
        It's called when window is clicked in active state. """

    def action_while_update(self):
        """Empty method. """

    def update(self, *args):
        """ `pygame.sprite.Sprite` method.
        Used when group(which sprite belongs to) updates. """

        self.action_while_update()
        # Check if it's time to remove temporary image.
        if self._has_tmp_image:
            self._try_to_clear_tmp_image()

    def _handle(self, mouse_pos: Tuple[int, int]):
        self._state.handle(mouse_pos)

    def _draw_borders(self):
        """ Realization of borders addition. """
        pygame.draw.rect(self.image, self._borders_color,
                         self.rect, self._borders_size)

    def _clear_borders(self):
        """ Realization of borders removal. """
        self.image = self._default_image.copy()

    def _try_to_clear_tmp_image(self):
        if time.time() - self._tmp_image_set_time > self._tmp_image_delay:
            self._has_tmp_image = False
            self.image = self._default_image
            if self._bordered:
                self._draw_borders()

    def _change_state(self, state: window_states.WindowState):
        self._state = state


class WindowError(Exception):
    pass
