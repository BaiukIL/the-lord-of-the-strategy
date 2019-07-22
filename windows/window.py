""" This module contains `Window` - surface extension.
Most game objects are inherited from this. """


from typing import Tuple
import pygame
# project modules #
from interface import interface_configs as configs
from windows import window_states, image_states, borders_states


class Window(pygame.sprite.Sprite):
    """ Surface extension. """

    _state: window_states.WindowState
    _borders_state: borders_states.BordersState
    _image_state: image_states.ImageState

    _default_image: pygame.Surface

    # Message which appears when player points to the window.
    _hint_message = None

    _default_alpha = 255

    borders_size = configs.BORDERS_SIZE
    borders_color = configs.BORDERS_COLOR

    def __init__(self, image: pygame.Surface, size: Tuple[int, int] = None):
        pygame.sprite.Sprite.__init__(self)
        if size is not None:
            self.image = pygame.transform.scale(image, size)
        else:
            self.image = image
        self.rect = self.image.get_rect()

        self._default_image = self.image.copy()

        self._image_state = image_states.ConstantImageState(self)
        # Every window is created without borders.
        self._borders_state = borders_states.DisabledBordersState(self)
        # Every window is created in passive state.
        self.passive()

    def set_default_alpha(self, alpha: int):
        """ `alpha` shows how bright window is.
        255 is bright, 0 is transparent. """

        self._default_alpha = alpha
        self.image.set_alpha(alpha)

    def set_constant_bordered(self):
        """ Makes window constant bordered. """
        self._borders_state.change_to_constant()

    def set_never_bordered(self):
        """ Removes window borders forever. """
        self._borders_state.change_to_never()

    def set_tmp_image(self, tmp_image: pygame.Surface, delay: float):
        """ Changes image to `image` for `delay` time. Does not copy `image`."""
        self._image_state = image_states.TemporaryImageState(self, tmp_image, delay)

    def reset_image(self, new_image: pygame.Surface):
        """ Changes image to `new_image`. Does not copy `new_image`.
        Use this instead of `=` or `blit`. """
        # We use `=` instead of `blit` because `=` does not save alpha.
        self.image = new_image
        self._borders_state.fix_borders()

    def hide(self):
        """ Switchs window to `hidden` state. """
        self._state = window_states.HiddenWindowState(self)
        self.action_after_hide()

    def is_hidden(self):
        """ Returns True if window is in hidden state. """
        return isinstance(self._state, window_states.HiddenWindowState)

    def action_after_hide(self):
        """ Action window does when it switchs to `hidden` state. """

    def passive(self):
        """ Switchs window to `passive` state. """
        self._state = window_states.PassiveWindowState(self)
        self.action_after_passive()

    def is_passive(self):
        """ Returns True if window is in passive state. """
        return isinstance(self._state, window_states.PassiveWindowState)

    def action_after_passive(self):
        """ Action window does when it switchs to `passive` state. """

    def active(self):
        """ Switchs window to `active` state. """
        self._state = window_states.ActiveWindowState(self)
        self.action_after_active()

    def is_active(self):
        """ Returns True if window is in active state. """
        return isinstance(self._state, window_states.ActiveWindowState)

    def action_after_active(self):
        """ Action window does when it switchs to `active` state. """

    def clear(self):
        """ Removes window image and makes it transparrent. """
        self.image.fill((0, 0, 0, 0))

    def add_borders(self):
        """ Makes window bordred (if it is not marked as never bordered). """
        self._borders_state.change_to_enabled()

    def remove_borders(self):
        """ Makes window unbordred (if it is not marked as constant bordered). """
        self._borders_state.change_to_disabled()

    def handle_click(self, mouse_pos: Tuple[int, int]) -> bool:
        """ Action window does when it can handle mouse click. """
        if self.can_handle_click(mouse_pos):
            self._handle(mouse_pos)
            return True
        return False

    def can_handle_click(self, mouse_pos: Tuple[int, int]) -> bool:
        """ Returns true if window can handle mouse click. """
        return self._state.can_handle(mouse_pos)

    def first_click_action(self):
        """ Is called when window is clicked in passive state. """

    def second_click_action(self):
        """ Is called when window is clicked in active state. """

    def action_while_update(self):
        """ Action will be executed when object `update` method is called. """

    def update(self, *args):
        """ `pygame.sprite.Sprite` method.
        Used when group(which sprite belongs to) updates. """

        self.action_while_update()
        # Check if it's time to remove temporary image.
        self._image_state.update()

    def _handle(self, mouse_pos: Tuple[int, int]):
        self._state.handle(mouse_pos)
