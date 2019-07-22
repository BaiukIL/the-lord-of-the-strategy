""" This module contains window borders states responsible for borders existence. """


from abc import ABC
import pygame


def draw_borders(window):
    """ Draws borders on window. """
    pygame.draw.rect(window.image, window.borders_color,
                     pygame.Rect((0, 0), window.rect.size), window.borders_size)


def clear_borders(window):
    """ Removes borders from window. """
    window.image = window._default_image.copy()


# State pattern.
class BordersState(ABC):
    """ Base class of borders states. """

    def __init__(self, window):
        self.window = window

    def change_to_enabled(self):
        """ Changes borders state to `enabled`. """

    def change_to_disabled(self):
        """ Changes borders state to `disabled`. """

    def change_to_constant(self):
        """ Changes borders state to `constant bordered`. """

    def change_to_never(self):
        """ Changes borders state to `never bordered`. """

    def fix_borders(self):
        """ Is called after image change to fix new image borders. """


class EnabledBordersState(BordersState):
    """ Class represents `enabled` borders state. """

    def change_to_disabled(self):
        clear_borders(self.window)
        self.window._borders_state = DisabledBordersState(self.window)

    def change_to_constant(self):
        self.window._borders_state = ConstantBordersState(self.window)

    def change_to_never(self):
        clear_borders(self.window)
        self.window._borders_state = NeverBordersState(self.window)

    def fix_borders(self):
        draw_borders(self.window)


class ConstantBordersState(EnabledBordersState):
    """ Class represents `constant bordered` borders state.
    In this state borders cannot be removed. """

    def change_to_disabled(self):
        pass

    def change_to_constant(self):
        pass

    def change_to_never(self):
        raise BordersError(
            'Contradictory borders settings: change constants to never borders.')


class DisabledBordersState(BordersState):
    """ Class represents `disabled` borders state. """

    def change_to_enabled(self):
        draw_borders(self.window)
        self.window._borders_state = EnabledBordersState(self.window)

    def change_to_constant(self):
        draw_borders(self.window)
        self.window._borders_state = ConstantBordersState(self.window)

    def change_to_never(self):
        self.window._borders_state = NeverBordersState(self.window)


class NeverBordersState(DisabledBordersState):
    """ Class represents `never bordered` borders state.
    In this state borders cannot be added. """

    def change_to_enabled(self):
        pass

    def change_to_never(self):
        pass

    def change_to_constant(self):
        raise BordersError(
            'Contradictory borders settings: change never to constant borders.')


class BordersError(Exception):
    pass
