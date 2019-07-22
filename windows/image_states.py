""" This module contains window image states (constant and temporary). """


from abc import ABC
import time
import pygame


# State pattern.
class ImageState(ABC):
    """ Base class of image states. """

    def __init__(self, window):
        self.window = window

    def update(self):
        """ Is called to check whether image should be changed or not. """


class ConstantImageState(ImageState):
    """ Class represents `constant` (simple) image state. """


class TemporaryImageState(ImageState):
    """ Class represents `temporary` image state. """

    def __init__(self, window, tmp_image: pygame.Surface, delay: float):
        ImageState.__init__(self, window)

        self._previous_image = window.image
        self._delay = delay
        self._set_time = time.time()

        window.reset_image(tmp_image)

    def update(self):
        if time.time() - self._set_time > self._delay:
            self.window.reset_image(self._previous_image)
            self.window._image_state = ConstantImageState(self.window)
